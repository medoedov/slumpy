"""Extracts a compact per-run record, leaving input traces and their directories intact.

Writes runs.jsonl next to aggregate-result.json: case, arm, score, cost, turns, final reply,
skills invoked, subagents spawned, grader verdicts. Traces themselves are not kept in git.
"""
import json
import os
import sys

out_dir = sys.argv[1]
agg = json.load(open(os.path.join(out_dir, "aggregate-result.json")))
records = []
for case in agg["cases"]:
    for arm, runs in case["arms"].items():
        for i, run in enumerate(runs):
            rec = {
                "case": case["name"], "arm": arm, "run": i,
                "score": run.get("score"), "costUsd": run.get("costUsd"),
                "judgeCostUsd": run.get("judgeCostUsd"), "turns": run.get("turns"),
                "durationSeconds": run.get("durationSeconds"), "error": run.get("error"),
                "skippedPaidGraders": bool(run.get("skippedPaidGraders")),
                "graders": {g["name"]: g["passed"] for g in run.get("graders", [])},
                "skills": [], "subagents": {}, "final": None,
            }
            trace = run.get("tracePath")
            if trace and os.path.exists(trace):
                for line in open(trace):
                    msg = json.loads(line)
                    if msg.get("type") == "assistant":
                        for block in msg["message"].get("content", []):
                            if block.get("type") == "tool_use" and block.get("name") == "Skill":
                                rec["skills"].append(block["input"].get("skill"))
                    elif msg.get("type") == "result":
                        rec["final"] = msg.get("result")
                        rec["subagents"] = (msg.get("subagent_stats") or {}).get("by_type", {})
            records.append(rec)

with open(os.path.join(out_dir, "runs.jsonl"), "w") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"collected {len(records)} runs into {out_dir}/runs.jsonl")
