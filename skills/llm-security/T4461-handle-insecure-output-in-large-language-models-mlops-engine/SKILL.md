---
name: t4461-handle-insecure-output-in-large-language-models-mlops-engi
description: You should ensure the following, no matter what type of vulnerability could result from an insecure output of a Large Language Models (LLM): - Avoid using functions that directly pass LLM outputs to privileged functions, such as system comm
---

# T4461: Handle insecure output in Large Language Models (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4461](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4461/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

You should ensure the following, no matter what type of vulnerability could result from an insecure output of a Large Language Models (LLM):

- Avoid using functions that directly pass LLM outputs to privileged functions, such as system commands, database queries, or HTML content.

### Implement secure output handling frameworks (Prompt-engineering)

- Develop and enforce frameworks prohibiting the direct passing of LLM outputs to privileged functions.

- Integrate intermediary layers that thoroughly vet and sanitize the outputs before interacting with critical system components like system commands, database queries, or HTML content.

## Success Criteria

- The control "Handle insecure output in Large Language Models (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
