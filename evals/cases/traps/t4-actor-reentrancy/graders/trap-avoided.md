---
type: llm
weight: 2
---

Trap: an `actor` cache that checks the dictionary, then `await`s the disk load, then stores the result. Because actors are reentrant, two concurrent requests for the same id both miss and both load from disk. Another trap is a class with a dictionary marked `@unchecked Sendable` or guarded inconsistently.

PASS if concurrent requests for the same id share a single in-flight load (for example storing `Task<UIImage, Error>` in the dictionary before awaiting, and returning `await task.value`), with isolation via an actor or a Mutex/lock, and no `@unchecked Sendable` on unsynchronized mutable state.
FAIL if the same cover can still be loaded twice under concurrent requests, or thread safety relies on `@unchecked Sendable`/`nonisolated(unsafe)` over unsynchronized state.
