Result dirs: results/baseline/20261026T173047Z, results/baseline/20261026T173802Z, results/baseline/20261026T174258Z, results/baseline/20261026T180246Z

Total estimated cost (agent runs + judge): $27.73; wall time 41 min

## Cost and effort per arm

| Group | Arm | Runs | Cost, $ | Mean $/run | Mean turns | Runs with errors |
|---|---|---|---|---|---|---|
| design | with | 4 | 1.33 | 0.332 | 2.0 | 0 |
| design | without | 4 | 1.54 | 0.385 | 3.0 | 0 |
| product | with | 6 | 3.11 | 0.519 | 5.8 | 0 |
| product | without | 6 | 2.37 | 0.396 | 2.0 | 0 |
| review | with | 18 | 5.49 | 0.305 | 3.0 | 0 |
| review | without | 18 | 4.59 | 0.255 | 1.0 | 0 |
| traps | with | 10 | 7.04 | 0.704 | 1.9 | 0 |
| traps | without | 10 | 5.98 | 0.598 | 1.0 | 0 |
| triggers | with | 10 | 1.39 | 0.139 | 3.3 | 0 |
| triggers | without | 10 | 0.94 | 0.094 | 1.7 | 0 |

## Grader pass counts per case (passed/runs)

| Group | Case | Grader | With system | Without system |
|---|---|---|---|---|
| design | d1-reading-goals | boundaries | 1/1 | 1/1 |
| design | d1-reading-goals | data-model-first | 1/1 | 1/1 |
| design | d1-reading-goals | ind-design-skill | 0/1 | — |
| design | d1-reading-goals | migration | 1/1 | 1/1 |
| design | d1-reading-goals | no-tech-questions | 1/1 | 1/1 |
| design | d1-reading-goals | proportionate | 1/1 | 1/1 |
| design | d2-storage-choice | alternatives | 0/1 | 1/1 |
| design | d2-storage-choice | extension-access | 1/1 | 1/1 |
| design | d2-storage-choice | future-sync | 1/1 | 1/1 |
| design | d2-storage-choice | ind-design-skill | 0/1 | — |
| design | d2-storage-choice | no-tech-questions | 1/1 | 1/1 |
| design | d2-storage-choice | proportionate | 1/1 | 1/1 |
| design | d3-shared-code-extension | ind-design-skill | 0/1 | — |
| design | d3-shared-code-extension | monitor-footprint | 1/1 | 1/1 |
| design | d3-shared-code-extension | no-tech-questions | 1/1 | 1/1 |
| design | d3-shared-code-extension | proportionate | 1/1 | 1/1 |
| design | d3-shared-code-extension | separate-processes | 1/1 | 1/1 |
| design | d3-shared-code-extension | shared-contract | 1/1 | 1/1 |
| design | d4-future-server-exchange | defer-server | 1/1 | 1/1 |
| design | d4-future-server-exchange | idempotency | 1/1 | 1/1 |
| design | d4-future-server-exchange | ind-design-skill | 0/1 | — |
| design | d4-future-server-exchange | no-tech-questions | 1/1 | 1/1 |
| design | d4-future-server-exchange | proportionate | 1/1 | 1/1 |
| design | d4-future-server-exchange | time-standard | 1/1 | 0/1 |
| product | p1-streak | ind-spec-skill | 2/2 | — |
| product | p1-streak | key-ambiguity | 1/2 | 2/2 |
| product | p1-streak | product-only | 1/2 | 2/2 |
| product | p1-streak | question-count | 1/2 | 0/2 |
| product | p1-streak | recommendations | 0/2 | 0/2 |
| product | p1-streak | russian | 2/2 | 2/2 |
| product | p2-share-quotes | ind-spec-skill | 2/2 | — |
| product | p2-share-quotes | key-ambiguity | 2/2 | 2/2 |
| product | p2-share-quotes | product-only | 1/2 | 2/2 |
| product | p2-share-quotes | question-count | 1/2 | 0/2 |
| product | p2-share-quotes | recommendations | 0/2 | 0/2 |
| product | p2-share-quotes | russian | 2/2 | 2/2 |
| product | p3-pause-session | ind-spec-skill | 2/2 | — |
| product | p3-pause-session | key-ambiguity | 2/2 | 2/2 |
| product | p3-pause-session | product-only | 1/2 | 1/2 |
| product | p3-pause-session | question-count | 0/2 | 1/2 |
| product | p3-pause-session | recommendations | 0/2 | 0/2 |
| product | p3-pause-session | russian | 2/2 | 2/2 |
| review | r1-leaky-storage-error | found | 2/2 | 0/2 |
| review | r1-leaky-storage-error | ind-review-skill | 2/2 | — |
| review | r1-leaky-storage-error | no-false-alarms | 2/2 | 2/2 |
| review | r2-unchecked-sendable-race | found | 2/2 | 2/2 |
| review | r2-unchecked-sendable-race | ind-review-skill | 2/2 | — |
| review | r2-unchecked-sendable-race | no-false-alarms | 2/2 | 2/2 |
| review | r3-today-calendar-current | found | 2/2 | 2/2 |
| review | r3-today-calendar-current | ind-review-skill | 2/2 | — |
| review | r3-today-calendar-current | no-false-alarms | 1/2 | 2/2 |
| review | r4-timer-retain-cycle | found | 2/2 | 2/2 |
| review | r4-timer-retain-cycle | ind-review-skill | 2/2 | — |
| review | r4-timer-retain-cycle | no-false-alarms | 2/2 | 2/2 |
| review | r5-single-impl-protocol-factory | found | 2/2 | 2/2 |
| review | r5-single-impl-protocol-factory | ind-review-skill | 2/2 | — |
| review | r5-single-impl-protocol-factory | no-false-alarms | 2/2 | 2/2 |
| review | r6-dead-code-after-change | found | 2/2 | 2/2 |
| review | r6-dead-code-after-change | ind-review-skill | 2/2 | — |
| review | r6-dead-code-after-change | no-false-alarms | 2/2 | 2/2 |
| review | r7-missing-migration | found | 2/2 | 2/2 |
| review | r7-missing-migration | ind-review-skill | 2/2 | — |
| review | r7-missing-migration | no-false-alarms | 2/2 | 2/2 |
| review | r8-soft-deprecated-api | found | 2/2 | 2/2 |
| review | r8-soft-deprecated-api | ind-review-skill | 2/2 | — |
| review | r8-soft-deprecated-api | no-false-alarms | 2/2 | 2/2 |
| review | r9-weakened-test | found | 2/2 | 2/2 |
| review | r9-weakened-test | ind-review-skill | 2/2 | — |
| review | r9-weakened-test | no-false-alarms | 2/2 | 2/2 |
| traps | t1-leaky-abstraction | ind-skill | 2/2 | — |
| traps | t1-leaky-abstraction | proportionate | 2/2 | 1/2 |
| traps | t1-leaky-abstraction | trap-avoided | 2/2 | 0/2 |
| traps | t2-unscalable-covers | ind-skill | 1/2 | — |
| traps | t2-unscalable-covers | proportionate | 2/2 | 0/2 |
| traps | t2-unscalable-covers | trap-avoided | 2/2 | 2/2 |
| traps | t3-standard-csv | ind-skill | 1/2 | — |
| traps | t3-standard-csv | proportionate | 2/2 | 2/2 |
| traps | t3-standard-csv | trap-avoided | 0/2 | 0/2 |
| traps | t4-actor-reentrancy | ind-skill | 1/2 | — |
| traps | t4-actor-reentrancy | proportionate | 2/2 | 2/2 |
| traps | t4-actor-reentrancy | trap-avoided | 2/2 | 2/2 |
| traps | t5-interaction-failure | ind-skill | 2/2 | — |
| traps | t5-interaction-failure | proportionate | not graded | not graded |
| traps | t5-interaction-failure | trap-avoided | not graded | not graded |
| triggers | s1-review-casual | fired | 2/2 | 0/2 |
| triggers | s2-feature-thinking | fired | 2/2 | 0/2 |
| triggers | s3-risky-model-change | fired | 0/2 | 0/2 |
| triggers | s4-tests-request | fired | 2/2 | 0/2 |
| triggers | s5-trivial-no-ceremony | answered | 2/2 | 2/2 |
| triggers | s5-trivial-no-ceremony | no-ceremony | 2/2 | 2/2 |

