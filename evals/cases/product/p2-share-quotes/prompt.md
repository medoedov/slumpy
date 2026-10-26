---
description: 'Ambiguous product request - sharing quotes with friends while friends do not exist yet.'
tags: [product]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Asks 1-5 product questions (no technical ones), each with a recommended option, in Russian; or resolves minor gaps as stated assumptions.'
---

Добавь возможность делиться цитатами с друзьями. Код пока не пиши, сначала договоримся, что именно делаем.

Контекст для тебя: iOS-приложение на SwiftUI. Цитаты пользователь сохраняет из книг, текст распознаётся с фото страницы. Друзей и аккаунтов в приложении пока нет, сервера тоже. Я владелец продукта, не программист.
