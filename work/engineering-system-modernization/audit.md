# Runtime and mechanism audit — 2026-11-03

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
