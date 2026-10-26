---
type: llm
weight: 2
---

Trap: driving the end of the session from the app process (a Timer, Task.sleep, or a local notification handler in the app) and keeping state in memory, so nothing happens if the app is suspended or killed; or both the app and the extension writing the same state without a clear owner, causing double-counted minutes.

PASS if (1) unblocking at the end is driven by the system: a DeviceActivity schedule whose `intervalDidEnd` in the monitor extension clears the ManagedSettings shields; AND (2) the session end is persisted in the App Group so the app can reconcile on next launch/foreground (credit minutes, show "Сессия окончена") without assuming it was running; AND (3) crediting minutes is protected against double counting (idempotent by session id / a "credited" flag, single owner of the write).
FAIL if any of the three is missing.
