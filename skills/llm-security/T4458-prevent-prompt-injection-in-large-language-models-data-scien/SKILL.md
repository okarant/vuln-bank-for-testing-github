---
name: t4458-prevent-prompt-injection-in-large-language-models-data-sci
description: To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy: - Avoid insecure functions that could be exploited through the LLM and use secure alternatives wherever possible. ### Develop and vali
---

# T4458: Prevent prompt injection in Large Language Models (Data Scientist)

**Category:** ML_CODE  
**SD Elements:** [T4458](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4458/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy:

- Avoid insecure functions that could be exploited through the LLM and use secure alternatives wherever possible.

### Develop and validate secure function libraries (Prompt-engineering)

- Create a set of secure function libraries that can be safely used with LLMs.

- Identify and validate secure alternatives to commonly exploited functions, ensuring these alternatives are against prompt injection attacks.

- Regularly update and test these libraries as part of the prompt engineering process.

## Success Criteria

- The control "Prevent prompt injection in Large Language Models (Data Scientist)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
