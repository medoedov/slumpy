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
- `@unchecked Sendable` and `nonisolated(unsafe)` need a comment with the reason and the invariant
  that makes them safe; the reviewer treats them as findings otherwise.
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