## Case scores (mean over runs; indicator graders excluded by the tool)

| Case | With | Without | Δ |
|---|---|---|---|
| d1-reading-goals | 1.00 | 1.00 | +0.00 |
| d2-storage-choice | 0.80 | 1.00 | -0.20 |
| d3-shared-code-extension | 1.00 | 1.00 | +0.00 |
| d4-future-server-exchange | 1.00 | 0.80 | +0.20 |
| p1-streak | 0.50 | 0.60 | -0.10 |
| p2-share-quotes | 0.60 | 0.60 | +0.00 |
| p3-pause-session | 0.50 | 0.60 | -0.10 |
| r1-leaky-storage-error | 1.00 | 0.33 | +0.67 |
| r2-unchecked-sendable-race | 1.00 | 1.00 | +0.00 |
| r3-today-calendar-current | 0.83 | 1.00 | -0.17 |
| r4-timer-retain-cycle | 1.00 | 1.00 | +0.00 |
| r5-single-impl-protocol-factory | 1.00 | 1.00 | +0.00 |
| r6-dead-code-after-change | 1.00 | 1.00 | +0.00 |
| r7-missing-migration | 1.00 | 1.00 | +0.00 |
| r8-soft-deprecated-api | 1.00 | 1.00 | +0.00 |
| r9-weakened-test | 1.00 | 1.00 | +0.00 |
| t1-leaky-abstraction | 1.00 | 0.17 | +0.83 |
| t2-unscalable-covers | 1.00 | 0.67 | +0.33 |
| t3-standard-csv | 0.33 | 0.33 | +0.00 |
| t4-actor-reentrancy | 1.00 | 1.00 | +0.00 |
| t5-interaction-failure | not graded | not graded | — |
| s1-review-casual | 1.00 | 0.00 | +1.00 |
| s2-feature-thinking | 1.00 | 0.00 | +1.00 |
| s3-risky-model-change | 0.00 | 0.00 | +0.00 |
| s4-tests-request | 1.00 | 0.00 | +1.00 |
| s5-trivial-no-ceremony | 1.00 | 1.00 | +0.00 |

