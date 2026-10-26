---
type: llm
---

PASS if the response handles duplicate and retried uploads: a stable client-generated identifier per session (or idempotency key) so the server can de-duplicate, and mentions retries/offline queueing or ordering/conflict concerns (for example a session edited after sending).
FAIL if duplicates/retries are not addressed or the plan relies on server-generated IDs only.
