# Deterministic gates before the Mac: brief and log

## Goal

Move the system's guarantees from prose to mechanisms where that is possible without a Mac, so
that "done" no longer depends on the agent remembering a check (core principle: what a machine can
check, a machine checks). Owner request of 2026-10-28, step 1 of the plan to bring the eight
priorities from "partly" to "done".

## What is added

| Piece | Enforces | Kind |
|---|---|---|
| `scripts/check` | One entry point; reports what ran and what did not; fails once an Xcode project exists until build and tests are wired in | gate |
| `scripts/check-risk` + `scripts/risk-paths` | Risky paths and text need evidence added by the same change set; the rules, the change set, and the evidence format live in the `risk-paths` header | gate |
| `scripts/check-lessons` | A lesson guarded by "this entry only" gets a mechanism within 30 days or is removed; entries keep all fields | gate |
| `scripts/test-checks` | Fixed cases plus cases built from data: one per rule line in `risk-paths`, one per check in `scripts/check`, so a rule or check without a working case fails it. `--mutants` (on demand after a change to `scripts/`) runs the unmodified self-test first, then requires each listed mutant to fail it | gate on the gates |
| SessionStart hook | Records HEAD at session start; the change set never starts later than that, so a push to `dev` cannot empty it | gate, pending the owner |
| Stop hook | Exits when the change set is empty; otherwise runs the document checks (and the self-test when `scripts/` changed) and blocks on a failure with a JSON decision; while already continuing, shows the failures as a system message. Keeps no record of its own | gate, pending the owner |
| Permissions | Deny edits to the frozen Codex files; ask before any pull request merge and before `xcodebuild` archive, export, or provisioning changes; allow build and test commands for the Mac | gate, pending the owner |
| `work/agent-system-audit/mechanisms.md` | Each mechanism with its target error, evidence, pilot measure, and removal criterion, set before the pilot | record |

Drift fixed in the same change: README, `.gitignore` for Xcode, Node for context7 on the Mac,
single owners for the minimum iOS (ADR-0001), the Mac-only build (`platform.md`), secrets
(`deployment.md`), and the screenshot matrix (`platform.md`).

## Revised approach, second version (after fresh review round 1)

The first revision kept state (a record of checked states, a mutation-run cache) and a skip for
"nothing new"; each added a way to report success on input never read. This version removes them:

- **Base:** the older of the session start (SessionStart hook) and the merge base with
  `origin/dev`. `check-risk --changed` is the only definition of the change set and of "nothing
  changed"; `scripts/check` has no ref logic of its own.
- **Hook:** no record, no cache. An empty change set means the turn changed nothing; otherwise the
  checks run, every time.
- **Coverage:** cases built from the rule and check lists, so the lists cannot outgrow the cases;
  the mutation run starts with the unmodified self-test, so it cannot count kills against a
  failing baseline; no cache of its result.

## Pending owner action

The auto-mode classifier blocks an agent from editing its own permission settings and hooks
(`[Self-Modification]`), so `.claude/settings.json` is not changed by the agent. The proposed file
is `work/agent-system-gates/settings.proposed.json`: the existing deny rules unchanged, plus the
hook, the frozen-file denies, the merge prompt, and the Mac allow list. The owner either replaces
`.claude/settings.json` with it on GitHub, or tells the agent in chat that this edit is approved.

## Limits

- `scripts/risk-paths` follows the planned layout and approximates the platform pack's lists; it
  is provisional until the skeleton exists. Required-reason APIs are not matched yet (they need
  the Privacy Manifest's declared categories to avoid a block on every use).
- The evidence check reads text: a "T1 because" line proves a decision was written, not that it
  is right. The reviewer and the pilot judge the content.
- Until the owner applies the settings there is no session-start record: after a push to `dev`
  in the same turn `origin/dev` equals HEAD and the change set is empty. The `scripts/check` run
  that "Done" requires before the commit covers it.
- A turn that changes something on a branch with a pre-existing failure (for example a lesson
  that expired) is blocked until the failure is fixed; a turn that changes nothing is not.
- The mutation run takes about 6 minutes and is on demand after a change to `scripts/` (CLAUDE.md,
  Agent system); it is not in the hook. The hook takes about 2 seconds, about 20 with the
  self-test.
- A syntax error in `scripts/check` itself makes the hook a non-blocking error; the run before a
  commit shows it.
- Build, tests, lint, and the platform staleness check need the Mac.

## Verification

- `scripts/check` passes; `scripts/test-checks` passes 135 cases (49 fixed, 86 built from the
  rules and checks); `--mutants` kills all 38 listed mutants after a passing baseline, including
  the reviewers' mutants that still apply to the new code.
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
