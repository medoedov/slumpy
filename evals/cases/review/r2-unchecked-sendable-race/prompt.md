---
description: 'Review diff with one planted defect - mutable class marked @unchecked Sendable is mutated from concurrent tasks (data race).'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags the data race hidden by @unchecked Sendable and proposes an actor, MainActor isolation, or a lock (Mutex).'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6 со строгой проверкой многопоточности. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- /dev/null
+++ b/Slumpy/Stats/SessionStats.swift
@@ -0,0 +1,24 @@
+import Foundation
+
+/// Running totals shown on the stats screen and in the Live Activity.
+final class SessionStats: @unchecked Sendable {
+    static let shared = SessionStats()
+
+    private(set) var totalMinutes = 0
+    private(set) var finishedSessionIDs: [UUID] = []
+
+    func record(sessionID: UUID, minutes: Int) {
+        guard !finishedSessionIDs.contains(sessionID) else { return }
+        finishedSessionIDs.append(sessionID)
+        totalMinutes += minutes
+    }
+}
--- a/Slumpy/Session/SessionImporter.swift
+++ b/Slumpy/Session/SessionImporter.swift
@@ -10,12 +10,19 @@ struct SessionImporter {
     let store: SessionStore
 
     /// Imports sessions saved by the DeviceActivity extension while the app was closed.
     func importPending() async throws {
         let pending = try await store.pendingSessions()
-        for session in pending {
-            try await store.markImported(session.id)
+        try await withThrowingTaskGroup(of: Void.self) { group in
+            for session in pending {
+                group.addTask {
+                    try await store.markImported(session.id)
+                    SessionStats.shared.record(sessionID: session.id, minutes: session.minutes)
+                }
+            }
         }
     }
 }
--- a/Slumpy/Session/ReadingSessionModel.swift
+++ b/Slumpy/Session/ReadingSessionModel.swift
@@ -40,6 +40,7 @@ final class ReadingSessionModel {
     func finish() {
         timer.stop()
         let minutes = Int(timer.elapsed / 60)
+        SessionStats.shared.record(sessionID: currentSessionID, minutes: minutes)
         state = .finished(minutes: minutes)
     }
 }
```

`ReadingSessionModel` объявлен как `@MainActor @Observable`.
