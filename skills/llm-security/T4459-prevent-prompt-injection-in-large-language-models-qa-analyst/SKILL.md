---
name: t4459-prevent-prompt-injection-in-large-language-models-qa-analy
description: To protect your Large Language Models (LLM) against prompt injection attacks, follow the following strategy: - Implement visual alerts to highlight potentially untrustworthy responses to the user, thus raising caution and encouraging user v
---

# T4459: Prevent prompt injection in Large Language Models (QA Analyst)

**Category:** ML_CODE  
**SD Elements:** [T4459](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4459/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect your Large Language Models (LLM) against prompt injection attacks, follow the following strategy:

- Implement visual alerts to highlight potentially untrustworthy responses to the user, thus raising caution and encouraging user verification.

### Design and execute prompt injection attack test cases (Prompt-engineering)

- Develop and run comprehensive test cases explicitly targeting prompt injection attack scenarios.

- These test cases should assess the model's responses and identify weaknesses.

- Ensure that the model handles potential injections gracefully and provides visual alerts in accordance with the defined strategy, raising user awareness and encouraging verification.

## Success Criteria

- The control "Prevent prompt injection in Large Language Models (QA Analyst)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
