# Slumpy

iOS app that replaces the evening scroll with reading: timed reading sessions that can block
distracting apps, a deadpan companion character, a personal library, friends and duels.
Product content comes from the draft `mvp.md`: treat it as hypotheses, not decisions.

## Map

- How the project is built and why: load the `project-knowledge` skill.
- Technical decisions: `docs/decisions/` (ADRs; stack in ADR-0001). Traps hit: `docs/lessons.md`.
  Domain notes: `docs/domains/`. Technical debt: `docs/tech-debt.md`.
- Feature work: `work/{feature}/spec.md` (what and why), `work/{feature}/plan.md` (brief,
  progress log, deviations). Later ideas and bugs: `backlog.md`. Default branch: `dev`.
- App code builds and tests only on a Mac with Xcode; cloud sessions cannot run it.
- Docs: Apple frameworks from Apple's documentation (recipe in `.claude/rules/swift.md`), other
  libraries through context7.
- `AGENTS.md`, `.agents/`, `.codex/`, `.githooks/` are frozen: do not edit, regenerate, or enable
  them, and do not read them as project facts (they describe the old Expo setup).

## Decision rights

The owner is not a programmer and does not read code. The owner decides only: what the user sees
or feels, scope, privacy and user data, money, and external actions (push or merge to `main`, App
Store Connect, TestFlight, publications). Decide everything else yourself and record it (plan.md;
an ADR for T2). Never ask the owner a technical question. Product questions go through the
`product-spec` skill. During implementation ask only about a deviation the user would notice;
otherwise take the conservative option and log it in plan.md.

## Risk tiers

Classify by the decision the change makes. When unsure, go higher.

- **T0 trivial:** text, color, a one-place edit without new types. Verify; no brief, no review.
- **T1 normal:** work inside decisions already made, including an additive optional field with a
  lightweight migration. A feature gets a short brief in plan.md (`engineering-design` skill); a
  bug gets a failing test first. Verify, reread your own diff against the brief. Run `reviewer`
  on the code when the change touches shared state or concurrency, or when you are unsure.
- **T2 new irreversible decision:** a new persisted entity or storage; a schema change that is
  not additive (rename, delete, type or relationship change); a new module boundary or a breaking
  change to the shared package's API; concurrency architecture; a new extension, entitlement, or
  system service; network, backend, sign-in, money; user data leaving the device (user-initiated
  system sharing does not count); a new third-party dependency. Each listed item is T2 the first
  time; repeating a pattern that an ADR records in detail is T1. Brief with two alternatives and
  cost of change in a year, an ADR, `reviewer` on the decision before code and on the code.
  Product consequences go to the owner.

Whatever the tier:

- A change that touches Keychain, permissions, ATS, the Privacy Manifest (including
  required-reason APIs), or user data leaving the device gets `reviewer` with a security pass.
- A persisted schema change ships with a test that opens a store created by the previous schema
  version.

## Scope

Change only what the task needs: no unrequested features, layers, settings, or rewrites of
adjacent code. Problems noticed along the way go to `docs/tech-debt.md`, or to `backlog.md` when
the user would notice them, instead of into this change.

## Review and lessons

`reviewer` is the only review agent: give it the mode, tier, round, and the diff or document. Fix
blocking findings yourself; a blocking finding you dispute gets a recheck, at any tier. Non-blocking and pre-existing findings go to `docs/tech-debt.md`, or to
`backlog.md` in plain Russian when the user would notice them. A finding class that repeats is
fixed at its source in the same task, preferring: compiler, lint rule, test, skill,
`docs/lessons.md`, this file. At most two rounds per mode (spec, decision, code); log each review
in plan.md (mode, round, verdict) and never start a fresh review to reset the count. On
`fix and verify`, apply the listed fixes and verify them without another round. On
`rethink approach`, revise the brief and review the new approach with a fresh pair of rounds, once
per change. If that also ends with `rethink approach`, do not ship the part that carries the open
blocking finding and keep the previous behavior; record it in plan.md and list it in the owner
report. If the user would notice the missing part, that becomes a product question.

## Done

"Done" needs evidence from the current state: verification output for the latest commit
(`scripts/check` once it exists). Say what could not be verified and why. Never weaken a test or
disable a check to get green; if one must change, state the reason where the reviewer sees it.
A finished feature also updates Project Knowledge as its "When finishing a feature" section says.

## Owner report

In Russian, without code: what changed for the user; screenshots when there is UI (light and dark,
large text, iOS 18 and current iOS); what was verified; decisions in plain words; deviations;
changes to product facts or hypotheses in Project Knowledge, one line each; parts left out because
a review did not converge; a manual iPhone checklist if a check needs the device.

## Language and secrets

- Russian for everything addressed to the owner (chat, specs, reports, backlog, README). English
  for code, comments, technical docs, ADRs, plans, skills, agent prompts.
- Ask questions as plain chat text, not with the AskUserQuestion tool.
- Never ask for secrets in chat; they live in a git-ignored `.env` on the Mac or Xcode Cloud secrets.

## Compaction

Keep: files changed so far, the current plan.md step, verification commands and their last
result, open review findings.
