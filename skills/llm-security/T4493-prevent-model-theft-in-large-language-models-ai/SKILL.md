---
name: t4493-prevent-model-theft-in-large-language-models-ai-ml-develop
description: Prevent model theft in Large Language Models (AI/ML Developer)
---

# T4493: Prevent model theft in Large Language Models (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4493](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4493/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# Besides securing your infrastructure, you can prevent Large Language Models (LLM) theft by following these recommendations: - Implement training techniques to detect extraction queries.
```

**Success Criteria:**
- The control described by T4493 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
