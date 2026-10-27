---
description: 'Skill trigger - persisted model change with shipped data (T2-level change) phrased as a small task.'
tags: [triggers]
runs: 2
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'An implementation/design skill fires before code is proposed.'
---

Добавь в модель книги поле «число страниц». Хранение в SwiftData, сборка уже у тестировщиков. Файлов у тебя нет, просто покажи, что поменять.
