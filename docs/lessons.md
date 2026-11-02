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
  in the platform pack and AGENTS.md) and `scripts/check-pointers` (section pointers that do not
  resolve), both covered by `scripts/test-checks`.
- **Stale when:** the checks have run on 10 changes to the agent system without a miss found in
  review.
- **Added:** 2026-10-28

### Hand-picked mutants overstate how much the self-test covers

- **Symptom:** in four review rounds of the gates (2026-10-28) each reviewer's own mutants survived
  the self-test while the author's list was fully killed: 12 of 18, 22 of 24, then 3 fail-open
  survivors. Three parts were left out because the review did not converge. It recurred in the
  self-review fixes (2026-10-28 and 29): reviewer mutants survived while the written list was fully
  killed; the first generated run found 133 of 602, and reviewer mutants of kinds the generator
  does not make still survived (11 of 75).
- **Cause:** the author of the cases also picked the mutants, so both share the same blind spots;
  state and caches added skip paths that no case exercised.
- **Now guarded by:** this entry only. Partial help: `scripts/test-checks --mutants` also
  generates mutants from the code of every check with the operators its comment lists, and
  `EQUIVALENT` holds only mutants equivalent on every input; mutants of any other kind depend on
  cases and reviewers.
- **Stale when:** the generated mutants have run on 10 changes to `scripts/` without a reviewer's
  own mutant surviving.
- **Added:** 2026-10-28
