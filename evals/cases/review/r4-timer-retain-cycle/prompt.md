---
description: 'Review diff with one planted defect - repeating Timer captures self strongly; invalidation lives in deinit, which never runs.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags the retain cycle (RunLoop -> Timer -> closure -> self) so deinit never runs and the timer keeps firing after the screen closes.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- /dev/null
+++ b/Slumpy/Session/SessionTimer.swift
@@ -0,0 +1,32 @@
+import Foundation
+import Observation
+
+/// Ticks once per second while the reading-session screen is open.
+/// Created by ReadingSessionView as @State and dropped when the screen closes.
+@MainActor
+@Observable
+final class SessionTimer {
+    private(set) var elapsed: TimeInterval = 0
+    private var timer: Timer?
+    private var startedAt: Date?
+
+    func start() {
+        startedAt = .now
+        timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
+            MainActor.assumeIsolated {
+                self.tick()
+            }
+        }
+    }
+
+    private func tick() {
+        guard let startedAt else { return }
+        elapsed = Date.now.timeIntervalSince(startedAt)
+    }
+
+    deinit {
+        timer?.invalidate()
+    }
+}
```
