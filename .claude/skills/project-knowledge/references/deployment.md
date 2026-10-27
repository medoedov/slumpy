# Deployment & Operations

- [Status](#status)
- [Build and Delivery](#build-and-delivery)
- [Accounts and Stores](#accounts-and-stores)
- [Environments](#environments)
- [Secrets](#secrets)
- [Monitoring](#monitoring)

## Status

Nothing is built or deployed yet. The path below is from
[ADR-0001](../../../../docs/decisions/0001-stack-and-project-structure.md); items from the draft
`mvp.md` are marked as hypotheses.

---

## Build and Delivery

- **Development host:** a dedicated Mac (planned, not yet set up). Builds, tests, simulators, and
  device installs run there with Apple's command-line tools.
- **CI and distribution:** Xcode Cloud, then TestFlight, then the App Store.
- **External actions** - App Store Connect, TestFlight uploads, any publication - are owner
  decisions and need explicit approval each time.

---

## Accounts and Stores

- **Apple Developer Program:** not enrolled yet, enrollment in progress. It blocks the Family
  Controls check on an iPhone and TestFlight.
- **Family Controls distribution entitlement:** requested from Apple right after enrollment;
  approval time is unpredictable.
- **Payments outside the App Store** (hypothesis from `mvp.md`: Apple payouts to Russia are
  closed, Pro sold through Google Play, RuStore, web): App Review Guideline 3.1.1 risk; decided
  together with monetization.
- **Android:** no date; possible later.

---

## Environments

- **Closed beta (hypothesis from `mvp.md`):** TestFlight, 50-150 testers, 2-4 weeks.
- **Production:** App Store; launch date open.

---

## Secrets

No secrets exist yet. Never in the repository or chat: local `.env` (git-ignored) on the Mac or
Xcode Cloud environment secrets.

---

## Monitoring

Nothing configured. No analytics until the first tester build; the analytics service and its
privacy impact are decided before that build.
