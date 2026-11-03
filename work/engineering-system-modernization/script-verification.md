# Script verification — 2026-11-03

## Confirmed failures before correction

Three isolated Git fixtures exercised the old check-risk implementation: committed work directly
on dev with an explicit task-start base, an invalid explicit base, and an unrelated explicit base.
All three expected rejection assertions returned False. These were behavior failures, before the
SLUMPY_CHECK_BASE implementation was added; later fixture cleanup hit Windows file-lock errors.

The former subprocess.run(timeout) behavior was reproduced with a disposable parent that spawned
a child writer. The parent timed out; the child still wrote afterward. Output:

```
OLD subprocess.run timeout: expected failure: child survived its parent's timeout
```

The fixture child exited after seven seconds. It was not a user process.

## Host repair

Thirty Python processes started on 2026-11-02 were still consuming CPU in check-upkeep scripts
under deleted temporary case fixtures. Every parent PID was absent. Exact command paths were
under six known temporary fixture roots; the files had already been deleted, so their exact loaded
mutant contents could not be inspected. The repository check-upkeep implementation only reads,
and the mutation operators do not introduce file writes. This evidence identifies obsolete
disposable checks, not arbitrary Python workloads.

At 2026-11-03 09:12:42 +03:00, exactly those 30 processes were stopped. Immediately before each
stop, its PID, Python executable name, creation date, exact fixture script path, absent parent,
and deleted fixture were revalidated. No wildcard process termination or user configuration
change was used. The repair script remains in the ignored local scratch directory for this run.

The harness now kills owned descendants on timeout. The regression spawns a child in a separate
session, matching nested harness processes. Windows uses taskkill /T; POSIX walks parent links
with a bounded freeze-and-kill loop. POSIX execution remains unverified on this Windows host;
daemonizing fixtures are outside the harness contract.

## Commands and scope

An explicit `python scripts/check` run after setting the child timeout to 45 seconds passed all
five document checks (24 changed files at that time). It explicitly reported build, application
tests, lint, and test-checks as not run. This intermediate result is not evidence for later edits.

`python scripts/test-checks` and `python scripts/test-checks --mutants` are run sequentially on
the final scripts. Sandbox attempts encountered denied temporary-directory creation, slow Git
subprocesses, and locked fixture cleanup; the final run uses the approved unsandboxed tool to
execute the same deterministic disposable-fixture tests. No paid/model evaluation is performed.

Intermediate standalone self-test output (before the test-validity correction below):

```
test-checks: 263 cases pass
```

Coverage: the existing 246 document/routing/risk/hook cases, seven explicit-base cases, nine
Codex-hook/timeout/unavailable-executable cases, and one separate-session descendant cleanup
regression. The cleanup regression ran on Windows; POSIX cleanup has only code review here.

The first full mutation attempt was stopped as incomplete after discovering a test-validity
problem: replacing the literal timeout value in source made numeric timeout mutants fail during
fixture setup. Those failures cannot be credited as behavioral kills. The two new execution
cases now run the public check CLI through runpy and simulate subprocess outcomes without editing
the checked source. Independent probe output:

```
timeout 45: exit 0; expected behavioral result
timeout 44: exit 1; expected behavioral result
timeout 46: exit 1; expected behavioral result
dropped timeout: behavior assertion failed as expected
missing executable probe: passed
internal status 124 to zero: behavior assertion failed as expected
internal status 127 to zero: behavior assertion failed as expected
```

Both changed timeouts and a missing deadline fail explicit behavior assertions. The probe models
the subprocess API's optional timeout default. No production probe flag was added. Four numeric
mutants (124 to 123/125 and 127 to 126/128) are narrowly documented equivalents: script() has only
two callers, both distinguish zero from nonzero, and neither exposes the exact internal code.
Two written mutants changing those codes to zero fail the public CLI behavior probes.

A related-but-non-ancestor base fixture was also checked: the baseline rejects it; removing the
ancestor flag incorrectly accepts it. Its soft reset preserves the mutated checker in the working
tree. This adds one case, bringing the corrected inventory to 264 cases and 895 executable
mutants (38 written, 870 generated, 13 documented equivalents).

The corrected full run began at 2026-11-03 09:38:13 +03:00; its exact output is saved locally in
the ignored scratch verification-run.log and will be copied into this record. Earlier interrupted runs
are not counted as passes. The old 246-case/846-mutant result is historical, not this run's result.

