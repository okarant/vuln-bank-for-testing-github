---
name: t4480-design-secure-plugins-for-large-language-models-mlops-engi
description: To ensure the secure design and use of plugins in Large Language Models (LLMs), use the following steps: - Ensure no potentially harmful methods are invoked when freeform inputs are accepted. - Use appropriate authentication identities, suc
---

# T4480: Design secure plugins for Large Language Models (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4480](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4480/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To ensure the secure design and use of plugins in Large Language Models (LLMs), use the following steps: 

- Ensure no potentially harmful methods are invoked when freeform inputs are accepted.

- Use appropriate authentication identities, such as OAuth2, for effective authorization and access control. Consider API Keys for custom authorization decisions reflecting the plugin route rather than the default interactive user.

- Perform taint tracing on all plugin content when chaining, ensuring the plugin is called with an authorization level corresponding to the lowest authorization of any plugin that has provided input to the LLM prompt.

### Implement secure authorization and tracing protocols (Prompt-engineering)

- Develop and enforce secure authorization protocols, utilizing OAuth2 and API Keys for effective access control specific to plugin routes.

- Implement taint tracing mechanisms to monitor all plugin content, ensuring that plugins are invoked with the appropriate level of authorization, corresponding to the lowest authorization level of any preceding plugin in the chain.

- Ensure that no potentially harmful methods are invoked when handling freeform inputs, maintaining high security standards throughout the process.

## Success Criteria

- The control "Design secure plugins for Large Language Models (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
