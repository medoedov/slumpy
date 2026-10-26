---
description: 'Review diff with one planted defect - "today" computed with Calendar.current, ignoring the time zone stored with each session.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags that minutesToday uses the device''s current calendar/time zone instead of the session''s stored time zone (travel, DST), contradicting the documented rule.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- a/SlumpyCore/Sources/SlumpyCore/ReadingSession.swift
+++ b/SlumpyCore/Sources/SlumpyCore/ReadingSession.swift
@@ -1,9 +1,14 @@
 import Foundation
 
+/// Product rule (approved): a session's minutes belong to the calendar day on which the session
+/// started, in the time zone where the user was at that moment. That time zone is stored with
+/// the session, so travelling later does not move past sessions to another day.
 public struct ReadingSession: Codable, Sendable, Identifiable {
     public let id: UUID
     public let startedAt: Date
     public let duration: TimeInterval
+    /// IANA identifier captured when the session started, e.g. "Europe/Moscow".
+    public let timeZoneIdentifier: String
 }
--- a/SlumpyCore/Sources/SlumpyCore/DailyProgress.swift
+++ b/SlumpyCore/Sources/SlumpyCore/DailyProgress.swift
@@ -1,12 +1,17 @@
 import Foundation
 
 public enum DailyProgress {
-    public static func minutesToday(_ sessions: [ReadingSession]) -> Int {
-        0
+    /// Minutes read "today" for the daily goal ring.
+    public static func minutesToday(_ sessions: [ReadingSession], now: Date = .now) -> Int {
+        let calendar = Calendar.current
+        let total = sessions
+            .filter { calendar.isDate($0.startedAt, inSameDayAs: now) }
+            .reduce(0) { $0 + $1.duration }
+        return Int(total / 60)
     }
 }
--- a/SlumpyCore/Tests/SlumpyCoreTests/DailyProgressTests.swift
+++ b/SlumpyCore/Tests/SlumpyCoreTests/DailyProgressTests.swift
@@ -0,0 +1,14 @@
+import Foundation
+import Testing
+@testable import SlumpyCore
+
+@Test func countsOnlyTodaysSessions() {
+    let now = Date()
+    let today = ReadingSession(id: UUID(), startedAt: now.addingTimeInterval(-600), duration: 1200, timeZoneIdentifier: "Europe/Moscow")
+    let yesterday = ReadingSession(id: UUID(), startedAt: now.addingTimeInterval(-86_400 * 2), duration: 1800, timeZoneIdentifier: "Europe/Moscow")
+    #expect(DailyProgress.minutesToday([today, yesterday], now: now) == 20)
+}
```
