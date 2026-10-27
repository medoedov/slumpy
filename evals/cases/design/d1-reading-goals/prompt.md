---
description: 'Design scenario - reading goals (book by a date, N books per season) before any code.'
tags: [design]
runs: 2
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'A brief that starts from the data model, derives progress from existing data, handles period/day boundaries, stays simple, and asks the owner no technical questions.'
---

Хочу добавить в Slumpy цели чтения. Два вида: «дочитать конкретную книгу к дате» и «прочитать N книг за сезон» (например, за осень). На главном экране видно, успеваю ли я. Продуктово это согласовано, подробности на твоё усмотрение.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Уже есть книги в библиотеке (у книги есть статус «читаю / прочитана» и дата, когда отмечена прочитанной) и сессии чтения (начало, длительность, часовой пояс, книга). Хранение в SwiftData, сборка уже у тестировщиков. Кода у тебя сейчас нет.

Прежде чем писать код, опиши, как ты это сделаешь: ключевые технические решения и почему. Код пока не пиши. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
