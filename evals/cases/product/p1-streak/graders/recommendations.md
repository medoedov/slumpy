---
type: llm
---

PASS if each question asked to the user comes with a recommended answer or a default the assistant proposes (for example "Рекомендую: ..." or "Предлагаю ..."), so the user can simply agree. If the response asks no questions, PASS if it proposes a concrete default for each open point.
FAIL if at least one question is asked without any recommendation or proposed default.
