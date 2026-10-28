---
name: product-spec
description: |
  Product specification for a new feature or a change in what the user sees: picks at most five
  product questions for the owner, each with a recommendation, writes work/{feature}/spec.md, and
  checks it from the implementer's side. Use when the owner wants a new feature, asks to think a
  feature through or agree on what to build, or describes a product idea with open points, before
  any technical design.
---

# Product spec

The owner decides product; you decide everything technical. A spec fixes what the user gets so
the implementation needs no further product questions.

## 1. Gather

Read the product context in `project-knowledge` (`project.md`, product rules in `patterns.md`).
Facts there are hypotheses unless marked confirmed; a feature that depends on one confirms it
through a question. List every open point in the request.

## 2. Sort the open points

- **Technical** (storage, architecture, libraries, how to compute something): decide yourself and
  record it as an assumption. Never ask the owner.
- **Minor product gaps** where a sensible default exists and changing it later is cheap: take the
  default and list it under assumptions in the spec.
- **Product questions:** what remains. Rank by impact on the user times uncertainty. Ask at most
  five; drop the rest to assumptions.

## 3. Ask

All questions in one message, numbered, highest impact first, in the owner's language (CLAUDE.md)
and terms, without technical vocabulary. End the message with a line saying the owner can answer
"per the recommendations" or name only the points they disagree with. Each question has these
parts, labeled in the owner's language:

- **Question:** the question itself, one sentence.
- **Why it matters:** what depends on it.
- **Options:** two or three concrete options.
- **Recommendation:** the option you recommend and why.
- **What changes for the user:** how each option looks to the user.

If the request has no product questions left after sorting, say so and go straight to the spec.

## 4. Write `work/{feature}/spec.md`

In the owner's language, addressed to the owner, with these sections (headings translated):

```markdown
# <Feature>

## Why
The user's problem and the expected effect.

## What the user sees
Scenarios step by step, including the empty state, interruptions, and failures the user can hit.

## Acceptance criteria
Testable statements: what must happen and how to check it.

## Out of scope
What this feature explicitly does not do.

## Owner decisions
Question → answer, date.

## Assumptions
Product decisions taken by default; the owner can change any of them.
```

## 5. Check from the implementer's side

Run `reviewer` in spec mode on the spec. Fix what it finds: one round, a second only on the
changed parts. A finding that needs a product choice becomes a question to the owner within the
five-question limit, or an assumption.

## 6. Hand over

Give the owner a short summary in their language: what will be built, decisions taken,
assumptions. The technical brief follows with the `engineering-design` skill.
