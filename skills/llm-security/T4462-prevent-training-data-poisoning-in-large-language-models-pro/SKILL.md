---
name: t4462-prevent-training-data-poisoning-in-large-language-models-p
description: To ensure the integrity of the training data and protect the model against poisoning attacks, use the following strategy: - Verify the supply chain of the training data. - Check the legitimacy of data sources and their content during the tr
---

# T4462: Prevent training data poisoning in Large Language Models (Project Manager)

**Category:** ML_DOC  
**SD Elements:** [T4462](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4462/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Why Not Directly Code-Fixable in This Repository

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To ensure the integrity of the training data and protect the model against poisoning attacks, use the following strategy:

- Verify the supply chain of the training data.

- Check the legitimacy of data sources and their content during the training and fine-tuning processes.

## Success Criteria

- The requirement "Prevent training data poisoning in Large Language Models (Project Manager)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
