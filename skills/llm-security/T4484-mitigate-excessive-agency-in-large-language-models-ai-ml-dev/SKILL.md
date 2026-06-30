---
name: t4484-mitigate-excessive-agency-in-large-language-models-ai-ml-d
description: To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices: - Limit the plugins/tools that LLM agents can call to only the minimum necessary functions. - Limit the functions implemented in LLM plug
---

# T4484: Mitigate excessive agency in Large Language Models (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4484](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4484/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices:

- Limit the plugins/tools that LLM agents can call to only the minimum necessary functions.

- Limit the functions implemented in LLM plugins/tools to the minimum necessary.

- Avoid open-ended functions where possible and use plugins/tools with more granular functionality.

### Develop plugins with granular and restricted functionality (Prompt-engineering)

- Design and implement plugins/tools for LLM agents that offer very specific and necessary functionalities, avoiding open-ended or overly broad functions.

- Restrict the LLM agents to calling only these essential plugins/tools, ensuring that each function provided is both minimal and precise.

- Regularly review and refine the available functions to ensure they remain aligned with the latest security standards and operational needs.

## Success Criteria

- The control "Mitigate excessive agency in Large Language Models (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
