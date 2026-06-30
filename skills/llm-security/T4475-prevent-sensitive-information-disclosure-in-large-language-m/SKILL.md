---
name: t4475-prevent-sensitive-information-disclosure-in-large-language
description: To prevent information disclosure in Large Language Models (LLMs), opt for the following steps: - Limit the model's access to external data sources, and enforce strict access control mechanisms. ### Implement secure data ingestion and acces
---

# T4475: Prevent sensitive information disclosure in Large Language Models (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4475](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4475/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To prevent information disclosure in Large Language Models (LLMs), opt for the following steps:

- Limit the model's access to external data sources, and enforce strict access control mechanisms.

### Implement secure data ingestion and access controls (RAG)

- Develop and enforce secure data ingestion processes to filter and anonymize incoming data before processing in the RAG system.

- Implement granular access controls, including role-based permissions and multi-factor authentication, to safeguard data and model access.

## Success Criteria

- The control "Prevent sensitive information disclosure in Large Language Models (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
