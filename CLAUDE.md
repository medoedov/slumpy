# Slumpy

iOS app that replaces the evening scroll with reading: timed reading sessions that can block
distracting apps, a deadpan companion character, a personal library, friends and duels.
Product content comes from the draft `mvp.md`: treat it as hypotheses, not decisions.

## Agent system

- Layers and their files: `.claude/rules/core-process.md`, first paragraph. Platform pack here:
  Apple iOS.
- The checks catch listed cases only; their self-test is `scripts/test-checks`. After changing
  `scripts/`, run `scripts/test-checks --mutants` (minutes; every mutant must be killed).

## Project facts

- Minimum iOS 18; Swift 6 language mode with strict concurrency; the latest stable Xcode
  (ADR-0001).
- The local logic package does not import SwiftUI, UIKit, or other UI frameworks (ADR-0001). It is
  the shared module where independent facts are merged on read (`engineering-design` menu,
  Concurrent code).
- Default branch: `dev`.
- External actions: push or merge to `main`, App Store Connect, TestFlight,
  publications.
- Check command: `scripts/check`. It runs the document checks now and will run build and tests once
  the Xcode project exists.
- The owner's language: Russian.
- Where secrets live: `deployment.md`, Secrets.
- `AGENTS.md`, `.agents/`, `.codex/`, `.githooks/` are frozen: do not edit, regenerate, or enable
  them, and do not read them as project facts (they describe the old Expo setup).
