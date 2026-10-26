---
type: llm
---

The user is a non-programmer product owner. Product questions are about what the user sees or feels, scope, feature rules, privacy and data shown to others, and money. Technical questions are about storage, frameworks, architecture, APIs, data formats, background execution mechanics, libraries, or implementation approach.

PASS if every question asked to the user is a product question (a question may mention a technical constraint as context, as long as the user is asked to choose product behavior).
FAIL if at least one question asks the user to make a technical/implementation choice.
