---
description: 'Review diff with one planted defect - protocol with a single implementation plus a factory around pure arithmetic (needless abstraction).'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags the protocol + Default implementation + factory as unnecessary indirection for a pure function and proposes a plain function or struct.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- /dev/null
+++ b/SlumpyCore/Sources/SlumpyCore/Goals/GoalProgressCalculating.swift
@@ -0,0 +1,38 @@
+import Foundation
+
+public protocol GoalProgressCalculating: Sendable {
+    func progress(minutesRead: Int, dailyTargetMinutes: Int) -> Double
+}
+
+public struct DefaultGoalProgressCalculator: GoalProgressCalculating {
+    public init() {}
+
+    public func progress(minutesRead: Int, dailyTargetMinutes: Int) -> Double {
+        guard dailyTargetMinutes > 0 else { return 0 }
+        return min(Double(minutesRead) / Double(dailyTargetMinutes), 1)
+    }
+}
+
+public enum GoalProgressCalculatorFactory {
+    public static func make() -> any GoalProgressCalculating {
+        DefaultGoalProgressCalculator()
+    }
+}
--- a/Slumpy/Home/DailyRingView.swift
+++ b/Slumpy/Home/DailyRingView.swift
@@ -3,12 +3,15 @@ import SlumpyCore
 
 struct DailyRingView: View {
     let minutesRead: Int
     let dailyTargetMinutes: Int
+    private let calculator = GoalProgressCalculatorFactory.make()
 
     var body: some View {
-        ProgressRing(value: 0)
+        ProgressRing(value: calculator.progress(minutesRead: minutesRead,
+                                                dailyTargetMinutes: dailyTargetMinutes))
             .accessibilityLabel("Цель на сегодня")
     }
 }
--- /dev/null
+++ b/SlumpyCore/Tests/SlumpyCoreTests/GoalProgressTests.swift
@@ -0,0 +1,12 @@
+import Testing
+@testable import SlumpyCore
+
+@Test func progressIsCappedAtOne() {
+    let calculator = DefaultGoalProgressCalculator()
+    #expect(calculator.progress(minutesRead: 50, dailyTargetMinutes: 30) == 1)
+    #expect(calculator.progress(minutesRead: 15, dailyTargetMinutes: 30) == 0.5)
+    #expect(calculator.progress(minutesRead: 10, dailyTargetMinutes: 0) == 0)
+}
```

Других реализаций `GoalProgressCalculating` в проекте нет и не планируется.
