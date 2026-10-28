---
paths:
  - "**/*.swift"
---

# Swift and Apple platform rules (platform pack)

## Facts

- Any API newer than the project's minimum iOS (CLAUDE.md) needs `if #available` / `@available`
  with a working path for the minimum. The compiler catches availability, not soft deprecations:
  when unsure whether an API is current, check its documentation page.
- Swift 6 language mode, strict concurrency. Default actor isolation is set per module (SE-0466,
  Swift 6.2); a module without the setting is `nonisolated`. The setting for each module, and the
  Approachable Concurrency build setting (it changes where nonisolated async code runs), are
  decided in an ADR; keep them consistent across modules. DeviceActivityMonitor callbacks come
  from the SDK without main-actor isolation.
- `@unchecked Sendable`, `nonisolated(unsafe)`, `@preconcurrency` (imports and conformances), and
  `MainActor.assumeIsolated` need a comment with the reason and the invariant that makes them safe;
  the reviewer treats them as findings otherwise. `assumeIsolated` and `@preconcurrency`
  conformances trap at runtime when called off their actor (SE-0423); the DeviceActivityMonitor
  callbacks above are not main-actor isolated.
- Toolchain: the latest stable Xcode; on 2026-10-27 that is Xcode 27.1 with Swift 6.4 and the iOS
  27 SDK. Any API released after mid-2026, and any API you are unsure about, is read in the docs
  before use.
- With the iOS 27 SDK `UIDesignRequiresCompatibility` is ignored, so iOS 26+ renders Liquid Glass
  and earlier iOS renders the old style. With a minimum below iOS 26, UI changes are checked on
  both.
- The DeviceActivity monitor extension has about 6 MB of memory (developer reports): no heavy
  frameworks or caches there.

## Design questions

Add these to the `engineering-design` menu for Apple platform work:

- Concurrency: Swift 6 checks only in-memory data races inside one process: not files, databases,
  or defaults shared with extensions through an App Group, and not state that changes across an
  `await`. What is `Sendable`, and which actor isolates the state?
- System services: what differs across iOS versions; background limits; what App Review and the
  privacy rules require.
- Standards: Sign in with Apple, APNs, Apple HIG, App Store Review Guidelines.
- Interface: Dynamic Type, VoiceOver.

## Review rubric

- Value or reference semantics, and why.
- Static or dynamic dispatch and its cost on hot paths.
- Protocols with associated types; generics versus `any`.
- ARC: reference cycles, closure captures.
- Actor isolation and `Sendable`.
- API availability for the minimum iOS and soft deprecations the compiler does not flag.
