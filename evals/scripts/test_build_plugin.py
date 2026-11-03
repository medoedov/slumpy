"""Deterministic filesystem tests; no model, network, or full project checkout."""
import hashlib
import json
import os
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from build_plugin import ROOT, build


class PackagingTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / "evals" / ".build"
        base.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="test-packaging-", dir=base)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in (".claude/rules", ".claude/skills/example", ".claude/agents", "evals/cases/sample"):
            (self.root / name).mkdir(parents=True)
        for name in ("AGENTS.md", ".claude/rules/core.md", ".claude/skills/example/SKILL.md", ".claude/agents/reviewer.md", "evals/cases/sample/prompt.md"):
            (self.root / name).write_text("fixture\n", encoding="utf-8")
        for args in (("init", "-q"), ("add", "."), ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture")):
            subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def output(self, name="result"):
        return self.root / "evals" / ".build" / name

    def test_refuses_outside_root_parent_and_existing_without_damage(self):
        protected = self.root / "keep"
        protected.mkdir()
        marker = protected / "owner-data"
        marker.write_text("preserve")
        for target in (protected, self.root, self.root / "evals" / ".build", self.output("../escape")):
            with self.subTest(target=target), self.assertRaises(ValueError):
                build("repo", target, self.root)
            self.assertEqual(marker.read_text(), "preserve")
        build("repo", self.output(), self.root)
        (self.output() / "sentinel").write_text("preserve")
        with self.assertRaises(FileExistsError):
            build("repo", self.output(), self.root)
        self.assertEqual((self.output() / "sentinel").read_text(), "preserve")

    def test_unknown_variant_does_not_create_output(self):
        with self.assertRaises(ValueError):
            build("invalid", self.output(), self.root)
        self.assertFalse(self.output().exists())

    def test_unsupported_python_rejected_before_creating_output(self):
        with patch("build_plugin.sys.version_info", (3, 11, 9)):
            with self.assertRaisesRegex(ValueError, "Python 3.12"):
                build("repo", self.output(), self.root)
        self.assertFalse(self.output().exists())

    def test_manifest_hashes_actual_contents_including_uncommitted_and_untracked(self):
        first = build("repo", self.output("first"), self.root)
        (self.root / "AGENTS.md").write_text("changed without commit\n")
        (self.root / ".claude/skills/example/extra.md").write_text("untracked\n")
        second = build("repo", self.output("second"), self.root)
        self.assertEqual(first["origin"]["head"], second["origin"]["head"])
        self.assertNotEqual(first["payload_sha256"], second["payload_sha256"])
        self.assertTrue(second["origin"]["dirty"])
        self.assertIn("skills/example/extra.md", second["files"])
        for relative, digest in second["files"].items():
            self.assertEqual(hashlib.sha256((self.output("second") / relative).read_bytes()).hexdigest(), digest)
        expected = hashlib.sha256(json.dumps(second["files"], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(second["payload_sha256"], expected)
        self.assertEqual(second, json.loads((self.output("second") / "MANIFEST.json").read_text()))

    def test_same_inputs_have_same_digest(self):
        first = build("repo", self.output("first"), self.root)
        second = build("repo", self.output("second"), self.root)
        self.assertEqual(first["payload_sha256"], second["payload_sha256"])

    def test_symlink_sources_and_output_rejected(self):
        link = self.root / ".claude/skills/example/link.md"
        try:
            link.symlink_to(self.root / "AGENTS.md")
        except OSError as error:
            self.skipTest(f"host cannot create symlinks: {error}")
        with self.assertRaises(ValueError):
            build("repo", self.output("source-link"), self.root)
        link.unlink()
        self.output("alias").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            build("repo", self.output("alias"), self.root)

    @unittest.skipUnless(os.name == "nt", "junctions are Windows-specific")
    def test_junction_build_root_rejected_without_modifying_target(self):
        target = self.root / "protected"
        target.mkdir()
        marker = target / "owner-data"
        marker.write_text("preserve")
        link = self.root / "evals" / ".build"
        # Both paths are fixture-owned. No deletion/move command is passed to another shell.
        quote = lambda value: "'" + str(value).replace("'", "''") + "'"
        command = f"New-Item -ItemType Junction -Path {quote(link)} -Target {quote(target)} -ErrorAction Stop | Out-Null"
        result = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", command], capture_output=True)
        if result.returncode:
            self.skipTest("host cannot create a junction")
        self.assertTrue(link.is_junction())
        try:
            with self.assertRaisesRegex(ValueError, "linked path"):
                build("repo", self.output(), self.root)
            self.assertEqual(marker.read_text(), "preserve")
            self.assertFalse((target / "result").exists())
        finally:
            link.rmdir()  # Remove only the fixture junction, never its target.


if __name__ == "__main__":
    unittest.main(verbosity=2)
