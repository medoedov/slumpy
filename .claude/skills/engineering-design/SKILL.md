---
name: engineering-design
description: |
  Technical brief before code: data model, boundaries and contracts, scenarios, assumptions, what
  else is affected, alternatives for irreversible choices, and the engineering question menu; plus
  a domain blind-spot pass for areas new to the project. Use before writing code for any T1 or T2
  change: a feature, a bug fix that crosses boundaries, a design or "how should this work"
  discussion, and any change that touches persisted data, module boundaries, concurrency, system
  services or extensions, network, privacy, money, or dependencies, even when it is phrased as a
  small edit.
---

# Engineering design

Apply what you already know at the moment of decision. The brief makes assumptions and trade-offs
explicit so the `reviewer` can check them against the code later.

## 1. Tier

Classify with the tiers in CLAUDE.md. T0 needs no brief. T1 gets a short brief. T2 gets the full
brief, an ADR, and a `reviewer` run in decision mode before any code.

## 2. Domain blind-spot pass (first serious decision in a new area)

Run it when the project has no page for the area in `docs/domains/` yet (examples of areas:
Screen Time, sync, HTTP caching, payments, sign-in). Write down briefly:

- what experienced practitioners know that newcomers miss;
- which standards, protocols, and platform rules apply;
- where implementations usually break.

Check each point against a primary source (Apple docs, the RFC or standard, the vendor's docs).
Save the result as a one-page `docs/domains/<area>.md`. The research may go to a subagent to keep
the main context clean. Then continue with the brief.

## 3. Brief

Lives at the top of `work/{feature}/plan.md`. Start with what is most expensive to change:

1. **Data model:** entities, fields, what is stored vs derived, identity, ownership.
2. **Boundaries and contracts:** which module or target owns what; inputs, outputs, errors,
   ordering, threading.
3. **User scenarios:** the flows the change must support, including interruptions and failures
   the user can hit.

Then:

4. **Assumptions** you are making, each one line.
5. **Also affected:** who else reads or writes this state; what changes for extensions; whether
   stored data needs a migration.
6. **Alternatives (T2 only):** at least two, each with reversibility and cost of replacing it in a
   year. Say which you chose and why.
7. **New elements:** one line per new type, protocol, layer, dependency, or setting: why now, and
   why something simpler does not work.
8. **Menu answers:** only the questions from the menu below that apply, one or two lines each.

Size: a T1 brief fits on one screen; a T2 brief stays well under the size of the code it
describes. Delete sections that have nothing to say. A product consequence found here goes to the
owner as a product question; technical choices you make yourself.

## 4. Question menu

| Decision type | Questions |
|---|---|
| New abstraction, type, module, or boundary | What leaks out: storage errors, async, threads, time, network? What happens with a second implementation? Who owns the state? What is the contract: inputs, outputs, errors, ordering, thread safety? |
| Data and growth | What happens at 10x and 100x: memory, launch time, scrolling, database size, migration time? How does the migration run? How reversible is it, what does replacing it cost in a year? |
| Interaction between parts, services, extensions | What is the exchange contract? What if the other side fails or is late? Is ordering guaranteed? Can duplicates happen? |
| Concurrent code | Where is the isolation, what is `Sendable`, who owns the state? What about cancellation? What runs on the main thread? |
| System service or external API | What if permission is denied? What differs across iOS versions? What are the background limits? What without network? What do App Review and privacy rules require? |
| Standard or protocol | Which standard applies and what does it require? Read the primary source: RFC, ISO 8601, IANA time zones, HTTP semantics, OAuth and Sign in with Apple, APNs, Unicode, WCAG and Apple HIG, App Store Review Guidelines. Do not answer from memory |
| Interface | Dynamic Type, VoiceOver, dark theme, small screens, list performance |
| Any | Can it be simpler? |

## 5. After the brief

- T2: write the ADR in `docs/decisions/` (format in its README), then run `reviewer` in decision
  mode on the brief and ADR before writing code.
- Keep a log at the bottom of `plan.md`: each step with its verification result, and each
  deviation from the brief with the reason and the conservative choice taken.
