---
name: t4466-prevent-large-language-model-denial-of-service-project-man
description: To protect a Large Language Model against denial-of-service attacks, ensure the following: - Educate your development team about the potential for DoS attacks on LLMs and provide them with guidelines for the secure implementation and mainte
---

# T4466: Prevent Large Language Model denial of service (Project Manager)

**Category:** ML_CODE  
**SD Elements:** [T4466](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4466/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect a Large Language Model against denial-of-service attacks, ensure the following:

- Educate your development team about the potential for DoS attacks on LLMs and provide them with guidelines for the secure implementation and maintenance of these systems.

### Establish incident response and mitigation protocols (Prompt-engineering)

- Develop and implement incident response and mitigation protocols to address and recover from denial-of-service (DoS) attacks on Large Language Models.

- Train the development team on these protocols and conduct regular simulations to ensure readiness. This will help maintain system integrity and availability during fine-tuning.

## Success Criteria

- The control "Prevent Large Language Model denial of service (Project Manager)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
