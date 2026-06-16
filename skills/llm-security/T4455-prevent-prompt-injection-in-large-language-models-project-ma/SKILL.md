---
name: t4455-prevent-prompt-injection-in-large-language-models-project
description: To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy: - Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function-level permissions. 
---

# T4455: Prevent prompt injection in Large Language Models (Project Manager)

**Category:** ML_CODE  
**SD Elements:** [T4455](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4455/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy:

- Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function-level permissions. 

- Follow the principle of least privilege by restricting the LLM to only the minimum level of access necessary for its intended operations.

- Add a human in the loop for extended functionality. When performing privileged operations, such as sending or deleting emails, the application requires the user to approve the action first. This reduces the opportunity for indirect prompt injections to lead to unauthorized actions on behalf of the user without their knowledge or consent.

- Establish clear trust boundaries between the LLM, external sources, and extensible modules like plugins. Treat the LLM as an untrusted user and maintain final user control on decision-making processes.

### Conduct scenario-based prompt injection simulations (Prompt-engineering)

- Design and execute a series of scenario-based simulations to test the model's resilience to different prompt injection attacks. Use these simulations to identify vulnerabilities and iterate on prompt engineering strategies.

## Success Criteria

- The control "Prevent prompt injection in Large Language Models (Project Manager)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
