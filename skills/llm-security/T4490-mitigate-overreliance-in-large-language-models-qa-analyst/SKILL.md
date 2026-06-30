---
name: t4490-mitigate-overreliance-in-large-language-models-qa-analyst
description: To mitigate the risks associated with overreliance and hallucination in Large Language Models (LLMs), follow these steps: - Design APIs and user interfaces that encourage LLMs' responsible and safe use. Measures can include content filters,
---

# T4490: Mitigate overreliance in Large Language Models (QA Analyst)

**Category:** ML_CODE  
**SD Elements:** [T4490](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4490/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate the risks associated with overreliance and hallucination in Large Language Models (LLMs), follow these steps:

- Design APIs and user interfaces that encourage LLMs' responsible and safe use. Measures can include content filters, warnings about potential inaccuracies, and clear labelling of AI-generated content.

## Success Criteria

- The control "Mitigate overreliance in Large Language Models (QA Analyst)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
