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

Conditions kept when moving review rules (lesson "An adapted or generalized rule loses the
condition that limits it"): reviewer is the only review agent; mode, tier, round, input; fix
blocking findings yourself; a disputed blocking finding gets a recheck at any tier; a disputed
non-blocking finding is the author's call with the reason in plan.md; non-blocking and
pre-existing findings to tech debt or, in plain words in the owner's language, to the backlog;
repeated class fixed at its source with the preference order; at most two rounds per mode; a
recheck is not a round; log every review; no fresh review to reset the count; `fix and verify`
fixes verified with tests or checks without another round, and in decision mode recorded and given
to code round 1; `rethink approach` once per change with a fresh pair; a second `rethink approach`
leaves the part out, keeps the previous behavior, is recorded and reported, and becomes a product
question if the user would notice. Reviewer side kept: round 2 reviews only the new diff and the
open findings; a security pass is part of code round 1; verdicts per round and mode; repeated class
named with its source; what makes a finding disputed.

New elements: one path rule (the rules for changing the agent system had no place that loads when
they apply; the always-loaded core would pay for them in every session), one check (the upkeep
dates; the same shape as `check-lessons`), one document (`docs/agent-system.md`, the ledger moved
out of a task folder). Nothing else.

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
