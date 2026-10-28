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
| `scripts/check-risk` + `scripts/risk-paths` | Risky paths and text need evidence added by the same change set; the rules and the evidence format live in the `risk-paths` header | gate |
| `scripts/check-lessons` | A lesson guarded by "this entry only" gets a mechanism within 30 days or is removed; entries keep all fields | gate |
| `scripts/test-checks` | Each planted violation fails its check, each valid change passes, an input a check cannot read fails it, every skip path and every part of the hook state has a case; runs inside every `scripts/check`. `--mutants` applies a fixed mutant list to a copy of the scripts and requires the self-test to fail on each; `scripts/check` runs it when `scripts/` is in the change set, once per exact content of `scripts/` | gate on the gates |
| Stop hook | Runs `scripts/check --hook` when a turn ends; see Revised approach for what counts as changed; a failure blocks once with a JSON decision; a repeat or a stop while already continuing shows the open failures as a system message | gate, pending the owner |
| Permissions | Deny edits to the frozen Codex files; ask before any pull request merge and before `xcodebuild` archive, export, or provisioning changes; allow build and test commands for the Mac | gate, pending the owner |
| `work/agent-system-audit/mechanisms.md` | Each mechanism with its target error, evidence, pilot measure, and removal criterion, set before the pilot | record |

Drift fixed in the same change: README, `.gitignore` for Xcode, Node for context7 on the Mac,
single owners for the minimum iOS (ADR-0001), the Mac-only build (`platform.md`), secrets
(`deployment.md`), and the screenshot matrix (`platform.md`).

## Revised approach (after review round 2, `rethink approach`)

- **What "changed" means for the hook.** Against the last state the hook actually checked (HEAD,
  the diff against HEAD, untracked names and contents), recorded only after its checks ran.
  Without a record, against the merge base with `origin/dev`: when HEAD equals it and the tree is
  clean, nothing on this branch is new and the hook exits without recording; in every other case,
  including a fresh clone whose first turn committed work, it runs. Without any base it runs.
- **How coverage of the self-test is proven.** A fixed mutant list in `scripts/test-checks`,
  reviewed like code, instead of mutants the author picks after the fact. Each mutant must make
  the self-test fail; a mutant whose text no longer occurs exactly once fails the run as stale.
  Every early return, skip path, and part of the hook state has a case whose skipped input holds a
  violation. Two switches stay outside the list because a case cannot observe them without
  recursing into the mutation run (named in the file); a real `scripts/check` run reports them.
- **One list per fact.** The files that mark an Xcode project are `project` rules in
  `scripts/risk-paths`; `scripts/check` reads them there. `check-risk --changed` is the only
  definition of the change set.

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
- After a push to `dev` in the same turn, the hook still runs (HEAD moved), but `check-risk` sees an
  empty change set once `origin/dev` equals HEAD. The `scripts/check` run that "Done" requires
  before the commit covers it.
- The mutation run takes about 2.5 minutes, once per exact content of `scripts/`; the proposed hook
  timeout is 600 seconds for that run.
- A syntax error in `scripts/check` itself makes the hook a non-blocking error; the run before a
  commit shows it.
- Build, tests, lint, and the platform staleness check need the Mac.

## Verification

- `scripts/check` passes: 54 cases, all 32 listed mutants killed, including the 18 the round-2
  reviewer planted. The stale-mutant guard fired once during the change (a mutant's text became
  ambiguous) and failed the run, as intended.
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
