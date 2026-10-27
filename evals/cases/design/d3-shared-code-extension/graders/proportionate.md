---
type: llm
---

PASS if the proposed design is proportionate: every new type, protocol, layer, module, dependency or configuration it introduces has a stated current reason, and it does not add generic frameworks, plugin/strategy hierarchies, protocols with a single implementation, repositories-over-repositories, or extra modules "for the future" without a concrete current need.
FAIL if the design introduces such speculative generality or layers without a current reason (for example a generic GoalEngine/strategy protocol for two goal kinds, a sync engine before a server exists, several new modules for a few files).
