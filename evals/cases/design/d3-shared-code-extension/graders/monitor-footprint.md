---
type: llm
---

PASS if the response accounts for the tight memory/footprint limits of the DeviceActivityMonitor extension (roughly a few MB) by keeping its dependencies minimal, for example not linking the full persistence stack or UI frameworks into it and reading only a small shared value.
FAIL if memory/footprint limits of the monitor extension are not considered, or it proposes loading the full database stack inside the monitor.
