---
description: 'Design scenario - choosing local storage for library and sessions with an extension and a possible future server.'
tags: [design]
runs: 2
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Compares at least two real options with migration and reversibility, covers extension access through the App Group, prepares for sync without building it, gives a recommendation with a revisit condition.'
---

Нам нужно выбрать, где на телефоне хранить данные Slumpy: библиотеку книг, сессии чтения, цитаты. Потом, возможно, появятся друзья и дуэли с сервером, но когда и будут ли, неизвестно. Live Activity и расширение блокировки приложений должны видеть текущую сессию.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Кода хранения ещё нет. Данных у пользователей пока нет.

Выбери вариант и объясни выбор так, чтобы через год было понятно, почему решили именно так. Код пока не пиши. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
