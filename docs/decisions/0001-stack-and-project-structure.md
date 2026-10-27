# ADR-0001: Stack, project structure, and baseline data rules

- **Status:** Accepted as the working stack (owner can override). The rule for
  [attributing minutes to a day](#owner-decision-attributing-minutes-to-a-day) was decided by the
  owner on 2026-10-27.
- **Date:** 2026-10-27
- **Tier:** T2
- **Source:** `work/agent-system-audit/audit-and-plan.md`, sections 11 and 12.

## Context

Slumpy starts on iOS; Android is possible later with no date. The riskiest parts (app blocking
through Family Controls, DeviceActivity, ManagedSettings; Live Activity) are native Swift
extensions in any stack. Almost the whole development cycle is done by an AI agent, so every extra
language, build system, or module is an extra place for an autonomous agent to break. The owner's
device is an iPhone 15 on iOS 18. Development will happen on a dedicated Mac.

## Decision

**Stack**
- SwiftUI, minimum iOS 18, latest stable Xcode.
- Swift 6 language mode with strict concurrency checking from day one.

**Structure**
- One app target and separate targets for extensions (Live Activity widget, DeviceActivity
  monitor, shield screen if needed).
- One local Swift package with pure logic: "today" calculation, session rules, models. No UI
  frameworks imported there.
- App Group shared by the app and its extensions from day one.

**Verification loop**
- Apple's command-line tools on the Mac (build, test, simulator, screenshots, device install);
  Xcode MCP only as an addition for previews and documentation search.
- Xcode Cloud for CI and TestFlight delivery.

**Data rules**
- Everything works on the device without network.
- Identifiers are created on the phone.
- Each session stores its time together with its time zone.
- Attributing minutes to a day follows one explicit rule, implemented once in the logic package
  and covered by tests. The rule is the owner's product decision, see the section below.

**Interface baseline**
- String Catalog from the first screen; Russian only for now.
- Dynamic Type, VoiceOver, and dark theme from the first screen.

**Dependencies**
- A new third-party library is added only through its own ADR.

## Rejected alternatives

| Alternative | Why rejected |
|---|---|
| React Native + Expo | Blocking and Live Activity still need native Swift extensions; Expo adds a second language and build system. Gains (shared Android code, OTA updates, cloud builds) do not outweigh that while Android has no date |
| Minimum iOS 26 | Raising the minimum later is cheap, lowering it is expensive; the owner's iPhone runs iOS 18; all key frameworks are available on iOS 18 |
| 3-4 SPM modules from the start | No second reason for each module yet; one package gives fast tests and a UI-import ban |
| Xcode MCP as the core of the loop | Needs an open Xcode project and connection approval; command-line tools work headless |

## Consequences

- Two visual styles: built with the Xcode 27 SDK, iOS 26+ always shows Liquid Glass; iOS 18 shows
  the old style. Screenshots for acceptance are taken on both.
- New APIs need availability checks with an iOS 18 fallback.
- Cloud agent sessions cannot build or test; code is verified only on the Mac.
- Blocking on iOS 26-27 is unverified on a device until a second device or testers.
- No shared code with a future Android app.

## Reversibility and cost of change in a year

- Raising the minimum iOS: cheap.
- Splitting the package into modules: moderate, done when a second reason appears.
- Moving to a cross-platform stack: expensive, a rewrite of the UI layer.

## Revisit when

- Android is needed within about six months after iOS, or monetization depends on Google Play or
  RuStore.
- Each major Xcode release: re-check the Swift rule and the minimum iOS.

## Owner decision: attributing minutes to a day

The code needs one rule for "which day do these minutes count for". It drives Slumpy's mood
"today", day counts, and any rule like "missed a day". It is a product decision: it changes what
the user sees.

**Decided by the owner on 2026-10-27:**

- **Reading day with a 04:00 cutoff (option C).** A whole session counts to the reading day in
  which it started. A reading day runs from 04:00 to 04:00 local time.
- **Each session keeps its own reading day (option X).** The reading day is computed in the time
  zone stored with the session and never recomputed after a trip.

**Implementation notes (technical, not owner decisions):**

- Reading day of a session: take its start in its stored time zone; if the local time is before
  04:00, the reading day is the previous calendar date, otherwise the same date. Compare wall-clock
  time instead of subtracting four hours, so daylight saving changes cannot shift the result.
- Compute the reading day once, when the session starts, and store it with the session. Time zone
  rules change with system updates, and the owner decided that history never changes on its own;
  only a stored value guarantees that.
- Do date arithmetic ("previous date", "days between") on year, month, and day components in a
  Gregorian calendar set to UTC, never on local `Date` values: in zones that switch clocks at
  midnight a local midnight may not exist. Build the `YYYY-MM-DD` string from integer components,
  never with a locale-dependent formatter.
- The reading day is a calendar date without a time zone: Gregorian year, month, and day (ISO 8601
  `YYYY-MM-DD`), computed with `Calendar(identifier: .gregorian)` set to the session's stored IANA
  time zone. Never store or compare it as a `Date`: midnight in one zone is a different instant
  than midnight in another, so after a trip "today" would stop matching. Never use
  `Calendar.current`: it follows the user's calendar setting (Buddhist, Japanese, and others).
- "Today" for Slumpy's mood is the current reading day in the phone's current time zone; it
  includes the sessions whose stored reading day equals that date.
- "Today" changes at 04:00 local time. System day-change notifications are tied to midnight and
  give no timing guarantee, so recompute "today" when the app returns to the foreground, at 04:00,
  and when the system time zone or clock changes. Read the zone through
  `TimeZone.autoupdatingCurrent`, or call `NSTimeZone.resetSystemTimeZone()` first: the system
  zone is cached. The widget timeline includes an entry at the next 04:00, because the app is
  usually not running then; the app reloads widget timelines on foreground and on a time zone or
  clock change.
- Tests cover: 23:30-00:40 counts to the start day; a start at 00:10 or 03:59 counts to the
  previous date; a start at 04:00 counts to the new date; a session read abroad keeps its day
  after returning; a session read in one time zone counts in "today" while the phone is in
  another zone on the same reading day; a daylight saving change does not move any session; the
  time zone changes while the app is open; on 2026-09-06 in America/Santiago (clocks jump from
  00:00 to 01:00) a session starting at 01:30 counts to 2026-09-05; the number of days between
  consecutive reading days is 1 across 23- and 25-hour local days.

The analysis the owner decided on follows.

**Situations the rule must answer**
1. A session starts at 23:30 and ends at 00:40.
2. The user travels and changes time zone.
3. Daylight saving time changes during or between sessions.

Technical facts that hold for any choice: each session stores its time zone, so either answer
to question 2 can be implemented; durations are stored, so daylight saving time does not change
minute totals.

**Question 1: a session that crosses midnight**

| Option | What the user sees | Cost |
|---|---|---|
| A. Whole session counts to the calendar day it started | Evening reading past midnight stays "yesterday"; after midnight a new session starts "today" | Simplest; a session started at 00:10 counts to the new day even if it is the same evening |
| B. Split at midnight | Minutes before midnight count to yesterday, after midnight to today; Slumpy's mood for "today" starts from the tail of last night's session | Most literal; feels wrong for night readers |
| C. Reading day with a cutoff hour (e.g. 04:00): the whole session counts to the reading day it started in | A night of reading until 3 a.m. is one "evening"; the day switches while the user sleeps | One extra constant; the cutoff hour is a product choice |

Recommendation: C with a 04:00 cutoff. The product is about evening reading instead of the feed;
with A or B the most typical usage, reading past midnight, would split or jump days.

**Question 2: time zone after a trip**

| Option | What the user sees | Cost |
|---|---|---|
| X. Each session keeps the day it had where it was read | History looks the same before and after the trip; on the travel day two "days" can overlap or one can be short | Days in history never change |
| Y. All history is recomputed in the phone's current time zone | After a flight, a late-evening session can move to the next or previous day in history | Days in past history can change after every trip |

Recommendation: X. History the user has already seen does not change on its own.

**Owner's answers (2026-10-27):** question 1, option C with a 04:00 cutoff; question 2, option X.
