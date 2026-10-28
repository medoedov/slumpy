# Deterministic gates before the Mac: brief and log

## Goal

Move the system's guarantees from prose to mechanisms where that is possible without a Mac, so
that "done" no longer depends on the agent remembering a check (core principle: what a machine can
check, a machine checks). Owner request of 2026-10-28, step 1 of the plan to bring the eight
priorities from "partly" to "done".

## What is shipped

| Piece | Enforces | Kind |
|---|---|---|
| `scripts/check` | One entry point for the document checks; reports what did not run (build, tests, lint until the skeleton; the self-test, which is on demand) | gate |
| `scripts/check-risk` + `scripts/risk-paths` | Risky paths and text need evidence added by the same change set since the merge base with `origin/dev`; the rules, the change set, and the evidence format live in the `risk-paths` header | gate |
| `scripts/check-lessons` | A lesson guarded by "this entry only" gets a mechanism within 30 days or is removed; entries keep all fields | gate |
| `scripts/test-checks` | On demand. Fixed cases plus cases built from data: one per rule line in `risk-paths` (with a count of rule lines independent of the parser) and one per check in `scripts/check`, each with a planted failure. `--mutants` runs the unmodified self-test first, then requires each listed mutant to fail it | gate on the gates |
| Stop hook | Exits when the change set is empty; otherwise runs the document checks and blocks on a failure with a JSON decision; while already continuing, shows the failures as a system message. Keeps no record of its own | gate |
| Permissions | Deny edits to the frozen Codex files; ask before any pull request merge and before `xcodebuild` archive, export, or provisioning changes; allow build and test commands for the Mac | gate |
| `work/agent-system-audit/mechanisms.md` | Each mechanism with its target error, evidence, pilot measure, and removal criterion, set before the pilot | record |

Drift fixed in the same change: README, `.gitignore` for Xcode, Node for context7 on the Mac,
single owners for the minimum iOS (ADR-0001), the Mac-only build (`platform.md`), secrets
(`deployment.md`), and the screenshot matrix (`platform.md`).

## Left out

The fresh pair of reviews ended `rethink approach`; per core-process.md, Review and lessons, the
parts with open blocking findings are not shipped and the previous behavior stays (no such gate):

- **Session-start base.** A SessionStart hook recording HEAD so a push to `dev` cannot empty the
  change set. Open: the "older of" choice had a case in one direction only, the record would be
  missing in resumed sessions, and the record's name lived in two scripts.
- **Self-test inside `scripts/check` and the hook.** Open: the switch that skips it inside the
  self-test was unobservable, and its planted failure was empty.
- **`scripts/check` failing once an Xcode project exists.** Open: the markers were read through
  the same parser that built their cases.

The way back is in `docs/tech-debt.md` (generated mutants first); the class is in
`docs/lessons.md`. Nothing here is visible to the app's user.

## Settings

`.claude/settings.json` holds the hook and the permissions: the earlier deny rules unchanged, plus
the Stop hook, the frozen-file denies, the merge and Xcode-distribution prompts, and the Mac allow
list. The auto-mode classifier blocks an agent from editing its own settings
(`[Self-Modification]`), also on the owner's request; on 2026-10-28 the owner switched the
session to Accept edits and asked the agent to apply them.

## Limits

- `scripts/risk-paths` follows the planned layout and approximates the platform pack's lists; it
  is provisional until the skeleton exists. Required-reason APIs are not matched yet (they need
  the Privacy Manifest's declared categories to avoid a block on every use).
- The evidence check reads text: a "T1 because" line proves a decision was written, not that it
  is right. The reviewer and the pilot judge the content.
- After a push to `dev` in the same turn, `origin/dev` equals HEAD and the change set is empty, so
  the hook is silent and `check-risk` sees nothing (the session-start base was left out). The
  `scripts/check` run that "Done" requires before the commit covers it.
- On a branch ahead of `origin/dev`, the normal state during feature work, every turn, chat-only
  turns included, is blocked once while any check fails (for example a lesson that expired); on
  `dev` with nothing new the hook is silent.
- The self-test (about 15 seconds) and the mutation run (about 4 minutes) are on demand after a
  change to `scripts/` (CLAUDE.md, Agent system); neither runs in the hook. The hook takes about
  2 seconds.
- A syntax error in `scripts/check` itself makes the hook a non-blocking error; the run before a
  commit shows it.
- Build, tests, lint, and the platform staleness check need the Mac.

## Verification

- `scripts/check` passes; `scripts/test-checks` passes 112 cases; `--mutants` kills all 29 listed
  mutants after a passing baseline. The listed mutants are hand-picked; the last reviewer's own
  mutants found fail-open survivors in the parts that were then left out.
- Ablation: traps T1 and T2 without the `engineering-design` skill, against the layer-split runs
  where the skill fired (`baseline.md`, section 16), to test whether the skill causes extra layers.

## Log
- Reviewer, code, round 1 (97307c3): `changes needed`, eight blocking. Repeated class: a check
  reported success on input it never read (no base ref, names with spaces or non-ASCII, deleted
  files, old evidence lines, a crash downgraded to a non-blocking hook error). Also: the hook
  could block chat-only turns; `xcodebuild` allow covered App Store uploads; the self-test left
  rules untested; the first lesson escaped its own expiry; ledger rows lacked criteria. Fixed: the
  checks fail when they cannot determine input; `-z` names, deleted files, added-line evidence
  anchored at line start, new ADRs only; the hook prints a JSON decision, skips unchanged states,
  and turns repeats into a system message; ask rules for archive, export, and provisioning; the
  self-test grew from 17 to 35 cases and kills all eight mutants; the lesson split in two; the
  ledger has criteria in every row. The self-test also found a bug of the author's: an untracked
  Xcode project went unnoticed.
- Ablation on traps T1 and T2 without the design skill: `baseline.md`, section 17.
- Reviewer, code, round 2 (40a4773): `rethink approach`. Both round-1 classes recurred: the hook
  skipped the first turn of a fresh clone that committed failing work (a gate reporting success on
  input it never read), and 12 of 18 reviewer mutants survived the self-test. Non-blocking: two
  lists of Xcode project markers; the crash path ignored `stop_hook_active`. Revised approach
  above; a fresh pair of rounds follows, once per change.
- Reviewer, code, fresh round 1 (1b093cd): `changes needed`. Both classes again: a push moved the
  base, a failing baseline still counted mutant kills and the cache kept the pass, 22 of 24 new
  mutants survived (risk rules, check list, skip paths), a second ref list in the hook, a core
  condition dropped ("once it exists"). Second revision above: state and caches removed, session
  base added, data-driven cases, baseline-first mutants, the condition restored.
- Reviewer, code, fresh round 2 (8a941d9): `rethink approach`, the last round. Gate logic no case
  observed recurred (the base direction, the self-test switch, the project markers), the
  session-start record would be missing in resumed sessions, the record name lived in two
  scripts, and a Limits sentence was wrong. Per the rule, the three parts are left out (section
  above) and the sentence corrected; the shipped rest re-verified: 112 cases, 29 of 29 mutants
  after a passing baseline.
