---
type: llm
---

PASS if the response defines a small explicit contract for the shared session state: what fields are shared, who writes and who only reads, and how changes are noticed or reconciled (for example the app reconciling on launch/foreground, ActivityKit updates, or a version field). Ownership of writes must be stated.
FAIL if the shared data and its ownership (who writes, who reads) are left unspecified.
