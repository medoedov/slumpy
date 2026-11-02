# Shared agent system and bounded work

## Brief

- Authorized on 2026-11-02: implement the audit findings and the agreed shared entry point for
  Claude Code and Codex, retaining the useful existing process and safety boundaries.
- T1 because this changes instructions and local checks inside the approved workflow; no app
  schema, network service, dependency, or product behavior changes.
- One maintained AGENTS.md; shared content remains under .claude/ to avoid an unnecessary move.
  Codex discovers three short skill adapters; its fresh review agents read the shared role.
- The installed Claude CLI is 2.1.220, so CLAUDE.md remains an import-only compatibility adapter.
  Updating the global CLI is unnecessary for this change. The old Codex mirrors are removed;
  unrelated global configuration and the frozen Git hooks are untouched.
- Review rechecks consume the original mode's two-call budget; new rounds need changed work or
  evidence. Important product questions remain open across batches of five rather than becoming
  assumptions. Domain research follows a material gap; review context loads by mode.
- Upkeep dates produce reminders, not failures or authorization to perform unrelated work.
  Invalid schedules still fail. Checks and the eval packager follow the shared entry point.
- Alternatives: a full directory relocation or generated copies add migration/synchronization
  work with no required result; keep shared sources and small adapters. A direct AGENTS-only
  entry needs a newer Claude CLI, so retain its documented import fallback.
- Keep the short brief example, risk tiers, security pass, and data-preservation requirements.

## Verification and measurement boundary

Run the document checks, deterministic self-tests, generated mutants, adapter/link checks, and
packaging smoke checks. Review the changed process, checks, and documentation in fresh context.
All paid/model-backed A/B runs are deferred until a runtime/model/budget is agreed; no claim of
quality, latency, or cost improvement follows from deterministic checks alone. Existing Claude
results remain historical and are not Codex measurements. The changes are a coordinated migration,
so a later comparison must not attribute its aggregate effect to one individual rule.

## Progress

- Read the current rules, scripts, prior measurements, and official runtime documentation.
- Confirmed installed CLI versions: Claude Code 2.1.220; Codex CLI 0.145.0.
- Implemented shared routing, process simplifications, advisory upkeep, and the matching docs.
- Removed the obsolete tracked project skill/agent mirrors; retained only three Codex skill
  adapters pointing to canonical sources. No user-wide settings or global skills were edited.
- `python scripts/check`: all five document checks passed.
- `python -I scripts/test-checks`: 245 cases passed on Windows after fixing UTF-8 Git decoding
  and replacing two illegal-on-Windows fixture names with equivalent portable cases.
- Actual Windows hook command: exit 0, no output for a clean check. Disposable eval plugin:
  shared AGENTS entry and all three canonical skills packaged correctly. Adapter metadata and
  relative source links matched; CLAUDE.md contains only the import.
- Codex CLI app-server `skills/list`: exactly the three current project adapters discovered and
  enabled, zero loader errors. This used no model turn.
- First full mutation run: 8 of 857 mutants survived; the coverage repairs below resolved them. The two Git
  subprocess mutants removed redundant text=True (encoding already implies text mode); removing
  that redundancy is preferable to an equivalence waiver. Other survivors exposed weak reminder
  boundary assertions and missing styled-section pointer cases.
- Independent review call 1 initially could not start because of the service usage limit; after
  the owner resumed, the same review was retried. This is an interrupted invocation, not a new
  review of a revised result. No review verdict was claimed for the failed invocation.
- Review call 1 (code, T1, including security and instruction/doc contracts): changes needed.
  Accepted both findings: the ledger's platform-upkeep row now says reminder, and Claude's
  permission list includes the exact documented python/python3 check and self-test commands.
  Arbitrary interpreter commands were not allowed. No other introduced defect was established.
- Coverage repairs: 246/246 self-test cases passed; all six remaining previously surviving
  mutants were killed in a targeted rerun. The two redundant text=True operands were removed;
  no new EQUIVALENT exemptions were added. The final full mutation run passed.
- Review call 2 (fresh context, code, T1, security pass): clean. Checked the two accepted fixes,
  UTF-8 subprocess behavior, strengthened pointer/date tests, and retained execution boundaries.
- All local Markdown links in the 14 active entry, runtime, skill, and knowledge files resolve.
  The documented interpreter commands have exact allow entries; main-push and frozen-hook
  restrictions remain present. After recording the mutation result, all five checks in
  `python scripts/check` passed and `git diff --check` was clean.

## Final result

- `python -I scripts/test-checks --mutants`: exit 0; all 846 executable mutants killed
  (36 written, 819 generated, 9 existing equivalent mutants excluded). The run includes its own
  clean baseline self-test; no exemption was added to make the result pass.
- Both independent review calls are complete; the final verdict is clean. The two accepted
  findings from call 1 were corrected and checked in call 2.
- Shared instructions and the agreed process simplifications are implemented. Native Codex skill
  discovery, the installed Claude compatibility route, Windows hook invocation, eval packaging,
  and active source links have been checked at the boundaries described above.
- Live task-quality/cost A/B comparisons on Claude and Codex were not run. Neither savings nor
  model behavior equivalence is claimed. A fresh conversation should use the updated catalog and
  entry point rather than the previous instructions already present in this conversation.
- The owner authorized committing and pushing the completed changes to `dev` after validation.
  No global configuration update or global CLI upgrade was performed.
