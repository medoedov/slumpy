"""Package component evals in a fresh direct child of evals/.build; never delete outputs."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FW_COMMIT = "ca44595f459eb84086cec8ed04d47f57bab945f3"


def reject_links(path):
    for part in (path, *path.parents):
        if part.is_symlink() or part.is_junction():
            raise ValueError(f"linked path is not allowed: {part}")


def copy(source, target):
    reject_links(source)
    if source.is_dir():
        target.mkdir()
        for child in sorted(source.iterdir()):
            copy(child, target / child.name)
    else:
        shutil.copyfile(source, target)


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def build(variant, destination, root=ROOT):
    if sys.version_info < (3, 12):
        raise ValueError("Python 3.12+ is required for safe junction detection")
    if variant not in ("repo", "v0"):
        raise ValueError(f"unknown variant: {variant}")
    root = root.resolve()
    base = root / "evals" / ".build"
    out = Path(destination).absolute()
    reject_links(base)
    reject_links(out)
    if out.parent.resolve() != base.resolve() or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", out.name):
        raise ValueError("output must be a named direct child of evals/.build")
    base.mkdir(exist_ok=True)
    out.mkdir()  # Exclusive creation: never remove or overwrite an existing result.
    for name in (".claude-plugin", "hooks", "context"):
        (out / name).mkdir()
    if variant == "repo":
        copy(root / "AGENTS.md", out / "context" / "00-AGENTS.md")
        for source in sorted((root / ".claude" / "rules").glob("*.md")):
            copy(source, out / "context" / ("10-rule-" + source.name))
        for name in ("skills", "agents"):
            copy(root / ".claude" / name, out / name)
        origin = {"repository": "slumpy", "head": git(root, "rev-parse", "HEAD"),
                  "dirty": bool(git(root, "status", "--porcelain", "--untracked-files=all"))}
    else:
        # Historical comparison only; invoking v0 explicitly requests this network clone.
        with tempfile.TemporaryDirectory(prefix="v0-source-", dir=base) as temp:
            source = Path(temp) / "framework"
            subprocess.run(["git", "clone", "-q", "https://github.com/pavel-molyanov/molyanov-ai-dev.git", str(source)], check=True)
            subprocess.run(["git", "-C", str(source), "checkout", "-q", FW_COMMIT], check=True)
            for name in ("skills", "agents"):
                copy(source / name, out / name)
            reject_links(source / "CLAUDE.md")
            content = (source / "CLAUDE.md").read_text(encoding="utf-8")
            content, count = re.subn(r"(?m)^- Artifacts addressed to the user .*Declare your language here.*$",
                "- Artifacts addressed to the user (chat, plans, plan-mode, interviews, validator summaries, user-spec, README): the language the user writes in. This user writes in Russian.", content)
            if count != 1:
                raise ValueError("historical language instruction not found exactly once")
            (out / "context" / "00-CLAUDE.md").write_text(content, encoding="utf-8")
        origin = {"repository": "molyanov-ai-dev", "head": FW_COMMIT, "dirty": False}
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "sys", "version": "0.0.0",
        "description": f"Agent system under test ({variant}), component eval only"}, indent=2) + "\n", encoding="utf-8")
    hook = out / "hooks" / "inject-context.sh"
    hook.write_text('''#!/usr/bin/env bash
set -euo pipefail
for f in "${CLAUDE_PLUGIN_ROOT}"/context/*.md; do
  [ -e "$f" ] || continue
  printf '# Instructions from %s\\n\\n' "$(basename "$f")"
  cat "$f"
  printf '\\n\\n'
done
''', encoding="utf-8", newline="\n")
    hook.chmod(0o755)
    (out / "hooks" / "hooks.json").write_text(json.dumps({"hooks": {"SessionStart": [
        {"hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/inject-context.sh"}]}]}}, indent=2) + "\n", encoding="utf-8")
    copy(root / "evals" / "cases", out / "evals")
    files = {p.relative_to(out).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted(out.rglob("*")) if p.is_file()}
    digest = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    manifest = {"format": 1, "variant": variant, "origin": origin,
                "loading": "all-rules SessionStart injection; component evaluation only",
                "payload_sha256": digest, "files": files}
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (out / "SOURCE").write_text(f"{origin['repository']}@{origin['head']} dirty={origin['dirty']} payload-sha256={digest}\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variant", choices=("repo", "v0"))
    parser.add_argument("output")
    args = parser.parse_args()
    try:
        result = build(args.variant, args.output)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        parser.exit(1, f"build failed: {error}\n")
    print(f"built {args.variant} plugin at {args.output} ({result['payload_sha256']})")
