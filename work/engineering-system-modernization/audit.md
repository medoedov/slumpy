# Runtime and mechanism audit — 2026-11-03

## Targeted engineering capabilities, 2026-11-03

Continuation at `4b0418592990e025a4c9ff2fdd03c95c6fc4ee5d`, following the owner's separate
A–D request. This section is a bounded evidence check, not a new general audit. Current local
verification and the concrete data-loss reproduction are in the latest plan section.

| Ability | Existing mechanism | Demonstrated evidence | Still unverified |
|---|---|---|---|
| A: challenge a premise | core-process decision rights; engineering-design material-unknown research and explicit assumptions; reviewer verifies claims | Historical v2 wrong-premise probe rejected response caching and diagnosed non-atomic effect/marker writes; current examination rejected the fixture's claim that a stage switch establishes an old version | That probe supplied the two failed fixes. It did not show autonomous recovery from the agent's own two failures, nor a matched Astra benefit over native baseline |
| B: systemic consequences | design data model/identity/ownership, also-affected readers/writers and migrations; concurrent-code transaction boundary; old-store test in core-process | Actual SYS-001 review found index/worktree/ignored-restoration effects outside the apparent document payload. Current cross-version counterexample demonstrates another missed boundary: ten same-version passes can hide loss of all old records; frozen initial acceptance now detects it | Real app data migration, Swift actors/reentrancy/cancellation, power-loss durability and future-change cost; no app skeleton/Mac evidence |
| C: revise own decisions | core-code first-cause repair and direct premise test after two failed fixes; reviewer repeated-class/rethink verdict; bounded review history | SYS-001 recorded two rounds, a recurring staging class, source correction and separately authorized narrow clean closeout with ten independent probes. Earlier acceptance integer-coercion and immutable-ID defects were corrected after external findings | No controlled longitudinal model run. That history required extra owner authorization for review and does not prove the policy caused better reasoning, automatic convergence or cost savings |
| D: external correctness | caller-visible/behavioral tests in core-code, fresh-context reviewer, immutable external acceptance in engineering protocol | Prior independent probes found defects after the author's checks. Current direct old-store assertion fails while the old ten-test suite passes; updated acceptance distinguishes compatible and incompatible versions without changing candidate requirements | This task's new test was written/checked by the same main executor under the explicit no-new-agents constraint, not freshly independently reviewed. One public fixture is not broad independent correctness or Swift competence |

Inspected actual sources and historical trace `evals/results/selfreview-final/20261028T221826Z/`:
the metadata says Claude 2.1.312 / Opus 5.5, ablation `none`, two text answers, not current Astra.
The first t1 response explicitly says its Swift was not compiled. Its recorded durations/costs
(575s / $1.6070638 and 156s / $0.4471476, excluding separate judge cost) are historical telemetry,
not a present with/without comparison. Role/skill invocation and generated code are not execution
evidence. The v2 wrong-premise observation is retained in the plan; this continuation did not
rerun that reviewer or manufacture a new independent verdict from the old one.

**Demonstrated weakness and disposition:** the evaluator used the follow-up executable to create
its alleged initial database. A candidate redirecting every database path to `.v2` passed all
ten checks but opened an actual previous-version store as empty. This justified one tool fix:
`--initial-candidate`, a visible same-version scope label, and two regression tests. They preserve
the original ten contract tests and reject the concrete incompatible-upgrade candidate. Frozen
initial dependencies must also be preserved; copying a wrapper around mutable code is insufficient.

No added always-loaded rule, role, review round, abstraction mandate, research requirement or
product change is justified by this evidence. The existing A–D rubrics already cover the intended
behaviors. Global strengthening of Clean Code/SOLID/DRY/KISS would add unmeasured prompt cost.
The only measured improvement is the local acceptance boundary: a known data-loss implementation
changes from false green to red; a compatible frozen/current pair stays green. The final regression
run took 44.360s across three acceptance suites. There were zero new model comparison calls and
zero new agent calls; model quality/token/dollar deltas are unavailable, not zero-cost evidence.

The [pilot](../../evals/engineering/pilot.md) is ready as fixed prompts, observable criteria and
executable acceptance, with a proposed two-sequence/six-submission allowance. Native baseline
context isolation and subscription execution remain unverified. No paid/subscription budget was
found in the new request or current EVAL-01 record; permission for the previous Git push/review
does not authorize this matrix. A C opportunity may not occur in a small successful pilot.

