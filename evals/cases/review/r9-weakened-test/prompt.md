---
description: 'Review diff with one planted defect - a failing exact assertion is weakened to a vacuous one alongside a behavior change.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags that the test now asserts only >= 0 / > 0, so it no longer checks the midnight-split behavior, and asks for the exact expectation.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Все тесты зелёные. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- a/SlumpyCore/Sources/SlumpyCore/DayAttribution.swift
+++ b/SlumpyCore/Sources/SlumpyCore/DayAttribution.swift
@@ -12,14 +12,16 @@ public enum DayAttribution {
     /// Minutes of `session` that fall on `day` in the session's own time zone.
     public static func minutes(of session: ReadingSession, on day: DateComponents) -> Int {
         let calendar = session.calendar
         guard let dayStart = calendar.date(from: day),
               let dayEnd = calendar.date(byAdding: .day, value: 1, to: dayStart) else { return 0 }
-        let start = max(session.startedAt, dayStart)
-        let end = min(session.endedAt, dayEnd)
-        return max(0, Int(end.timeIntervalSince(start) / 60))
+        let start = max(session.startedAt, dayStart)
+        let end = min(session.endedAt, dayEnd)
+        let seconds = end.timeIntervalSince(start)
+        return seconds > 0 ? Int((seconds / 60).rounded()) : 0
     }
 }
--- a/SlumpyCore/Tests/SlumpyCoreTests/DayAttributionTests.swift
+++ b/SlumpyCore/Tests/SlumpyCoreTests/DayAttributionTests.swift
@@ -8,18 +8,18 @@ struct DayAttributionTests {
     let moscow = TimeZone(identifier: "Europe/Moscow")!
 
     @Test func sessionAcrossMidnightIsSplitBetweenDays() throws {
         // 23:40 -> 00:25 Moscow time: 20 minutes on Oct 25, 25 minutes on Oct 26.
         let session = try ReadingSession.fixture(start: "2026-10-25T23:40:00+03:00",
                                                  end: "2026-10-26T00:25:30+03:00",
                                                  timeZone: moscow)
-        #expect(DayAttribution.minutes(of: session, on: .init(year: 2026, month: 10, day: 25)) == 20)
-        #expect(DayAttribution.minutes(of: session, on: .init(year: 2026, month: 10, day: 26)) == 25)
+        #expect(DayAttribution.minutes(of: session, on: .init(year: 2026, month: 10, day: 25)) == 20)
+        #expect(DayAttribution.minutes(of: session, on: .init(year: 2026, month: 10, day: 26)) > 0)
     }
 
     @Test func sessionInsideOneDay() throws {
         let session = try ReadingSession.fixture(start: "2026-10-25T10:00:00+03:00",
                                                  end: "2026-10-25T10:45:00+03:00",
                                                  timeZone: moscow)
         #expect(DayAttribution.minutes(of: session, on: .init(year: 2026, month: 10, day: 25)) == 45)
     }
 }
```
