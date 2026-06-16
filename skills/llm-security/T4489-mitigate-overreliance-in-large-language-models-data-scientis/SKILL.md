---
name: t4489-mitigate-overreliance-in-large-language-models-data-scient
description: To mitigate the risks associated with overreliance and hallucination in Large Language Models (LLMs), follow these steps: - Cross-verify the information provided by the LLM with trusted external sources. - Divide complex tasks into smaller,
---

# T4489: Mitigate overreliance in Large Language Models (Data Scientist)

**Category:** ML_CODE  
**SD Elements:** [T4489](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4489/)  
**Priority:** 6  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate the risks associated with overreliance and hallucination in Large Language Models (LLMs), follow these steps:

- Cross-verify the information provided by the LLM with trusted external sources.

- Divide complex tasks into smaller, manageable subtasks, and assign these to different agents. This strategy can reduce the complexity of tasks and limit the occurrence of hallucinations.

## Success Criteria

- The control "Mitigate overreliance in Large Language Models (Data Scientist)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
