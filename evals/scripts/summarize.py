"""Builds markdown tables from one or more result dirs written by run.sh.

Usage: python3 -I scripts/summarize.py <results dir>... > summary.md
Arms: "with" = the packaged system, "without" = bare Claude Code (same model, no plugin).
"""
import collections
import json
import os
import sys

GROUPS = {"r": "review", "d": "design", "p": "product", "t": "traps", "s": "triggers"}
dirs = sys.argv[1:]
runs, total_cost, durations = [], 0.0, 0
for d in dirs:
    agg = json.load(open(os.path.join(d, "aggregate-result.json")))
    total_cost += agg.get("costUsd") or 0
    durations += agg.get("durationSeconds") or 0
    paid = {(c["name"], g["name"]) for c in agg["cases"] for g in c["graders"]
            if g.get("type") in ("llm", "baseline")}
    skipped = {(c["name"], arm, i) for c in agg["cases"] for arm, rs in c["arms"].items()
               for i, r in enumerate(rs) if r.get("skippedPaidGraders")}
    for line in open(os.path.join(d, "runs.jsonl")):
        rec = json.loads(line)
        if (rec["case"], rec["arm"], rec["run"]) in skipped:
            # The cost ceiling skipped this run's judge graders: their verdicts are not results.
            rec["graders"] = {g: (None if (rec["case"], g) in paid else v)
                              for g, v in rec["graders"].items()}
            rec["score"] = None
        rec["group"] = GROUPS.get(rec["case"][0], "other")
        runs.append(rec)

ARMS = ("with", "without")
INDICATOR_PREFIX = "ind-"


def pct(values):
    values = [v for v in values if v is not None]
    return f"{sum(values)}/{len(values)}" if values else "—"


def mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else 0.0


print(f"Result dirs: {', '.join(os.path.relpath(d) for d in dirs)}")
print(f"\nTotal estimated cost (agent runs + judge): ${total_cost:.2f}; wall time {durations // 60} min\n")

print("## Cost and effort per arm\n")
print("| Group | Arm | Runs | Cost, $ | Mean $/run | Mean turns | Runs with errors |")
print("|---|---|---|---|---|---|---|")
for group in sorted({r["group"] for r in runs}):
    for arm in ARMS:
        sel = [r for r in runs if r["group"] == group and r["arm"] == arm]
        if not sel:
            continue
        cost = sum((r["costUsd"] or 0) + (r["judgeCostUsd"] or 0) for r in sel)
        print(f"| {group} | {arm} | {len(sel)} | {cost:.2f} | {cost / len(sel):.3f} | "
              f"{mean([r['turns'] for r in sel]):.1f} | {sum(1 for r in sel if r['error'])} |")

print("\n## Grader pass counts per case (passed/runs)\n")
print("| Group | Case | Grader | With system | Without system |")
print("|---|---|---|---|---|")
by_case = collections.defaultdict(list)
for r in runs:
    by_case[(r["group"], r["case"])].append(r)
for (group, case), sel in sorted(by_case.items()):
    graders = sorted({g for r in sel for g in r["graders"]})
    for g in graders:
        cells = []
        for arm in ARMS:
            present = [r["graders"][g] for r in sel if r["arm"] == arm and g in r["graders"]]
            vals = [int(v) for v in present if v is not None]
            cells.append(pct(vals) if vals else ("not graded" if present else "—"))
        print(f"| {group} | {case} | {g} | {cells[0]} | {cells[1]} |")

print("\n## Case scores (mean over runs; indicator graders excluded by the tool)\n")
print("| Case | With | Without | Δ |")
print("|---|---|---|---|")
for (group, case), sel in sorted(by_case.items()):
    ws = [r["score"] for r in sel if r["arm"] == "with" and r["score"] is not None]
    wos = [r["score"] for r in sel if r["arm"] == "without" and r["score"] is not None]
    if not ws or not wos:
        print(f"| {case} | not graded | not graded | — |")
        continue
    w, wo = mean(ws), mean(wos)
    print(f"| {case} | {w:.2f} | {wo:.2f} | {w - wo:+.2f} |")

review = [r for r in runs if r["group"] == "review"]
if review:
    print("\n## Review: planted defects found and false alarms per repetition\n")
    print("| Arm | Repetition | Defects found (of 9) | Cases with ≥2 false alarms |")
    print("|---|---|---|---|")
    for arm in ARMS:
        for rep in sorted({r["run"] for r in review}):
            sel = [r for r in review if r["arm"] == arm and r["run"] == rep]
            found = sum(1 for r in sel if r["graders"].get("found"))
            fa = sum(1 for r in sel if r["graders"].get("no-false-alarms") is False)
            print(f"| {arm} | {rep + 1} | {found}/{len(sel)} | {fa} |")

print("\n## Skills and subagents used\n")
print("| Case | Skills invoked (all runs) | Subagents spawned (all runs) |")
print("|---|---|---|")
for (group, case), sel in sorted(by_case.items()):
    for arm in ARMS:
        arm_sel = [r for r in sel if r["arm"] == arm]
        skills = collections.Counter(s for r in arm_sel for s in r["skills"])
        agents = collections.Counter()
        for r in arm_sel:
            for k, v in (r["subagents"] or {}).items():
                agents[k] += v if isinstance(v, int) else 1
        if skills or agents:
            label = case if arm == "with" else f"{case} (without)"
            print(f"| {label} | {', '.join(f'{k}×{v}' for k, v in skills.items()) or '—'} | "
                  f"{', '.join(f'{k}×{v}' for k, v in agents.items()) or '—'} |")
