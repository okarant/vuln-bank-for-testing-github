---
name: t4479-design-secure-plugins-for-large-language-models-ai-ml-deve
description: To ensure a secure design and use of plugins in Large Language Models (LLMs), use the following steps: - Enforce strict parameterized input wherever possible, including input type and range checks. - Design plugins to minimize the impact of
---

# T4479: Design secure plugins for Large Language Models (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4479](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4479/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To ensure a secure design and use of plugins in Large Language Models (LLMs), use the following steps: 

- Enforce strict parameterized input wherever possible, including input type and range checks.

- Design plugins to minimize the impact of any insecure input parameter exploitation.

### Implement parameterized input and safeguards (Prompt-engineering)

- Develop and enforce strict parameterized input protocols for all plugins, ensuring thorough type and range checks.

- Design plugins with built-in safeguards that minimize the impact of any exploitation of insecure input parameters, such as incorporating error handling and fail-safe mechanisms to prevent cascading failures or system breaches.

- Review and update these plugins to maintain high security standards.

## Success Criteria

- The control "Design secure plugins for Large Language Models (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
