# Platform pack: Apple iOS

Rules for any iOS project. This project's own choices (minimum iOS, Swift language mode, module
layout) are in CLAUDE.md and the ADRs.

- Code rules: `.claude/rules/swift.md` (loads with `.swift` files), with the platform's review
  rubric.
- Builds and tests need a Mac with Xcode; cloud sessions cannot run them.
- Docs recipe: append `.md` to a developer.apple.com documentation URL to get markdown, e.g.
  `https://developer.apple.com/documentation/familycontrols.md`.
- New platform capabilities: an app extension, an entitlement, a system service.
- Security-pass triggers: Keychain, permissions, App Transport Security, the Privacy Manifest, and
  a required-reason API whose category or reason the Privacy Manifest does not declare yet.
- Owner report screenshots: light and dark, large text, the minimum and the current iOS.

## Design questions

Names and answers for the `engineering-design` menu:

- Concurrency: isolation means actors, and what may cross threads is `Sendable`. What the compiler
  does not check: Swift 6 checks only in-memory data races inside one process, not files,
  databases, or defaults shared with extensions through an App Group, and not state that changes
  across an `await`.
- System services: the supported OS versions are iOS versions; the store's review is App Review.
- Standards: Sign in with Apple, APNs, Apple HIG, App Store Review Guidelines.
- Interface: text size settings are Dynamic Type; the screen reader is VoiceOver.
