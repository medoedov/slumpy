---
type: llm
---

PASS if the response compares at least two real storage options (for example SwiftData, Core Data, SQLite via GRDB) on concrete criteria that matter here, including schema migrations and the cost of switching later (reversibility), and states which risks each carries.
FAIL if it picks one option without a real comparison, or the comparison omits both migrations and reversibility.
