# Agent system: upkeep and mechanism ledger

How to change the agent system: `.claude/rules/core-agent-system.md`. Measurement results:
`work/agent-system-audit/baseline.md`.

## Upkeep

`scripts/check-upkeep` fails when a task's last date is older than its interval. A task with an
interval of "on event" is not dated; the task says when it is due. A new task starts with the date
it was added.

| Task | Every | Last done | How |
|---|---|---|---|
| Platform facts | 180 days | 2026-10-27 | Check each dated fact in the platform pack against the platform's documentation and the latest stable toolchain, and update the dates in the facts. Also due at each new major toolchain release |
| Prompt and skill audit | 30 days | 2026-10-27 | `/doctor prompt-audit` and `/skill-doctor` on the agent system; apply what is right, record the rest in `docs/tech-debt.md` |
| Cleanup pass | 60 days | 2026-10-28 | Work through `docs/tech-debt.md`; remove stale documents and lessons whose "stale when" has come; once code exists, also dead code and lint drift |
| Measurement after a model change | on event | — | As `.claude/rules/core-agent-system.md` says; update "Known so far" below |

## Mechanism ledger

Each mechanism, the error it exists for, what is known, and the result that removes or changes it.
The pilot on the Mac decides by this table. Thresholds are initial and may be set before the pilot
starts, never after its results. Rules: the files in "Where".

Kind: **gate** (a script, hook, or compiler blocks), **trigger** (a script decides when it runs),
**prose** (the model must remember).

