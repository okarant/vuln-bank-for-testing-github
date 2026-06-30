---
name: t4468-prevent-large-language-models-denial-of-service-ai-ml-deve
description: To protect a Large Language Model against denial-of-service attacks, ensure the following: - Implement robust input validation and sanitization mechanisms to filter out user inputs. - Set strict input constraints based on your LLM's context
---

# T4468: Prevent Large Language Models denial of service (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4468](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4468/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect a Large Language Model against denial-of-service attacks, ensure the following:

- Implement robust input validation and sanitization mechanisms to filter out user inputs.

- Set strict input constraints based on your LLM's context window to avoid overloading the system and exhausting its resources.

### Design context-aware input filtering and constraints (Prompt-engineering)

- Develop input filtering mechanisms that are context-aware, ensuring inputs are validated and sanitized according to the specific requirements of the LLM's context window.

- Implement strict input constraints to cap the size and complexity of user inputs, thereby preventing resource exhaustion and protecting against denial-of-service attacks.

- Update these mechanisms to adapt to new threat vectors and usage patterns.

## Success Criteria

- The control "Prevent Large Language Models denial of service (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
