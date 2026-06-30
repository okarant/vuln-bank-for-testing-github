---
name: t4472-protect-large-language-models-against-supply-chain-vulnera
description: To protect Large Language Models (LLMs) against supply chain vulnerabilities, ensure the following: - Use model and code signing to ensure authenticity when using external models and suppliers. - Update and patch all components regularly, i
---

# T4472: Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer)

**Category:** ML_CODE  
**SD Elements:** [T4472](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4472/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect Large Language Models (LLMs) against supply chain vulnerabilities, ensure the following:

- Use model and code signing to ensure authenticity when using external models and suppliers.

- Update and patch all components regularly, including APIs and the underlying models.

### Implement dependency and provenance tracking (RAG)

- Develop and integrate dependency tracking mechanisms to monitor changes and updates in external models, APIs, and datasets.

- Implement provenance tracking for models and code to trace all versions and their origins within the RAG infrastructure.

## Success Criteria

- The control "Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
