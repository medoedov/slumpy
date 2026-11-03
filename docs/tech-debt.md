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

### Full mutation-run cost and sparse progress evidence

- **Where:** `scripts/test-checks`, mutation runner; SYS-001 v2 script-verification record.
- **Problem:** the completed 1081-variant run took 6149.616 seconds on Windows and emitted results
  only at the end. One survivor label named two distinct AST variants, requiring both to be
  rechecked. This is measured verification cost and limited trace precision, not model latency.
- **Fix:** at the next test-infrastructure change, measure fixture/setup/check cost and consider
  narrow progress/variant-identity improvements while preserving isolation and every accepted
  case. No runner refactor or optimization is part of SYS-001 v2.
- **Found:** 2026-11-03, complete mutation run and targeted follow-up for SYS-001.

### baseline.md describes a past rule in the present tense

- **Where:** `work/agent-system-audit/baseline.md`, section 10.2, "как требует CLAUDE.md для задач T1 и T2".
- **Problem:** the sentence was true for the measured version; read today it sounds like the current
  rule, which no longer requires the reviewer on every T1. Low cost: the current rule (`core-process.md`, Risk tiers) is always in context.
- **Fix:** "как требовал тогда CLAUDE.md".
- **Found:** 2026-10-27, final review of the post-verification changes.

### check-pointers misses pointers by skill or plan name

- **Where:** `scripts/check-pointers`, `POINTER`; examples in AGENTS.md ("`engineering-design`
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
- **Update 2026-11-03:** commit `9366805` added an explicit task-start base via
  `SLUMPY_CHECK_BASE`; do not reimplement that fix. Automatic session-start capture and the other
  two deferred parts remain distinct, unshipped work.

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

### Self-test gaps that reviewer mutants found

- **Where:** `scripts/test-checks` and the checks it tests.
- **Problem:** in the last review of the self-review fixes 11 of 75 reviewer mutants survived, all
  of kinds the generator does not make; the code they change predates the fixes. Inputs that slip
  through: two pointers on one line, the second wrong (`finditer` cut to the first match); a
  multi-line file with a text trigger (`any` turned into `all`); a skipped prefix (`.claude/`,
  `work/`, `evals/`) holding a non-Markdown violation such as `work/spike/Package.swift`; a lesson
  without `Symptom` or `Stale when`; `evals/results/` in `check-pointers`' frozen list (the
  self-test does not copy `evals/`); `origin/dev` and `dev` both present and different; a
  bare-name pointer whose section exists only in a later file of that name; an upkeep header row
  without a trailing `|` (`startswith` turned into `endswith`). Logic inside f-strings is not
  mutated (`check-pointers`, `check-layers`, `check-lessons`, `check-risk`). The case "an upkeep
  date without dashes" was removed: from about 2026-11-27 it could not tell a compact date from
  an overdue one.
- **Fix:** a case per input; the date case asserts the message ("the last date YYYY-MM-DD");
  consider generator operators for builtin swaps (`any`/`all`), `finditer`, collection elements,
  order, and `startswith` against `endswith`; keep logic out of f-strings. Then state in the
  generator's comment, ledger row 26, and the lesson that the generator covers only the operators
  it lists.
- **Found:** 2026-10-29, review of the self-review fixes, fresh round 2.
