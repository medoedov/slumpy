# Agent system: upkeep and mechanism ledger

How to change the agent system: `.claude/rules/core-agent-system.md`. Historical measurement results:
`work/agent-system-audit/baseline.md`. Current migration evidence:
`work/completed/agent-system-unified/plan.md`. Current modernization and verification limits:
`work/engineering-system-modernization/plan.md` and its audit.

## Runtime loading

Confirmed by the owner on 2026-11-02: one maintained `AGENTS.md` for Claude Code and Codex,
shared rules and skills, and only small runtime adapters. This replaces Codex option A and the
generated mirrors; the former converter must not regenerate this repository.

| Component | Shared source | Claude Code | Codex |
|---|---|---|---|
| Entry point | `AGENTS.md` | Direct loading when supported; `CLAUDE.md` imports it for compatibility | Native repository instructions |
| Process and platform rules | `.claude/rules/` | Native rule loading | Explicit routes in `AGENTS.md` |
| Three project skills | `.claude/skills/` | Native skill discovery | `.agents/skills/` contains links to these sources |
| Review role | `.claude/agents/reviewer.md` | Native agent definition | Give this file to a fresh subagent with the mode, tier, call number, artifacts, and evidence |
| Completion checks | `scripts/check` | Stop hook in `.claude/settings.json`, plus explicit verification | `.codex/hooks.json` adapter, pending native trust/live smoke; explicit verification remains required |

The Codex adapters own discovery only. Their name and description follow the source skill;
instructions and references are read from that source, not copied. Old project skill copies and
the old `.codex/agents/` definitions have been removed. Generic globally installed skills are not
another project workflow: use the routing in `AGENTS.md`. User-wide settings are not changed by
this migration, and a new session is needed to drop catalogs already injected into a conversation.

For a Codex review, use the runtime's available fresh subagent mechanism and ask it to read the
shared review role; do not assume a registered Claude agent exists. If independent agents are
unavailable, report the review as unverified rather than presenting self-review as independent.
The same applies to checks a host cannot execute. Claude permission settings and its Stop hook do
not configure Codex; approval restrictions still come from the host and shared instructions.

