# Project state

Reconciled: 2026-11-03. Finalization starts at `d68d2f0` on `dev`; verification belongs to the
linked plan and its state manifest, not this date. Windows preparation; Mac is not configured.

## Now

| ID | State | Plan | Owner / scope | Current step / next check |
|---|---|---|---|---|
| SYS-001 | blocked | [Engineering system](engineering-system-modernization/plan.md) | Astra; agent instructions, checks, task state | Windows fixes and separately approved staged-scope review complete; RT-01/02 and Mac acceptance pending |

## Blocked / waiting for Mac

All pending runtime and Mac evidence has one owner list:
[deferred acceptance](engineering-system-modernization/deferred.md). A document-check pass is
not iOS acceptance. No app skeleton exists.

## Next

1. Finish available SYS-001 checks, then execute its deferred acceptance when prerequisites exist.
2. The next product step is to agree the first vertical slice through product-spec, then the
   skeleton decision under [ADR-0001](../docs/decisions/0001-stack-and-project-structure.md).
   No feature task is approved by this pointer.
3. [Future product proposals](../backlog.md) remain proposed, not implementation commitments.

## Recently completed

- [Unified instructions](completed/agent-system-unified/plan.md), committed in `d4d87c3`.
  Earlier audit/layer/gate/self-review folders are historical evidence, not active task queues.

## State convention

New work has one stable ID. `proposed` and `ready` live in backlog; `in-progress`, `blocked` and
`verified` live in a plan; `done` lives in completed. `verified` names its evidence scope in the
plan and is not a synonym for done. Before creating a task, match ID and meaning against this
index, backlog, relevant active/completed plans, debt and related remote issues when available.
At a state change, update plan, index and affected canonical facts together. Keep one writer per
area. Read this index and the relevant plan at start/resume; history loads only for a named gap.
Exact record format and validation: [task-state contract](../docs/agent-system.md#task-state).
