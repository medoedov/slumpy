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
| `scripts/test-checks` | Each planted violation fails its check, each valid change passes, an input a check cannot read fails it; runs inside every `scripts/check` | gate on the gates |
| Stop hook | Runs `scripts/check --hook` when a turn ends and the repository changed since its last run; a failure blocks once with a JSON decision; a repeat shows the open failures to the owner as a system message | gate, pending the owner |
| Permissions | Deny edits to the frozen Codex files; ask before any pull request merge and before `xcodebuild` archive, export, or provisioning changes; allow build and test commands for the Mac | gate, pending the owner |
| `work/agent-system-audit/mechanisms.md` | Each mechanism with its target error, evidence, pilot measure, and removal criterion, set before the pilot | record |

Drift fixed in the same change: README, `.gitignore` for Xcode, Node for context7 on the Mac,
single owners for the minimum iOS (ADR-0001), the Mac-only build (`platform.md`), secrets
(`deployment.md`), and the screenshot matrix (`platform.md`).

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
- A commit pushed to `dev` in the same turn is not seen by the hook: the change set is empty once
  `origin/dev` equals HEAD. The `scripts/check` run that "Done" requires before the commit covers
  it.
- A syntax error in `scripts/check` itself makes the hook a non-blocking error; the run before a
  commit shows it.
- Build, tests, lint, and the platform staleness check need the Mac.

## Verification

- `scripts/check` passes; `scripts/test-checks` passes 35 cases. Eight mutants of the scripts that
  the round-1 reviewer or the author planted (t2 rule off, new-ADR evidence ignored, all evidence
  accepted, grace period removed, root-level match removed, unanchored security phrase, edited ADR
  accepted, chat-only guard removed) each fail the self-test.
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
