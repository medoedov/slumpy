---
type: llm
weight: 2
---

Ground truth: the planted defect is dead code. After the change, `sortedBooks(by:)` and `LegacySortKey` have no remaining callers (the only uses, `visibleBooks` and the picker tags, were replaced), so they should be deleted in the same change.

PASS if the response points out that `sortedBooks(by:)` and/or `LegacySortKey` are now unused (dead/leftover code) and should be removed, or explicitly asks to confirm and delete them.
FAIL if the response does not mention the leftover unused code.
