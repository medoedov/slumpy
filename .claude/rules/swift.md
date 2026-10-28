---
paths:
  - "**/*.swift"
---

# Swift and Apple platform facts for Slumpy

- Minimum iOS 18. Any API newer than iOS 18 needs `if #available` / `@available` with a working
  iOS 18 path. The compiler catches availability, not soft deprecations: when unsure whether an
  API is current, check its documentation page.
- Swift 6 language mode, strict concurrency. Default actor isolation is set per module (SE-0466,
  Swift 6.2); a module without the setting is `nonisolated`. The setting for each target and for
  the logic package, and the Approachable Concurrency build setting (it changes where nonisolated
  async code runs), are decided in the skeleton ADR; keep them consistent across modules.
  DeviceActivityMonitor callbacks come from the SDK without main-actor isolation.
- `@unchecked Sendable`, `nonisolated(unsafe)`, `@preconcurrency` (imports and conformances), and
  `MainActor.assumeIsolated` need a comment with the reason and the invariant that makes them safe;
  the reviewer treats them as findings otherwise. `assumeIsolated` and `@preconcurrency`
  conformances trap at runtime when called off their actor (SE-0423); the DeviceActivityMonitor
  callbacks above are not main-actor isolated.
- Toolchain: the latest stable Xcode; on 2026-10-27 that is Xcode 27.1 with Swift 6.4 and the iOS
  27 SDK. Any API released after mid-2026, and any API you are unsure about, is read in the docs
  before use.
- Apple docs recipe: append `.md` to a developer.apple.com documentation URL to get markdown,
  e.g. `https://developer.apple.com/documentation/familycontrols.md`.
- With the iOS 27 SDK `UIDesignRequiresCompatibility` is ignored and we do not set it, so iOS 26+
  renders Liquid Glass and iOS 18 renders the old style. UI changes are checked on both.
- The DeviceActivity monitor extension has about 6 MB of memory (developer reports): no heavy
  frameworks or caches there.
- The local logic package does not import SwiftUI, UIKit, or other UI frameworks.
- Platform traps you hit go to `docs/lessons.md`.

## Tests and fixes

- A test calls the code the way its caller does and checks what the caller observes. Judge it by
  two imagined edits: break the behavior (a wrong value, an effect skipped or done twice) and the
  test must fail; restructure the internals with the same observable result and it must still
  pass. Every behavior a change adds needs such a test: deleting a line of new logic fails at least
  one test. A rule of the form "do not do X" needs a test input on which X gives a different answer.
  When no automated test can honestly observe the behavior (layout, system UI, an effect only a
  device shows), do not write one pinned to the implementation; the check goes to the screenshots
  or the device checklist (`patterns.md`, Verification).
- Fix a crash or wrong state at its first cause. First decide whether the state is legitimate: the
  system may be in it (an independent fact another process recorded, arriving in any order; left by
  a crash or a killed extension; a permission the user revoked). If it is, the code that broke on it
  is the cause, and handling it there is the fix. If it should never exist, fix the code that
  produced it; a `guard`, `??`, early return, retry, or clamp where it surfaced hides the cause and
  is not the fix by itself. If an older version already stored it on devices, the reading code also
  handles it or a migration repairs it. Each part gets a test.
- If two fixes that rest on the same premise fail the same check, write the premise in one
  sentence and test it directly before a third fix.
