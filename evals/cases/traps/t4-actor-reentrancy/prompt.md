---
description: 'Trap: language mechanics - shared cover image cache used by several screens concurrently.'
tags: [traps]
runs: 2
max_turns: 15
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Uses an actor (or a Mutex) without @unchecked Sendable and handles actor reentrancy: concurrent requests for the same key share one in-flight load (stored Task) instead of loading twice.'
---

Сделай кеш обложек: несколько экранов одновременно запрашивают обложку по id книги. Если обложки нет в памяти, она загружается с диска (это медленно, функция `loadCoverFromDisk(id:) async throws -> UIImage` уже есть). Одна и та же обложка не должна грузиться с диска дважды, даже если два экрана попросили её одновременно.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6 со строгой проверкой многопоточности. Файлов проекта у тебя нет: приведи код целиком в ответе и коротко объясни ключевые решения. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
