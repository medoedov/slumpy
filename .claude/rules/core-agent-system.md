---
paths:
  - "CLAUDE.md"
  - ".claude/rules/**"
  - ".claude/agents/**"
  - ".claude/skills/*/SKILL.md"
  - ".claude/settings*.json"
  - "scripts/**"
  - "docs/agent-system.md"
---

# Changing the agent system (core)

The rules below apply to any project; `paths` above lists this project's agent-system files and is
set per project. The agent system is the always-loaded rules, path rules, skills, agents, hooks,
settings, and checks; the project facts a skill holds are not mechanisms.

- Choose the mechanism in the order `core-process.md` gives (Review and lessons). Delete a rule
  the agent would follow without it.
- Each mechanism has a row in the mechanism ledger (CLAUDE.md names the file): the error it
  targets, its kind, what is known, the measure, and the result that removes or changes it. A
  change that adds, changes, or removes a mechanism updates its row in the same change.
- A change to what the agent does is measured against the previous version on the same cases,
  model, and settings, one change per variant; grade the result, not the path, and fix errors in
  the cases before measuring. It stays if correctness is not worse, no case flips to a failure
  without an explained cause, and cost grows by at most 25%. A mechanism that makes no measurable
  difference is removed, unless both versions are at the ceiling of the cases (then the first three
  conditions decide) or its ledger row keeps it by policy. A change the cases cannot exercise says
  so in its plan and stays until the measure its ledger row names decides. Thresholds are set
  before measuring, never after the results.
- When the main model changes, the measurements describe the old model: run them again before
  relying on the ledger.
- Regular upkeep (the ledger file lists each task, its interval, and when it was last done): do a
  due task in its own commit and update its date there.