| # | Mechanism | Where | Error it targets | Kind | Known so far | Pilot measure | Remove or change if |
|---|---|---|---|---|---|---|---|
| 1 | Decision rights, product questions with recommendations | core-process; `product-spec` | Owner turned into a tech lead | prose | P1–P3: recommendations and product-only questions 6/6 and 30/30 (sections 8, 16) | Technical questions to the owner per feature; owner minutes per feature | A technical question reaches the owner in more than 1 of 10 features |
| 2 | Risk tiers | core-process | Shallow analysis of irreversible decisions | prose | S3: the agent named T2 and skipped the T2 order (section 8) | Share of T2 changes with brief, ADR, and decision review before code | Below 80%: the tier comes from `check-risk` paths only |
| 3 | Brief and question menu | `engineering-design` | Code before the data model, boundaries, scenarios | prose | Graders at ceiling; fires more after the layer split. Traps T1 and T2: extra layers only when it fired (2/4 against 0/8 without it), trap avoided 12/12 either way (sections 16, 17). The owner chose on 2026-10-28 to keep the T1 brief and decide in the pilot. Same day: the simplest-design row moved first, "a question checks the design", a T1 example (`work/agent-system-self-review/plan.md`) | Hidden-test pass rate and extra types on T1 and T2 tasks, with and without the skill | No hidden-test gain and either cost above +25% or more extra types than without it |
| 4 | Domain blind-spot pass | `engineering-design` | Missing practitioner knowledge in a new area | prose | Never run | Facts from the pass used in later decisions | Two passes yield no fact used in a decision |
| 5 | Reviewer, decision mode | `reviewer` | Wrong irreversible choice | prose trigger | Design cost +120% when it ran (section 10) | Confirmed blocking findings per review; cost per confirmed finding | Fewer than 1 confirmed blocking finding per 3 reviews |
| 6 | Reviewer, code mode | `reviewer`; core-process T1 trigger | Defects the author misses; a tier stated lower than the change | prose trigger | Not launched in R1–R9; mandatory on T1 failed on cost (section 10) | Findings confirmed by a test or later bug; escaped defects with and without | Fewer than 1 confirmed blocking finding per 3 reviews, or more than 3 USD per confirmed blocking finding |
| 7 | Reviewer, spec mode | `product-spec` step 5 | Specs an implementer must ask about | prose | Unmeasured: single-turn eval never reaches it | Spec changes caused by the review; later product questions during implementation | No spec change in 3 specs |
| 8 | Review convergence | `reviewer` (verdicts); core-process (author's side) | Endless review loops | prose | Two changes converged in 4 rounds each | Rounds per change; parts left out | Average above 3 rounds per mode |
| 9 | Security pass | core-process; `platform.md`; `check-risk` | Privacy and App Review failures, leaked secrets | gate (evidence line) | Self-test only | Security findings; App Review rejections | Kept by policy: the cost of one miss is high |
| 10 | Schema test against the previous store | core-process | Data loss on update | prose | No schema yet | Migrations shipped with the test | Kept by policy: data loss cannot be undone |
| 11 | ADRs | `docs/decisions/` | Decisions forgotten between sessions | prose | One ADR; unmeasured | Later sessions contradicting an ADR | Two contradictions in the pilot: add a check that the brief cites the ADRs for the paths it touches |
| 12 | Lessons with an expiry for unguarded entries | `docs/lessons.md`; `check-lessons` | Repeated mistakes | gate (expiry of unguarded entries only; "stale when" is read by people) | The first lesson recurred within a day; its restating part got scripts, the rest is still unguarded | Repeats of a recorded class | A recorded class repeats after its mechanism landed: the mechanism is replaced |
| 13 | Technical debt register | `docs/tech-debt.md` | Non-blocking findings lost or widening changes | prose | 3 entries | Items closed against items added | More than 30 open items: a cleanup pass |
| 14 | Test and fix rules | `core-code.md` | Tests that prove nothing; fixes that hide causes | prose | R9 at ceiling | Mutation survivors in the logic package; escaped defects | No difference against the bare model on hidden tests |
| 15 | Premise check after two failed fixes | `core-code.md` | Fix loops on a wrong assumption | prose | Unmeasured | Third fixes on the same premise in debugging tasks | Never triggered in the pilot |
| 16 | `Verified:` line in commits | core-process | "Done" without proof | prose | 14 of 15 recent commits | Lines with real command output | Below 90%: a commit-message hook |
| 17 | Platform facts and design questions | `platform.md`; `swift.md`; Upkeep above | Outdated or wrong platform knowledge | prose; compiler later; recheck date gated by `check-upkeep` | R8 at ceiling | Deprecation and availability errors from the compiler; wrong facts found | Facts never used in a brief or review are removed at the next major Xcode |
| 18 | Layer and pointer checks | `check-layers`; `check-pointers`; `test-checks` | Details in the wrong layer; a rule file in no layer; stale pointers, including a pointer whose path no longer exists | gate | Self-test only; the cases come from what reviewers found by hand during the layer split | False positives and misses per change to the agent system | More than 1 false positive per 5 changes: narrow the term list; a miss found in review: add a case |
| 19 | Risk evidence check | `check-risk`; `scripts/risk-paths` | Risky change without a decision record | gate | Self-test only; paths provisional until the skeleton | Blocks that found a real gap against noise | More than 1 false block per feature: narrow the paths |
| 20 | Stop hook running `scripts/check` | `.claude/settings.json`; `work/agent-system-gates/plan.md` | Checks skipped because nobody remembered | gate | Self-test only | Blocked stops that fixed a real issue against noise | More noise than real issues over 10 features |
| 21 | Owner report format | core-process | Owner cannot judge the result | prose | — | Owner follow-up questions per report | Owner asks for the same missing item twice |
| 22 | Project Knowledge | `project-knowledge` | Product facts re-asked or invented | prose | Helped in P1 (section 12) | Facts re-asked from the owner | A fact re-asked in more than 1 of 10 features: restructure the references |
| 23 | Boundary representation rule | core-process, Whatever the tier; `engineering-design` menu; `reviewer` rubric | Ambiguous values where data leaves the process: time without its zone, money as a float, text compared without normalization | prose | Before the rule: trap T3 (time in a CSV export) failed in every measurement, with and without the system; D4 time standard 4 of 7 | Pass rate on T3 and D4; boundary bugs found later | No gain on T3 and D4 over two measurements |
| 24 | Upkeep check | `check-upkeep`; Upkeep above | Regular tasks never done: stale platform facts, unaudited prompts, debt piling up | gate; keeps any branch session working once a task is due, like an expired lesson | Self-test only | Due tasks that found something to fix against those that found nothing; interruptions the owner notices | A task finds nothing twice in a row: lengthen its interval. The owner finds the interruptions disruptive, or two branches do the same task: block only changes to the agent system and show a message elsewhere |
| 25 | Rules for changing the agent system | `core-agent-system.md` (path rule) | Mechanisms added without measurement; the always-loaded files growing | prose | Added 2026-10-28 | Agent-system changes with a ledger row and a measurement | One change ships without its ledger row: add a check that a change to the agent system also changes this file |
| 26 | Generated mutants | `scripts/test-checks`, `GENERATED_FROM`, `EQUIVALENT`; test seams `SLUMPY_TEST_HOOK_CRASH`, `SLUMPY_NOW` | Self-test cases that miss logic in the checks | prose (CLAUDE.md says when to run it); blocks when run | First run: 133 of 602 survived. After review round 2 (`rethink approach`): `EQUIVALENT` keeps only mutants equivalent on every input, unreachable code got test seams, logic with no observable effect was deleted. Fresh round 1: 19 of 20 reviewer mutants survived (string predicates, regex functions, string methods, call arguments); those operators were added. Not generated: changes inside a regular expression or an f-string | Reviewers' own mutants that survive | A reviewer's mutant survives: add its operator to the generator |
