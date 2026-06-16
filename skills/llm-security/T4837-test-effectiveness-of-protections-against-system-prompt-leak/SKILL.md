---
name: t4837-test-effectiveness-of-protections-against-system-prompt-le
description: Ensure that security controls effectively prevent the unauthorized disclosure of system prompts, internal instructions, or confidential directives while maintaining LLM functionality and performance. - Test access control enforcement by sim
---

# T4837: Test effectiveness of protections against system prompt leakage

**Category:** ML_CODE  
**SD Elements:** [T4837](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4837/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

Ensure that security controls effectively prevent the unauthorized disclosure of system prompts, internal instructions, or confidential directives while maintaining LLM functionality and performance.

  - Test access control enforcement by simulating unauthorized modification attempts to system prompts and reviewing access logs.
  - Measure impact on model performance to confirm that security controls do not degrade response accuracy or usability.

## Success Criteria

- The control "Test effectiveness of protections against system prompt leakage" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
