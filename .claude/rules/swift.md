---
paths:
  - "**/*.swift"
---

# Swift and Apple platform code rules (platform pack)

## Facts

- Any API newer than the project's minimum iOS (AGENTS.md) needs `if #available` / `@available`
  with a working path for the minimum. The compiler catches availability, not soft deprecations:
  when unsure whether an API is current, check its documentation page.
- Default actor isolation is set per module (SE-0466, Swift 6.2); a module without the setting is
  `nonisolated`. The setting for each module, and the
  Approachable Concurrency build setting (it changes where nonisolated async code runs), are
  decided in an ADR; keep them consistent across modules. DeviceActivityMonitor callbacks come
  from the SDK without main-actor isolation.
- `@unchecked Sendable`, `nonisolated(unsafe)`, `@preconcurrency` (imports and conformances), and
  `MainActor.assumeIsolated` need a comment with the reason and the invariant that makes them safe.
  `assumeIsolated` and `@preconcurrency`
  conformances trap at runtime when called off their actor (SE-0423); the DeviceActivityMonitor
  callbacks above are not main-actor isolated.
- Toolchain: checked 2026-11-03 against Apple's
  [Xcode requirements](https://developer.apple.com/xcode/system-requirements): the table lists
  Xcode 27.2 with Swift 6.4 and the iOS 27.2 SDK. This is not an installed-toolchain observation;
  confirm release status and the actual Mac toolchain before building. Read documentation for
  an API whose availability or behavior could change the implementation.
- With the iOS 27 SDK `UIDesignRequiresCompatibility` is ignored, so iOS 26+ renders Liquid Glass
  and earlier iOS renders the old style. With a minimum below iOS 26, UI changes are checked on
  both. Checked 2026-11-03 against the
  [Apple Frameworks Engineer clarification](https://developer.apple.com/forums/thread/838637):
  this depends on the build SDK, not just the deployment target.
- Developer reports of roughly 6 MB for DeviceActivity monitors are not a guaranteed Apple
  memory budget. Keep extensions minimal; measure memory and termination on the target device
  before relying on a framework, cache, or numerical limit.

## Review rubric

- Value or reference semantics, and why.
- Static or dynamic dispatch and its cost on hot paths.
- Protocols with associated types; generics versus `any`.
- ARC: reference cycles, closure captures.
- Actor isolation and `Sendable`.
- API availability for the minimum iOS and soft deprecations the compiler does not flag.
