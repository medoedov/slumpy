# Slumpy

iOS app that replaces the evening scroll with reading: timed reading sessions that can block
distracting apps, a deadpan companion character, a personal library, friends and duels.
Product content comes from the draft `mvp.md`: treat it as hypotheses, not decisions.

## Agent system

- Layers and their files: `.claude/rules/core-process.md`, first paragraph. Platform pack here:
  Apple iOS.
- `scripts/check-layers` fails when a core file holds a platform or project detail.

## Project facts

- Minimum iOS 18. The local logic package does not import SwiftUI, UIKit, or other UI frameworks
  (ADR-0001).
- Default branch: `dev`.
- External actions, decided by the owner: push or merge to `main`, App Store Connect, TestFlight,
  publications.
- Check command: `scripts/check`, planned; it runs on the Mac.
- The owner's language: Russian.
- Secrets live in a git-ignored `.env` on the Mac or in Xcode Cloud secrets.
- `AGENTS.md`, `.agents/`, `.codex/`, `.githooks/` are frozen: do not edit, regenerate, or enable
  them, and do not read them as project facts (they describe the old Expo setup).
