# Architecture

- [Status](#status)
- [Stack](#stack)
- [Targets and Package](#targets-and-package)
- [Architecture Map](#architecture-map)
- [Deferred Decisions](#deferred-decisions)
- [Data Rules](#data-rules)
- [Planned Entities](#planned-entities)
- [App Blocking](#app-blocking)
- [External Integrations](#external-integrations)

## Status

App code does not exist yet; all of it will live in this repository (decided 2026-10-23). The stack and structure below are decided in
[ADR-0001](../../../../docs/decisions/0001-stack-and-project-structure.md). Entities and
integrations come from the draft [mvp.md](../../../../mvp.md) and are product hypotheses.

---

## Stack

- **UI:** SwiftUI. Minimum iOS, Xcode, and Swift language mode: ADR-0001. Swift-specific facts:
  [.claude/rules/swift.md](../../../rules/swift.md).
- **Third-party libraries:** none yet. A new one is added only through an ADR.
- **Storage:** not chosen. SwiftData or SQLite through GRDB, decided before the reading-session
  model in ADR-0002.
- **Backend:** none until social features. Personal reading works without an account.
- **Character rendering:** not chosen. Working assumption: a SwiftUI prototype of the simple face
  before the character feature; Rive from the draft is a hypothesis.

---

## Targets and Package

- One app target.
- Separate targets for extensions: Live Activity widget, DeviceActivity monitor, shield screen
  if needed. Extensions stay minimal (monitor memory limit, see the Swift rule).
- One local Swift package with pure logic: the "today" calculation, session rules, models. It
  must not import UI frameworks.
- App Group shared by the app and its extensions from day one.
- A new module appears only when there is a second reason for it.

---

## Architecture Map

Not created yet. When the project skeleton exists, record here the real directory map, which
target owns which state, and how the app and extensions exchange data. Keep it current at feature
finalization.

---

## Deferred Decisions

Deliberately not decided yet; each is decided at the step named.

- **Skeleton ADR (first step on the Mac):**
  - how the agent changes the Xcode project: folders that Xcode syncs without editing
    `project.pbxproj`, or a project generated from a description (XcodeGen, Tuist). Hand edits of
    `project.pbxproj` are a known trap for agents: merge conflicts, lost files, a broken project;
  - default actor isolation and Approachable Concurrency for each target and the logic package,
    including the DeviceActivity monitor (see the Swift rule);
  - the test framework (working assumption: Swift Testing for the logic package).
- **Storage:** ADR-0002 before the reading-session model.
- **Sync and conflict resolution:** together with accounts and the backend.
- **Agent runtime integration:** shared entry point and loading adapters are decided in
  [docs/agent-system.md](../../../../docs/agent-system.md#runtime-loading), confirmed 2026-11-02.

---

## Data Rules

From ADR-0001:

- Everything works on the device without network.
- Identifiers are created on the phone.
- Each session stores its time together with its time zone.
- Attributing minutes to a day follows one explicit rule covered by tests, see the "Today"
  invariant in [patterns.md](patterns.md#business-invariants).

---

## Planned Entities

Product hypotheses from `mvp.md`; the schema is designed with ADR-0002.

- **ReadingSession** - core record with a reading type so audio, longreads, and comics can be
  added without schema rework. Hypothesized fields: book, start, duration, time zone, mode (book
  in hands / on phone), reading type, source (timer / added later), flags.
- **Book, LibraryEntry** - book metadata; the user's status for a book (current, finished, set
  aside, queued in "read next"), hidden flag, queue order.
- **Goal** - a book by a date, N books for a season, volume per year.
- **Quote** - text or OCR'd photo, always linked to a book.
- **Friendship, Invitation, JointSession, Duel** - social layer; needs a backend and accounts,
  deferred until social features.

---

## App Blocking

The main platform risk. Inclusion in the MVP is decided after the blocking check on an iPhone.

- Screen Time API: Family Controls (authorization and app selection), DeviceActivity (schedule and
  monitoring), ManagedSettings (shields).
- The development capability needs a paid Apple Developer Program membership; App Store
  distribution needs an entitlement request for the app and for each extension, see
  [deployment.md](deployment.md#accounts-and-stores).
- Works only on a physical device, not in the simulator.
- There is no public iOS API for the device lock state; "face down" is a start ritual.

---

## External Integrations

All are hypotheses from `mvp.md`, decided when the feature that needs them is planned.

- **Book metadata:** a free open database; which one is open.
- **Backend and hosting:** decided before friends and duels, including 152-FZ requirements.
- **Accounts and sign-in:** with the backend; App Review Guideline 4.8 applies.
- **On-device OCR for quotes:** Apple Vision.
