---
name: t4460-handle-insecure-output-in-large-language-models-ai-ml-deve
description: You should ensure the following, no matter what type of vulnerability could result from an insecure output of a Large Language Models (LLM): - Implement strong sanitization measures on LLM output before passing it to backend, privileged, or
---

# T4460: Handle insecure output in Large Language Models (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4460](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4460/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

You should ensure the following, no matter what type of vulnerability could result from an insecure output of a Large Language Models (LLM):

- Implement strong sanitization measures on LLM output before passing it to backend, privileged, or client-side functions. Always presume the output to be untrusted and potentially harmful.

### Develop output sanitization and validation pipelines (Prompt-engineering)

- Create and integrate dedicated pipelines that sanitize and validate the LLM's output before interacting with backend, privileged, or client-side functions.

- These pipelines should treat all outputs as potentially harmful, ensuring comprehensive checks and cleansing to mitigate risks associated with insecure outputs.

## Success Criteria

- The control "Handle insecure output in Large Language Models (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
