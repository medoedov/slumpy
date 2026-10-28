# Agent system self-review fixes: brief and log

## Goal

Close the weak spots the self-review of 2026-10-28 found that can be fixed without code or a Mac
(owner request: «да, все это делай»). Each item names the evidence that makes it a weak spot.

- T1 because it changes rules, a skill, the reviewer, and the document checks inside the decisions
  already made (layer split, gates); no app code, storage, or platform capability.

## Brief

| # | Weak spot | Evidence | Change | Where |
|---|---|---|---|---|
| 1 | The agent does not notice a subtlety at a boundary when the task looks small | Trap T3 (time in a CSV export) failed in every measurement, with and without the system; the design skill never loaded there; D4, where the exchange is named, passed 4 of 7 | One tier-independent rule: data that crosses a boundary gets an explicit representation for the values that break there (time, money, text, identifiers, units and number formats), checked against the primary source. The menu row "Standard or protocol" becomes "Data crosses a boundary, or a standard applies" and points to the rule; the reviewer rubric checks it | `core-process.md`, Whatever the tier; `engineering-design` menu; `reviewer` rubric |
| 2 | The brief adds layers | Extra layers in 2 of 4 runs where the skill fired, 0 of 8 without it (`baseline.md`, section 17) | "Any: can it be simpler" becomes the first menu row and asks for the simplest design that covers the scenarios; a sentence says a menu question checks the design and does not ask for a mechanism; an example of a T1 brief at the right size, with "New elements: none" and a "does not apply" answer | `engineering-design`, sections 3 and 4 |
| 3 | Dense review rules, one rule kept in two core files | "Review and lessons" was one paragraph of 209 words with about ten rules; the round limit and the recheck rule were in both `core-process.md` and `reviewer.md` | The section becomes a list; the author's side (rounds, what to do with each verdict, disputes) lives only in `core-process.md`, the verdict definitions only in `reviewer.md`, which points to the core section | `core-process.md`; `reviewer.md`, Convergence |
| 4 | The system does not maintain itself | The adoption rule, the ledger, and the upkeep list lived in a task folder (`work/agent-system-audit/`) with no pointer from the always-loaded files; the core tells the agent to fix a repeated class with a rule, up to an always-loaded file, with no counterweight | A path rule `core-agent-system.md` (loads when agent-system files are read or edited): the order of preferred mechanisms, the ledger row per mechanism, the adoption rule, re-measurement after a model change, upkeep. The ledger and the upkeep table move to `docs/agent-system.md`, named in CLAUDE.md | `.claude/rules/core-agent-system.md`; `docs/agent-system.md`; CLAUDE.md |
| 5 | Freshness of platform facts and the regular upkeep rely on memory | Facts in `swift.md` dated 2026-10-27, nothing makes anyone recheck them; the monthly prompt audit, the cleanup pass, and the toolchain check in the audit plan have no trigger | `scripts/check-upkeep` fails when an upkeep task in `docs/agent-system.md` is older than its interval, like the expiry of unguarded lessons | `scripts/check-upkeep`; `scripts/check` |
| 6 | Nobody checks that the stated tier is true | `check-risk` requires a `T1 because` line, not a true one | Reviewer rubric: the tier in the plan matches what the change does | `reviewer.md`, Rubric |
| 7 | Two holes in the checks | `docs/tech-debt.md`: a rule file outside both layers is never scanned; a pointer with a path is checked against any file of that name | `check-layers` fails on a rule file that is neither core nor named by `platform.md`; `check-pointers` resolves a pointer with a path by that path (from the repository root or the pointing file's folder) and reports a missing file | `scripts/check-layers`, `scripts/check-pointers` |
| 8 | Tester bugs cannot be diagnosed from data | Crash reports and logs are not mentioned anywhere | The monitoring decision before the first tester build includes crash reports and diagnostic logs | `deployment.md`, Monitoring |
| 9 | Hand-picked mutants overstate the self-test (added after review round 1, a class repeated for the third time) | The reviewer's own mutants survived while the written list was fully killed | `scripts/test-checks --mutants` also generates mutants from the code of every check; a survivor needs a case or an `EQUIVALENT` entry with its reason | `scripts/test-checks` |

Conditions kept when moving the review rules (lesson "An adapted or generalized rule loses the
condition that limits it"): the table in the next section maps each one to its new place.

## Item 9, revised after review round 2 (`rethink approach`)

Round 2 found that `EQUIVALENT` exempted mutants that do change what a check reports (on inputs
the author judged unlikely), that occurrence-numbered keys could pass an exemption to a new line,
and that the generator lacked two operators. The author was still deciding which logic needs no
case. Revised approach:

- `EQUIVALENT` holds only mutants that are equivalent on every input. Logic whose mutants are
  equivalent only for today's files is deleted (`check-layers` joins the whole first paragraph,
  maxsplit arguments that cannot matter, `check-pointers` reports through one problem list) or
  gets a case.
- Code no case could reach becomes reachable through two test seams instead of a list of
  exemptions: `SLUMPY_TEST_HOOK_CRASH` makes the hook raise, so its crash handler is tested;
  `SLUMPY_NOW` sets the clock of `check-upkeep` and `check-lessons`, so the date edges are tested at
  fixed instants. Both checks compute dates without the machine's zone: a date is in the future if
  it is later than today in UTC+14, and an age counts from today in UTC−12.
- A key is the script, the enclosing function, the mutation, and the line; an `EQUIVALENT` entry
  must match exactly one generated mutant, or the run fails as stale or ambiguous. No occurrence
  numbers.
- The generator also flips each operator of a chained comparison and drops each operand of a
  binary operator.
- A case for each input the reviewer found: a body line starting with `paths:` and a list item
  right after the frontmatter in a core file; a nested repository in the change set (no
  traceback; failing on it is a separate debt); a root file named `*.swift` beside a trigger in
  `docs/`; a `|` above the upkeep table; a row without its leading pipe right under the table;
  a check that prints nothing or two lines; the order of reasons in the hook message.

## Conditions of the moved review rules
| Condition (where it was) | Where it is now |
|---|---|
| `reviewer` is the only review agent (core-process) | core-process, Review and lessons, first line |
| Give it the mode, tier, round, and input (core-process) | core-process, first bullet |
| At most two rounds per mode (both files) | core-process, Rounds; the reviewer points to it |
| A recheck is not a round (reviewer) | core-process, Rounds |
| Log each review; never start a fresh review to reset the count (core-process) | core-process, Rounds |
| Fix blocking findings yourself (core-process) | core-process, Blocking findings |
| A disputed blocking finding, including one the reviewer is not sure of, gets a recheck at any tier (both files) | core-process, Blocking findings; "disputed" defined in the reviewer, Convergence |
| A disputed non-blocking finding is the author's call, reason in plan.md (reviewer) | core-process, Non-blocking |
| Non-blocking and pre-existing findings to tech debt, or to the backlog in the owner's language (core-process) | core-process, Non-blocking |
| A repeated class is fixed at its source in the same task, with a preference order (core-process; a shorter list in the reviewer) | core-process, one order; the reviewer and `core-agent-system.md` point to it |
| `fix and verify`: no other round; tests or checks in code mode; in decision mode recorded in plan.md and checked by code round 1 (both files) | core-process, `fix and verify` |
| `rethink approach`: revise the brief, a fresh pair once per change; a second one leaves the part out, keeps the old behavior, is recorded and reported, and is a product question if the user would notice (core-process; "the author goes back to the brief" in the reviewer) | core-process, `rethink approach` |
| Round 2 reviews only the new diff and open findings; settled points stay closed (reviewer) | reviewer, Convergence |
| A security pass is part of code round 1 (reviewer) | reviewer, Convergence |
| Verdicts per round and mode, with the conditions for `fix and verify` (reviewer) | reviewer, Convergence |
| A shared class is named with its source (reviewer) | reviewer, Convergence |
| What makes a finding disputed; mark the unsure ones (reviewer) | reviewer, Convergence |

New elements: one path rule (the rules for changing the agent system had no place that loads when
they apply; the always-loaded core would pay for them in every session), one check (the upkeep
dates; the same shape as `check-lessons`), one document (`docs/agent-system.md`, the ledger moved
out of a task folder), and the mutant generator in the self-test (item 9). Nothing else; `check-risk`
and `check-layers` each lost logic that no case observed.

Alternatives considered: the adoption rule in `core-process.md` (always loaded; costs every session
for a rule used only when the system changes); upkeep as scheduled sessions (costs money on every
run whether or not anything is due, and each run needs a branch and a merge); upkeep reported
without failing (nothing makes anyone act on it, the class this item fixes).

## Blocked: the logic package on Linux

The owner approved building and testing the logic package in cloud sessions. The toolchain host
`download.swift.org` is denied by the environment's network policy (403 on 2026-10-28, checked
twice), so nothing here is built yet and no setup script is written: it could not be tested. When
the host is allowed: install the toolchain matching the Mac's Swift version, prove that a package
with Swift Testing builds and runs here, then record in the skeleton ADR that the logic package
must build on Linux (Foundation only; no Apple-only modules; storage models outside the package or
a store that builds on Linux, decided in ADR-0002), and change the platform pack's build line.

