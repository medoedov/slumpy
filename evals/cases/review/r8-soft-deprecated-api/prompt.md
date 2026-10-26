---
description: 'Review diff with one planted defect class - soft-deprecated SwiftUI APIs the compiler does not warn about (NavigationView, foregroundColor) in new code for an iOS 18 minimum.'
tags: [review]
runs: 2
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'Reviewer flags NavigationView (use NavigationStack) and/or foregroundColor (use foregroundStyle) as deprecated APIs in new code.'
---

Сделай ревью этого изменения перед мержем. Контекст: Slumpy — iOS-приложение на SwiftUI, минимальная iOS 18, Swift 6. Сборка проходит без предупреждений. Файлов проекта у тебя нет, только дифф ниже. Перечисли то, что нужно исправить до мержа. Если всё в порядке, так и скажи.

```diff
--- /dev/null
+++ b/Slumpy/Quotes/QuotesScreen.swift
@@ -0,0 +1,36 @@
+import SwiftUI
+import SlumpyCore
+
+struct QuotesScreen: View {
+    let quotes: [Quote]
+
+    var body: some View {
+        NavigationView {
+            List(quotes) { quote in
+                NavigationLink {
+                    QuoteDetailView(quote: quote)
+                } label: {
+                    VStack(alignment: .leading, spacing: 4) {
+                        Text(quote.text)
+                            .lineLimit(3)
+                        Text(quote.bookTitle)
+                            .font(.footnote)
+                            .foregroundColor(.secondary)
+                    }
+                }
+            }
+            .navigationTitle("Цитаты")
+            .overlay {
+                if quotes.isEmpty {
+                    ContentUnavailableView("Пока нет цитат",
+                                           systemImage: "quote.opening",
+                                           description: Text("Сфотографируй страницу во время чтения"))
+                }
+            }
+        }
+    }
+}
```
