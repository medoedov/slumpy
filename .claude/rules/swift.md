---
paths:
  - "**/*.swift"
---

# Swift and Apple platform facts for Slumpy

- Minimum iOS 18. Any API newer than iOS 18 needs `if #available` / `@available` with a working
  iOS 18 path. The compiler catches availability, not soft deprecations: when unsure whether an
  API is current, check its documentation page.
- Swift 6 language mode, strict concurrency. App and extension targets use default MainActor
  isolation (SE-0466). `@unchecked Sendable` and `nonisolated(unsafe)` need a comment with the
  reason and the invariant that makes them safe; the reviewer treats them as findings otherwise.
- Toolchain as of 2026-10-26: Xcode 27.1, iOS 27, Swift 6.4. Any API released after mid-2026
  (iOS 27, Xcode 27, Swift 6.4 and later), and any API you are unsure about, is read in the docs
  before use.
- Apple docs recipe: append `.md` to a developer.apple.com documentation URL to get markdown,
  e.g. `https://developer.apple.com/documentation/familycontrols.md`.
- Built with the Xcode 27 SDK, iOS 26+ always renders Liquid Glass (`UIDesignRequiresCompatibility`
  is ignored); iOS 18 renders the old style. UI changes are checked on both.
- The DeviceActivity monitor extension has about 6 MB of memory (developer reports): no heavy
  frameworks or caches there.
- The local logic package does not import SwiftUI, UIKit, or other UI frameworks.
- Platform traps you hit go to `docs/lessons.md`.
