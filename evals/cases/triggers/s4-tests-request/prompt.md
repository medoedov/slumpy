---
description: 'Skill trigger - request to cover logic with tests.'
tags: [triggers]
runs: 2
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'A testing-role skill fires.'
---

Покрой тестами вот эту функцию. Тесты на Swift Testing, файлов у тебя нет, просто покажи код тестов.

```swift
public enum DailyProgress {
    public static func minutesToday(_ sessions: [ReadingSession], now: Date, calendar: Calendar) -> Int {
        let total = sessions
            .filter { calendar.isDate($0.startedAt, inSameDayAs: now) }
            .reduce(0) { $0 + $1.duration }
        return Int(total / 60)
    }
}
```
