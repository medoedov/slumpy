---
type: llm
---

Count the distinct questions the response asks the user (numbered items or sentences that require the user's answer; a question with several options counts once).

PASS if the response asks between 1 and 5 questions, or asks none but states explicit assumptions for the open points and proposes a concrete scope for the user to confirm.
FAIL if it asks more than 5 questions, or neither asks questions nor states assumptions (for example it silently specifies everything as decided).
