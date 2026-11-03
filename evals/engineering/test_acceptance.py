"""Regression for acceptance across two executable versions, with real process/store IO."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


class MigrationAcceptance(unittest.TestCase):
    def run_acceptance(self, candidate, initial=None):
        command = [sys.executable, "-I", str(ROOT / "acceptance.py"), str(candidate)]
        if initial is not None:
            command += ["--initial-candidate", str(initial)]
        return subprocess.run(command, capture_output=True, text=True, timeout=180)

    def test_distinct_initial_executable_exposes_lost_data(self):
        # Local initial/follow-up runs remain correct in the new namespace, but an actual
        # upgrade loses the old namespace. A same-version test cannot expose that regression.
        with tempfile.TemporaryDirectory(prefix="migration-", dir=ROOT / ".tmp") as folder:
            candidate = Path(folder) / "new.py"
            candidate.write_text(
                "import runpy, sys\nsys.argv[1] += '.v2'\nrunpy.run_path("
                + repr(str(ROOT / "reference.py")) + ", run_name='__main__')\n",
                encoding="utf-8",
            )
            same_version = self.run_acceptance(candidate)
            self.assertEqual(same_version.returncode, 0, same_version.stderr)
            self.assertIn("no upgrade evidence", same_version.stdout)
            upgrade = self.run_acceptance(candidate, ROOT / "reference.py")
            self.assertEqual(upgrade.returncode, 1, upgrade.stderr)
            self.assertIn("follow-up must open the initial store", upgrade.stderr)
            self.assertNotIn("ERROR:", upgrade.stderr)
            self.assertIn("Ran 10 tests", upgrade.stderr)

    def test_compatible_frozen_initial_and_current_pass(self):
        # Snapshot bytes separately: the follow-up must not silently rewrite its own history.
        with tempfile.TemporaryDirectory(prefix="compatible-", dir=ROOT / ".tmp") as folder:
            initial = Path(folder) / "initial.py"
            frozen = (ROOT / "reference.py").read_bytes()
            initial.write_bytes(frozen)
            result = self.run_acceptance(ROOT / "reference.py", initial)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(initial.read_bytes(), frozen)


if __name__ == "__main__":
    if (ROOT / ".tmp").is_symlink() or (ROOT / ".tmp").resolve().parent != ROOT:
        raise SystemExit("fixture temporary root must stay beside acceptance.py")
    (ROOT / ".tmp").mkdir(exist_ok=True)
    unittest.main(verbosity=2)
