---
name: t4836-implement-verification-and-fact-checking-to-mitigate-misin
description: Implement safeguards on all LLM-generated content to detect, prevent, or correct misinformation before it is distributed. This can be achieved by: - Integrate fact-checking mechanisms that compare model outputs against trusted knowledge bas
---

# T4836: Implement verification and fact-checking to mitigate misinformation

**Category:** ML_CODE  
**SD Elements:** [T4836](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4836/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

Implement safeguards on all LLM-generated content to detect, prevent, or correct misinformation before it is distributed. This can be achieved by:

  - Integrate fact-checking mechanisms that compare model outputs against trusted knowledge bases and authoritative sources.
  - Use retrieval-augmented generation (RAG) to ground responses in verified external datasets and reduce hallucinations.
  - Apply confidence scoring to label potentially unreliable outputs and provide users with indicators of certainty.
  - Cross-validate outputs using multiple independent model runs or ensemble methods to detect inconsistencies.
  - Implement human-in-the-loop review for high-risk content areas, such as medical, legal, or financial information, to ensure accuracy.

## Success Criteria

- The control "Implement verification and fact-checking to mitigate misinformation" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
