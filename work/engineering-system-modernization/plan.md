# Engineering system modernization

Task-ID: SYS-001
State: blocked
Blockers: deferred.md (live client and Mac acceptance)
Owner: Astra

## Separately authorized staged-scope closeout — 2026-11-03

The owner explicitly approved one additional narrow Astra review, then commit/push to `dev`.
This continues the review history below; neither earlier call is reset or relabeled. Source,
full diff and index hashes matched the finalization manifest before starting. `git fetch origin`
confirmed HEAD and origin/dev both at `d68d2f03dc60a6590e861605a18ea78ac714770e`; hooks remain
disabled at `/dev/null`. No unrelated changes were present.

- Independent fresh Astra, code/security T1, **one separately approved closeout: clean**.
  Scope only: index/working snapshot comparison, `--no-renames`, restored index-deleted paths
  including ignored files, the `--final` consumer and corresponding regressions.
- Ten independent minimal Git scenarios passed: hidden staged modification; restored deletion
  and rename (including ignored restorations); staged addition removed from the working tree;
  aligned staged deletion/rename/modification; unrelated unstaged edits. Real `check-risk` and
  `check --final` ran; unrelated document checks were stubbed to isolate this boundary. A first
  fixture setup error was corrected before this ten-case result; it was not counted as a pass.
- Production and index SHA256 matched before/after. Reviewer tools were write-capable under a
  no-source-edit instruction, not an enforced read-only profile. No production fix was needed;
  existing 373-case and mutation evidence still covers these unchanged scripts.
- Only the formal staged-scope review blocker is closed. Runtime, Mac/device and comparative
  model evidence remain in the same [deferred registry](deferred.md). No full audit, full
  mutation run, native hook acceptance or iOS acceptance was added by this review.
- [The manifest](finalization-state.json) records the reviewed source, independent outputs and
  pre-commit acceptance snapshot. The committed checkpoint is obtained with
  `git log -1 --format=%H -- work/engineering-system-modernization/finalization-state.json`;
  a file cannot contain its own future commit SHA. Verify after commit against the original
  task base below, then publish only an ordinary fast-forward `dev` push as authorized.
- Next: the existing RT/MAC acceptance dependencies, not another source-review round.

## Finalization continuation — 2026-11-03

Task-base: d68d2f03dc60a6590e861605a18ea78ac714770e

The owner authorized the attached finalization guide after the external audit. This is the same
SYS-001; earlier v2 evidence and review rounds below remain historical. One Astra executor owns
this bounded scope. Start: clean `dev` at Task-base above; no product or global settings changes,
push at that stage, paid model comparison, additional checkout or new deferred registry.

- T1 because these are reversible local acceptance fixes inside the existing tooling boundary.
- Scenarios: preserve current-task risk evidence through verified/archive/recheck; reject old
  moved evidence, new unidentified plans, and final acceptance without a reliable nonempty range.
  Stop feedback must distinguish document success, no changed input, and unavailable checks.
- Mechanism: compare evidence by stable Task-ID across active/archive paths; four explicit legacy
  paths; reject reactivated completed IDs from the task base. `check --final` requires an explicit
  ancestor base and refuses divergent index/working snapshots. Ordinary check stays local.
- Verification: failing regression first, complete fast suite, scoped mutations with full
  inventory validation; no unbudgeted multi-hour full run. Fresh Astra code/security review has
  its own maximum two calls for this new audit scope; fresh handoff after commit and archive.
- At the end of that stage, additional independent closeout required separate agreement. The
  owner-approved follow-up and its result are recorded above; the original review history follows.

### Pre-authorization handoff (historical)

Windows implementation and available direct checks are complete. Final ordinary suite: **373
cases pass**, 124.071s. Source/dirty-range identity and command output:
[finalization-state.json](finalization-state.json). HEAD remains the Task-base above; no project
commit, push or global configuration change. Final acceptance is document/tooling scope only.

The last independent verdict is **rethink approach**, not clean. Both calls are exhausted.
All concrete findings were reproduced and corrected with direct tests; the final staged-scope
correction, additive coverage and order-only test change did not receive a third independent
review. `core-process.md`, Review and lessons, says: “`rethink approach` or a blocking risk those
checks cannot resolve leaves the affected part unfinished” and “A revision requiring further
independent review is separate agreed work.” The literal formal closeout therefore remains open;
the remaining action is independent acceptance of this bounded correction if separately agreed,
not another known implementation defect. The accepted guide authorized the local fixes; their
execution and evidence do not relabel the independent verdict. No further review is launched.

### Finalization evidence

- Before production changes, 12 new acceptance cases plus the preserved 347 ran: **9 of 359
  failed**, 221.615s. Direct failures reproduce archive evidence loss, new active/archived plans
  without ID, missing final base after a dev commit, empty final scope, and the three full
  lifecycle variants. Historical evidence rejection and non-ancestor tests already passed.
  Initial sandbox attempts could not execute the process-cleanup regression; no test result
  inferred from those attempts. Authorized local execution supplied the red run above.
- First post-fix run: **360/361 passed**, 125.059s. Remaining failure was the old empty-error
  formatting assertion; updated to require the new explicit unavailable report (same failure
  exit preserved). Six hook expectations now require scoped messages rather than silence/{}.
- Found a related runner defect: any nonzero harness exit counted as killed. The outcome
  classifier now requires an actual completed assertion-failure summary and rejects setup/case
  errors or harness traceback. Timeout remains unavailable. Six deterministic result probes
  guard the boundary. Mutation generation and fixture/process cleanup are unchanged.
