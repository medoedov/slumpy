# Platform pack: Apple iOS

Rules for any iOS project. This project's own choices (minimum iOS, module layout) are in CLAUDE.md
and the ADRs.

- Code rules: `.claude/rules/swift.md`, with the platform's design questions and review rubric. It
  loads on its own only when a `.swift` file is read, created, or edited; read it first for any
  platform design or review.
- Builds and tests need a Mac with Xcode; cloud sessions cannot run them.
- Docs: Apple frameworks from Apple's documentation: append `.md` to a developer.apple.com
  documentation URL to get markdown, e.g. `https://developer.apple.com/documentation/familycontrols.md`.
  Other libraries through context7.
- New platform capabilities (T2 the first time): an app extension, an entitlement, a system
  service.
- Security-pass triggers: Keychain, permissions, App Transport Security, the Privacy Manifest, and
  a required-reason API whose category or reason the Privacy Manifest does not declare yet.
- Owner report screenshots: light and dark, large text, the minimum and the current iOS.
