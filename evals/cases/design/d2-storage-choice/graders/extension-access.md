---
type: llm
---

PASS if the response addresses how the Live Activity / app-blocking extensions access the current session: separate processes, a shared App Group container, and either limiting what extensions read (a small shared snapshot instead of the full database) or handling concurrent multi-process access to the store safely.
FAIL if extension access is not discussed, or the answer assumes extensions can share the app's in-memory state.
