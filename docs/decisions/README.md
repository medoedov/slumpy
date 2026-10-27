# Architecture Decision Records

One file per T2 decision: `NNNN-short-title.md`, numbered in order. A superseded ADR stays in
place with its status changed and a link to the one that replaces it.

## Index

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-stack-and-project-structure.md) | SwiftUI, iOS 18, Swift 6 strict; one app target, extension targets, one local package; data rules | Accepted; "today" rule decided by the owner 2026-10-27 |

## Format

```markdown
# ADR-NNNN: <decision>

- **Status:** Proposed | Accepted | Superseded by ADR-MMMM
- **Date:** YYYY-MM-DD
- **Tier:** T2

## Context
What forces the decision now; constraints; what is known and unknown.

## Decision
What we do, specific enough to check in code.

## Rejected alternatives
At least two, each with why it lost.

## Consequences
What gets easier, what gets harder, what the user notices (product consequences go to the owner).

## Reversibility and cost of change in a year
How hard it is to undo, and what would have to change.

## Revisit when
The concrete trigger that makes this decision stale.
```
