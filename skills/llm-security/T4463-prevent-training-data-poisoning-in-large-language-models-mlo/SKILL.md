---
name: t4463-prevent-training-data-poisoning-in-large-language-models-m
description: To ensure the integrity of the training data and protect the model against poisoning attacks, use the following strategy: - Implement sufficient sandboxing to prevent the model from accessing unintended data sources. - Minimize the effect o
---

# T4463: Prevent training data poisoning in Large Language Models (MLOps Engineer)

**Category:** ML_DOC  
**SD Elements:** [T4463](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4463/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Why Not Directly Code-Fixable in This Repository

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To ensure the integrity of the training data and protect the model against poisoning attacks, use the following strategy:

- Implement sufficient sandboxing to prevent the model from accessing unintended data sources.

- Minimize the effect of outliers or adversarial training, and include an auto poisoning technique as part of an "MLSecOps" approach.

## Success Criteria

- The requirement "Prevent training data poisoning in Large Language Models (MLOps Engineer)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
