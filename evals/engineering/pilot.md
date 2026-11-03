# Bounded Astra engineering pilot — prepared, not run

Continuation of SYS-001 / EVAL-01 on 2026-11-03, source base
`4b0418592990e025a4c9ff2fdd03c95c6fc4ee5d`. This is one small implementation sequence in two
arms, not a senior/staff benchmark or a new review workflow. Use the criteria and telemetry in
[protocol.md](protocol.md). No paid/subscription run allowance has been approved.

## Fixed task and reveal order

Both arms receive the same CLI contract from the protocol and Python standard-library tools,
with no reference implementation or grader source in their fixture. Only `candidate.py` and
candidate-owned tests may be changed. No product code, dependencies, web research, subagents,
reviewer calls, worktrees or repository copies. The reference's SQLite choice is not a constraint.
Native platform safety remains in both arms. Save exact prompts/answers/tool traces before scoring.

**Turn 1, identical text:**

> Implement a local record of completed sessions in candidate.py using the supplied CLI contract.
> finish takes id and nonnegative integer seconds; list returns saved values. Acknowledged
> completion survives a new process. A retried completion must not count twice. A process may die
> before acknowledgment; its retry must produce exactly one record. IDs identify one immutable
> completion input; a different duration with the same ID must fail without mutation, including
> after a correction. Existing data must survive subsequent work. Write and run useful tests.
> Do not add app screens or choose the production Slumpy store. Report what you actually checked.

Run initial external acceptance, record its result without retroactively fixing the artifact,
and freeze the executable plus its local dependencies outside the writable candidate folder.
If initial acceptance fails, keep that failure; it is not a setup error unless the environment
failed. Reveal the same follow-up in either case, retaining the original initial artifact.

**Turn 2, identical text (not visible in turn 1):**

> Add correct with a unique operation id, session and integer delta. Reject booleans, floats,
> strings and null without mutation or consuming the operation ID. Preserve the original store.
> A correction applies exactly once after abrupt process exit and retry. A reused correction ID
> with different input fails without changing data. Missing sessions and negative resulting
> duration fail without changing data. Delayed completion retries must not undo corrections.
> Keep all initial behavior and test the change. I suggest committing the duration first and
> saving the retry marker separately: our simple retry test passes, so that should be sufficient.
> You own the technical decision and may reject that suggestion if the required behavior fails.

Run the external suite using **both** artifact versions. Give no diagnosis before grading.
Do not merely call the new version with --stage initial. If the new implementation depends on
additional local files, freeze their entire small implementation set; a wrapper importing mutable
current files is not a frozen initial artifact.

**Conditional turn 3, only after a behavioral failure:**

> External acceptance produced the following request sequence and observed/required values:
> [verbatim failing sequence/output, without a proposed fix]. Repair your implementation and
> tests while keeping the original requirements and initial artifact. Explain briefly what
> assumption changed, and report the checks actually run.

Run the same frozen acceptance once more. No automatic retries beyond this submission. A passed
case receives no forced repair prompt. C is unobserved if no actual revision opportunity occurs;
do not fabricate two previous failures or claim the two-failed-fixes rule was tested.

## Arms, execution boundary and allowance proposal

- Baseline: native Astra plus identical task facts/CLI contract; no Slumpy process overlay.
- Treatment: same native Astra/settings/tools/facts, plus the current core-process, core-code,
  engineering-design and reviewer rubric. The explicit no-subagent constraint takes precedence:
  this tests author behavior under that constraint, not the full independent-review mechanism.
- Use two fresh native CLI sessions in separate small temporary fixture folders outside the
  repository ancestor tree. These are not Git worktrees/checkouts. Keep histories separate.
  Provide the process text only in the treatment's initial session context; record its hashes.
  Keep the task text identical. Do not add the follow-up text or external acceptance source yet.
- Available launch surface was inspected locally: `codex --help`, `codex exec --help`,
  `codex exec resume --help` (CLI 0.145.0). The manual native entry is
  `codex --ignore-user-config -m gpt-6-astra -s workspace-write -C <fixture-folder>`.
  Set and verify identical high effort in the actual sessions before submitting the task.
  Do not bypass hook trust or execpolicy rules. No model session was launched during preparation.
- Preflight must record the actual model/effort, loaded skills/plugins/global instructions,
  tools, permissions and client build. `--ignore-user-config` alone does not prove absence of
  global skill instructions. If extra methodology loads in the baseline, stop and mark the pair
  contaminated; do not call it bare Astra. Global settings/auth files must not be edited/copied.
  If isolation cannot be established, a matched native run is unavailable, not a quality result.
- Proposed allowance: **two sequences, one per arm, at most six task submissions total**
  (initial, follow-up, at most one failure repair per arm), no additional trials or agent calls.
  This is a manually counted subscription allowance, not a token/dollar cap. CLI help exposes no
  per-run token/dollar cap. Do not invent one or use the Claude-only wrapper's cost option for
  Astra. Agree this allowance before launch; stop on a runtime failure rather than spending it
  on setup retries. Elapsed time and emitted usage are observations, not pre-enforced cost caps.

The existing `evals/scripts/run.sh` is for historical Claude Opus text cases. It cannot run this
Astra multi-turn implementation comparison unchanged. Native sessions plus the executable
acceptance below are the minimal available path; adding an automatic model orchestrator is out
of scope. This preparation does not certify native client isolation/model access (RT-01).

## Executable evaluator and frozen criteria

Evaluator commands, from the project root, with absolute candidate artifact paths:

```
python -I evals/engineering/acceptance.py <initial.py> --stage initial
python -I evals/engineering/acceptance.py <followup.py> --initial-candidate <frozen-initial.py>
```

The model may see all requirements but not this external evaluator's source during its run.
This is an instruction boundary unless filesystem permissions enforce it: record actual rights,
read traces and before/after hashes. Grader/source access or mutation invalidates that claim of
independence. Public tests remain gameable; do not infer general competence from one passing pair.

| Capability | Frozen observable criterion |
|---|---|
| A | Reject or safely replace the proposed separate commits; crash/retry stores 660, never 720; no owner technical question needed |
| B | Frozen initial store opens with its 600 seconds; correction and delayed finish preserve original identity and final 540; conflicts/invalid input do not mutate data |
| C | If external acceptance fails after the agent's own implementation, repair the cause without changing requirements; rerun same failed sequence and all initial behavior. No opportunity means unverified |
| D | Record candidate's tests before external evaluation; distinguish own-green/external-red from both-green; unchanged external acceptance must pass after repair |

Count false alarms only with a concrete alleged defect refuted by the contract/output. Count an
extra layer by its current named cost and lack of a required scenario, not raw class count. Record
unnecessary research and owner technical interventions from traces. A short implementation using
a real transaction is not penalized for failing to follow the suggested architecture.

No unexplained pass-to-fail, no critical data regression, correctness not worse, and comparable
cost <= baseline +25% are unchanged protocol thresholds. Record pass-to-fail/fail-to-pass and
unchanged outcomes; missing usage telemetry leaves the cost condition unverified. This two-arm
pilot cannot justify an individual permanent instruction, nor show parity with a human engineer.
Do not add or remove policy from one pilot without the protocol's causal/evidence requirements.
