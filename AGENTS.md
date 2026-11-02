# Slumpy

iOS app that replaces the evening scroll with reading: timed reading sessions that can block
distracting apps, a deadpan companion character, a personal library, friends and duels.
Product content comes from the draft `mvp.md`: treat it as hypotheses, not decisions.

## Shared instructions

This is the maintained entry point for Claude Code and Codex. `CLAUDE.md` only imports this file
for older Claude Code installations; do not generate a second copy of these instructions.

Read `.claude/rules/core-process.md` and `.claude/rules/platform.md` at the start of project work
unless already loaded. The `.claude/` paths below hold shared content, not a second methodology.
Use this project's workflow where a generic installed skill prescribes a different workflow;
do not run the former Claude-to-Codex converter on this repository.

Load only the additional context needed by the task:

- Project changes, debugging, or explanations: `.claude/skills/project-knowledge/SKILL.md` and
  the relevant references it names.
- Product requirements with open decisions: `.claude/skills/product-spec/SKILL.md`.
- Feature design and new hard-to-reverse technical choices:
  `.claude/skills/engineering-design/SKILL.md`.
- Swift work: `.claude/rules/core-code.md` and `.claude/rules/swift.md`.
- Agent-system changes: `.claude/rules/core-agent-system.md`.
- Independent checks, when the process calls for them: `.claude/agents/reviewer.md`.

Runtime setup and the mechanism ledger: `docs/agent-system.md`. Codex skill entries in
`.agents/skills/` are small adapters to the shared skills. Historical `work/` records describe
the versions measured then; they do not override current instructions.

## Project facts

- Minimum iOS 18; Swift 6 language mode with strict concurrency; the latest stable Xcode
  (ADR-0001).
- The local logic package does not import SwiftUI, UIKit, or other UI frameworks (ADR-0001). It is
  the shared module where independent facts are merged on read (`engineering-design` menu,
  Concurrent code).
- Default branch: `dev`. Backlog: `backlog.md`.
- External actions: push or merge to `main`, App Store Connect, TestFlight, publications.
- Check command: `python scripts/check` (`python3 scripts/check` on hosts with that executable).
  It runs document checks now; application build and tests await the Xcode skeleton.
- After changing `scripts/`, run `python scripts/test-checks` and
  `python scripts/test-checks --mutants`; report what their listed cases cover and any gaps.
- The owner's language: Russian.
- Where secrets live: Project Knowledge, `deployment.md`, Secrets.
- `.githooks/` remains frozen and disabled; its old hooks call files outside the repository.
