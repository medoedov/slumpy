# Component evals for the Slumpy agent system

Component cases from section 9 of `work/agent-system-audit/audit-and-plan.md`. They measure the
agent system on text-only tasks (no build, no Mac): review of Swift diffs with planted defects,
design briefs, product questions to the owner, engineering traps, and skill triggering.
Results and conclusions live in `work/agent-system-audit/baseline.md`.

Do not edit cases after the baseline was taken: before/after comparisons are only valid on the
same cases, graders, model, effort, and judge.

## Layout

```
evals/
├── cases/
│   ├── review/    r1..r9  Swift diffs, one planted defect each
│   ├── design/    d1..d4  design scenarios for a brief before code
│   ├── product/   p1..p3  ambiguous product requests
│   ├── traps/     t1..t5  one trap per subtlety category
│   └── triggers/  s1..s5  skill triggering on natural phrasing (s5 is negative)
├── scripts/
│   ├── build-plugin.sh   packages a system as a plugin (v0 = molyanov-ai-dev@ca44595, repo = this repo)
│   ├── run.sh            runs the suite with pinned settings, both arms
│   ├── collect.py        compact per-run records (runs.jsonl) from kept traces
│   └── summarize.py      markdown tables from result dirs
└── results/<label>/<timestamp>/   aggregate-result.json, runs.jsonl, console.log, SOURCE
```

Each case is a `claude plugin eval` case: `prompt.md` (frontmatter: runs, limits, tools; body: the
user's message) and `graders/*.md`. Success criteria are the graders; `expected_outcome` in the
frontmatter states the intended result in one line. Graders named `ind-*` only record which skill
fired; the tool excludes them from the score.

## Method

- Tool: `claude plugin eval` (Claude Code 2.1.310). Every case runs in two arms: **with** the
  packaged system and **without** it (bare Claude Code, same model). The without arm is the
  "model without system" baseline; it is re-measured on every run.
- Runs happen in an empty temp workspace; project `.claude/` and `CLAUDE.md` do not load there.
  `build-plugin.sh` therefore packages the system as a plugin: skills and agents as components,
  always-on instructions (`CLAUDE.md`, `.claude/rules/*.md`) injected as session context by a
  SessionStart hook.
- Pinned: agent model `claude-opus-5-5`, `CLAUDE_CODE_EFFORT_LEVEL=high`, judge
  `claude-sonnet-5-5`, 2 runs per case per arm (from case frontmatter), concurrency 4.
- Tools allowed in runs: Read, Glob, Grep, Skill, Agent, TodoWrite. No Bash/Write: every case
  carries its inputs in the prompt and expects the answer in the reply.

## Reproduce

Requires Claude Code ≥ 2.1.269 with `claude plugin eval`, git ≥ 2.31, network access to GitHub.

```bash
# system "before": molyanov-ai-dev at ca44595
evals/scripts/run.sh v0 baseline --tag review   --max-cost-usd 13
evals/scripts/run.sh v0 baseline --tag design   --max-cost-usd 8
# ...same for product, traps, triggers

# system "after": this repository's CLAUDE.md, .claude/rules, .claude/skills, .claude/agents
evals/scripts/run.sh repo after --tag review --max-cost-usd 13

python3 -I evals/scripts/summarize.py evals/results/baseline/*/
```

`--max-cost-usd` is the tool's list-price estimate ceiling per invocation.

Two settings are environment variables of `run.sh` because they change which arms run and the
wall time, not how a single run behaves (added in session B, defaults unchanged):

- `ABLATION=none` runs only the with-system arm and reuses an earlier without-system arm for
  comparison (default `with-without`).
- `CONCURRENCY=1` launches runs one at a time, so the cost ceiling is checked before each run and
  is not overrun by parallel expensive cases (default `4`).

```bash
ABLATION=none CONCURRENCY=1 evals/scripts/run.sh repo after --tag traps --max-cost-usd 8
python3 -I evals/scripts/compare.py evals/results/baseline/*/ -- evals/results/after/*/
```

`compare.py` puts the with-system arm of the "before" result dirs next to the with-system arm of
the "after" ones, per grader, plus the baseline without-system arm for reference.
