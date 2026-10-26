#!/usr/bin/env bash
# Runs the component eval suite against one packaged agent system with `claude plugin eval`.
# Each case runs in two arms: with the system (plugin) and without it (bare Claude Code).
#
# Usage: scripts/run.sh <variant: v0|repo> <label> [extra claude plugin eval args...]
#   e.g. scripts/run.sh v0 baseline-v0 --tag review --max-cost-usd 12
#
# Results: evals/results/<label>/<timestamp>/ (aggregate-result.json + runs.jsonl).
# Pinned settings below must stay identical between the "before" and "after" measurements.
set -euo pipefail

VARIANT="${1:?variant: v0 | repo}"
LABEL="${2:?label}"
shift 2

EVALS="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$EVALS/.build/$VARIANT"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="$EVALS/results/$LABEL/$STAMP"
mkdir -p "$OUT"

"$EVALS/scripts/build-plugin.sh" "$VARIANT" "$BUILD"

export CLAUDE_CODE_EFFORT_LEVEL=high
set +e
(cd "$BUILD" && claude plugin eval . \
  --trust-plugin \
  --ablation with-without \
  --model claude-opus-5-5 \
  --judge-model claude-sonnet-5-5 \
  --concurrency 4 \
  --keep-temp \
  --no-publish \
  --output-dir "$OUT" \
  "$@" 2>&1 | grep -v '^⚠ kept ' | tee "$OUT/console.log")
STATUS=${PIPESTATUS[0]}
set -e

python3 -I "$EVALS/scripts/collect.py" "$OUT"
cp "$BUILD/SOURCE" "$OUT/SOURCE"
echo "exit status $STATUS; results in $OUT"
