---
description: 'Review diff with one planted defect - a shipped SwiftData versioned schema is edited in place (new non-optional property) with no new schema version or migration stage.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags that SchemaV1 already shipped to testers, so the change needs SchemaV2 plus a migration stage (or at least a default/optional value), otherwise opening existing stores fails.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6, хранение в SwiftData. Сборка с этой схемой уже стоит у тестировщиков в TestFlight, и у них есть данные. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- a/Slumpy/Persistence/Schema.swift
+++ b/Slumpy/Persistence/Schema.swift
@@ -1,35 +1,37 @@
 import Foundation
 import SwiftData
 
 enum SchemaV1: VersionedSchema {
     static let versionIdentifier = Schema.Version(1, 0, 0)
     static var models: [any PersistentModel.Type] { [Book.self, ReadingSession.self] }
 
     @Model
     final class Book {
         @Attribute(.unique) var id: UUID
         var title: String
         var author: String
         var addedAt: Date
+        var pageCount: Int
 
-        init(id: UUID = UUID(), title: String, author: String, addedAt: Date = .now) {
+        init(id: UUID = UUID(), title: String, author: String, addedAt: Date = .now, pageCount: Int) {
             self.id = id
             self.title = title
             self.author = author
             self.addedAt = addedAt
+            self.pageCount = pageCount
         }
     }
 
     @Model
     final class ReadingSession {
         @Attribute(.unique) var id: UUID
         var startedAt: Date
         var duration: TimeInterval
         var book: Book?
 
         init(id: UUID = UUID(), startedAt: Date, duration: TimeInterval, book: Book?) {
             self.id = id; self.startedAt = startedAt; self.duration = duration; self.book = book
         }
     }
 }
 
 typealias Book = SchemaV1.Book
 typealias ReadingSession = SchemaV1.ReadingSession
 
 enum SlumpyMigrationPlan: SchemaMigrationPlan {
     static var schemas: [any VersionedSchema.Type] { [SchemaV1.self] }
     static var stages: [MigrationStage] { [] }
 }
--- a/Slumpy/Library/AddBookView.swift
+++ b/Slumpy/Library/AddBookView.swift
@@ -20,7 +20,8 @@ struct AddBookView: View {
     private func save() {
-        context.insert(Book(title: title, author: author))
+        context.insert(Book(title: title, author: author, pageCount: Int(pageCountText) ?? 0))
         dismiss()
     }
```
