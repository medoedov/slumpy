#!/usr/bin/env bash
# Packages an agent system as a Claude Code plugin so `claude plugin eval` can load it.
#
# Usage:
#   build-plugin.sh v0   <out-dir>   # molyanov-ai-dev framework at the pinned commit (system "before")
#   build-plugin.sh repo <out-dir>   # this repository's own system: AGENTS.md, .claude/rules, skills, agents
#
# Always-on instructions (the entry point and path rules) cannot load inside an eval run, so they are
# injected by a SessionStart hook that prints them as session context. Skills and agents are
# copied as plugin components. The cases under evals/cases are copied to <out-dir>/evals.
set -euo pipefail

VARIANT="${1:?variant: v0 | repo}"
OUT="${2:?output dir}"
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FW_URL="https://github.com/pavel-molyanov/molyanov-ai-dev.git"
FW_COMMIT="ca44595f459eb84086cec8ed04d47f57bab945f3"

rm -rf "$OUT"
mkdir -p "$OUT/.claude-plugin" "$OUT/hooks" "$OUT/context"

case "$VARIANT" in
  v0)
    SRC="$(mktemp -d)"
    git clone -q "$FW_URL" "$SRC/fw"
    git -C "$SRC/fw" checkout -q "$FW_COMMIT"
    cp -R "$SRC/fw/skills" "$SRC/fw/agents" "$OUT/"
    # The framework README installs CLAUDE.md as the global ~/.claude/CLAUDE.md and asks the owner
    # to declare the user's language in it; the Slumpy owner's project CLAUDE.md declares Russian.
    sed 's/^- Artifacts addressed to the user (chat, plans, plan-mode, interviews, validator summaries, user-spec, README): the language the user writes in\. Declare your language here.*$/- Artifacts addressed to the user (chat, plans, plan-mode, interviews, validator summaries, user-spec, README): the language the user writes in. This user writes in Russian./' \
      "$SRC/fw/CLAUDE.md" > "$OUT/context/00-CLAUDE.md"
    grep -q 'This user writes in Russian' "$OUT/context/00-CLAUDE.md"
    echo "molyanov-ai-dev@$FW_COMMIT" > "$OUT/SOURCE"
    rm -rf "$SRC"
    ;;
  repo)
    cp "$REPO_ROOT/AGENTS.md" "$OUT/context/00-AGENTS.md"
    if [ -d "$REPO_ROOT/.claude/rules" ]; then
      for f in "$REPO_ROOT"/.claude/rules/*.md; do
        [ -e "$f" ] && cp "$f" "$OUT/context/10-rule-$(basename "$f")"
      done
    fi
    [ -d "$REPO_ROOT/.claude/skills" ] && cp -R "$REPO_ROOT/.claude/skills" "$OUT/skills"
    [ -d "$REPO_ROOT/.claude/agents" ] && cp -R "$REPO_ROOT/.claude/agents" "$OUT/agents"
    echo "slumpy@$(git -C "$REPO_ROOT" rev-parse HEAD)" > "$OUT/SOURCE"
    ;;
  *) echo "unknown variant: $VARIANT" >&2; exit 1 ;;
esac

cat > "$OUT/.claude-plugin/plugin.json" <<JSON
{
  "name": "sys",
  "version": "0.0.0",
  "description": "Agent system under test ($VARIANT), packaged for claude plugin eval"
}
JSON

cat > "$OUT/hooks/inject-context.sh" <<'SH'
#!/usr/bin/env bash
# Prints the packaged always-on instructions; SessionStart stdout becomes session context.
for f in "${CLAUDE_PLUGIN_ROOT}"/context/*.md; do
  [ -e "$f" ] || continue
  printf '# Instructions from %s\n\n' "$(basename "$f")"
  cat "$f"
  printf '\n\n'
done
SH
chmod +x "$OUT/hooks/inject-context.sh"

cat > "$OUT/hooks/hooks.json" <<'JSON'
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/inject-context.sh" } ] }
    ]
  }
}
JSON

mkdir -p "$OUT/evals"
cp -R "$REPO_ROOT/evals/cases/." "$OUT/evals/"
echo "built $VARIANT plugin at $OUT ($(cat "$OUT/SOURCE"))"
