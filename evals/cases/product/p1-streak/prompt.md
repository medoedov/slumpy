---
description: 'Ambiguous product request - praise for a reading streak.'
tags: [product]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Asks 1-5 product questions (no technical ones), each with a recommended option, in Russian; or resolves minor gaps as stated assumptions.'
---

Хочу, чтобы Slumpy хвалил меня за серию дней чтения подряд. Код пока не пиши, сначала договоримся, что именно делаем.

Контекст для тебя: iOS-приложение на SwiftUI. Есть сессии чтения с датой, длительностью и часовым поясом, есть персонаж Slumpy с невозмутимыми репликами. Я владелец продукта, не программист.
