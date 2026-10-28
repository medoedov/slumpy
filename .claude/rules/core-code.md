---
paths:
  - "**/*.swift"
---

# Tests and fixes (core)

The rules below apply to any project; `paths` above lists this project's code files and is set per
project.

- A test calls the code the way its caller does and checks what the caller observes. Judge it by
  two imagined edits: break the behavior (a wrong value, an effect skipped or done twice) and the
  test must fail; restructure the internals with the same observable result and it must still
  pass. Every behavior a change adds needs such a test: deleting a line of new logic fails at least
  one test. A rule of the form "do not do X" needs a test input on which X gives a different answer.
  When no automated test can honestly observe the behavior (layout, system UI, an effect only a
  device shows), do not write one pinned to the implementation; the check goes to the screenshots
  or the device checklist (Project Knowledge, verification).
- Fix a crash or wrong state at its first cause. First decide whether the state is legitimate: the
  system may be in it (an independent fact another process recorded, arriving in any order; left by
  a crash or a killed process; a permission the user revoked). If it is, the code that broke on it
  is the cause, and handling it there is the fix. If it should never exist, fix the code that
  produced it; a guard, default value, early return, retry, or clamp where it surfaced hides the
  cause and is not the fix by itself. If an older version already stored it on devices, the
  reading code also handles it or a migration repairs it. Each part gets a test.
- If two fixes that rest on the same premise fail the same check, write the premise in one
  sentence and test it directly before a third fix.
- Traps you hit go to `docs/lessons.md` (format in that file).
