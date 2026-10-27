---
type: llm
weight: 2
---

Trap: a "storage abstraction" that still leaks SwiftData: protocol methods taking or returning `@Model` classes (`Quote` model objects), `ModelContext`, `FetchDescriptor`/`#Predicate`, `PersistentIdentifier`, or rethrowing SwiftData errors. Such a protocol cannot be reimplemented on GRDB without changing the screens, and `@Model` objects are not Sendable across actors.

PASS if the boundary the screens use exposes only plain value types (for example a `struct QuoteRecord: Sendable`) and its own errors, with SwiftData types confined to the implementation; OR the response deliberately argues that no protocol is needed now and keeps SwiftData usage in one small type whose public API still uses plain values.
FAIL if the screens' API exposes `@Model` objects, ModelContext, FetchDescriptor/Predicate, PersistentIdentifier, or SwiftData error types.
