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
- **Fix:** mutants are generated since 2026-10-28 (`scripts/test-checks`, `GENERATED_FROM`); bring
  the three parts back, each through review. The project-marker failure is due at the skeleton
  ADR at the latest.
- **Found:** 2026-10-28, gates review, fresh round 2.

### check-pointers scans only tracked Markdown

- **Where:** `scripts/check-pointers`, the `git ls-files` list.
- **Problem:** a pointer in a new, uncommitted file (a new plan.md) is not checked when the Stop
  hook runs; it is checked after the commit.
- **Fix:** add untracked Markdown files (`git ls-files --others --exclude-standard`) to the scan,
  with a case.
- **Found:** 2026-10-28, review of the self-review fixes, round 1 (pre-existing).

### An untracked nested repository hides its files from check-risk

- **Where:** `scripts/check-risk`, `change_set` (`git ls-files --others`).
- **Problem:** git lists an untracked nested repository as one directory entry (`Packages/Logic/`),
  so a `Package.swift` or a Keychain call inside it passes with "evidence present". Realistic when
  a local package gets its own repository.
- **Fix:** fail on a directory entry in the change set, with the reason; the case "a nested
  repository in the change set does not crash the check" then expects the failure.
- **Found:** 2026-10-28, review of the self-review fixes, round 2 (pre-existing).

### A time in an export is written without its zone

- **Where:** the agent system; eval trap T3 (`evals/cases/traps/t3-standard-csv`).
- **Problem:** asked for a CSV export, the agent writes each session's start as local time without
  an offset or a zone column ("you did not ask for it": the Scope rule wins). Every measurement so
  far failed this trap; a tier-independent boundary rule did not change it and was removed
  (`work/agent-system-audit/baseline.md`, section 18).
- **Fix:** not known yet. Candidates: treat the representation of a value as part of correctness
  in the Scope rule, or a check once code exists (a date formatter without a zone in export code).
  Measure on T3 and D4 before keeping either.
- **Found:** 2026-10-28, measurement of the self-review fixes.
