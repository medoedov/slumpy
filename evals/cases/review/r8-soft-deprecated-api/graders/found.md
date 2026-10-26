---
type: llm
weight: 2
---

Ground truth: the planted defect is use of soft-deprecated SwiftUI APIs that compile without warnings: `NavigationView` (deprecated in favour of `NavigationStack` / `NavigationSplitView` since iOS 16) and `foregroundColor(_:)` (deprecated in favour of `foregroundStyle(_:)` since iOS 17). With an iOS 18 minimum, new code should use the replacements.

PASS if the response flags `NavigationView` as deprecated/outdated and recommends `NavigationStack` (or NavigationSplitView), OR flags `foregroundColor` as deprecated and recommends `foregroundStyle`, presenting it as something to change.
FAIL if neither deprecated API is identified.
