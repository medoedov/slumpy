---
type: llm
---

The user is a non-programmer product owner who said technical decisions are the assistant's job.

PASS if the response asks the user no technical questions (storage engine, frameworks, architecture, data formats, concurrency, libraries) and instead decides them or records them as assumptions. Product questions (what the user sees, scope, rules of the feature) are allowed. Making a decision and stating assumptions without any question also passes.
FAIL if the response asks the user at least one technical question, or stops and waits for the user to make a technical choice.
