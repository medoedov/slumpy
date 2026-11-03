# Engineering system modernization

Task-ID: SYS-001
State: blocked
Blockers: deferred.md (live client and Mac acceptance)
Owner: Astra

## v2 continuation — 2026-11-03

Continue the existing modernization at clean `dev` HEAD `9366805`, not a second refactor.
The owner's v2 supplement authorizes this new scope; previous review rounds and evidence below
remain historical and are not reset. One writer (Astra) owns agent instructions, state and checks.

- T1 because the additions are reversible task-state validation and runtime policy within the
  existing system. No app feature, dependency, global configuration, paid run or release changes.
- Model: explicit `gpt-6-astra` executor; independent Astra review for this supplement. Terra is
  optional and remains disconnected on CLI 0.145.0; no untested profile or silent fallback.
- Data: Markdown is the source, with Task-ID/State/Blockers/Owner in new active plans, one index
  and existing backlog. Old records retain their IDs/paths except the demonstrably completed
  unified migration, which moves to completed with its references repaired.
- Boundary: a small document check validates declared IDs, plan/index links and completion
  blockers. It cannot detect semantic duplicates, prove a blocker was resolved or certify iOS.
- Scenarios: duplicate ID/plan, missing link, orphan active task, done with required blocker,
  blocked Mac handoff, and completion/archive transition. Empty or malformed state fails closed.
- P0: verify actual runtime/model and prior work; P1: state check, one deferred registry and
  fresh-context handoff; P2: keep existing useful mechanisms and report unmeasured behavior.
- Verification: check, self-tests and mutants for scripts; fresh independent review of this
  new scope (at most two calls), fresh-context handoff, exact final file identities. No model
  comparison or engineering-quality/cost claim without comparable runs.

Latest step: available Windows implementation is verified; overall acceptance is blocked
on the live-client/Mac rows in [deferred.md](deferred.md). The sections after this continuation
describe the previous commit unless explicitly labeled v2.

### v2 evidence

- `python scripts/check` with `SLUMPY_CHECK_BASE=9366805` passes six document checks.
  Build/app tests/lint remain explicitly not run. Final document-state result and file identities
  are recorded in `verification-state.json`; the script evidence is detailed below.
- Sandbox self-test attempts failed before acceptance: OS temp access denied, then `taskkill`
  denied for an owned child. Approved local execution with workspace tmp passed the process
  cleanup case; no assertion or sandbox restriction was bypassed in the implementation.
- `codex --version` 0.145.0; hooks stable/enabled; Claude 2.1.220; repository Git hooks `/dev/null`.
  Read-only user config is Astra/high; explicit executor spawn is Astra. No global edits.
- Read the three source-routing adapters and current shared role. Stable reading-day decision
  remains ADR-0001; no new app code or approved product fact. Archived only the completed unified
  migration; other old work folders remain identified as historical in STATUS.
- Independent review and fresh-context handoff are recorded below; the previous commit's clean
  review is not relabeled as review of this supplement.

### v2 review and handoff

- Code T1 call 1, fresh explicit Astra, verdict `changes needed`: in-memory execution reproduced
  a fail-open parser class. Compact/indented Markdown rows bypassed duplicate detection; empty
  duplicate metadata declarations were ignored. Fixed recognition once in a shared row parser,
  count every field declaration before validating its value. Added canonical/compact/indented/
  no-outer-pipe rows and all four empty/spaced duplicate-field regressions. Targeted state plus
  check-integration suite: **105 passed**. Explicit-base check: six pass; diff whitespace check pass.
- Previous expanded full suite: **309 passed**. The first mutation run was stopped incomplete
  after 87.74 seconds when review found the parser gap; no score retained. Revalidated only its
  Python PID/parent/command before terminating that tree. Subsequent process listing found no
  remaining Python workers under the task's tmp path. The later completed run is recorded below.
