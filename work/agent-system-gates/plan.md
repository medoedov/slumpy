# Deterministic gates before the Mac: brief and log

## Goal

Move the system's guarantees from prose to mechanisms where that is possible without a Mac, so
that "done" no longer depends on the agent remembering a check (core principle: what a machine can
check, a machine checks). Owner request of 2026-10-28, step 1 of the plan to bring the eight
priorities from "partly" to "done".

## What is added

| Piece | Enforces | Kind |
|---|---|---|
| `scripts/check` | One entry point; reports what ran and what did not (build and tests until the Xcode project exists) | gate |
| `scripts/check-risk` + `scripts/risk-paths` | A change to risky paths needs an ADR or a "T1 because" line; a security-pass trigger needs a "security pass" line; both in files the same change set touches | gate |
| `scripts/check-lessons` | A lesson guarded by "this entry only" gets a mechanism within 30 days or is removed; entries keep all fields | gate |
| `scripts/test-checks` | Each check fails on a planted violation and passes on a clean copy; runs inside `scripts/check` when `scripts/` changed | gate on the gates |
| Stop hook | Runs `scripts/check --hook` when a session finishes a turn; a failure keeps the session working; no second block in a row | gate, pending the owner |
| Permissions | Deny edits to the frozen Codex files; ask before any pull request merge; allow build and test commands for the Mac | gate, pending the owner |
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

- `scripts/risk-paths` follows the planned layout; it is provisional until the skeleton exists.
- The evidence check reads text: a "T1 because" line proves a decision was written, not that it
  is right. The reviewer and the pilot judge the content.
- Build, tests, lint, and the platform staleness check need the Mac.

## Verification

- `scripts/check` passes; `scripts/test-checks` passes 17 cases (each planted violation fails its
  check, a clean copy passes, the hook exits 2 on failure and 0 when already continuing).
- Ablation: traps T1 and T2 without the `engineering-design` skill, against the layer-split runs
  where the skill fired (`baseline.md`, section 16), to test whether the skill causes extra layers.

## Log
