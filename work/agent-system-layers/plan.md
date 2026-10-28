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
- Platform always-loaded part (tier and security triggers, screenshot matrix, docs recipe, Mac-only
  build) goes to `platform.md` without `paths`; code-time platform rules, the platform design
  questions, and the Swift review rubric go to path-scoped `swift.md`, which the design skill and
  the reviewer read explicitly.
- `scripts/check-layers` fails when a core file contains a platform or project term or Cyrillic
  text (the core is English; the owner's language comes from CLAUDE.md).

## Mapping (nothing dropped)

| Old place | New place |
|---|---|
| CLAUDE.md: product summary, mvp.md status, frozen dirs, default branch | CLAUDE.md |
| CLAUDE.md: Map (docs, work, backlog, project-knowledge) | core-process, Where things live |
| CLAUDE.md: Mac-only build, Apple docs recipe | platform.md |
| CLAUDE.md: Decision rights | core-process; external actions listed in CLAUDE.md |
| CLAUDE.md: Risk tiers, Whatever the tier | core-process with generic categories; platform names in platform.md |
| CLAUDE.md: Scope, Review and lessons, Done, Compaction | core-process ("plain Russian" becomes the owner's language; check command named in CLAUDE.md) |
| CLAUDE.md: Owner report | core-process; screenshot matrix in platform.md |
| CLAUDE.md: Language and secrets | core-process; owner's language and secret location in CLAUDE.md |
| swift.md: minimum iOS 18, logic package without UI imports | CLAUDE.md, Project facts |
| swift.md: other facts, bypass list, toolchain, docs, Liquid Glass, monitor memory | swift.md (docs recipe to platform.md) |
| swift.md: Tests and fixes; "traps go to lessons" | core-code.md |
| reviewer: Swift rubric items | swift.md, Review rubric |
| engineering-design menu: Swift 6 checking, App Group, iOS versions, App Review, Apple standards, Dynamic Type, VoiceOver | swift.md, Design questions; the menu keeps generic wording |
| product-spec: Russian phrases and labels | owner's language from CLAUDE.md |
| project-knowledge: mvp.md paragraph | CLAUDE.md names the source; the skill keeps the status rule |

## Verification

- `scripts/check-layers` passes.
- Reviewer, code mode, on the diff: nothing lost or changed in meaning, layers clean, pointers.
- Eval: all groups on the new commit against the current dev (traps, review, design from
  `evals/results/ubmode-treatment*`, same rule text; product and triggers re-run on dev).

## Log