- Fresh-context handoff passed before the reviewer read the diff: recovered SYS-001, Astra,
  blocked state, the earlier verified snapshot versus tests still running, next explicit-base
  command, Mac/live-client dependencies and the approved 04:00/start-day/stored-zone contract.
  Observed reads: STATUS -> plan -> ADR; all three adapters -> shared sources -> patterns reference.
  No owner question or duplicate task. This is a fresh subagent test, not actual compaction or
  cross-client root-session proof. Tree hashes before/after review were identical (342 files).
- Wrong-premise probe: reviewer rejected response caching after two stipulated failed fixes and
  identified separate durable effect/marker transactions. Crash after 600->660 before marker,
  then retry ->720; recommended atomic operation identity+effect without weakening acceptance.
  Actual unchanged fixture runs: reference **10 pass**, 7.605s; faulty exits 1 with four failing
  methods/six assertions, 8.779s. This diagnoses the planted premise and weak-test case; it is
  not an autonomous before/after implementation run or model-quality comparison.
- Remote duplicate check: read-only `gh issue list` and `gh pr list`, open state, both returned
  empty arrays. Initial sandbox network attempt was unavailable; approved read succeeded.
- Code T1 call 2, fresh explicit Astra, verdict **clean**. Reviewed the parser fixes, affected
  integration and open invariants; 26 additional in-memory probes passed (normal row variants,
  duplicate IDs/fields and malformed IDs). Both v2 review calls are used; original commit review
  budget remains unchanged. Tree hashes before/after call 2 were identical. This is source review,
  not live-client/Mac acceptance. Subsequent changes added only acceptance cases and final evidence;
  those additions were checked directly within the exhausted review budget, not by a third review.

### v2 final script evidence and handoff

- Full standalone suite before mutation: **330 pass**, 68.0148s. Completed full mutation run:
  **1053/1081 executable mutants killed**, exit **1**, 6149.616s (102m29.6s). Inventory: 38 written
  +1057 generated -14 existing equivalents. All 28 survivors concern the new check-state;
  no stale entry or survivor in an older checker. No files changed during that run.
- Added **17 cases**, retaining the earlier 330 cases, their order and all production/runner
  logic. Full ordinary suite: **347 pass** (266 existing, 3 new check-integration, 78 state cases).
  The additions isolate archive/ID/state violations from other guards, validate error diagnostics,
  minimal rows, identifier boundaries, table separators, scoped plan discovery and file fragments.
- Addressed every survivor label with the unchanged `run_copy` and four workers: **29/29
  candidates killed**, exit 0, 927.817s (15m27.8s). One label maps to two AST variants, so both
  were checked; this covers 28 prior survivors plus one ambiguous already-killed candidate.
  No new equivalent exemption. This is a **composite result**, not a second green full run.
- Removing only the new 17-case block reconstructs the exact full-run test-source SHA256.
  All production-script hashes are unchanged. Detailed hashes and raw output:
  [script-verification.md](script-verification.md), [v2-mutation-results.txt](v2-mutation-results.txt).
  Old kills remain applicable at that explicit boundary; an arbitrary future script change does
  not inherit this result. Temporary task Python workers after completion: **0**.
- Available source checks and fresh-agent handoff are complete. Native root-client Stop/trust,
  actual compaction/cross-client continuation, Terra CLI and Apple execution remain unverified
  as listed in deferred.md. SYS-001 stays blocked and its folder stays active; do not open a
  duplicate migration or mark the iOS app done. Next: RT-01/RT-02 when a suitable live client is
  available, then MAC-01 and its dependent rows on the configured Mac.
- No commit, push, publication, global configuration update or paid model run. No product scope
  or approved reading-day fact changed. Restore only this supplement against clean base 9366805
  if reverting, preserving unrelated later work and keeping frozen Git hooks disabled.

## Brief

- T1 because this changes reversible local tooling and shared engineering guidance within the
  existing dual-runtime architecture; no product scope, dependency, storage decision or release.
- Baseline: `dev`, `d4d87c32c75fb70834a4e582b880a067440044d6`, clean index/worktree/untracked state.
  Git preserves tracked originals; no user configuration is changed. No checkout/worktree added.
