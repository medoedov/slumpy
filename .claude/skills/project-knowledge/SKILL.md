---
name: project-knowledge
description: |
  How this project is built: architecture, conventions, configuration, skills and pipelines,
  deployment, and operations. Use whenever the project itself is changed, extended, debugged,
  deployed, or explained, including small fixes and questions about how something in it works.
---

# Project Knowledge

Each fact has one owner file below; update that file instead of repeating the fact elsewhere.
When a fact or status changes, search the repository (README, `work/`, ADRs, CLAUDE.md, `.claude/`) for other
copies and update them or replace them with a link to the section that states the fact, keeping
its status (hypothesis or approved).

**Status of facts.** Product facts are hypotheses, marked as such, until the owner approves them;
CLAUDE.md names where the product draft lives. Technical
decisions live in ADRs under [docs/decisions/](../../../docs/decisions/); where this skill and an
ADR disagree, the ADR wins and this skill is fixed.

## References

- **[project.md](references/project.md)** - product overview, audience, principles, feature
  hypotheses, open product decisions.
- **[architecture.md](references/architecture.md)** - stack, modules, architecture map, data
  rules, planned entities, external integrations.
- **[patterns.md](references/patterns.md)** - git workflow, verification, business invariants
  and product rules (hypotheses).
- **[deployment.md](references/deployment.md)** - build and delivery path, accounts, environments.
- **[ux-guidelines.md](references/ux-guidelines.md)** - interface language, tone, glossary,
  accessibility baseline.

## Decisions and lessons

- **Decision index:** [docs/decisions/README.md](../../../docs/decisions/README.md). Read the
  relevant ADR before changing anything it covers.
- **Lessons (traps already hit):** [docs/lessons.md](../../../docs/lessons.md). Check it before
  working in an area it lists.

## When finishing a feature

Update the architecture map in [architecture.md](references/architecture.md), the decision index,
and any business invariant the feature changed. Move the owner's decisions from the spec into the
file that owns each fact, marked as confirmed with the date, so the owner is not asked again. Move
`work/{feature}/` to `work/completed/`.
