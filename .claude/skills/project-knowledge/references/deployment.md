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

- **Apple Developer Program:** not enrolled yet. Development and the simulator do not need it; the
  blocking check on an iPhone (the Family Controls capability), the entitlement request, and
  TestFlight do. Paid with a foreign card in the founder's name, which
  may take time to arrange. Individual vs organization enrollment is an open owner decision: it
  sets the App Store seller name and is hard to change later.
- **Family Controls distribution entitlement:** requested by the Account Holder for the app bundle
  ID and separately for each Screen Time extension bundle ID (DeviceActivity monitor, shield),
  right after the blocking check on an iPhone; approval time is unpredictable. Check the current
  request form when submitting: developers report it may have changed.
- **Payments outside the App Store** (hypothesis from `mvp.md`: Apple payouts to Russia are
  closed, Pro sold through Google Play, RuStore, web): App Review Guideline 3.1.1 risk; decided
  together with monetization.
- **Android:** no date; possible later.

---

## Environments

- **Closed beta (hypothesis from `mvp.md`):** TestFlight; size and duration in
  [project.md](project.md#mvp-scope).
- **Production:** App Store; launch date open.

---

## Secrets

No secrets exist yet. Never in the repository or chat: local `.env` (git-ignored) on the Mac or
Xcode Cloud environment secrets.

---

## Monitoring

Nothing configured. No analytics until the first tester build; the analytics service and its
privacy impact are decided before that build.
