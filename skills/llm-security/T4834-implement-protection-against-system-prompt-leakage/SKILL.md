---
name: t4834-implement-protection-against-system-prompt-leakage
description: Implement security controls to prevent unauthorized disclosure of system prompts, internal instructions, or confidential directives embedded in LLM applications. This can be achieved by: - Separate system and user inputs to ensure prompts c
---

# T4834: Implement protection against system prompt leakage

**Category:** ML_CODE  
**SD Elements:** [T4834](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4834/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

Implement security controls to prevent unauthorized disclosure of system prompts, internal instructions, or confidential directives embedded in LLM applications. This can be achieved by:

  - Separate system and user inputs to ensure prompts controlling model behavior are never exposed to user queries.
  - Use prompt obfuscation techniques such as encoding, encryption, or dynamic prompt generation to prevent direct extraction.
  - Apply strict access controls to limit who can modify or view system-level instructions within the model.
  - Implement response filtering to detect and block any unintended exposure of system prompts before delivering output to users.

## Success Criteria

- The control "Implement protection against system prompt leakage" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
