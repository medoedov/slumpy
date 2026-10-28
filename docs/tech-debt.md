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
