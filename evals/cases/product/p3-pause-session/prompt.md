---
description: 'Ambiguous product request - pausing a reading session, which conflicts with the anti-procrastination purpose.'
tags: [product]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Asks 1-5 product questions (no technical ones), each with a recommended option, in Russian; or resolves minor gaps as stated assumptions.'
---

Сделай, чтобы сессию чтения можно было поставить на паузу. Код пока не пиши, сначала договоримся, что именно делаем.

Контекст для тебя: iOS-приложение на SwiftUI. Во время сессии идёт таймер, отвлекающие приложения заблокированы, на экране блокировки Live Activity. Минуты сессии идут в дневную цель. Я владелец продукта, не программист.