- Boundaries: one shared process, existing check entry point, runtime-specific completion feedback;
  eval packaging and disposable engineering fixtures remain outside the product.
- Scenarios: unsafe output path rejected without deletion; actual evaluated inputs identifiable;
  committed and dirty task changes checked against an explicit task base; blocked verification
  never reported as app acceptance; first implementation followed by a change preserves data.
- P0: diagnose tools and checks, reproduce and repair concrete safety/evidence defects.
  P1: repair demonstrated process gaps, add executable outcome cases and fresh review.
  P2: retain unmeasured procedures unless a concrete correctness gap justifies a policy correction.
- Acceptance: deterministic checks pass; independent code/security review; evidence separated into
  infrastructure, live integration and engineering outcomes. Unavailable runtime/build evidence is
  recorded, not inferred from configuration or historical scores.
- Budget: no paid model/API runs, global installs, user settings, push or publishing. Before/after
  behavior comparisons require identical model/settings and the existing +25% cost ceiling; no
  quality/cost improvement claim from this coordinated unmeasured policy migration.

## Progress

2026-11-03: read the attached one-time brief, shared process/platform/agent-system rules, Project
Knowledge, engineering-design, reviewer, lessons and existing eval/check implementations.
Original snapshot matches; no restore archive needed for the initially clean tracked state.
Confirmed arbitrary deletion in eval packaging and task-base ambiguity in risk checks. Delegated
disjoint tooling fixes and a disposable engineering fixture; independent review follows changes.

## Verification and review

Runtime/source observations and disposition: [audit.md](audit.md).

- Packaging after review fix: initial sandbox run 7 cases, 5 passed and two skips. Approved local
  execution then passed **6 of 7**, with only symlink creation unavailable, exit 0, 31.706 seconds;
  the real junction guard passed. Python 3.12+ is enforced before filesystem work.
  Existing/outside paths preserved; same HEAD with changed payload changes digest; repeated payload
  stable. Current repository packaging passed. Git Bash wrapper plus run.sh exercised with a local
  stub evaluator: package/manifest created, zero-run collection succeeded, evaluator exit 7
  propagated as exit 7. No model/network invoked. Real Claude and v0 network path not verified.
- Engineering fixture after review fixes: initial 4 passed / 6 explicitly skipped; full reference
  10 passed, exit 0 (71.453 seconds). Planted-fault final run returned 1 as expected: 10 methods,
  6 successful and 4 failing (6 assertion failures including subcases), 100.954 seconds. Earlier seven-test run
  detected crash/retry double correction (720 rather than 660 seconds), but missed the validation
  defects found by review. These are harness outcomes, not model scores or Swift tests.
- Review: code mode, T1, call 1, security/test pass, verdict `changes needed`. Confirmed Python
  3.10/3.11 junction guard gap and oracle/acceptance omissions for conflicting completion IDs and
  non-integer corrections. Fixed both at source plus regression tests. Code mode call 2, including
  new process-tree cleanup and affected callers, verdict `clean`; no findings remain. This is
  independent source review, not a substitute for final checks. Reviewer performed no mutations.
- `scripts/check`: all five document checks passed after increasing per-check timeout from 15 to
  45 seconds and both hook budgets to 300 seconds; the earlier timeout was unavailable, not green.
  Direct Windows hook command from `evals/` resolved the root and returned exit 0 / `{}`. This
  verifies command invocation, not native lifecycle dispatch or trust.
