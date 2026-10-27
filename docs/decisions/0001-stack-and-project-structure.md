# ADR-0001: Stack, project structure, and baseline data rules

- **Status:** Accepted as the working stack (owner can override). One section is **pending the
  owner's product decision**: [attributing minutes to a day](#pending-owner-decision-attributing-minutes-to-a-day).
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
  and covered by tests. The rule itself is a product decision, see the pending section below.

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

## Pending owner decision: attributing minutes to a day

The code needs one rule for "which day do these minutes count for". It drives Slumpy's mood
"today", day counts, and any rule like "missed a day". It is a product decision: it changes what
the user sees. Until the owner decides, the agent does not ship behavior that depends on it
without recording the assumption.

**Situations the rule must answer**
1. A session starts at 23:30 and ends at 00:40.
2. Daylight saving time changes during or between sessions.
3. The user travels and changes time zone; past days must not move.

**Options**

| Option | What the user sees | Cost |
|---|---|---|
| A. Whole session counts to the calendar day it started | Evening reading past midnight stays "yesterday"; after midnight a new session starts "today" | Simplest; a session started at 00:10 counts to the new day even if it is the same evening |
| B. Split at midnight | Minutes before midnight count to yesterday, after midnight to today; Slumpy's mood for "today" starts from the tail of last night's session | Most literal; feels wrong for night readers |
| C. Reading day with a cutoff hour (e.g. 04:00): the whole session counts to the reading day it started in | A night of reading until 3 a.m. is one "evening"; the day switches while the user sleeps | One extra constant; the cutoff hour is a product choice |

For all options, the day is computed in the time zone stored with the session, not the phone's
current one. A trip does not move past sessions to other days. Daylight saving time does not
change minute totals because durations are stored, not derived from wall-clock times.

**Recommendation:** C with a 04:00 cutoff. The product is about evening reading instead of the
feed; with A or B the most typical usage, reading past midnight, would split or jump days.

**Owner decides:** the option, and for C the cutoff hour.
