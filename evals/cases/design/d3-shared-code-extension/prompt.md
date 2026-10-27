---
description: 'Design scenario - sharing session state between the app, a Live Activity widget extension and a DeviceActivityMonitor extension.'
tags: [design]
runs: 2
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Treats extensions as separate processes, keeps the monitor extension tiny (memory limit), defines a small explicit shared contract via the App Group, avoids over-modularization.'
---

Во время сессии чтения приложение блокирует отвлекающие приложения, а на экране блокировки идёт Live Activity с таймером. Когда время сессии вышло, блокировка должна сняться, даже если Slumpy закрыт. Нужно решить, как приложение, виджет Live Activity и расширение мониторинга активности (DeviceActivityMonitor) делят между собой код и данные о текущей сессии.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Есть цель приложения и локальный пакет SlumpyCore с логикой. Расширений пока нет.

Опиши, как ты это устроишь и почему. Код пока не пиши. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
