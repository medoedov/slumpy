---
description: 'Trap: failure of interaction between parts - ending a session while the app may be suspended or killed.'
tags: [traps]
runs: 2
max_turns: 15
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'End of session is driven by the system (DeviceActivity schedule end in the monitor extension and Live Activity staleDate/end), state is persisted in the App Group with one owner of each write, the app reconciles on launch/foreground, and handling is idempotent.'
---

Сделай завершение сессии чтения. Пользователь ставит сессию на 30 минут. Когда время вышло, нужно: снять блокировку приложений, завершить Live Activity, засчитать минуты в дневную цель, и чтобы Slumpy сказал «Сессия окончена» при следующем открытии приложения. Важно: к концу сессии приложение может быть в фоне или вообще выгружено системой.

Контекст: iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Блокировка сделана через FamilyControls/ManagedSettings, есть расширение DeviceActivityMonitor и виджет Live Activity, App Group настроен. Файлов проекта у тебя нет: приведи код целиком в ответе и коротко объясни ключевые решения. Я не программист, технические вопросы мне не задавай: решай сам и запиши допущения.
