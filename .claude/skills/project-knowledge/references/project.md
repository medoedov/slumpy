# Project Context

- [Status](#status)
- [Project Overview](#project-overview)
- [Target Audience](#target-audience)
- [Core Problem](#core-problem)
- [Product Principles](#product-principles)
- [Feature Hypotheses](#feature-hypotheses)
- [MVP Scope](#mvp-scope)
- [Success Metrics](#success-metrics)
- [Out of Scope](#out-of-scope)
- [Open Decisions](#open-decisions)

## Status

Source: the draft [mvp.md](../../../../mvp.md) (v0.3, 2026-10-22). The owner treats it as a
draft: **everything below is a product hypothesis**, not a decision, unless marked as confirmed.
Confirmed by the owner so far:

- Start with iOS; Android is possible later, with no date.
- App blocking is potentially important; whether it is in the MVP is not decided.
- The MVP composition is not approved.
- Visual design is made in Claude Design.

Working assumption until the owner says otherwise: the interface is Russian only.

Product decisions belong to the owner. Confirm a hypothesis through `product-spec` before a
feature depends on it.

---

## Project Overview

**Name:** Slumpy (working name; trademark, store, domain, and handle checks pending).

**Description:** A reading app that replaces the evening social-media scroll with a book. The
user starts a reading session: puts the phone face down while reading paper or an e-reader, or
reads on the phone while selected apps are blocked. Slumpy, a deadpan companion character, gets
happier from today's reading. Friends see what you read and can challenge you to a duel.

Store tagline candidate: «Slumpy: читай, а не листай» (not decided).

---

## Target Audience

Hypothesis: people aged 18-35 in Russia who consider themselves readers but lose their evenings to
the feed. Women report liking reading more often (73% vs 58%, figures cited in `mvp.md`).

Use case: "I want to read but cannot start: the phone pulls me in."

---

## Core Problem

Figures cited in `mvp.md` (VTsIOM 2025, Statista), not re-verified: "fewer social media" is a more
common goal than "read more" (21% of New Year resolutions); 66% of Russians like reading, 29% read
daily; about a third of started books are abandoned.

Positioning hypothesis: Forest and Opal fight the phone but are not about reading; Bookly and
Goodreads are about reading but do not fight the phone; Yandex Books works only with its own
catalog.

---

## Product Principles

Hypotheses from `mvp.md`:

1. Reading only; expand only deeper into reading (audiobooks, longreads, comics).
2. Valuable for one person from day one; people and duels are a second layer.
3. No Duolingo mechanics: no streaks, XP, or "your streak burned".
4. Not a catalog: no reviews, book ratings, or recommendation engine.
5. Any book: paper, Kindle, Litres, audio.
6. Visual quality on par with the best apps, no feature overload.
7. Concrete outward communication, no abstractions.

---

## Feature Hypotheses

- **Reading session** - timed session in two modes, minutes recorded automatically.
- **Slumpy** - personal character whose mood reflects today's reading.
- **Library** - current, finished, set aside, "read next" queue, goals, quotes, hidden books.
- **Friends** - what friends read, "reading now", invitations, joint sessions, shelves.
- **Duel** - challenge a friend with a non-monetary stake and a loss rule.

---

## MVP Scope

Not approved. The draft proposes an iOS closed beta in TestFlight (50-150 people, 2-4 weeks) with
onboarding, both session modes with blocking, Slumpy, the library, friends, and duels, on a
"session with reading type" data model. The 6-8 week estimate in the draft is a model estimate.

---

## Success Metrics

Draft closed-beta thresholds from `mvp.md`, to be re-validated in a spec:

| Metric | Target | Alarm |
|---|---|---|
| First session of 5+ minutes within 48 hours | >= 40% | < 20% |
| Week-2 return: sessions on 3+ days during days 8-14 | >= 35% | < 20% |
| Share of minutes from the timer rather than added later | >= 70% | < 50% |
| Enabled blocking at least once | >= 50% | observe |
| Created a duel or invited a friend | >= 25% | < 10% |
| Return of duel participants vs others | +10 pp or more | observe |

---

## Out of Scope

Hypotheses from `mvp.md`: streaks and XP; reviews, ratings, recommendation engine; global
leaderboards and a public feed; dedicated story-sharing features; AI features; processing money
(244-FZ); a Telegram bot as a test channel.

---

## Open Decisions

Owner decisions not taken yet:

1. MVP composition, including app blocking (after the blocking check on an iPhone).
2. Whether Slumpy looks the same for everyone or slightly different per user.
3. Duel details: duration, result confirmation, draws, three or more participants.
4. Store tagline; name checks.
5. Monetization and Pro.
6. Public launch date.
7. Apple Developer enrollment as an individual or an organization (sets the App Store seller
   name, hard to change later).