- Self-tests: `python scripts/test-checks` passed **263 cases** (246 historical, seven explicit-base,
  nine Codex-hook/unavailable-check cases, one separate-session descendant cleanup regression).
  First `python scripts/test-checks --mutants` was stopped incomplete after its baseline passed.
  Inspection found the new timeout case edited an exact source literal; boundary mutants could
  fail fixture setup and be credited incorrectly. No mutation score retained. Replace the brittle
  setup with simulated-duration outcome probes and rerun the final tests. Production checks unchanged.
  Preflight confirmed baseline45 succeeds, limits44/46 and a missing limit fail behavioral
  assertions. Two written zero-return-code mutants are rejected. Four internal nonzero-code
  +/-1 variants are proven equivalent because every caller tests only zero/nonzero; narrow
  reasons recorded in EQUIVALENT, no timeout exemption. Added a related-but-nonancestor base
  case that catches removal of ancestry validation. Restarted inventory: **264 cases, 895
  executable mutants** (38 written + 870 generated - 13 equivalents). That full run completed
  with exit 1: 892/895 killed in 4913.51 seconds (81m 53.5s). Three survivors were investigated:
  the crash-response argument is redundant when error=True; two others exposed missing acceptance
  cases for a leading-dash Git ref and an ambiguous object prefix resolved specifically as a commit.
  Production behavior stays unchanged; added those two regressions and one narrowly documented
  equivalent. Final full case suite: **266 passed**; targeted survivor variants: two killed and
  one confirmed equivalent, exit 0. All 14 equivalent keys match exactly one variant. No temporary
  Python check workers remained. Do not relabel the
  original exit-1 run as a successful rerun of the revised inventory.
- Explicit final-task-base check passed all five checks (26 changed files then); build/app tests/lint
  explicitly not run. Final file identity is recorded in `verification-state.json`, excluding only
  that artifact itself and ignored scratch outputs. Baseline `scripts/check` completed while workers
  had already changed two files, so it is not presented as a clean baseline measurement.
- Final explicit-base `python -I scripts/check`: all five document checks passed, 30 changed
  files, exit 0. `git diff --check` passed (line-ending normalization warnings only). HEAD remains
  the initial commit; index is empty and no push/commit was performed. Final state capture and
  check are repeated after this evidence entry so the recorded file hashes cover this report.

## Policy changes and preserved conditions

Technical ownership keeps the product/external-action boundary. Compaction keeps previous changed
files, step, check result and findings, adding goal/rationale/task-base/input-state. Platform build
rule still requires Apple tools, replacing the inaccurate cloud exclusion with observed capability.
Review still excludes unrelated old bugs and retains two calls; changed-scenario safety and
revision-induced downstream evidence are explicit exceptions. Memory guidance retains minimal
extensions without upgrading anecdotal reports to an Apple limit. No brief/ADR/evidence requirement
weakened; no product hypothesis changed. Behavioral and cost effect remains unmeasured by policy.
The reviewer output heading was also aligned with the new pre-existing-blocker exception; it no
longer labels all such findings non-blocking by construction.

## Additional demonstrated safety findings

- Local `.git/config` had `core.hooksPath=.githooks`, despite documentation saying disabled.
  Reading pre-commit confirmed it calls the prohibited old external converter with `--apply`.
  Set only this repository's value to `/dev/null`, confirmed by `git config --show-origin --get
  core.hooksPath`; frozen hook files remain untouched. The old
  local value is recorded here for recovery, but re-enabling it would restore the demonstrated risk.
- Old orphaned `check-upkeep` processes explain part of host contention. Initially left untouched;
  later identified exactly 30 from deleted disposable `case*/scripts/check-upkeep` paths with
  absent parents and prior-session creation times. Revalidated each PID/command/parent before
  stopping only that set at 09:12:42 Moscow time on 2026-11-03; no unknown workload stopped.
  The parent-only self-test timeout reproduced a surviving child. Added bounded process-tree
  cleanup and a separate-session descendant regression; POSIX implementation is not executed on
  this Windows host. This is a scope refinement supported by evidence, not a new orchestrator.
- After code review, preparation of the local runner smoke exposed the same unsafe cleanup class
  in `evals/scripts/collect.py`: tracePath selected a directory for recursive deletion with only a
  basename-prefix test. Regression first failed by deleting a sentinel in a disposable fixture;
  after removing automatic deletion, the same test passed (0.450 seconds), retaining the trace,
  sentinel and all extracted fields. Repeated Bash stub run on the final collector returned exact
  exit 7, confirmed via PowerShell LASTEXITCODE and process exit. This is a local source fix with direct checks within the exhausted review
  budget; the earlier clean source review does not cover this later change.