Mac work remains MAC-01..06 and DEV-01 under the single [registry](deferred.md), especially actual
Swift/toolchain, real persisted-store upgrade and concurrency tests, simulator/04:00/DST/travel
and device boundaries. RT-01/02 remains live-client acceptance. No further methodology optimization
or new audit is required by this report; stop after the available checks and resume product work
when requested.

## Evidence boundaries

This is a coordinated tooling/policy correction, not an experiment demonstrating a stronger
model. Initial HEAD was `d4d87c32c75fb70834a4e582b880a067440044d6` on `dev`, with no staged,
unstaged or untracked changes. Historical component scores remain historical. Current source
changes are recoverable with Git; no user settings, paid runs, global installs or remote changes.

| Capability | Observed | Limit / next proof |
|---|---|---|
| Active surface | Codex Desktop 26.1027.51404, build 23880, prod; Windows, PowerShell, workspace-write, automatic approval review | App connector reported version and up_to_date; orchestration location not exposed; do not equate CLI with Desktop |
| Model | User config says `gpt-6-astra`, medium; no top-level instruction override found | Config is not proof of this session's exact backend model/effort; context budget and consumption not exposed |
| CLI | `codex --version`: 0.145.0; `claude --version`: 2.1.220 | Version probes are not model calls |
| Hooks | `codex features list`: hooks stable true; project trust entries trusted | Each new hook definition still needs native trust review; no bypass |
| Global context | Three project adapters present in live skill catalog; shared sources read; broader installed catalog also present | Shared project workflow takes precedence over generic installed procedures; no global cleanup authorized |
| User hooks | User hooks JSON contains SessionStart; inline hooks table contains state, no Stop handler | User configuration unchanged; no observed Stop conflict, not proof of every plugin's behavior |
| Git hooks | `git config --show-origin --get core.hooksPath` returned local `.githooks`; pre-commit calls old converter | Concrete configuration drift; disable repository-local setting to `/dev/null`, frozen files untouched |
| Instructions | Provided AGENTS entry, explicit core/platform reads, adapter relative source paths resolve | This turn proves reads, not a fresh root-session discovery test |
| Tools | Python, Git, shell, web and fresh subagents available; global MCP name `node_repl`; repo `.mcp.json` declares Context7 | No Context7/Xcode tools in active catalog; declaration is not activation |
| Apple execution | `shutil.which`: no swift or xcodebuild; Windows host | App build, Swift tests, simulator/device UI and resource measurements unavailable |
| Review | Fresh subagent supported; shared reviewer role can be passed explicitly | Workers inherit write-capable workspace: read-only instruction is not an enforced sandbox |
| Continuity | Goal, decisions, task base, modified paths and verification state now named in compaction contract | Cross-client continuation still requires a live smoke run |

Shell startup is unusually slow in this session; Git Bash additionally fails before execution
with `NtCreateDirectoryObject 0xC0000022`. Neither is evidence of poor architectural reasoning.
Codex version probes warn that PATH-alias/temp cleanup under the user directory was denied; no
permission bypass or global repair attempted.

Later controlled verification: an approved unsandboxed local test ran Git Bash with a stub
evaluator (no model/network): packaging and collection succeeded, stub exit 7 propagated exactly.
The real Windows junction test also passed outside the sandbox; symlink creation still lacked
privilege. Initial sandbox errors remain environment failures, not evidence that Bash is absent.
The collector's unsafe trace-directory deletion was reproduced and removed after the final review;
its direct regression passes, but the earlier review verdict is not attributed to this later fix.

## Findings and disposition

