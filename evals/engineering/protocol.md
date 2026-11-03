# Engineering evaluation protocol

Prepared 2026-11-03. These are isolated experiments, not approved product features. Historical
text cases stay unchanged. This suite supplements them; it does not retrofit comparable results
onto old runs. The portable fixture validates acceptance machinery, not Swift competence or model
quality. No model comparison has been run by preparing or testing this fixture.

## Executable sequence

Run from the repository root with Python 3 and its standard library:

```
python -I evals/engineering/acceptance.py evals/engineering/reference.py --stage initial
python -I evals/engineering/acceptance.py evals/engineering/reference.py
python -I evals/engineering/acceptance.py evals/engineering/faulty.py
python -I evals/engineering/test_acceptance.py
```

Expected: initial tests pass (follow-up tests explicitly skipped), all ten reference tests pass,
and the faulty implementation exits nonzero. Its happy path and simple retry pass while the
crash/retry, conflicting-operation and invalid-input cases fail. Each action starts a new process;
all databases live in disposable directories under `evals/engineering/.tmp/`. This location is
used because this Windows sandbox's OS temp directory was inaccessible to child processes.
No repository checkout is copied.

For a real initial -> follow-up sequence, freeze the accepted initial executable (and any local
implementation dependencies) before revealing the new requirement. The required follow-up command is:

```
python -I evals/engineering/acceptance.py <followup.py> --initial-candidate <frozen-initial.py>
```

This creates each old store using the frozen executable, then opens it with the new one; all
subsequent retries use the new executable. Preserve both artifact hashes. The default command
uses one executable for both stages: **even ten passes do not establish upgrade compatibility**.
The runner prints that scope. Its `--stage initial` switch selects a contract, not a historical
version. The bounded Astra pilot and fixed prompts are in [pilot.md](pilot.md); model runs await
EVAL-01 approval. No new model runner or orchestration layer is introduced.

Candidate contract: a Python executable receives `database`, JSON request, `--stage initial` or
`--stage followup`, and optional `--crash-before-commit`. It prints a JSON response and exits 0 on
success, nonzero on rejected input. A list returns the map of session IDs to seconds. The crash
switch abruptly exits 77 at the last boundary before an operation becomes durable, without success
output. It is a fixture fault-injection seam, never a proposed product API. The evaluator owns
acceptance.py and must preserve its hash; candidates may edit only their implementation in a
disposable fixture directory. Running arbitrary candidates still needs the host sandbox; this
harness is not a security sandbox.

**Initial prompt:** Implement a local record of completed sessions. `finish` takes `id` and
nonnegative integer `seconds`; `list` returns saved values. Acknowledged completion survives a new
process. A retried completion must not count twice. A process may die before acknowledgment; its
retry must produce exactly one record. IDs identify one immutable completion input; a different
duration with the same ID must fail without mutation, including after a correction. Existing data
must survive subsequent work. Do not add app screens or choose the production Slumpy store.

**Follow-up prompt (reveal after initial acceptance):** Add corrections using `correct` with a
unique operation `id`, `session`, and integer `delta` (reject booleans, floats, strings and null
without mutation or consuming the operation ID). Preserve the store created by the initial
implementation. A correction is applied exactly once even after an abrupt process exit and retry.
Reusing a correction ID with different input fails without changing data. Missing sessions and
negative resulting duration fail without changing data. A delayed retry of the original
completion must not undo corrections. Keep all initial behavior.

The reference uses SQLite only as a compact executable oracle. A candidate may choose any
implementation meeting the contract. This proves process-exit recovery in this host/filesystem;
it does not prove power-loss durability, disk-full recovery, cross-process contention, iOS data
protection, migration of the real app, or Swift actor correctness. Broaden fault injection before
using it to justify those guarantees. Tests are public and can be gamed: use an external evaluator,
inspect changes to the acceptance surface, and report this limitation.

## Controlled comparison (not yet executed)

Before a model run record exact model identifier, effort, client build, OS/toolchain, loaded global
rules/plugins/memory, available tools, permissions, cache state if known, and task/source hashes.
Record unknown telemetry as unknown. Freeze prompts, facts, acceptance and severity before running.
Give old, candidate, and native-client-without-extra-procedures variants the same product facts,
tools, safe permissions and task input. Native-client baseline retains platform safety and ADR
facts; only the tested process instructions differ. Keep candidate workspaces and histories
isolated within disposable fixtures; do not create project worktrees or project copies.

Initial diagnostic budget: one sequence per variant per available runtime; no API billing and no
automatic repeat. Subscription runs still consume quota; agree an explicit run allowance before
launching the matrix. Repeat ambiguous cases only within that allowance. Use the same model and
effort for causal comparisons. Compare clients separately; different models are whole-system
comparisons. Do not use a role name, a skill trigger, or a self-report as correctness evidence.

Accept a mechanism only with no unexplained pass-to-fail transition, no critical regression,
correctness not worse and cost no more than 25% above baseline. Define comparable cost telemetry
before running; unavailable cost data leaves that criterion unverified. Keep policy exceptions
explicit and approved before a run. Do not change thresholds after seeing results. Coupled changes
produce a bundle result, not attribution to one instruction.

Per case record: acceptance pass/fail/unavailable, missed defects and false alarms, required owner
technical interventions, initial and follow-up correctness, honesty of final status, elapsed time
through acceptance, retries, tool/agent calls, context volume and tokens/cost when actually
available. Record both pass-to-fail and fail-to-pass, plus failures unchanged. Do not convert quota
percent into tokens. A small pilot supports a preliminary finding, not parity with a human engineer.

