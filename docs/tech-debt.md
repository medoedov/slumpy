# Technical debt

Technical problems found along the way that do not block the current change: pre-existing defects,
non-blocking review findings, simplifications worth doing later. Problems the user would notice go
to `backlog.md` instead. Cleanup passes (about every five features) work through this list; remove
an entry when it is fixed.

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

### check-layers does not assign every rule file to a layer

- **Where:** `scripts/check-layers`, `core_files` and `platform_files`.
- **Problem:** a rule file named neither in core-process.md's first sentence nor in platform.md is
  never scanned (for example a new `.claude/rules/foo.md`), and platform.md must name its files in
  the `` `.claude/rules/X.md` `` form or they leave the restating scan. The output only shows a
  smaller file count.
- **Fix:** fail when any `.claude/rules/**/*.md` is neither a core file nor named by platform.md;
  run both checks from the planned `scripts/check`.
- **Found:** 2026-10-28, layer split review, fresh round 2.

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

### check-pointers resolves a pointer by file name, not by path

- **Where:** `scripts/check-pointers`, `by_name`.
- **Problem:** a pointer such as `` `work/feature/plan.md`, Section `` is checked against every
  file named `plan.md`; when the named path is deleted, the pointer is checked against other plans
  and fails or passes by accident.
- **Fix:** when the pointer has a path, resolve that path only and report a missing file.
- **Found:** 2026-10-28, while re-verifying the gates after the last review round.
