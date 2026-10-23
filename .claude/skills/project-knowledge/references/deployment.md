# Deployment & Operations

- [Purpose](#purpose)
- [Deployment Platform](#deployment-platform)
- [Accounts and Stores](#accounts-and-stores)
- [Operating Model](#operating-model)
- [Environment Variables](#environment-variables)
- [Deployment Triggers](#deployment-triggers)
- [Required Manual Release Steps](#required-manual-release-steps)
- [Emergency Recovery](#emergency-recovery)
- [Environments](#environments)
- [Monitoring & Observability](#monitoring--observability)

## Purpose
Delivery, infrastructure, and operations for AI agents. Nothing is deployed yet; this file records
the agreed plan from [mvp.md](../../../../mvp.md).

---

## Deployment Platform

**Mobile:** iOS app built by EAS Build (Expo cloud) and distributed through TestFlight for the
closed beta, then the App Store.

**Backend:** Self-hosted Supabase or PocketBase in a Russian cloud with Russian S3-compatible
storage (choice open).

**Why this platform:** EAS builds iOS without a Mac; Russian hosting satisfies 152-FZ.

---

## Accounts and Stores

- Apple Developer Program: $99/year, paid with a foreign card in the founder's name; the app is
  published under the founder's personal account (allowed for a free app).
- Apple payouts to Russia are closed, so Pro is not sold through the App Store; paid features go
  through Google Play, RuStore, and the web later. A Russian sole proprietorship is needed once
  payments start.
- Google Play ($25) is needed only for the deferred Android version.

---

## Operating Model

**Routine delivery:** Not set up yet. Planned: EAS Build for iOS builds and EAS Submit or manual
upload to TestFlight.

**Direct target operations:** Not applicable until the backend exists.

**Agent/operations host:** Not applicable yet.

**Environment strategy:** TBD with the backend.

**Production authorization:** Any App Store Connect / TestFlight submission and any production
backend change require the user's explicit approval.

---

## Environment Variables

**See:** [.env.example](../../../../.env.example) in project root. No variables defined yet;
backend URLs and keys will be added with the backend choice. EAS build secrets live in EAS, not in
the repository.

---

## Deployment Triggers

**Production:** Not configured.

**Staging:** Not configured.

**Preview:** Not configured.

---

## Required Manual Release Steps

- [ ] Request the Family Controls entitlement from Apple for the app bundle ID and every extension
  bundle ID in the first week of development; approval takes days to weeks and blocks app blocking.
- [ ] Enroll in the Apple Developer Program before the first TestFlight build.

---

## Emergency Recovery

Not applicable yet: no production release or backend.

---

## Environments

**Closed beta:** TestFlight, 50-150 testers for 2-4 weeks.

**Production:** App Store, after the beta; public launch date is open.

---

## Monitoring & Observability

No logging, error tracking, or analytics configured yet. The beta must measure the success metrics
in [project.md](project.md#success-metrics); the analytics tool is not chosen.
