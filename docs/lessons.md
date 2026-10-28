# Lessons

Traps this project has already hit. Add an entry only if a future implementer reading the code
would likely repeat the mistake without it. Prefer fixing at the source first: compiler, then
linter, test, skill; an entry here comes after those. Remove entries whose "stale when" has come.
An entry guarded by "this entry only" gets a test, lint rule, check, or skill within 30 days, or
is removed; `scripts/check-lessons` enforces this.

## Format

```markdown
### <short symptom>

- **Symptom:** what went wrong, as observed.
- **Cause:** the real root cause.
- **Now guarded by:** the test, lint rule, check, or skill that catches it (or "this entry only").
- **Stale when:** the condition after which this entry can be deleted.
- **Added:** YYYY-MM-DD
```

## Entries

### An adapted or generalized rule loses the condition that limits it

- **Symptom:** while adapting ub-mode and pstack principles into the agent system (2026-10-27),
  three review rounds in a row found a shortened rule that dropped its source's limiting
  condition: the code-side test check, the migration option, legitimate states for fixes, and
  the exit when no honest test is possible. It happened again on 2026-10-28 when the core was
  generalized out of the platform and project layers.
- **Cause:** shortening or generalizing a rule keeps its main clause and drops its conditions and
  exceptions.
- **Now guarded by:** this entry only. When adapting an external rule, generalizing a rule, or
  moving it between layers, list each condition and exception of the source and either keep it or
  record why it is dropped.
- **Stale when:** the agent system gets an eval case that catches a dropped condition.
- **Added:** 2026-10-27

### A rule restated in a second file drifts from its source

- **Symptom:** during the layer split (2026-10-28) platform and project lines restated core rules
  and dropped their conditions ("T2 the first time", merge on read for all data), and section
  pointers went stale after sections moved.
- **Cause:** a copy of a rule is edited, or not edited, separately from its source.
- **Now guarded by:** `scripts/check-layers` (tier labels, reviewer rules, or decision-rights text
  in the platform pack and CLAUDE.md) and `scripts/check-pointers` (section pointers that do not
  resolve), both covered by `scripts/test-checks`.
- **Stale when:** the checks have run on 10 changes to the agent system without a miss found in
  review.
- **Added:** 2026-10-28
