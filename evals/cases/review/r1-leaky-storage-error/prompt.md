---
description: 'Review diff with one planted defect - storage (GRDB) error types leak into a SwiftUI view.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags that AddBookView depends on GRDB.DatabaseError / SQLite result codes and asks to map storage errors to a domain error inside BookStore.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6 со строгой проверкой многопоточности, хранение через GRDB. Файлов проекта у тебя нет, только дифф ниже. Место, где создаётся `AddBookView`, обновлено в этом же изменении и в дифф не попало. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- a/Slumpy/Library/BookStore.swift
+++ b/Slumpy/Library/BookStore.swift
@@ -1,20 +1,32 @@
 import Foundation
 import GRDB
 
 struct Book: Codable, FetchableRecord, PersistableRecord, Identifiable, Sendable {
     var id: UUID
     var title: String
     var author: String
     var isbn: String?
 }
 
 final class BookStore: Sendable {
     private let dbQueue: DatabaseQueue
 
     init(dbQueue: DatabaseQueue) {
         self.dbQueue = dbQueue
     }
 
     func allBooks() throws -> [Book] {
         try dbQueue.read { db in try Book.order(Column("title")).fetchAll(db) }
     }
+
+    /// Inserts a book. The `book` table has a UNIQUE index on `isbn`.
+    func add(_ book: Book) throws {
+        try dbQueue.write { db in try book.insert(db) }
+    }
 }
--- a/Slumpy/Library/AddBookView.swift
+++ b/Slumpy/Library/AddBookView.swift
@@ -1,25 +1,49 @@
 import SwiftUI
+import GRDB
 
 struct AddBookView: View {
     let store: BookStore
+    let onAdded: () -> Void
     @State private var title = ""
     @State private var author = ""
     @State private var isbn = ""
+    @State private var alertMessage: String?
 
     var body: some View {
         Form {
             TextField("Название", text: $title)
             TextField("Автор", text: $author)
             TextField("ISBN", text: $isbn)
-            Button("Добавить") {}
+            Button("Добавить", action: save)
+                .disabled(title.isEmpty)
         }
+        .alert(alertMessage ?? "", isPresented: Binding(
+            get: { alertMessage != nil },
+            set: { if !$0 { alertMessage = nil } }
+        )) {}
+    }
+
+    private func save() {
+        let book = Book(id: UUID(), title: title, author: author, isbn: isbn.isEmpty ? nil : isbn)
+        do {
+            try store.add(book)
+            onAdded()
+        } catch let error as DatabaseError where error.extendedResultCode == .SQLITE_CONSTRAINT_UNIQUE {
+            alertMessage = "Эта книга уже есть в библиотеке"
+        } catch {
+            alertMessage = "Не удалось сохранить книгу"
+        }
     }
 }
```
