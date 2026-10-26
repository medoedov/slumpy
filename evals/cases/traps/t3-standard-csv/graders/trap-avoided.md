---
type: llm
weight: 2
---

Trap: joining fields with commas without escaping. Per RFC 4180 a field containing a comma, double quote or line break must be enclosed in double quotes, and embedded double quotes doubled. Titles like «Тихий Дон, том 1» or with quotes break naive CSV.

PASS if the code quotes fields that need it (or all fields) AND doubles embedded double quotes, AND writes the start time unambiguously (ISO 8601 with offset, or local time plus an explicit time zone column/offset based on the session's timeZoneIdentifier).
FAIL if escaping is missing or incomplete (for example quotes not doubled), or timestamps are written in an ambiguous locale format without offset/time zone.
