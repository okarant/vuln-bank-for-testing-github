---
name: t4467-prevent-large-language-model-denial-of-service-mlops-engin
description: To protect a Large Language Model against denial-of-service attacks, ensure the following: - Limit the resources used per request or step, ensuring that requests requiring intensive computations execute slower. - Enforce strict API rate lim
---

# T4467: Prevent Large Language Model denial of service (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4467](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4467/)  
**Priority:** 7  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect a Large Language Model against denial-of-service attacks, ensure the following:

- Limit the resources used per request or step, ensuring that requests requiring intensive computations execute slower.

- Enforce strict API rate limiting to control the number of requests a particular user or IP address can make within a given timeframe.

### Implement adaptive resource management and rate limiting (Prompt-engineering)

- Develop adaptive resource management systems that dynamically allocate and limit computational resources per request based on current load and past usage patterns.

- Implement API rate limiting mechanisms that not only set fixed limits but adjust in real-time to detect and mitigate suspicious spikes in traffic, ensuring protection against denial-of-service attacks.

## Success Criteria

- The control "Prevent Large Language Model denial of service (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