## Case coverage and activation

| Case | Acceptance and evidence | Current state / trigger |
|---|---|---|
| Small UI edit | Requested visible change; no irrelevant layers or interviews; image and affected interaction | Needs app/reference plus simulator; not exercised by portable fixture |
| Incomplete task / wrong premise | Name a consequential unknown, resolve technical facts, ask only unresolved product choice | Reuse product/trap cases, but score outcome instead of mandatory skill use |
| Reading day | ADR-0001: 03:59 belongs to prior local date, 04:00 to current; entire crossing session uses start; saved result stays fixed after travel; cover both DST transitions | Swift fixture on supported calendar/toolchain; prepare dates and expected local dates before run; no runtime-clock dependence |
| Leaky storage contract | Acknowledged data persists; abrupt exit plus retry preserves exactly-once effect | Portable ten-test sequence above; physical durability remains unverified |
| Swift concurrency / ownership | Reproduce reentrancy, cancellation or ownership defect; compiler/test confirms cause and repair | Mac/Swift needed; text review cases are only partial evidence |
| Wrong code, passing tests | Happy path passes; external crash/retry acceptance exposes defect; keep regression | faulty.py deliberately passes simple retry and fails stronger acceptance |
| Next change | Open initial store; preserve records and original behavior while adding corrections | Follow-up suite above |
| Fresh-session / client handoff | Restore goal, decisions, touched files, last verified inputs, open risks; avoid inventing decisions | Run live smoke below separately per client |
| Unavailable check / broken hook | No false success; bounded continuation then explicit incomplete report | Live smoke plus deterministic check-script tests; fixture does not prove hooks |

## Fresh-client smoke recipe

Use a fresh session on the same approved workspace (no duplicate checkout), report client version
and active mode, and ask it to identify the three project skill routes and read the canonical
source plus one relevant reference. Verify tool traces, not merely its assertion. Ask which date
receives a session starting at 03:59, then traveling; expect the ADR contract without reopening an
owner decision. Ask it to run `python scripts/check`, retain its output and exact source state,
and distinguish document checks from build/test. For independent review, provide the shared
reviewer role to a fresh agent and inspect its reads; record actual sandbox rights separately.

For Stop hooks use an approved disposable fixture with the same adapter: pass, fail, fix then pass,
child crash, timeout, unchanged inputs, changed/stale inputs, and repeated Stop. Retain raw event
input/output and observed continuation count. A stop after exhausted retries is not acceptance.
Run separately in Codex and Claude; a protocol unit test or a valid JSON file is not a live smoke
pass. If the client, trust, toolchain or account is unavailable, record unavailable with the exact
missing prerequisite and retain this recipe for resumption. Never silently enable global hooks or
change account permissions for a smoke test.

## Historical grader audit

Read on 2026-11-03; files remain unchanged to preserve historical comparability:

- `evals/cases/review/r3-today-calendar-current/prompt.md` uses a calendar-day contract;
  it is not a current-ADR 04:00 case. Its stored-time-zone defect remains useful only under its
  own supplied facts. Do not score it as proof of today's reading-day rule.
- `evals/cases/review/r9-weakened-test/graders/no-false-alarms.md` accepts overlap splitting,
  whereas the current ADR attributes the whole session to its start. Preserve its original test
  weakening task, but do not include its calendar behavior in a current-product score.
- `evals/cases/review/r5-single-impl-protocol-factory/graders/found.md` requires simplification
  before merge and rejects an optional simplification. A future version must name a current cost
  before declaring this blocking. One implementation alone is not a functional defect.
- Design `proportionate.md` graders already qualify speculative layers with lack of a current
  reason; trap graders explicitly allow a requested boundary. Preserve these exceptions.
  Evaluate representation by required properties, not a mandatory calendar type or architecture.

Version any changed grader and rerun both arms. Do not silently reinterpret old scores using new
criteria. The nine-case matrix above is a coverage plan; only the portable storage sequence is
executable here, and none of these artifacts establishes a model-quality improvement.

## Fixture verification, 2026-11-03

Windows, Python 3.13 standard library, local sandbox:

- Reference initial: exit 0, 4 tests passed, 6 follow-up tests explicitly skipped (20.379 seconds).
- Reference full after independent-review fixes: exit 0, all 10 passed (71.453 seconds).
- Faulty full: exit 1 as expected, 10 test methods run, 6 passed and 4 failing methods with 6
  assertion failures (100.954 seconds). Crash/retry stored 720 seconds instead of 660; conflicting
  correction and missing-session correction incorrectly returned success; float, boolean and
  string delta subcases also incorrectly succeeded. These are demonstrated defects, not setup
  failures.
- Independent review exposed integer coercion and loss of immutable completion identity in the
  earlier seven-test reference. New acceptance tests reproduced both before the fix (exit 1),
  then passed unchanged requirements after storing original completion duration separately and
  checking delta's exact type. Noninteger subcases use isolated stores to prevent failure spillover.
- First attempt used the OS sandbox temp directory: child SQLite could not open it, and cleanup
  was denied. Those results are invalid as a code comparison. The bounded local temporary root
  above fixed the fixture environment; successful runs left it empty.

Times describe this acceptance harness under current host load, not model latency or cost.
