---
description: 'Skill trigger negative - trivial copy change must not start planning/spec ceremony.'
tags: [triggers]
runs: 2
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'No planning, spec or design skill fires; the change is just made.'
---

Поменяй текст кнопки «Начать» на «Погнали». Кнопка выглядит так: `Button("Начать", action: start)`. Файлов у тебя нет, просто покажи новую строку.
