---
name: engineering-design
description: |
  Technical brief before code: data model, boundaries and contracts, scenarios, assumptions, what
  else is affected, alternatives for irreversible choices, and the engineering question menu; plus
  a domain blind-spot pass for areas new to the project. Use before writing code for a feature or
  a design discussion, and before any new irreversible decision: storage or schema, module
  boundaries, concurrency, system services or extensions, network, sign-in, money, user data
  leaving the device, or a new dependency.
---

# Engineering design

Apply what you already know at the moment of decision. The brief makes assumptions and trade-offs
explicit so the `reviewer` can check them against the code later.

## 1. Tier

Classify with the tiers in `core-process.md`. T0 needs no brief. A T1 feature gets a short brief;
a T1 bug gets the failing test `core-process.md` describes instead. T2 gets the full brief, an ADR,
and a `reviewer` run in decision mode before any code. The platform pack (`platform.md`, always
loaded) adds design questions to the menu below. For platform work, read the platform's code rules
first (`platform.md` names them): they load on their own only when a matching file is read,
created, or edited. Test and fix rules for a bug: `core-code.md`.

## 2. Domain blind-spot pass (first serious decision in a new area)

Run it when the project has no page for the area in `docs/domains/` yet (examples of areas: a
system service, sync, HTTP caching, payments, sign-in). Write down briefly:

- what experienced practitioners know that newcomers miss;
- which standards, protocols, and platform rules apply;
- where implementations usually break.

Check each point against a primary source (the platform's docs, the RFC or standard, the vendor's
docs). Save the result as a one-page `docs/domains/<area>.md`. The research may go to a subagent to
keep the main context clean. Then continue with the brief.

## 3. Brief

Lives at the top of `work/{feature}/plan.md`. Start with what is most expensive to change:

1. **Data model:** entities, fields, what is stored vs derived, identity, ownership.
2. **Boundaries and contracts:** which module or target owns what; inputs, outputs, errors,
   ordering, threading.
3. **User scenarios:** the flows the change must support, including interruptions and failures
   the user can hit.

Then:

4. **Assumptions** you are making, each one line.
5. **Also affected:** who else reads or writes this state; what changes for other processes or
   extensions; whether stored data needs a migration.
6. **Alternatives (T2 only):** at least two, each with reversibility and cost of replacing it in a
   year. Say which you chose and why.
7. **New elements:** one line per new type, protocol, layer, dependency, or setting: why now, and
   why something simpler does not work.
8. **Menu answers:** only the questions from the menu below that apply, one or two lines each. A
   question checks the design. It asks for a new mechanism only when its row states a rule
   (Concurrent code) or the answer finds a case the design does not handle: add that case to the
   scenarios, then its mechanism. Otherwise the answer is that the simplest design already handles
   it, or that it does not apply here and why.

Size: a T1 brief fits on one screen; a T2 brief stays well under the size of the code it
describes. Delete sections that have nothing to say. A product consequence found here goes to the
owner as a product question; technical choices you make yourself.

A T1 brief at the right size:

```markdown
## Brief
- T1 because it sorts existing data on one screen; nothing stored changes.
- Data model: no new field; the last-opened date comes from the existing history of opens.
- Boundaries: the list screen gets documents with their last-opened date from the existing query.
- Scenarios: never-opened documents go last; ties sort by title the way the system sorts names
  (localized, case-insensitive); the order updates after an open.
- Assumptions: up to a few thousand documents.
- New elements: none; one sort next to the existing query.
- Menu: Any: this is the simplest design. Data and growth: a few thousand items sort in memory in
  milliseconds. Interaction between parts: does not apply, no other process reads the order.
```

## 4. Question menu

| Decision type | Questions |
|---|---|
| Any | What is the simplest design that covers the scenarios? Each element beyond it needs its line in New elements |
| New abstraction, type, module, or boundary | What leaks out: storage errors, async, threads, time, network? What happens with a second implementation? Who owns the state? What is the contract: inputs, outputs, errors, ordering, thread safety? |
| Data and growth | Which field combinations do the types allow that the domain forbids? What happens at 10x and 100x: memory, launch time, scrolling, database size, migration time? How does the migration run? How reversible is it, what does replacing it cost in a year? |
| Interaction between parts, services, extensions | What is the exchange contract? What if the other side fails or is late? Is ordering guaranteed? What if an operation runs twice, or again after a crash at any point: does it end in the same state, and does the next run recognize what a crashed run left behind? |
| Concurrent code | Where is the isolation, what may cross threads, who owns the state? What does the compiler not check (the platform's design questions say)? Which processes write shared data? Writers that record independent facts get their own file or key, merged on read in one shared module; a record that must be one gets one writer or the store's transactions. What about cancellation? What runs on the main thread? |
| System service or external API | What if permission is denied? What differs across supported OS versions? What are the background limits? What without network? What do the store's review and privacy rules require? |
| Data crosses a boundary (`core-process.md`, "Whatever the tier"), or a standard or protocol applies | What does the other side assume? Is each value the rule lists represented explicitly? Which standard applies and what does it require? Read the primary source: RFC, ISO 8601, IANA time zones, HTTP semantics, OAuth, Unicode, WCAG, the platform's interface guidelines and store rules. Do not answer from memory |
| Interface | Text size settings, screen reader, dark theme, small screens, list performance |

## 5. After the brief

- T2: write the ADR in `docs/decisions/` (format in its README), then run `reviewer` in decision
  mode on the brief and ADR before writing code.
- Keep a log at the bottom of `plan.md`: each step with its verification result, each review with
  its mode, round, and verdict, and each deviation from the brief with the reason and the
  conservative choice taken.
