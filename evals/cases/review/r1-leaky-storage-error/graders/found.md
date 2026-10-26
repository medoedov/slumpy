---
type: llm
weight: 2
---

Ground truth: the planted defect is a leaky abstraction. AddBookView imports GRDB and pattern-matches `DatabaseError` with `.SQLITE_CONSTRAINT_UNIQUE`, so the UI layer depends on the storage library and its SQLite error codes. The fix is for BookStore to translate storage errors into its own domain error (for example `BookStoreError.duplicateISBN`) so the view never sees GRDB types.

PASS if the response flags, as something to fix, that the view depends on GRDB / DatabaseError / SQLite constraint codes (storage details leaking into the UI) or explicitly recommends mapping the storage error to a domain error inside BookStore.
FAIL if the response does not raise this point, or mentions it only as an optional style nit while saying the change is fine to merge as is.