| Symptom | Hypothesis / observation | Local action | Control / limits |
|---|---|---|---|
| Arbitrary eval output removed | `rm -rf "$OUT"` precedes variant validation | Exclusive creation in a bounded generated directory, no deletion of existing output | Filesystem regression cases, including direct invalid calls |
| HEAD identifies dirty package incorrectly | Builder copies working files but writes only HEAD | Hash actual package files; retain source metadata | Same HEAD / changed content must yield different digest |
| Failed eval can look successful | Pipeline status discarded before final successful echo | Propagate evaluator failure | Git Bash stub integration returned exact exit 7; live model execution unverified |
| Committed work on dev can vanish from risk diff | Default merge-base may equal HEAD | Explicit task-start base for acceptance | Dev/feature, staged/untracked and invalid-base regressions |
| Codex has no project Stop adapter | Current docs and CLI feature support confirmed | Small protocol adapter over shared checks; native trust remains required | JSON contract tests are not a live Stop event |
| Cloud label used to deny builds | platform.md said cloud cannot build | Test host/tools rather than surface label | No available Apple tools here |
| Old bug never blocks / recheck ignores affected callers | Review rules exempt unsafe changed scenarios and downstream regression | Narrow exceptions tied to the changed acceptance contract | Policy retention pending engineering cases; keep two-call budget |
| Founder must foresee technical omissions | Ownership implicit, continuation handoff incomplete | Explicit technical completeness and recoverable goal/state | Unmeasured behavioral correction; no quality claim |
| Numerical extension limit looks guaranteed | Rule cites unspecified developer reports | Mark anecdotal, require device measurement | No new Apple limit invented |

Retained pending comparison: T1 brief (owner-approved), alternatives only for T2, per-element
justification, 10x/100x prompts, primary-source standard checks, UI screenshot matrix, three skill
descriptions and one reviewer. Their cost is not demonstrated by this task. Concurrent independent
facts recipe is not generalized into a new storage decision. No forced skill shortening, role
merger, effort increase, framework install or new memory system.

## Sources and external candidates

Read on 2026-11-03. These are sources for mechanisms, not comparative Slumpy measurements. No
third-party source code/skill imported, so no new dependency or redistributed license obligation.

