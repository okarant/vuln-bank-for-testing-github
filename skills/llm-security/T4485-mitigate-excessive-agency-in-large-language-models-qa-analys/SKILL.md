---
name: t4485-mitigate-excessive-agency-in-large-language-models-qa-anal
description: To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices: - Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the conte
---

# T4485: Mitigate excessive agency in Large Language Models (QA Analyst)

**Category:** ML_CODE  
**SD Elements:** [T4485](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4485/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices:

- Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user and with the minimum privileges necessary.

### Validate user authorization and security scope compliance (Prompt-engineering)

- Develop and execute test cases that track and validate user authorization and security scope throughout the LLM's interaction with downstream systems.

- Ensure that actions are executed in the context of the specific user and with the minimum necessary privileges.

- Audit these processes to verify compliance with the defined best practices, and identify any deviations or potential vulnerabilities that need addressing.

## Success Criteria

- The control "Mitigate excessive agency in Large Language Models (QA Analyst)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
