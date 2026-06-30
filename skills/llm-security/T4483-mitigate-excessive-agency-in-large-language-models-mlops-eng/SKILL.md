---
name: t4483-mitigate-excessive-agency-in-large-language-models-mlops-e
description: To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices: - Limit the permissions that LLM plugins/tools are granted to other systems to the minimum necessary. - Log and monitor the activity of L
---

# T4483: Mitigate excessive agency in Large Language Models (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4483](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4483/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices:

- Limit the permissions that LLM plugins/tools are granted to other systems to the minimum necessary.

- Log and monitor the activity of LLM plugins/tools and downstream systems to identify where undesirable actions occur and respond accordingly.

- Implement rate-limiting to reduce the number of undesirable actions that can occur within a given period.

### Implement permission management and activity monitoring systems (Prompt-engineering)

- Design and deploy a fine-grained permission management system that ensures LLM plugins/tools are granted only the minimum necessary permissions.

- Set up comprehensive logging and monitoring systems to track the activity of LLM plugins/tools and downstream systems, enabling the identification and quick response to undesirable actions.

- Implement rate-limiting mechanisms to restrict the frequency of actions, thereby reducing the potential for excessive or undesirable activities within a specific time frame.

## Success Criteria

- The control "Mitigate excessive agency in Large Language Models (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