| Source / scope read | Existing mechanism / possible contribution | Decision, cost and verification |
|---|---|---|
| [OpenAI Astra skills guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), article | Addressed loading, explicit local autonomy | Retain three adapters; explicit scope/completion correction. Compare behavior before narrowing descriptions |
| [OpenAI current model guide](https://developers.openai.com/api/docs/guides/latest-model), API guidance | Effort/authority guidance | Do not overwrite client system prompt or assume API settings equal Desktop settings; calibration deferred |
| [Codex hooks](https://learn.chatgpt.com/docs/hooks), schema/trust/surface sections | Shared check with separate Stop protocol | Adapt; `commandWindows` exists, hook definitions require trust. Local command hooks are unsupported under cloud orchestration even with local tools; active Desktop mode unverified |
| [Claude best practices](https://code.claude.com/docs/en/best-practices) and [hooks](https://code.claude.com/docs/en/hooks), check/context/Stop sections | Existing addressable knowledge, tests, bounded hook | Retain Claude additionalContext: current docs explicitly support it. Do not silently substitute Codex schema |
| [single-agent-loop-kit Fold](https://github.com/anthropics/single-agent-loop-kit/blob/release/skill/steps/03-fold.md), step only | Duty transfer and neighboring-chain checks | No surplus project roles to fold. Retain reviewer; no code imported or claim of full kit audit |
| [Superpowers debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md), individual skill | Reproduction, hypothesis, root cause already in core-code | Retain existing narrower process; no complete package or fixed architecture verdict by attempt count |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin), README only | Lessons/references already exist | No second knowledge store; full plugin audit/installation unnecessary |
| [Spec Kit](https://github.com/github/spec-kit), README only | Existing spec/plan/ADR links | No parallel constitution or framework; test outcomes against requirements |
| [Swift Agent Skills](https://github.com/twostraws/Swift-Agent-Skills), catalog only | Potential targeted Swift references | Defer until an actual implementation knowledge gap; catalog inclusion is not endorsement |
| [Apple Xcode table](https://developer.apple.com/xcode/system-requirements) | Dated toolchain note | Table now lists 27.2 / Swift 6.4 / iOS 27.2; record as source observation, verify installed release on Mac |

Apple UIKit Markdown retrieval returned unsupported content-type in the browser tool. A targeted
follow-up opened the [Apple Frameworks Engineer clarification](https://developer.apple.com/forums/thread/838637)
and confirmed that the compatibility-key behavior depends on the build SDK, including when the
deployment target is older. The Swift rule now cites it. No platform-upkeep date advanced on this
partial audit. Opus/Fable tuning and
historical author essays do not change a local decision here; no unsupported superiority claims.

## Three levels of acceptance

Infrastructure: final commands and counts belong in plan.md. Integration: adapter discovery in
this session, CLI version/features and schema tests; fresh root Stop/trust and Claude integration
not yet demonstrated. Engineering outcomes: disposable fixture reference/fault discrimination,
not an autonomous model comparison, app test, Swift compiler test or UI/resource measurement.

Use evals/engineering for the future same-input comparison and initial/follow-up sequence.
Critical pass-to-fail regressions reject a variant; retain +25% cost policy and record unavailable
telemetry instead of estimating tokens from quota. No run here establishes equivalence to a human
engineer or explains old Codex failures without comparable traces.

## Product/platform coverage triggers

No app feature is added by this audit. Apply the following when its first implementation exists:

| Area | Existing coverage and next evidence |
|---|---|
| Session lifecycle | Design scenarios/core tests; test interruption, restoration, duplicate finish and elapsed-time source in the logic package |
| Reading day | ADR-0001 remains authoritative; executable calendar cases for 04:00, DST, crossing midnight and immutable travel history on Swift |
| Local data | Migration rule and storage fixture; disk-full, interrupted writes, real previous-schema store and concurrent writers at storage implementation |
| SwiftUI | Swift rubric plus design interface row; verify state ownership, list identity, scene/task lifetime against actual UI |
| System capabilities | Existing T2 and security triggers; permission denial, entitlements, background limits and physical-device evidence before blocking feature acceptance |
| Interface | Approved reference and primary/error flows, Dynamic Type, VoiceOver, themes and OS coverage at UI implementation |
| Resources | Use realistic launch/list/storage workloads and measured memory/energy; no numerical extension budget from anecdote |
| Network/accounts | Deferred in architecture; contract/offline/retry/auth/data-egress checks before first integration |
| Release | Deferred until skeleton/delivery; signing, privacy, diagnostics and compatibility evidence before TestFlight/store action |

## Ledger wording archived during finalization — 2026-11-03

Historical snapshots below preserve the prior measurements and reasons. Current rules
are only in docs/agent-system.md and the sources its ledger names.

### 2026-11-03 corrections to existing entries

These update the rows below; earlier measurements remain historical. No same-model behavior/cost
comparison was run for this coordinated migration. Policy changes stay pending the named measures,
not as measured improvements.

- **1, 21, 27:** core-process explicitly owns technical completeness and preserves goal, rationale,
  task base and verification state at handoff. Measure omitted technical obligations, false
  completion and repeated research in the engineering cases; revert/narrow if no benefit at equal
  correctness or cost exceeds the existing +25% policy. Shared adapters/descriptions unchanged.
- **6, 8:** reviewer checks affected callers/invariants after fixes and allows a demonstrated old
  defect to block acceptance of the changed scenario. Two-call limit retained. Kept by correctness
  policy until follow-up-change cases test escaped regressions; unrelated old defects do not block.
- **17:** tool availability is observed, not inferred from “cloud”; extension memory reports are
  explicitly not a guaranteed limit. Updated toolchain source observation, not full platform audit.
- **19:** explicit task-start base supplements the default comparison. It is a record-presence gate,
  not proof of substantive decision/security review. Measure committed-dev/feature and dirty cases.
- **20:** Codex adapter uses the same checks with separate JSON feedback; native trust and fresh
  Stop dispatch still unverified. Measure pass/fail/fix/crash/timeout/empty/repeated Stop; no acceptance
  from exhausted continuation. Keep explicit verification for unsupported surfaces.
- **26:** new deterministic regression and protocol cases supplement historical operators. Final
  self-test/mutation counts and execution limitations are in the current plan; no score inflation
  from unexecuted or skipped cases.


### Superseded row evidence

| # | Mechanism | Where | Error it targets | Kind | Known so far | Pilot measure | Remove or change if |
|---|---|---|---|---|---|---|---|
| 31 | One task index with checked transitions | `work/STATUS.md`; `scripts/check-state`; `scripts/test-checks` | Duplicate IDs, orphan plans, forgotten blockers and completed work reappearing | gate plus semantic handoff | SYS-001 v2: 347 total cases pass; composite mutation evidence and fresh Astra handoff in active plan; semantic truth, unmarked legacy plans and remote consistency are outside the lint | Fresh agent restores ID/decision/last evidence/next step; blocked-to-completed fixture; false positives | A real transition bypasses a check or >1 false positive in 5 changes: repair/narrow, no task database |
| 1 | Decision rights, product questions with recommendations | core-process; `product-spec` | Owner turned into a tech lead | prose | 2026-11-02: questions are batched at five per message; material decisions stay open until answered. The new multi-turn stopping rule is not yet measured. P1–P3: recommendations and product-only questions 6/6 and 30/30 (sections 8, 16) | Technical questions to the owner per feature; owner minutes per feature | A technical question reaches the owner in more than 1 of 10 features |
| 6 | Reviewer, code mode | `reviewer`; core-process T1 trigger | Defects the author misses; a tier stated lower than the change | prose trigger | 2026-11-02: engineering-design loads only when needed to check a design contract. Not launched in R1–R9; mandatory on T1 failed on cost (section 10) | Findings confirmed by a test or later bug; escaped defects with and without | Fewer than 1 confirmed blocking finding per 3 reviews, or more than 3 USD per confirmed blocking finding |
| 8 | Bounded review and rechecks | `reviewer` (verdicts); core-process (author's side) | Repeated reviews without new evidence | prose | 2026-11-02: at most two calls per original mode, rechecks included; revising the approach does not reset the budget. Historical two changes used four rounds each. New limit not yet measured end to end | Calls per mode, escaped defects, parts left unfinished | The limit repeatedly prevents resolution of a demonstrated blocking risk: revisit with those cases |
| 17 | Platform facts and design questions | `platform.md`; `swift.md`; Upkeep above | Outdated or wrong platform knowledge | prose; compiler later; recheck date reminded by `check-upkeep` | R8 at ceiling | Deprecation and availability errors from the compiler; wrong facts found | Facts never used in a brief or review are removed at the next major Xcode |
| 19 | Risk evidence check | `check-risk`; `scripts/risk-paths` | Risky change without a decision record | gate | Self-test only; paths provisional until the skeleton | Blocks that found a real gap against noise | More than 1 false block per feature: narrow the paths |
| 20 | Stop hook running `scripts/check` | `.claude/settings.json`; `work/agent-system-gates/plan.md` | Checks skipped because nobody remembered | gate | 2026-11-02: overdue maintenance is reported without a continuation request; actual validation failures keep their existing feedback path. Codex runs the same check explicitly; its host does not inherit this hook | Blocked stops that fixed a real issue against noise | More noise than real issues over 10 features |
| 21 | Owner report format | core-process | Owner cannot judge the result | prose | — | Owner follow-up questions per report | Owner asks for the same missing item twice |
| 26 | Generated mutants | `scripts/test-checks`, `GENERATED_FROM`, `EQUIVALENT`; test seams `SLUMPY_TEST_HOOK_CRASH`, `SLUMPY_NOW` | Self-test cases that miss logic in the checks | prose (AGENTS.md says when to run it); blocks when run | First run: 133 of 602 survived. After review round 2 (`rethink approach`): `EQUIVALENT` keeps only mutants equivalent on every input, unreachable code got test seams, logic with no observable effect was deleted. Fresh round 1: 19 of 20 reviewer mutants survived (string predicates, regex functions, string methods, call arguments); those operators were added. Fresh round 2: 11 of 75 reviewer mutants survived, all of kinds the generator does not make (`docs/tech-debt.md`, self-test gaps) On 2026-11-02, after the shared-entry/advisory-upkeep changes: 246 cases pass; all 846 executable mutants killed (36 written, 819 generated, 9 existing equivalents). This validates the listed cases and operators, not arbitrary future mutants or model behavior. | Reviewers' own mutants that survive | A reviewer's mutant survives: add its operator to the generator |
| 27 | Shared entry point and runtime adapters | AGENTS.md; Runtime loading above | Divergent Claude and Codex workflows and stale generated instructions | prose routing; native discovery | Owner-approved 2026-11-02; old project copies removed; live model behavior not yet compared | Fresh-session loading and outcome/cost on each runtime separately | A source is skipped or rules diverge: fix the adapter, not a second copy of the methodology |
