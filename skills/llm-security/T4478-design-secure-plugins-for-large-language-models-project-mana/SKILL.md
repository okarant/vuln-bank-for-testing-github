---
name: t4478-design-secure-plugins-for-large-language-models-project-ma
description: To ensure the secure design and use of plugins in Large Language Models (LLMs), use the following steps: - Avoid plugin chaining with each user input and prevent sensitive plugins from being called after any other plugin. ### Establish secu
---

# T4478: Design secure plugins for Large Language Models (Project Manager)

**Category:** ML_CODE  
**SD Elements:** [T4478](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4478/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To ensure the secure design and use of plugins in Large Language Models (LLMs), use the following steps: 

- Avoid plugin chaining with each user input and prevent sensitive plugins from being called after any other plugin.

### Establish secure plugin integration protocols (Prompt-engineering)

- Develop and implement protocols that ensure secure integration of plugins within LLMs. These protocols should include guidelines for avoiding plugin chaining, particularly with sensitive plugins, and rules to prevent the sequential calling of sensitive plugins following any other plugin.

- Conduct regular code reviews and security assessments to ensure compliance with these protocols and update them as necessary to address emerging threats.

## Success Criteria

- The control "Design secure plugins for Large Language Models (Project Manager)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
