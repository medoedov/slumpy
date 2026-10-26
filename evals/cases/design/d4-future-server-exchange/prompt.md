---
description: 'Design scenario - preparing local data for a future server (friends, duels) without building it now.'
tags: [design]
runs: 2
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Does only cheap preparation now (client-generated IDs, absolute timestamps with time zone, change tracking), addresses idempotency/duplicates and conflicts for later, avoids building a sync layer or backend now.'
---

Сейчас Slumpy работает без аккаунта и без сервера. Позже, возможно, появятся друзья и дуэли: кто больше прочитал за неделю. Тогда сессии чтения придётся отправлять на сервер, причём телефон может быть офлайн, а одна и та же сессия может отправиться дважды. Сервер ещё не выбран.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Сессии чтения хранятся локально в SwiftData, сборка уже у тестировщиков.

Что из этого нужно учесть уже сейчас, а что отложить? Опиши решение и почему. Код пока не пиши. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
