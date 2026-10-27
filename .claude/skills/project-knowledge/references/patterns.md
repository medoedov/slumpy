# Patterns & Conventions

- [Code Patterns](#code-patterns)
- [Git Workflow](#git-workflow)
- [Verification](#verification)
- [Business Invariants](#business-invariants)
- [Product Rules (hypotheses)](#product-rules-hypotheses)

---

## Code Patterns

No app code yet. The first vertical slice becomes the reference implementation for later
features only after a review audit; until then there is no house pattern to copy.

---

## Git Workflow

- **`dev`** - default branch, active development.
- **`main`** - release-ready code. Pushing or merging to `main` is an owner decision. GitHub has
  no branch protection; `.claude/settings.json` denies agent pushes to `main`.
- `AGENTS.md`, `.codex/`, and `.githooks/` are frozen (Codex option A): not edited, not
  regenerated, hooks not enabled. The hooks call scripts outside the repository and would fail.

---

## Verification

- Building and testing happen only on a Mac with Xcode. Cloud sessions can review text, specs,
  and diffs but cannot build or run code.
- Planned (Mac setup): `scripts/check` as the single entry point - build, package and app tests,
  lint, format, gate-bypass scan, minimum risk tier from changed paths. Not created yet.
- Package logic is tested with Swift Testing on the smallest reliable boundary.
- Device-only checks (Family Controls blocking, motion sensors, Live Activity on the lock screen
  over time) go to the owner as a ready checklist.

---

## Business Invariants

Rules the code must keep regardless of feature:

- **"Today".** A reading day runs from 04:00 to 04:00 local time; a whole session counts to the
  reading day in which it started, computed in the time zone stored with the session and never
  recomputed after a trip. One implementation in the logic package, covered by tests; details in
  [ADR-0001](../../../../docs/decisions/0001-stack-and-project-structure.md#owner-decision-attributing-minutes-to-a-day).
- **Session time** is stored with its time zone.

---

## Product Rules (hypotheses)

From the draft `mvp.md`, not approved. Use them as context; confirm through `product-spec` before
building a feature on them.

- **Session modes:** "book in hands" (phone face down, timer runs; a ritual, not a detector) and
  "reading on the phone" (selected apps blocked, reader app open, timer in a Live Activity).
- **Blocking** is part of the session. Pro features (schedule, strict mode, custom lists) are a
  proposal.
- **Audiobooks** count as reading with a separate icon.
- **Forgotten session** added as "+N minutes" in one tap, marked as added later.
- **Light anti-cheat:** a session over 3 hours asks before counting (when and how is not designed); honest peeks do not reset the
  session; time checked against server time once a server exists.
- **Slumpy mood** reflects today's reading only, does not accumulate; reactions are deadpan.
- **Library:** current, finished, set aside without penalty, own "read next" queue (not a
  recommendation engine); a hidden book shows friends minutes but not the title; quote cards show
  author and title; sharing through the system share sheet.
- **Duel:** stake is dinner, coffee, a gift, or the user's own option; the app never processes
  money (244-FZ); loss rule chosen at
  creation ("first to miss a day" or "read less by the date"). Duration, result confirmation,
  draws, and 3+ participants are open.
