# Slumpy

iOS app that replaces the evening scroll with reading: timed reading sessions that can block
distracting apps, a deadpan companion character, a personal library, friends and duels.
Product content comes from the draft `mvp.md`: treat it as hypotheses, not decisions.

## Map

- How the project is built and why: load the `project-knowledge` skill.
- Technical decisions: `docs/decisions/` (ADRs; stack in ADR-0001). Traps hit: `docs/lessons.md`.
- Feature work: `work/{feature}/spec.md` (what and why), `work/{feature}/plan.md` (brief,
  progress log, deviations). Later ideas and bugs: `backlog.md`. Default branch: `dev`.
- App code builds and tests only on a Mac with Xcode; cloud sessions cannot run it.
- Docs: Apple frameworks from Apple's documentation (recipe in `.claude/rules/swift.md`), other
  libraries through context7.
- `AGENTS.md`, `.codex/`, `.githooks/` are frozen: do not edit, regenerate, or enable them.

## Decision rights

The owner is not a programmer and does not read code. The owner decides only: what the user sees
or feels, scope, privacy and user data, money, and external actions (push or merge to `main`, App
Store Connect, TestFlight, publications). Decide everything else yourself and record it (plan.md;
an ADR for T2). Never ask the owner a technical question. Product questions go through the
`product-spec` skill. During implementation ask only about a deviation the user would notice;
otherwise take the conservative option and log it in plan.md.

## Risk tiers

Classify by what the change touches. When unsure, go higher.

- **T0 trivial:** text, color, a one-place edit without new types. Verify; no brief, no review.
- **T1 normal:** feature or bug inside existing boundaries. Brief in plan.md (`engineering-design`
  skill), verify, `reviewer` on the code, at most two review rounds.
- **T2 irreversible:** persisted model or migration; module boundaries or the shared package;
  concurrency architecture; system services and extensions (entitlements, Info.plist, App Group);
  network, backend, sign-in, privacy, money; a new third-party dependency. Brief with two
  alternatives and cost of change in a year, an ADR, `reviewer` on the decision before code and on
  the code, re-check of disputed findings, a separate security pass when it touches Keychain, ATS,
  Privacy Manifest, or user data. Product consequences go to the owner.

## Scope

Change only what the task needs: no unrequested features, layers, settings, or rewrites of
adjacent code. Problems noticed along the way go to `backlog.md` instead of into this change.

## Review and lessons

`reviewer` is the only review agent: give it the tier and the diff or document. Fix valid findings
yourself. A finding class that repeats is fixed at its source in the same task, preferring:
compiler, lint rule, test, skill, `docs/lessons.md`, this file. Rounds count per change: never
start a fresh review to reset them. On `rethink approach`, revise the brief; if the new approach
also ends round 2 with a blocking finding, stop and report it to the owner as unresolved.
Pre-existing findings do not block: add each to `backlog.md` under «Баги» in plain Russian.

## Done

"Done" needs evidence from the current state: verification output for the latest commit
(`scripts/check` once it exists). Say what could not be verified and why. Never weaken a test or
disable a check to get green; if one must change, state the reason where the reviewer sees it.
A finished feature also updates Project Knowledge as its "When finishing a feature" section says.

## Owner report

In Russian, without code: what changed for the user; screenshots when there is UI (light and dark,
large text, iOS 18 and current iOS); what was verified; decisions in plain words; deviations; a
manual iPhone checklist if a check needs the device.

## Language and secrets

- Russian for everything addressed to the owner (chat, specs, reports, backlog, README). English
  for code, comments, technical docs, ADRs, plans, skills, agent prompts.
- Ask questions as plain chat text, not with the AskUserQuestion tool.
- Never ask for secrets in chat; they live in a git-ignored `.env` on the Mac or Xcode Cloud secrets.

## Compaction

Keep: files changed so far, the current plan.md step, verification commands and their last
result, open review findings.
