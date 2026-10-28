# Lessons

Traps this project has already hit. Add an entry only if a future implementer reading the code
would likely repeat the mistake without it. Prefer fixing at the source first: compiler, then
linter, test, skill; an entry here comes after those. Remove entries whose "stale when" has come.

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

### An adapted or moved rule loses the condition that limits it

- **Symptom:** while adapting ub-mode and pstack principles into the agent system (2026-10-27),
  three review rounds in a row found a shortened rule that dropped its source's limiting
  condition: the code-side test check, the migration option, legitimate states for fixes, and
  the exit when no honest test is possible.
- **Cause:** shortening a source rule keeps its main clause and drops its conditions and
  exceptions; restating a rule in a second file does the same.
- **Now guarded by:** this entry only. When adapting an external rule, generalizing a rule, or
  moving it between layers, list each condition and exception of the source and either keep it or
  record why it is dropped; state each rule in one file and point to it from others. It happened
  again on 2026-10-28 when the core was split from the platform and project layers.
- **Stale when:** the agent system gets an eval case that catches a dropped condition.
- **Added:** 2026-10-27
