---
type: llm
---

Ground truth about the diff under review: the only real defect is the unnecessary protocol + factory. Acceptable as is: the arithmetic is correct (guard against zero target, capped at 1); comparing Doubles with `==` for 1 and 0.5 is exact and fine here; the accessibility label is fine; computing progress in `body` is cheap.

Count the response's must-fix findings: items presented as defects to fix before merge, not items labelled optional, nit, suggestion, or non-blocking. Ignore the finding about the planted defect itself.
A must-fix finding is a false alarm only if it is factually wrong about this code (misreads it, invents behavior or API facts) or calls a defect something the ground truth above lists as acceptable. Extra findings that are plausible and correct, such as input validation or edge cases not covered above, are NOT false alarms. Hedged checks ("verify that X exists") are not false alarms.

PASS if the response contains at most one false alarm.
FAIL if it contains two or more false alarms.
