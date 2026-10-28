# Agent process (core)

This file, `core-code.md`, `core-agent-system.md`, the `reviewer` agent, and the
`engineering-design`, `product-spec`, and `project-knowledge` skills are the core: they hold only what applies to any project. Platform rules
live in the platform pack (`.claude/rules/platform.md` and the files it names); this project's facts
live in CLAUDE.md, Project Knowledge, and `docs/`. Put each new rule in the layer it belongs to. A
platform or project line names what a core rule leaves open (a file, a module, a value) and points
to the rule; it never restates the rule.

## Where things live

- How the project is built and why: the `project-knowledge` skill.
- Docs: platform frameworks from the platform's documentation (the platform pack says how to read
  it); other libraries through context7.
- Technical decisions: `docs/decisions/` (ADRs). Traps hit: `docs/lessons.md`. Domain notes:
  `docs/domains/`. Technical debt: `docs/tech-debt.md`.
- Feature work: `work/{feature}/spec.md` (what and why), `work/{feature}/plan.md` (brief,
  progress log, deviations). Later ideas and bugs: `backlog.md`.

## Decision rights

The owner is not a programmer and does not read code. The owner decides only: what the user sees
or feels, scope, privacy and user data, money, and external actions (CLAUDE.md lists them). Decide
everything else yourself and record it (plan.md; an ADR for T2). Never ask the owner a technical
question. Product questions go through the `product-spec` skill. During implementation ask only
about a deviation the user would notice; otherwise take the conservative option and log it in
plan.md.

## Risk tiers

Classify by the decision the change makes. When unsure, go higher.

- **T0 trivial:** text, color, a one-place edit without new types. Verify; no brief, no review.
- **T1 normal:** work inside decisions already made, including an additive optional field with a
  lightweight migration. A feature gets a short brief in plan.md (`engineering-design` skill); a bug
  a test can observe gets a failing test first, failing because of the bug (a build or setup error
  does not count; a session whose environment cannot run tests at all, as the platform pack says,
  names the test in the commit's `Unverified:` line).
  Verify, reread your own diff against the brief. Run `reviewer` on the code when the change
  touches shared state or concurrency, or when unsure.
- **T2 new irreversible decision:** a new persisted entity or storage; a schema change that is
  not additive (rename, delete, type or relationship change); a new module boundary or a breaking
  change to a shared package's API; concurrency architecture; a new platform capability (the
  platform pack names them); network, backend, sign-in, money; user data leaving the device
  (user-initiated system sharing does not count); a new third-party dependency. Each listed item
  is T2 the first time; repeating a pattern that an ADR records in detail is T1. Brief with two
  alternatives and cost of change in a year, an ADR, `reviewer` on the decision before code and on
  the code. Product consequences go to the owner.

Whatever the tier:

- A change that touches secret storage, permissions, transport security, user data leaving the
  device, or the platform's privacy declarations, or meets another security-pass trigger the
  platform pack lists, gets `reviewer` with a security pass.
- A persisted schema change ships with a test that opens a store created by the previous schema
  version.
- Data that crosses a boundary (a file, an export, another app or process, the network) gets a
  representation the other side reads without guessing: an instant with its offset or time zone; a
  calendar date or a wall-clock time marked as such, without a zone; money as a decimal with its
  currency; text with its encoding, and its normalization and collation where it is compared or
  sorted; identifiers in a stated format; units and number formats. Where a standard applies,
  check against its primary source.

## Scope

Change only what the task needs: no unrequested features, layers, settings, or rewrites of
adjacent code. Problems noticed along the way go to `docs/tech-debt.md`, or to `backlog.md` when
the user would notice them, instead of into this change.

## Review and lessons

`reviewer` is the only review agent; its verdicts are defined in the agent. This section is the
author's side.

- Give `reviewer` the mode, tier, round, and the diff or document.
- Rounds: at most two per mode (spec, decision, code); a recheck is not a round. Log each review in
  plan.md (mode, round, verdict). Never start a fresh review to reset the count.
- Blocking findings: fix them yourself. A blocking finding you dispute, or one the reviewer marks
  as not sure, gets a recheck, at any tier.
- Non-blocking and pre-existing findings go to `docs/tech-debt.md`, or to `backlog.md` in plain
  words in the owner's language when the user would notice them. A non-blocking finding you
  dispute, or one the reviewer marks as not sure, is your call; record the reason in plan.md.
- A finding class that repeats is fixed at its source in the same task, preferring, in this order:
  project structure or the compiler, a lint rule, test, check, or hook, a review step, a skill or
  path rule, `docs/lessons.md`, an always-loaded file of the layer the rule belongs to.
- `fix and verify`: apply the listed fixes without another round. In code mode, verify them with
  tests or checks; in decision mode, record them in plan.md, and code round 1 checks them.
- `rethink approach`: revise the brief and review the new approach with a fresh pair of rounds,
  once per change. If that also ends with `rethink approach`, do not ship the part that carries the
  open blocking finding and keep the previous behavior; record it in plan.md and list it in the
  owner report. If the user would notice the missing part, that becomes a product question.

## Done

"Done" needs evidence from the current state: verification output for the latest commit (the
check command CLAUDE.md names, once it exists). Say what could not be verified and why. Never
weaken a test or disable a check to get green; if one must change, state the reason where the
reviewer sees it. Each commit message body has one line above the trailer lines:
`Verified: <command and result>` or `Unverified: <why>`. A finished feature also updates Project
Knowledge as its "When finishing a feature" section says.

## Owner report

In the owner's language, without code: what changed for the user; screenshots when there is UI
(the matrix the platform pack sets); what was verified; decisions in plain words; deviations;
changes to product facts or hypotheses in Project Knowledge, one line each; parts left out because
a review did not converge; a manual device checklist if a check needs the device.

## Language and secrets

- The owner's language (CLAUDE.md names it) for everything addressed to the owner: chat, specs,
  reports, backlog, README. English for code, comments, technical docs, ADRs, plans, skills, agent
  prompts.
- Ask questions as plain chat text, not with the AskUserQuestion tool.
- Never ask for secrets in chat; CLAUDE.md says where they live.

## Compaction

Keep: files changed so far, the current plan.md step, verification commands and their last
result, open review findings.
