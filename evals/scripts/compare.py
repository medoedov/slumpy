"""Compares the with-system arm of a "before" measurement with the with-system arm of an "after" one.

Usage: python3 -I scripts/compare.py <before result dir>... -- <after result dir>...
Prints per-grader pass counts: before (with system), after (with system), and the without-system
arm found in the "before" dirs for reference; then cost per group. Runs whose paid graders were
skipped by the cost ceiling count as not graded.
"""
import collections
import json
import os
import sys

GROUPS = {"r": "review", "d": "design", "p": "product", "t": "traps", "s": "triggers"}
args = sys.argv[1:]
if "--" not in args:
    sys.exit("usage: compare.py <before dirs>... -- <after dirs>...")
split = args.index("--")
sides = {"before": args[:split], "after": args[split + 1:]}


def load(dirs):
    runs = []
    for d in dirs:
        agg = json.load(open(os.path.join(d, "aggregate-result.json")))
        paid = {(c["name"], g["name"]) for c in agg["cases"] for g in c["graders"]
                if g.get("type") in ("llm", "baseline")}
        skipped = {(c["name"], arm, i) for c in agg["cases"] for arm, rs in c["arms"].items()
                   for i, r in enumerate(rs) if r.get("skippedPaidGraders")}
        for line in open(os.path.join(d, "runs.jsonl")):
            rec = json.loads(line)
            if (rec["case"], rec["arm"], rec["run"]) in skipped:
                rec["graders"] = {g: (None if (rec["case"], g) in paid else v)
                                  for g, v in rec["graders"].items()}
            rec["group"] = GROUPS.get(rec["case"][0], "other")
            runs.append(rec)
    return runs


data = {side: load(dirs) for side, dirs in sides.items()}
# With --ablation none the tool still names the plugin arm "with".
columns = [("before", "with", "Before, with system"), ("after", "with", "After, with system"),
           ("before", "without", "Without system (baseline)")]


def cell(side, arm, case, grader):
    vals = [r["graders"].get(grader) for r in data[side]
            if r["arm"] == arm and r["case"] == case and grader in r["graders"]]
    graded = [int(v) for v in vals if v is not None]
    if not vals:
        return "—"
    return f"{sum(graded)}/{len(graded)}" if graded else "not graded"


cases = sorted({(r["group"], r["case"]) for side in data.values() for r in side})
print("| Group | Case | Grader | " + " | ".join(c[2] for c in columns) + " |")
print("|---|---|---|" + "---|" * len(columns))
for group, case in cases:
    graders = sorted({g for side in data.values() for r in side if r["case"] == case
                      for g in r["graders"]})
    for g in graders:
        print(f"| {group} | {case} | {g} | " +
              " | ".join(cell(s, a, case, g) for s, a, _ in columns) + " |")

print("\n| Group | Arm | Runs | Cost, $ (agent + judge) | Mean $/run |")
print("|---|---|---|---|---|")
for group in sorted({g for g, _ in cases}):
    for side, arm, label in columns:
        sel = [r for r in data[side] if r["group"] == group and r["arm"] == arm]
        if sel:
            cost = sum((r["costUsd"] or 0) + (r["judgeCostUsd"] or 0) for r in sel)
            print(f"| {group} | {label} | {len(sel)} | {cost:.2f} | {cost / len(sel):.3f} |")

skills = collections.Counter()
agents = collections.Counter()
for r in data["after"]:
    skills.update(f"{r['case']}: {s}" for s in r["skills"])
    for k, v in (r["subagents"] or {}).items():
        agents[f"{r['case']}: {k}"] += v if isinstance(v, int) else 1
print("\nAfter, skills invoked:", ", ".join(f"{k}×{v}" for k, v in sorted(skills.items())) or "—")
print("After, subagents spawned:", ", ".join(f"{k}×{v}" for k, v in sorted(agents.items())) or "—")
