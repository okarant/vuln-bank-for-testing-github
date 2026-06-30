---
name: t4833-test-fine-tuning-alignement-of-generative-ai-models
description: Validate that fine-tuning processes reinforce safety, security, and content policies. - Ensure that the dataset used for fine-tuning promotes responsible outputs and aligns with safety guidelines. - Verify that reinforcement learning from h
---

# T4833: Test fine-tuning alignement of generative AI models

**Category:** ML_DOC  
**SD Elements:** [T4833](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4833/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Why Not Directly Code-Fixable in This Repository

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Validate that fine-tuning processes reinforce safety, security, and content policies.

  - Ensure that the dataset used for fine-tuning promotes responsible outputs and aligns with safety guidelines.
  - Verify that reinforcement learning from human feedback (RLHF) or AI feedback improves model alignment.
  - Test model resistance to adversarial prompts post-fine-tuning. The model should effectively rejects adversarial prompts and maintains safe responses.

## Success Criteria

- The requirement "Test fine-tuning alignement of generative AI models" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
