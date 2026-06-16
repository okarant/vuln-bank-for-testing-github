---
name: t4474-prevent-sensitive-information-disclosure-in-large-language
description: To prevent information disclosure in a Large Language Models (LLMs), opt for the following steps: - Establish and enforce data handling policies to prevent sensitive user data from entering the training data for the model. - Ensure adequate
---

# T4474: Prevent sensitive information disclosure in Large Language Models (Project Manager)

**Category:** ML_CODE  
**SD Elements:** [T4474](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4474/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To prevent information disclosure in a Large Language Models (LLMs), opt for the following steps:

- Establish and enforce data handling policies to prevent sensitive user data from entering the training data for the model.

- Ensure adequate terms of use policies are in place to inform users about data handling practices and offer the ability to opt out of data collection for model training.

### Implement continuous data sanitization and monitoring protocols (RAG)

- Develop continuous data sanitization processes to remove sensitive information from training datasets before they enter the RAG system.

- Implement monitoring protocols to ensure adherence to data handling policies.

## Success Criteria

- The control "Prevent sensitive information disclosure in Large Language Models (Project Manager)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
