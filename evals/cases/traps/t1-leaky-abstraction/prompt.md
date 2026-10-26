---
description: 'Trap: leaky abstraction - a storage protocol meant to allow swapping SwiftData for GRDB.'
tags: [traps]
runs: 2
max_turns: 15
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'The boundary exposes only plain Sendable domain values and domain errors (no @Model classes, ModelContext, FetchDescriptor, PersistentIdentifier or SwiftData errors), or argues convincingly that no protocol is needed yet.'
---

Нужен слой хранения цитат, чтобы экраны работали с ним, а не напрямую с SwiftData: через полгода мы, возможно, перейдём на GRDB и не хотим переписывать экраны. Экранам нужно: список цитат книги (новые сверху), добавить цитату, удалить цитату.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6 со строгой проверкой многопоточности. Сейчас цитата — это SwiftData-модель `Quote` (id, text, bookID, createdAt). Файлов проекта у тебя нет: приведи код целиком в ответе и коротко объясни ключевые решения. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
