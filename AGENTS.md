# Project: Slumpy

> **iOS app that replaces the evening scroll with reading: a timed reading session that blocks
> distracting apps, a deadpan companion character, a personal library, and friends with duels.**

---

## How This Project Works

**Context:** Load the `project-knowledge` skill before changing, debugging, or explaining how this
project works: its code, configuration, skills, agents, or pipelines.

**Product source:** `./mvp.md` (MVP v0.3, partially agreed). Approved facts live in Project
Knowledge; items marked "proposal" or listed as open in `mvp.md` are not decisions.

**Default branch:** `dev`

**Backlog:** `./backlog.md`

**Library Documentation:** Always use context7 when you need code generation, setup or configuration steps, or library/API documentation. This means you should automatically use the Context7 MCP tools to resolve library id and get library docs without user having to explicitly ask.

## Language

- Artifacts addressed to the user (chat, plans, plan-mode, interviews, validator summaries,
  user-spec, README, backlog): the language the user writes in. This user writes in Russian.
- Technical docs, code, code comments, AI prompts, internal logs (tech-spec, tasks, AGENTS.md,
  skills): English.

## Behavior

- No "Great question!", no filler, no water.
- NEVER use plain chat question tool. Ask questions as plain text in chat instead.
- Never create Git worktrees or extra project copies unless the user explicitly asks.

## Task Scope

- The user's request and any explicitly approved plan define the authorized scope of work.
- Choose the minimal solution sufficient for the task. Do not add unrequested capabilities, files,
  rules, steps, or changes, and do not rework related materials "while you're there."
- Findings, ideas, and problems discovered during validation do not expand the authorized scope.
- Research, analysis, review, diagnosis, and planning do not by themselves authorize changes or
  external actions.

## Security

- NEVER ask the user to write secrets in chat; explain where to store them instead (local `.env`,
  EAS secrets, GitHub Actions secrets).
- ALWAYS ask before pushing to `main`.
- Be cautious with external actions (push, deploy, App Store Connect / TestFlight submissions,
  sending messages, creating PRs). Ask before acting externally when uncertain.
