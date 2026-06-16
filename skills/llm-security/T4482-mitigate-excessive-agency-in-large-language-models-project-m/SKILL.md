---
name: t4482-mitigate-excessive-agency-in-large-language-models-project
description: To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices: - Use human-in-the-loop control to require a human to approve all actions before they are taken. ### Implement human-in-the-loop review p
---

# T4482: Mitigate excessive agency in Large Language Models (Project Manager)

**Category:** ML_CODE  
**SD Elements:** [T4482](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4482/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices:

- Use human-in-the-loop control to require a human to approve all actions before they are taken.

### Implement human-in-the-loop review protocols (Prompt-engineering)

- Establish comprehensive human-in-the-loop review protocols that mandate human approval for all actions proposed by the LLM.

- Define clear steps and responsibilities for human reviewers to follow in assessing and approving actions and integrate these protocols into the workflow.

- Train and update the reviewing team to ensure consistency and security in decision-making processes.

## Success Criteria

- The control "Mitigate excessive agency in Large Language Models (Project Manager)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