Corrected standalone suite, completed before the mutation command started at 09:40:46 +03:00:

```
test-checks: 264 cases pass
```

## Completed full mutation run and follow-up

The full command ended at 2026-11-03 11:02:39.937 +03:00, after 4913.51 seconds
(81 minutes 53.5 seconds). It exited **1**, not 0: **892 of 895 executable mutants were killed**.
There were three survivors, no stale entries:

```
surviving mutant: check, run_hook: argument 4 dropped at column 0: respond("scripts/check --hook crashed:\n" + traceback.format_exc(), continuing, error=True, codex=codex)
surviving mutant: check-risk, base: argument 3 dropped at column 11: resolved = out("rev-parse", "--verify", "--end-of-options", explicit + "^{commit}").strip()
surviving mutant: check-risk, base: right operand dropped at column 60: resolved = out("rev-parse", "--verify", "--end-of-options", explicit + "^{commit}").strip()
test-checks: 3 of 908 mutants survive or are stale
```

Classification, established before changing tests:

1. Dropping `codex=codex` from this crash response is equivalent. `error=True` already selects
   the block response for either client. When continuing, `respond` selects `systemMessage`
   before either flag. Thus the dropped argument cannot alter any CLI outcome at this call site.
   One exact generated mutant is now documented as equivalent; no operator class is skipped.
2. Dropping `--end-of-options` is a real coverage gap. A fixture creates the valid ref
   `refs/tags/-task-base` with `git update-ref`, and invokes the CLI with
   `SLUMPY_CHECK_BASE=-task-base`. The baseline accepts that commit tag; the mutant rejects it.
   The tempting `--default=HEAD` counterexample was rejected by both versions and is not claimed
   as a vulnerability.
3. Dropping `^{commit}` is a real coverage gap. A fixture takes the first four hex digits of its
   HEAD commit and constructs a blob with the same Git object-hash prefix. Only that blob is
   written using `git hash-object -w --stdin`; no repository source is altered. With that short
   prefix as SLUMPY_CHECK_BASE, the baseline resolves the unique commit; the mutant rejects the
   ambiguous commit/blob prefix. One observed example was prefix `d692`. The permanent case
   constructs the collision from its own fixture HEAD, rather than relying on that example.

Only tests and the exact equivalence entry changed after the full run. Production check scripts
did not change. The resulting inventory is 266 cases and 894 executable mutants (38 written,
870 generated, 14 documented equivalents). This is **not** represented as another full run:
the updated suite and the three previous survivors were checked separately.

The completed full run left zero temporary Python check workers. Its production and harness
hashes matched the frozen inputs:

| Input | SHA256 during completed full run |
|---|---|
| scripts/check | 67418B6ECFDDBA216F3DE46FBB535F23338E277BC389FA9B4933C4F6342A09CA |
| scripts/check-risk | 27AB819141409508AFE95A05F88EBBBC3AA5FC9E7A7D1049668C64B28609D171 |
| scripts/test-checks | 3B3650B2584788C75F02F0D7BAF0830934D9234CF6FCF647487455A36A61A6AC |
| scripts/risk-paths | 860BB261951781466D72447F6DF5D194417F3E06C4902F49C55D7988D6C7485F |

Final follow-up completed at 11:10:18 +03:00, exit 0:

```
test-checks: 266 cases pass
14 equivalent keys: each matches exactly one generated variant
targeted survivors: 2 killed, 1 confirmed equivalent
temporary Python check workers after completion: 0
```

The final suite covers 246 historical cases, ten explicit-base cases, nine hook/unavailable-check
cases and one descendant-cleanup regression. The two new cases exercise the public CLI using
`SLUMPY_CHECK_BASE=-task-base` (a valid tag) and a four-hex prefix shared by a commit and blob.
Production scripts retain the hashes above. Final `scripts/test-checks` SHA256:
`3B85C3495F897C928934ECC706703DD93D7F71D08DA0483F2BE1BB60E7B55DF3`.
Raw local follow-up output is in ignored `evals/results/check-temp/final-targeted.log`;
the completed full run is in `verification-run.log` alongside it. The 894-variant revised inventory
was not fully rerun: evidence is the completed 895-variant run plus the targeted follow-up.
