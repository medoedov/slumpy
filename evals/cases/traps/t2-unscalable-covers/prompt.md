---
description: 'Trap: unscalable solution - book cover photos stored and loaded naively.'
tags: [traps]
runs: 2
max_turns: 15
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Stores downscaled covers outside the main row (external storage or files with a path), shows thumbnails decoded off the main thread, so a 500-book library does not load hundreds of MB.'
---

Добавь обложки книг: пользователь фотографирует обложку камерой, и она показывается в списке библиотеки и на экране книги. У активных читателей в библиотеке бывает 500 книг и больше.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Книга — SwiftData-модель `Book` (id, title, author, addedAt). Фото приходит как `UIImage` с камеры (12 Мп). Файлов проекта у тебя нет: приведи код целиком в ответе и коротко объясни ключевые решения. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
