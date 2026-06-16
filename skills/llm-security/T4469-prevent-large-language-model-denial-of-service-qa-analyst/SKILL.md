---
name: t4469-prevent-large-language-model-denial-of-service-qa-analyst
description: To protect a Large Language Model against denial-of-service attacks, ensure the following: - Monitor the resource utilization of your LLM systems to detect abnormal usage or patterns that could indicate an ongoing DoS attack. ### Develop co
---

# T4469: Prevent Large Language Model denial of service (QA Analyst)

**Category:** ML_CODE  
**SD Elements:** [T4469](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4469/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect a Large Language Model against denial-of-service attacks, ensure the following:

- Monitor the resource utilization of your LLM systems to detect abnormal usage or patterns that could indicate an ongoing DoS attack.

### Develop comprehensive resource utilization test scenarios (Prompt-engineering)

- Create and execute detailed test scenarios designed to monitor resource utilization under various conditions.

- These scenarios should simulate different usage patterns and identify any anomalies that could indicate potential DoS attacks.

- Ensure these tests are continuously run and analyzed to provide timely detection and feedback for prompt engineering processes.

## Success Criteria

- The control "Prevent Large Language Model denial of service (QA Analyst)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
