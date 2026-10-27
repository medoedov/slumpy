---
description: 'Review diff with one planted defect - the old sorting function and enum lose their only call site but are left in place (dead code).'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer notices that LibraryViewModel.sortedBooks(by:) and LegacySortKey are no longer used after the change and asks to delete them.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Файлов проекта у тебя нет, только дифф ниже: в нём файлы целиком. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- a/Slumpy/Library/LibraryViewModel.swift
+++ b/Slumpy/Library/LibraryViewModel.swift
@@ -1,30 +1,33 @@
 import Foundation
 import Observation
 import SlumpyCore
 
 enum LegacySortKey {
     case title, author, recentlyAdded
 }
 
+enum LibrarySort: String, CaseIterable, Identifiable {
+    case title = "По названию"
+    case author = "По автору"
+    case recentlyRead = "Недавно читал"
+    var id: Self { self }
+}
+
 @MainActor
 @Observable
 final class LibraryViewModel {
     var books: [Book] = []
-    var sortKey: LegacySortKey = .title
+    var sort: LibrarySort = .title
 
-    var visibleBooks: [Book] { sortedBooks(by: sortKey) }
+    var visibleBooks: [Book] {
+        switch sort {
+        case .title: books.sorted { $0.title.localizedStandardCompare($1.title) == .orderedAscending }
+        case .author: books.sorted { $0.author.localizedStandardCompare($1.author) == .orderedAscending }
+        case .recentlyRead: books.sorted { ($0.lastReadAt ?? .distantPast) > ($1.lastReadAt ?? .distantPast) }
+        }
+    }
 
     func sortedBooks(by key: LegacySortKey) -> [Book] {
         switch key {
         case .title: books.sorted { $0.title < $1.title }
         case .author: books.sorted { $0.author < $1.author }
         case .recentlyAdded: books.sorted { $0.addedAt > $1.addedAt }
         }
     }
 }
--- a/Slumpy/Library/LibraryView.swift
+++ b/Slumpy/Library/LibraryView.swift
@@ -1,20 +1,20 @@
 import SwiftUI
 
 struct LibraryView: View {
     @State private var model = LibraryViewModel()
 
     var body: some View {
         List(model.visibleBooks) { book in
             BookRow(book: book)
         }
         .toolbar {
-            Picker("Сортировка", selection: $model.sortKey) {
-                Text("По названию").tag(LegacySortKey.title)
-                Text("По автору").tag(LegacySortKey.author)
-                Text("Недавно добавленные").tag(LegacySortKey.recentlyAdded)
+            Picker("Сортировка", selection: $model.sort) {
+                ForEach(LibrarySort.allCases) { sort in
+                    Text(sort.rawValue).tag(sort)
+                }
             }
         }
     }
 }
```
