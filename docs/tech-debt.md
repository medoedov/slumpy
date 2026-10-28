# Technical debt

Technical problems found along the way that do not block the current change: pre-existing defects,
non-blocking review findings, simplifications worth doing later. Problems the user would notice go
to `backlog.md` instead. Cleanup passes (the upkeep table in `docs/agent-system.md`) work through
this list; remove an entry when it is fixed.

## Format

```markdown
### <short title>

- **Where:** file and line, or area.
- **Problem:** what is wrong and its cost.
- **Fix:** the smallest change that resolves it.
- **Found:** YYYY-MM-DD, by whom (review of <change>, cleanup pass, ...).
```

## Entries

### baseline.md describes a past rule in the present tense

- **Where:** `work/agent-system-audit/baseline.md`, section 10.2, "как требует CLAUDE.md для задач T1 и T2".
- **Problem:** the sentence was true for the measured version; read today it sounds like the current
  rule, which no longer requires the reviewer on every T1. Low cost: the current rule (`core-process.md`, Risk tiers) is always in context.
- **Fix:** "как требовал тогда CLAUDE.md".
- **Found:** 2026-10-27, final review of the post-verification changes.

### check-pointers misses pointers by skill or plan name

- **Where:** `scripts/check-pointers`, `POINTER`; examples in CLAUDE.md ("`engineering-design`
  menu, Concurrent code") and the mapping table in `work/agent-system-layers/plan.md`
  ("core-process, Where things live").
- **Problem:** only the `` `file.md`, Section `` form is parsed, so renaming the menu row or a
  core-process section does not flag these pointers.
- **Fix:** resolve skill names to their SKILL.md and accept file names without `.md`, or write
  those pointers in the parsed form.
- **Found:** 2026-10-28, layer split review, fresh round 2.

### Gate parts left out after the gates review did not converge

- **Where:** `work/agent-system-gates/plan.md`, «Left out».
- **Problem:** the session-start base (a push to `dev` in the same turn empties the change set),
  the self-test inside `scripts/check` and the hook, and the failure of `scripts/check` once an
  Xcode project exists were not shipped: the last review round found logic in them that no case
  observed.
- **Fix:** generate mutants mechanically (an `ast` walk over `check` and `check-risk` that forces
  each condition, drops each operand, removes each early return), with an allowlist of equivalent
  mutants and reasons; then bring the three parts back, each through review. The project-marker
  failure is due at the skeleton ADR at the latest.
- **Found:** 2026-10-28, gates review, fresh round 2.
