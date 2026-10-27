---
description: 'Skill trigger - casual request to look over a change.'
tags: [triggers]
runs: 2
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'A review-role skill fires.'
---

Глянь, пожалуйста, нормально ли я тут поменял? Это iOS-приложение на SwiftUI.

```diff
--- a/Slumpy/Home/GreetingView.swift
+++ b/Slumpy/Home/GreetingView.swift
@@ -4,7 +4,9 @@ struct GreetingView: View {
     let name: String
 
     var body: some View {
-        Text("Привет, \(name)")
+        Text("Привет, \(name)")
+            .font(.title2)
+            .accessibilityAddTraits(.isHeader)
     }
 }
```