- Fast final check at this intermediate tree: all six document checks passed; 10 changed
  tracked files, zero staged/untracked. App build/tests/lint remain explicitly not run.
- Fresh committed-fixture handoff: read STATUS -> plan -> facts/Git. Astra recovered FIX-001,
  owner, verified state, base `82429f9356ecd8cd7cb51f58011ab6f5a4de1b8a`, checked commit
  `5857914b7a2ec3c23114fbadf3876d1577dce813`, scope limits and archive/recheck next step.
  No new task/owner question, unchanged clean fixture. This is a minimal synthetic Git fixture,
  not another project checkout or live root-client compaction. The archived handoff follows.
- Archived handoff: a second fresh Astra read STATUS -> archived plan -> facts/Git, recovered
  done/no blockers/no pending work and did not reactivate FIX-001. HEAD/tag matched
  `736ac359d2ff30c66e7ed317ddb16e1ba2acf4b1`; risk/state reacceptance passed at the same original
  base. Both agents distinguished persisted execution claims from their own observed Git refs.
  Both fixture trees stayed clean. These handoffs used the pre-round-1 checker candidate; they
  establish recovery from those persisted records, not a full new-session client launch.
- Review scope: finalization diff from d68d2f0 only, code T1 plus security/test pass; v2 calls
  below are historical. Call 1: **changes needed**. Reviewer independently reproduced an old
  archive renamed to another folder authorizing new risk, a risky staged payload hidden by the
  working snapshot, and a completed ID moved back to active. All three are within the accepted
  guide and were fixed. Diff-file hashes before/after review matched (11 files); the reviewer had
  write-capable tools under a no-edit instruction, not an enforced read-only sandbox.
- All three review regressions failed first (5.700s). After fixes, all three passed (6.778s).
  An intermediate run had two failures because Git's -z followed the -- path delimiter; fixing
  the shared names helper placed options before paths. Added ambiguous-history and committed
  resurrection cases. No blind retry or weakening of the assertion.
- Stopped the obsolete 21-mutant candidate run after 94.647s when review established blockers;
  no mutation score retained. Revalidated runner PID/parent/command and stopped only its tree.
  No mutation score retained; no multi-hour full run.
- Code T1 call 2, fresh Astra security/test review: **rethink approach**, repeated index/working
  snapshot class. Staged deletion and rename followed by restoring the old path escaped the
  initial mismatch calculation. Reviewer found no further concrete issue in historical Task-ID
  binding/completed state, confirmed the ndiff whitespace equivalent and six outcome-classifier
  probes. All 12 diff-file hashes matched before/after review; no root index changes.
- Within the authorized local fix scope, read staged and deleted paths with `--no-renames`, and
  detect restored index-deleted paths on disk even if ignored. No index rewrite. Deletion,
  rename and ignored restoration failed before; aligned staged deletion passed. All **10 review
  regressions passed** after (18.555s), then **372 ordinary cases passed** (102.829s).
  A superseded scoped run was stopped at 178.077s, no score retained. Taskkill reported already
  disappearing children; the following CIM query found zero remaining Python processes.
- Final scoped run on that production: **27/28 killed**, exit **1**, **1615.141s (26m55s)**.
  The survivor was `check-risk, plan_lines: 2 to 3 at column 13`: removing the first character
  from a bullet evidence line leaves accepted whitespace. This is not universally equivalent:
  valid plain `T1 because` / `Security pass:` lines break. Added one positive plain-evidence case;
  the same candidate is now **killed**, 17.397s, through unchanged `run_copy`.
- Retained all **370 prior fixture scenarios**, including expectation bytecode/defaults/closures,
  edit contents, environment and Git steps; added only the plain-evidence scenario. Moved the
  existing finalization block first. Before/after ordering have the identical **371-scenario**
  multiset SHA256 `46e9648fd21d35b87cb4239cf444c194bffb5e3b7badf19b62e12b3273ee5a7e`.
  Fixtures are independent: per-case copies and Git state; shared template read-only; the sole
  outside sentinel belongs to one case and has no other consumer. Both infrastructure checks
  remain, making the final ordinary total **373**. No assertion or exclusion was removed.
- Paired one-candidate measurement, same production/scenarios/clock and one worker using
  `run_copy`: archive-evidence-ignored **killed in 74.708s before**, **18.393s after** ordering.
  This measures one fail-fast candidate, not every mutation or model performance. The full
  28-candidate run was not repeated: evidence is **27 prior kills + 1 addressed survivor** at the
  explicit unchanged-production/retained-scenarios boundary, not a fabricated new green full run.
  All 14 old equivalence reasons remain; one narrow ndiff extra-leading-space equivalent was
  added and independently confirmed. Empty mutation selection fails with “no result”.
- Costs: final six-document check 3.928s (earlier intermediate check 9.206s); ordinary suite 124.071s;
  scoped old order 26m55s; paired/archive and survivor costs above. Historical full 102m29.6s
  remains historical and was not repeated. Fast/scoped/full triggers now have one canonical
  owner in docs/agent-system.md; timing is not coverage or an Astra quality score.
- Available runtime facts repeated: Codex CLI 0.145.0, Claude 2.1.220; user config requests
  Astra/high. Explicit Astra helper launches are not proof of the root client's effective model.
  Three discovery adapters still route to the shared skills; native trust/Stop dispatch and
  root-client compaction remain unverified. Existing RT/MAC/DEV/EVAL rows own those dependencies.

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
