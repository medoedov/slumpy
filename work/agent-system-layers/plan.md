# Agent system layers: brief and log

## Goal

Separate the agent system into three layers so platform and project details have one designated
place each, and the core can be reused in another project without edits:

| Layer | Files | Holds |
|---|---|---|
| Core | `.claude/rules/core-process.md`, `.claude/rules/core-code.md`, `.claude/agents/reviewer.md`, `SKILL.md` of `engineering-design`, `product-spec`, `project-knowledge` | Process and engineering rules that apply to any project |
| Platform pack (Apple iOS) | `.claude/rules/platform.md`, `.claude/rules/swift.md` | Rules and facts for any iOS project |
| Project (Slumpy) | `CLAUDE.md`, `project-knowledge/references/`, `docs/`, `work/` | This project's facts and choices |

Core files name the platform pack only through `.claude/rules/platform.md` and the project only
through CLAUDE.md. `core-code.md` keeps a `paths` glob, which each project sets.

## Mechanism

- Core process moves from CLAUDE.md to `.claude/rules/core-process.md` without `paths`: rules
  without `paths` load at launch with the same priority as CLAUDE.md, and subagents receive project
  rules with the CLAUDE.md hierarchy (Claude Code memory and subagents docs, 2026-10-28).
  `@path` imports were the alternative; rules need no new mechanism and the eval packaging already
  injects every rule file.
- Platform pack: always-loaded `platform.md` holds the tier and security triggers, the screenshot
  matrix, the docs recipe, the Mac-only build, and the platform design questions (needed during a
  brief, before any code file exists). Path-scoped `swift.md` keeps code-time facts, the bypass
  list, and the Swift review rubric; the design skill and the reviewer read it explicitly.
- Binding, not restating (revised approach after review round 2): a platform or project line names
  what a core rule leaves open (a file, a module, a value) and points to the rule; it never
  restates the rule. Stated in core-process.md, first paragraph.
