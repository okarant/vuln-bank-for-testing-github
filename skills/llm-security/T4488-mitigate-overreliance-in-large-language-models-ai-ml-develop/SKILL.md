---
name: t4488-mitigate-overreliance-in-large-language-models-ai-ml-devel
description: To mitigate the risks associated with overreliance and hallucinations in Large Language Models (LLMs), follow these steps: - Implement techniques such as self-consistency or voting to filter out inconsistent or inaccurate responses. - Speci
---

# T4488: Mitigate overreliance in Large Language Models (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4488](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4488/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate the risks associated with overreliance and hallucinations in Large Language Models (LLMs), follow these steps:

- Implement techniques such as self-consistency or voting to filter out inconsistent or inaccurate responses.

- Specify automatic validation mechanisms that can cross-check the outputs of the LLM against known facts or data. This can provide an additional layer of security to mitigate the risks associated with hallucinations.

- Ensure fine-tuning, prompt engineering, parameter efficient tuning (PET), full model tuning, and other methods to enhance the performance of the LLM. Specialized models are typically more reliable than generic pre-trained ones.

## Success Criteria

- The control "Mitigate overreliance in Large Language Models (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
