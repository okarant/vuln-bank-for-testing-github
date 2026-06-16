---
name: t4456-prevent-prompt-injection-in-large-language-models-mlops-en
description: To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy: - Restrict access to only what is essential for the LLM's operations. - Segregate external content from user prompts. Separate and den
---

# T4456: Prevent prompt injection in Large Language Models (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4456](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4456/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy:

- Restrict access to only what is essential for the LLM's operations.

- Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit their influence on user prompts. For example, ChatML can be used for OpenAI API calls to indicate the source of prompt input to the LLM.

### Implement continuous monitoring and alerting systems (Prompt-engineering)

- Set up continuous monitoring systems to detect real-time unusual or suspicious prompt activity.

- Implement alerting mechanisms to notify the relevant teams when potential prompt injection attempts are identified.

- This allows for immediate response and iterative fine-tuning of prompt engineering strategies to mitigate identified risks.

## Success Criteria

- The control "Prevent prompt injection in Large Language Models (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