- `scripts/check-layers` fails when a core file contains a listed platform or project term or
  Cyrillic text (the core is English; the owner's language comes from CLAUDE.md); it derives the
  core list from core-process.md and checks both directions. `scripts/check-pointers` fails when a
  `file.md`, Section pointer names a section the file does not have (dated records skipped).

## Mapping (nothing dropped)

The last column lists each condition of the old rule and where it is kept; the reviewer checks it.

| Old place | New place | Conditions kept |
|---|---|---|
| CLAUDE.md: product summary, mvp.md status, frozen dirs, default branch | CLAUDE.md | verbatim |
| CLAUDE.md: Map (docs, work, backlog, project-knowledge) | core-process, Where things live | verbatim |
| CLAUDE.md: Mac-only build, Apple docs recipe | platform.md | verbatim |
| CLAUDE.md: Decision rights | core-process | owner decides only the listed areas; external actions named in CLAUDE.md (push or merge to `main`, App Store Connect, TestFlight, publications); deviation questions only when the user would notice |
| CLAUDE.md: T1 | core-process | bug test only when a test can observe the bug; fails because of the bug; build or setup error does not count; exemption only where tests cannot run at all (platform.md: cloud sessions), the test named in `Unverified:`; reviewer when shared state, concurrency, or unsure |
| CLAUDE.md: T2 | core-process; platform.md names capabilities | every category kept; "extension, entitlement, system service" as platform capabilities; first time T2, repeat of a recorded pattern T1 |
| CLAUDE.md: Whatever the tier | core-process; platform.md lists triggers | Keychain, permissions, ATS, Privacy Manifest edits, undeclared required-reason API (platform.md); user data leaving the device (core); schema test against the previous version |
| CLAUDE.md: Scope, Done, Compaction | core-process | check command named in CLAUDE.md (`scripts/check`, planned, Mac) |
| CLAUDE.md: Review and lessons | core-process | backlog in plain words in the owner's language; fix ladder ends at an always-loaded file of the rule's layer; round limits and verdict actions verbatim |
| CLAUDE.md: Owner report | core-process; platform.md | owner's language; screenshot matrix light and dark, large text, minimum and current iOS; device checklist |
| CLAUDE.md: Language and secrets | core-process; CLAUDE.md | owner-facing list verbatim; Russian and the secret location in CLAUDE.md |
| swift.md: minimum iOS 18, logic package without UI imports, Swift 6 mode, latest Xcode | CLAUDE.md, Project facts | verbatim; availability rule in swift.md refers to the minimum |
| engineering-design menu: merge on read in the logic package | core menu: independent facts merged on read in one shared module, a single record gets one writer or transactions; CLAUDE.md binds the module name only | both branches stay in the menu |
| swift.md: other facts, bypass list, toolchain, Liquid Glass, monitor memory | swift.md | isolation per module decided in an ADR (architecture.md names the skeleton ADR); both UI styles checked while the minimum is below iOS 26 |
| swift.md: Tests and fixes; "traps go to lessons" | core-code.md | verbatim except generic examples (guard, default value; a killed process); device-only exit points to Project Knowledge, verification |
| reviewer: Swift rubric items | swift.md, Review rubric | verbatim; "iOS 18" becomes the minimum iOS |
| reviewer: business rule in two places | reviewer | "(app, extension, widget, package)" becomes "(two modules, targets, or processes)" |
| engineering-design menu: Swift 6 checking, App Group, iOS versions, App Review, Apple standards, Dynamic Type, VoiceOver | platform.md, Design questions (always loaded) | verbatim; the menu keeps generic wording that points to them |
| product-spec: Russian phrases and labels | product-spec | owner's language from CLAUDE.md; the closing line keeps both options (per recommendations, or only the disagreements) |
| project-knowledge: mvp.md paragraph | project-knowledge; CLAUDE.md | hypotheses until approved; CLAUDE.md names the draft |

## Verification

- `scripts/check-layers` passes.
- Reviewer, code mode, on the diff: nothing lost or changed in meaning, layers clean, pointers.
- Eval: all groups on the new commit against the current dev (traps, review, design from
  `evals/results/ubmode-treatment*`, same rule text; product and triggers re-run on dev).
  Two confounds, stated before the run: the packaging injects every rule file into the main
  session, path-scoped ones included, so the eval cannot show loading changes; and the packaged
  reviewer subagent gets no injected context and no `.claude/rules/` files, while it lost the
  Swift rubric from its own prompt. Changes in groups where the reviewer runs (traps, design) are
  not attributed to this restructure unless they also show in the main agent's answer.

## Log

- Reviewer, code, round 1 (770f46e): `changes needed`, five blocking. Three generalized rules lost
  their limiting condition (plain words for the backlog, the no-tests exemption scoped to sessions
  that cannot run tests, merge-on-read in the logic package); the platform design questions moved
  behind a path-scoped file; three pointers were stale; `scripts/check-layers` missed most moved
  details and an unlisted core file; the eval confounds were unstated. All fixed: the design
  questions moved to always-loaded `platform.md`, the check derives the core list from
  core-process.md and checks both directions, the lesson in `docs/lessons.md` now covers moving
  rules between layers. Pre-existing fix in scope: Swift 6 mode and the latest-Xcode choice moved
  from swift.md to CLAUDE.md.
- Reviewer, code, round 2 (10226e4): `rethink approach`. Small findings, but two repeat round-1
  classes: a project line restated a core rule and dropped its condition (merge on read for all
  multi-writer data), and two pointers went stale after the design questions moved; check-layers
  still skipped frontmatter descriptions. Revised approach: platform and project lines bind names
  and point to rules (core-process.md), the mapping table lists conditions per rule,
  `scripts/check-pointers` catches stale section pointers, check-layers skips only `paths`. A fresh
  pair of rounds follows, once per change.