2026-11-03: CLI probes still report Codex 0.145.0 and Claude 2.1.220. Codex reports `hooks` stable
and enabled. The project Stop definition uses `--codex-hook`; the existing Claude protocol remains
`--hook`. Review/trust the exact definition using native `/hooks` in a supported local Codex client,
then run the fresh-session smoke protocol in `evals/engineering/protocol.md`. Do not bypass trust.
Current Desktop orchestration mode and actual Stop dispatch are unverified; command hooks are not
supported by cloud orchestration, even with local execution, per the
[current hook documentation](https://learn.chatgpt.com/docs/hooks). Direct adapter tests establish
only protocol behavior. A bounded hook may let the conversation end with failed checks; that is
not acceptance. The ordinary check exit status remains authoritative for its documented scope.

The shared reviewer is behaviorally read-only, not a security sandbox: Bash and current Codex
subagents can write. Supply a read-only tool profile when available. Otherwise explicitly prohibit
mutations, use disposable fixtures for experiments, compare the tree before/after, and report this
limit; never claim enforced read-only access from a role prompt alone.

The local CLI check on 2026-11-02 found Claude Code 2.1.220 and Codex CLI 0.145.0. Claude's
[direct AGENTS.md support](https://code.claude.com/docs/en/memory#agents-md) requires 2.1.277 or
later and enabled instruction loading. Keep the one-line `CLAUDE.md` import while older sessions
are used. After upgrading, verify loading before removing that adapter. Codex discovers the
project adapters through [`.agents/skills`](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

At the next fresh session in each runtime, confirm the shared entry point, the three project
skills and their source routes, and a review call using the shared role. This is a loading smoke
check, not a quality or cost measurement. Compare outcome quality, cost per successful task, tool
calls, time, and owner involvement separately on each runtime before claiming an improvement.

## Model policy

Owner decision, 2026-11-03: Codex implementation and final engineering responsibility use
`gpt-6-astra`. Launch CLI work with `codex -m gpt-6-astra`; select Astra explicitly in other
clients and verify their actual session setting. No silent model substitution. The shared
review role remains `.claude/agents/reviewer.md`; model selection is a launch property, not a
second profession or copy of the review prompt. Critical independent review uses fresh Astra.
Terra may assist with a bounded factual checklist or low-risk diff only after access and a
small smoke test are confirmed; it never solely judges architecture, concurrency, migrations,
security, privacy, data or a new system API. The author verifies each finding.

Observed during SYS-001 v2: the executor was explicitly spawned with `gpt-6-astra` in a fresh
context. Read-only inspection of user config found `model = "gpt-6-astra"` and effort `high`;
the earlier audit's `medium` is historical. No settings were edited. Cached model discovery
contains Astra and Terra but does not prove availability or execution. Installed CLI remains
0.145.0; [official model documentation](https://learn.chatgpt.com/docs/models), checked
2026-11-03, requires 0.159.0+ for Terra. Terra therefore remains disconnected in this CLI;
no untested `.codex/agents` file is installed. This explicit Astra call confirms the current
executor, not every future Desktop chat's effective model or effort. Recheck on a new host.

There is one writing executor per area;
reviewers receive the bounded diff, shared role and necessary source links. Current tool access
is write-capable despite the no-edit review instruction: compare content before/after. The
[custom-agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents)
explicitly says a custom agent's `sandbox_mode` does not override its parent, so a TOML flag
must not be described as enforced read-only access. No custom orchestrator or additional role.

## Task state

`work/STATUS.md` is the start/resume index; the linked plan owns progress, accepted scope and
evidence. Backlog owns only unstarted proposed/ready work; ADRs, knowledge, lessons and debt
keep their existing distinct responsibilities. IDs are allocated when work is recorded, never
from a second memory. Historical plans without Task-ID are not active state records.

New plans declare exactly one `Task-ID: PREFIX-001`, `State: in-progress|blocked|verified|done`,
`Blockers: <reason or none>` and `Owner: <executor>` line. Active index rows use
`| ID | State | [plan](relative-path) | owner/scope | next step |`. Future backlog rows begin
`| ID | proposed|ready |`. Semantic duplicate search is still the author's job. On completion,
resolve required blockers with evidence, update affected canonical facts and remove the active
row while moving the plan folder into `work/completed/`; keep a short result link. This is one
logical transition. `scripts/check-state` checks these declarations and local index links,
including untracked plans; it cannot certify the claims in them or remote issue consistency.

Current pending live-client/Mac checks have one registry linked from STATUS. Existing historical
checklists are not competing active queues. Model updates invalidate behavioral measurements;
no historical Claude score establishes present Astra/Terra quality or cost.

## Upkeep

`scripts/check-upkeep` reports an advisory reminder when a task's last date is older than its
interval. It does not make unrelated work fail or authorize a maintenance task. Malformed dates
or tables still fail because the schedule cannot be read. An "on event" task is not dated; the
task says when it is due. Update dates after doing the work, not to dismiss a reminder.

| Task | Every | Last done | How |
|---|---|---|---|
| Platform facts | 180 days | 2026-10-27 | Check each dated fact in the platform pack against the platform's documentation and the latest stable toolchain, and update the dates in the facts. Also due at each new major toolchain release |
| Prompt and skill audit | 30 days | 2026-11-02 | Audit the active instructions for conflicting sources, unnecessary work, and demonstrated gaps; propose changes outside the maintenance scope instead of applying them automatically |
| Cleanup pass | 60 days | 2026-10-28 | Work through `docs/tech-debt.md`; remove stale documents and lessons whose "stale when" has come; once code exists, also dead code and lint drift |
| Measurement after a model change | on event | — | As `.claude/rules/core-agent-system.md` says; update "Known so far" below |

## Mechanism ledger

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

### Added mechanisms

| # | Mechanism | Where | Error it targets | Kind | Known so far | Pilot measure | Remove or change if |
|---|---|---|---|---|---|---|---|
| 28 | Bounded eval output and content provenance | `evals/scripts/build_plugin.py`; `test_build_plugin.py`; `run.sh`; `collect.py`; `test_collect.py` | Arbitrary deletion, dirty input mislabeled as HEAD, failed eval reported successful | gate | Existing output never deleted; collector retains trace directories; actual payload hashed; real junction guard and Bash stub exit propagation verified; symlink/real Claude/v0 unverified | Rejected dangerous paths, preserved unrelated trace-neighbor files, changed-content digest, runner failure propagation | A direct unsafe path passes or input changes without digest changing; revise guard |
| 29 | Executable initial/follow-up engineering fixture | `evals/engineering/` | Text-only graders and weak tests mistaken for engineering evidence | test when run | Reference/fault discrimination only; no autonomous model comparison or Swift evidence | Accepted behavior, escaped defects, owner interventions, next-change regressions and total cost | Cases cannot distinguish realistic defects or leak acceptance changes into runs; revise before comparison |
| 30 | Bounded test process cleanup | `scripts/test-checks` | Timed-out mutant leaves descendants consuming resources | executable cleanup and regression | Old parent-only timeout reproduced a surviving child; final platform results in current plan | Descendant stops after timeout; no leaked workers after mutant run | Any owned descendant survives; do not interpret timeout as a killed mutant |
| 31 | One task index with checked transitions | `work/STATUS.md`; `scripts/check-state`; `scripts/test-checks` | Duplicate IDs, orphan plans, forgotten blockers and completed work reappearing | gate plus semantic handoff | SYS-001 v2: 347 total cases pass; composite mutation evidence and fresh Astra handoff in active plan; semantic truth, unmarked legacy plans and remote consistency are outside the lint | Fresh agent restores ID/decision/last evidence/next step; blocked-to-completed fixture; false positives | A real transition bypasses a check or >1 false positive in 5 changes: repair/narrow, no task database |
| 32 | Explicit Astra ownership and conditional Terra | Model policy above | Unobserved model inheritance or a cheaper helper replacing critical review | owner policy plus launch evidence | User config and explicit Astra executor observed; Terra CLI unsupported; no model-quality comparison | Actual model on fresh host/client; bounded helper findings and cost if enabled | Revisit on owner's model decision or client change; never infer support from cache |

Local installation correction on 2026-11-03: `.git/config` still selected `.githooks`, contrary to
the documented disabled state. Its pre-commit invokes the prohibited external converter. Only the
repository-local `core.hooksPath` was set to `/dev/null` and read back; frozen hook files unchanged.
Check this setting after copying/reinitializing the workspace; do not reactivate those hooks.

Each mechanism, the error it exists for, what is known, and the result that removes or changes it.
The pilot on the Mac decides by this table. Thresholds are initial and may be set before the pilot
starts, never after its results. Rules: the files in "Where".

Kind: **gate** (a script, hook, or compiler blocks), **trigger** (a script decides when it runs),
**prose** (the model must remember).

| # | Mechanism | Where | Error it targets | Kind | Known so far | Pilot measure | Remove or change if |
|---|---|---|---|---|---|---|---|
| 1 | Decision rights, product questions with recommendations | core-process; `product-spec` | Owner turned into a tech lead | prose | 2026-11-02: questions are batched at five per message; material decisions stay open until answered. The new multi-turn stopping rule is not yet measured. P1–P3: recommendations and product-only questions 6/6 and 30/30 (sections 8, 16) | Technical questions to the owner per feature; owner minutes per feature | A technical question reaches the owner in more than 1 of 10 features |
| 2 | Risk tiers | core-process | Shallow analysis of irreversible decisions | prose | S3: the agent named T2 and skipped the T2 order (section 8) | Share of T2 changes with brief, ADR, and decision review before code | Below 80%: the tier comes from `check-risk` paths only |
| 3 | Brief and question menu | `engineering-design` | Code before the data model, boundaries, scenarios | prose | Graders at ceiling; fires more after the layer split. Traps T1 and T2: extra layers only when it fired (2/4 against 0/8 without it), trap avoided 12/12 either way (sections 16, 17). The owner chose on 2026-10-28 to keep the T1 brief and decide in the pilot. Same day: the simplest-design row moved first, "a question checks the design", a T1 example (`work/agent-system-self-review/plan.md`); measured in section 18: proportionate 11 of 12 over two measurements against 3 of 6, cost +7% on average, +25% in the run where the skill loaded twice | Hidden-test pass rate and extra types on T1 and T2 tasks, with and without the skill | No hidden-test gain and either cost above +25% or more extra types than without it |
| 4 | Research a material knowledge gap | `engineering-design` | An unknown fact changes a design or correctness decision | prose | 2026-11-02: research is triggered by a named gap, not a missing domain page; stop once the decision has evidence. Reusable findings may become a domain page. Behavioral effect not yet measured | Design changes supported by researched facts; research cost per useful answer | Research produces no decision-relevant evidence in two tasks: narrow the trigger |
| 5 | Reviewer, decision mode | `reviewer` | Wrong irreversible choice | prose trigger | 2026-11-02: engineering-design is loaded in decision mode, not preloaded for every review. Design cost +120% when it ran (section 10) | Confirmed blocking findings per review; cost per confirmed finding | Fewer than 1 confirmed blocking finding per 3 reviews |
| 6 | Reviewer, code mode | `reviewer`; core-process T1 trigger | Defects the author misses; a tier stated lower than the change | prose trigger | 2026-11-02: engineering-design loads only when needed to check a design contract. Not launched in R1–R9; mandatory on T1 failed on cost (section 10) | Findings confirmed by a test or later bug; escaped defects with and without | Fewer than 1 confirmed blocking finding per 3 reviews, or more than 3 USD per confirmed blocking finding |
| 7 | Reviewer, spec mode | `product-spec` step 5 | Specs an implementer must ask about | prose | 2026-11-02: spec review does not preload engineering-design; material owner choices return to another question batch. Unmeasured: single-turn eval never reaches it | Spec changes caused by the review; later product questions during implementation | No spec change in 3 specs |
| 8 | Bounded review and rechecks | `reviewer` (verdicts); core-process (author's side) | Repeated reviews without new evidence | prose | 2026-11-02: at most two calls per original mode, rechecks included; revising the approach does not reset the budget. Historical two changes used four rounds each. New limit not yet measured end to end | Calls per mode, escaped defects, parts left unfinished | The limit repeatedly prevents resolution of a demonstrated blocking risk: revisit with those cases |
| 9 | Security pass | core-process; `platform.md`; `check-risk` | Privacy and App Review failures, leaked secrets | gate (evidence line) | Self-test only | Security findings; App Review rejections | Kept by policy: the cost of one miss is high |
| 10 | Schema test against the previous store | core-process | Data loss on update | prose | No schema yet | Migrations shipped with the test | Kept by policy: data loss cannot be undone |
| 11 | ADRs | `docs/decisions/` | Decisions forgotten between sessions | prose | One ADR; unmeasured | Later sessions contradicting an ADR | Two contradictions in the pilot: add a check that the brief cites the ADRs for the paths it touches |
| 12 | Lessons with an expiry for unguarded entries | `docs/lessons.md`; `check-lessons` | Repeated mistakes | gate (expiry of unguarded entries only; "stale when" is read by people) | The first lesson recurred within a day; its restating part got scripts, the rest is still unguarded | Repeats of a recorded class | A recorded class repeats after its mechanism landed: the mechanism is replaced |
| 13 | Technical debt register | `docs/tech-debt.md` | Non-blocking findings lost or widening changes | prose | 3 entries | Items closed against items added | More than 30 open items: a cleanup pass |
| 14 | Test and fix rules | `core-code.md` | Tests that prove nothing; fixes that hide causes | prose | R9 at ceiling | Mutation survivors in the logic package; escaped defects | No difference against the bare model on hidden tests |
| 15 | Premise check after two failed fixes | `core-code.md` | Fix loops on a wrong assumption | prose | Unmeasured | Third fixes on the same premise in debugging tasks | Never triggered in the pilot |
| 16 | `Verified:` line in commits | core-process | "Done" without proof | prose | 14 of 15 recent commits | Lines with real command output | Below 90%: a commit-message hook |
| 17 | Platform facts and design questions | `platform.md`; `swift.md`; Upkeep above | Outdated or wrong platform knowledge | prose; compiler later; recheck date reminded by `check-upkeep` | R8 at ceiling | Deprecation and availability errors from the compiler; wrong facts found | Facts never used in a brief or review are removed at the next major Xcode |
| 18 | Layer and pointer checks | `check-layers`; `check-pointers`; `test-checks` | Details in the wrong layer; a rule file in no layer; stale pointers, including a pointer whose path no longer exists | gate | 2026-11-02: AGENTS.md and active Codex adapters join the checked sources; dated prior-system records are historical. Deterministic cases cover entry-point rules and active pointers | False positives and misses per change to the agent system | More than 1 false positive per 5 changes: narrow the term list; a miss found in review: add a case |
| 19 | Risk evidence check | `check-risk`; `scripts/risk-paths` | Risky change without a decision record | gate | Self-test only; paths provisional until the skeleton | Blocks that found a real gap against noise | More than 1 false block per feature: narrow the paths |
| 20 | Stop hook running `scripts/check` | `.claude/settings.json`; `work/agent-system-gates/plan.md` | Checks skipped because nobody remembered | gate | 2026-11-02: overdue maintenance is reported without a continuation request; actual validation failures keep their existing feedback path. Codex runs the same check explicitly; its host does not inherit this hook | Blocked stops that fixed a real issue against noise | More noise than real issues over 10 features |
| 21 | Owner report format | core-process | Owner cannot judge the result | prose | — | Owner follow-up questions per report | Owner asks for the same missing item twice |
| 22 | Project Knowledge | `project-knowledge` | Product facts re-asked or invented | prose | Helped in P1 (section 12) | Facts re-asked from the owner | A fact re-asked in more than 1 of 10 features: restructure the references |
| 23 | Boundary representation rule (removed 2026-10-28) | was core-process, Whatever the tier; `engineering-design` menu; `reviewer` rubric | Ambiguous values where data leaves the process | removed | No measurable difference on its cases (`work/agent-system-audit/baseline.md`, section 18): T3 0 of 4 runs with two wordings, D4 at the ceiling in both versions. The agent leaves out a time zone column as a feature nobody asked for | — | — |
| 24 | Upkeep reminders | `check-upkeep`; Upkeep above | Maintenance forgotten without making unrelated tasks wait | advisory for overdue tasks; gate for malformed schedule | 2026-11-02: a due date no longer fails check-upkeep or scripts/check; hook reminders do not demand maintenance. Covered by deterministic cases; effect on owner interruptions not yet measured | Useful maintenance tasks against interruptions; ignored reminders | A task finds nothing twice: lengthen its interval; missed necessary maintenance: revise that task trigger |
| 25 | Rules for changing the agent system | `core-agent-system.md` (path rule) | Mechanisms added without measurement; the always-loaded files growing | prose | 2026-11-02: runtime-specific evidence and explicit unmeasured status required; paid measurements need an agreed budget. Historical results remain labeled with their model and runtime | Agent-system changes with a ledger row and a measurement | One change ships without its ledger row: add a check that a change to the agent system also changes this file |
| 26 | Generated mutants | `scripts/test-checks`, `GENERATED_FROM`, `EQUIVALENT`; test seams `SLUMPY_TEST_HOOK_CRASH`, `SLUMPY_NOW` | Self-test cases that miss logic in the checks | prose (AGENTS.md says when to run it); blocks when run | First run: 133 of 602 survived. After review round 2 (`rethink approach`): `EQUIVALENT` keeps only mutants equivalent on every input, unreachable code got test seams, logic with no observable effect was deleted. Fresh round 1: 19 of 20 reviewer mutants survived (string predicates, regex functions, string methods, call arguments); those operators were added. Fresh round 2: 11 of 75 reviewer mutants survived, all of kinds the generator does not make (`docs/tech-debt.md`, self-test gaps) On 2026-11-02, after the shared-entry/advisory-upkeep changes: 246 cases pass; all 846 executable mutants killed (36 written, 819 generated, 9 existing equivalents). This validates the listed cases and operators, not arbitrary future mutants or model behavior. | Reviewers' own mutants that survive | A reviewer's mutant survives: add its operator to the generator |
| 27 | Shared entry point and runtime adapters | AGENTS.md; Runtime loading above | Divergent Claude and Codex workflows and stale generated instructions | prose routing; native discovery | Owner-approved 2026-11-02; old project copies removed; live model behavior not yet compared | Fresh-session loading and outcome/cost on each runtime separately | A source is skipped or rules diverge: fix the adapter, not a second copy of the methodology |