## Verification

- `scripts/check`, `scripts/test-checks`, `scripts/test-checks --mutants`.
- Measurement against the current `dev` (e046484) on the same cases, model, and settings: traps
  T1–T3, design D1–D4, trigger S3 for both; review R1–R9, product P1–P3, and triggers for the new
  version against `baseline.md`, section 16. Items 3 and 4 change multi-turn behavior the
  single-turn cases cannot exercise; the measurement shows only that they do no harm there.

## Log
- Control measurement on `dev` (e046484), with-system arm only, 2 runs per case
  (`evals/results/selfreview-control/`): T1 trap 2/2, proportionate 0/2; T2 trap 2/2,
  proportionate 2/2; T3 trap 0/2, proportionate 1/2; design D1, D3, D4 all criteria, D2 one run
  failed future sync and proportionate; S3 design skill 0/2. The design skill did not load in any
  trap run. Cost 7.97 USD.
- Changes committed (0635083): `scripts/check` passes; `scripts/test-checks` 130 cases; `--mutants`
  45 of 45 killed (one mutant survived first: the new "rule file in no layer" check covered the
  old "unnamed core file" check; a case with a `core-` file listed by the platform pack now tells
  them apart).
- Reviewer, code, round 1 (0635083): `changes needed`, seven blocking, five non-blocking, two
  repeated classes. Fixed:
  1. The recheck covers a blocking finding the reviewer marks as not sure, and a marked
     non-blocking one is the author's call; `fix and verify` verifies with tests or checks in code
     mode, and in decision mode code round 1 checks the fixes (conditions table below).
  2. The adoption rule keeps a mechanism its ledger row keeps by policy, decides at the ceiling by
     the other three conditions, keeps a change the cases cannot exercise until its ledger measure
     decides, and keeps the two measuring principles ("grade the result, not the path"; "fix
     errors in the cases first").
  3. A menu question asks for a mechanism when its row states a rule (Concurrent code) or the
     answer finds a case the design does not handle; that case goes to the scenarios first.
  4. The boundary rule separates an instant (offset or zone) from a calendar date or wall-clock
     time (marked as such, without a zone).
  5. `check-upkeep` accepts dates up to today in UTC+14, so a date written in any zone passes.
  6. New cases: a task done today, today in UTC+14, a day after it, a dash for the date, an
     interval in months, a row without its leading pipe, a row after a blank line; the table must
     be one block of rows that start with "|".
  7. The prompt audit is every 30 days, as the audit plan approved ("раз в месяц"). The cleanup
     pass stays at 60 days: the approved cadence is about every five features, a dated check needs
     days, and the pace of features is unknown until the pilot. `docs/tech-debt.md` now points to
     the upkeep table instead of stating a cadence.
  Non-blocking, fixed: the path rule lists the mechanism paths (Project Knowledge references do not
  load it) and says project facts are not mechanisms; one preference order in core-process that
  the path rule and the reviewer point to; the menu row points to the boundary rule instead of
  repeating its scope; the reviewer drops the author clause; "where a standard applies" for the
  primary source; the example sorts titles the way the system sorts names.
  Non-blocking, disputed (finding 8, a due task pulls upkeep into any branch session): kept as for
  expired lessons. At the current intervals that is about 20 continuations a year, each in its own
  commit; showing it only as a message outside agent-system changes leaves nothing that makes
  anyone do the task, the class item 5 fixes. Ledger row 24 names when to change it.
  Pre-existing: `check-pointers` scans only tracked Markdown; recorded in `docs/tech-debt.md`.
  Repeated classes:
  - Hand-picked mutants (third time): fixed at the source. `scripts/test-checks --mutants` now
    also generates mutants from the code of every check (each condition forced true and false,
    each operand of and/or dropped, each `not` removed, each single comparison flipped, each
    integer moved by one, each statement removed); a survivor needs a case or an `EQUIVALENT`
    entry with the reason. Each mutant runs only the cases that run its script and stops at the
    first failure; a case that hangs fails after 60 seconds. The lesson is now guarded by it.
  - A moved rule loses its condition: the conditions table below maps each condition to its new
    place, for the reviewer to diff.
- Run 1 (13452d5): 602 mutants (45 written, 557 generated), 133 survived. About half turned a clean
  failure into a crash, which also exits non-zero; the rest were missing edge cases (the grace
  period and interval boundaries, messages and line numbers, quoted and unquoted pointers,
  frontmatter handling, rule-file parsing), a bulk diff parse in `check-risk` that the per-file
  read already covered, and equivalent mutants.
- Fixes: an expected failure now excludes a Python traceback; every check's success line and its
  planted detail are checked; 35 new cases; `check-risk` reads each file's diff instead of parsing
  one bulk diff (12 lines less); `check-layers` skips frontmatter `paths` in every file instead of
  taking a flag; exit codes mutate only between zero and non-zero; identical mutations on
  identical lines are numbered so an `EQUIVALENT` entry covers one mutant.
- Run 2 (8d4e26f): 569 mutants, 42 survived; 9 more cases, 33 `EQUIVALENT` entries with reasons
  (the hook's crash handler, None returned as exit 0, maxsplit, cosmetic order and summary line,
  frontmatter lines that hold no term, a one-hour shift of the latest date).
- Run 3 (8c9191d): 568 mutants, 2 survived, both from cases that tested the wrong thing (a lesson
  case that failed for a missing field instead of the overdue entry; a frontmatter case whose key
  held no list). Fixed; both mutants and a related one are killed.
- Reviewer, code, round 2 (718a614): `rethink approach` for item 9 only; the rest of the diff is
  clean and round-1 findings 1–7 and 9–12 are resolved, finding 8 accepted as disputed. Blocking:
  `EQUIVALENT` exempted mutants that change a check's report (a body `paths:` line, a list item
  after the fence, a nested repository, the crash handler, the clock), with unstable keys; three
  reviewer mutants survived (the literal pathspec, a chained comparison, the end of the upkeep
  table). Non-blocking: a baseline timeout crashes the run; ledger row 26 is prose, not a gate; a
  stale comment. Pre-existing: an untracked nested repository hides its files from `check-risk`
  (recorded in `docs/tech-debt.md`); cases read the clock once. Item 9 revised above; a fresh pair
  of rounds follows, once per change.
- Revised item 9 applied (90f4e26 and the next commit): seams `SLUMPY_TEST_HOOK_CRASH` and
  `SLUMPY_NOW`; dates in `check-upkeep` and `check-lessons` without the machine's zone;
  `check-risk` split into dispatch and `check()`; the hook's entry moved to `run_hook()`; keys by
  function; chained comparisons and binary operands in the generator; cases for every input from
  round 2. A run with 653 mutants left 21 survivors: message texts no case read (now asserted in
  full), a second quoted section, a rule matching an empty name, and four bits of logic with no
  observable effect, deleted (blanking fence lines, the stdout of a failed change set, a chained
  index comparison, the fence branch of a mutant kept as equivalent: outside the frontmatter
  nothing is blanked). `EQUIVALENT`: 8 entries, each equivalent on every input (the module guard,
  `None` returned where the value becomes the exit code, the closing-fence operand).
