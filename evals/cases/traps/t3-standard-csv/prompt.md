---
description: 'Trap: standard violation - CSV export of reading history.'
tags: [traps]
runs: 2
max_turns: 15
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Escapes fields per RFC 4180 (quotes, commas, newlines in titles/quotes), writes unambiguous timestamps (ISO 8601 with offset) and handles encoding for Excel (UTF-8, optionally BOM).'
---

Сделай экспорт истории чтения в CSV, чтобы пользователь мог открыть его в Excel или Numbers. Колонки: дата и время начала, длительность в минутах, название книги, автор. Названия бывают любые, например «Тихий Дон, том 1» или книги с кавычками в названии.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Есть массив `[ReadingSession]`: startedAt: Date, duration: TimeInterval, timeZoneIdentifier: String, bookTitle: String, bookAuthor: String. Отдать файл можно через ShareLink. Файлов проекта у тебя нет: приведи код целиком в ответе и коротко объясни ключевые решения. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