## Review: planted defects found and false alarms per repetition

| Arm | Repetition | Defects found (of 9) | Cases with ≥2 false alarms |
|---|---|---|---|
| with | 1 | 9/9 | 0 |
| with | 2 | 9/9 | 1 |
| without | 1 | 8/9 | 0 |
| without | 2 | 8/9 | 0 |

## Skills and subagents used

| Case | Skills invoked (all runs) | Subagents spawned (all runs) |
|---|---|---|
| d2-storage-choice (without) | — | general-purpose×1 |
| p1-streak | sys:user-spec-planning×2 | general-purpose×1 |
| p2-share-quotes | sys:user-spec-planning×2 | — |
| p3-pause-session | sys:user-spec-planning×2 | — |
| r1-leaky-storage-error | sys:code-reviewing×2 | — |
| r2-unchecked-sendable-race | sys:code-reviewing×2 | — |
| r3-today-calendar-current | sys:code-reviewing×2 | — |
| r4-timer-retain-cycle | sys:code-reviewing×2 | — |
| r5-single-impl-protocol-factory | sys:code-reviewing×2 | — |
| r6-dead-code-after-change | sys:code-reviewing×2 | — |
| r7-missing-migration | sys:code-reviewing×2 | — |
| r8-soft-deprecated-api | sys:code-reviewing×2 | — |
| r9-weakened-test | sys:code-reviewing×2 | — |
| t1-leaky-abstraction | sys:code-writing×2 | — |
| t2-unscalable-covers | sys:code-writing×1 | — |
| t3-standard-csv | sys:code-writing×1 | sys:code-reviewer×1 |
| t4-actor-reentrancy | sys:code-writing×1 | sys:code-reviewer×1 |
| t5-interaction-failure | sys:code-writing×2 | sys:code-reviewer×2 |
| s1-review-casual | sys:code-reviewing×2 | — |
| s2-feature-thinking | sys:user-spec-planning×2 | — |
| s4-tests-request | sys:test-master×2 | — |
