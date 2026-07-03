---
name: t4484-mitigate-excessive-agency-in-large-language-models-ai-ml-d
description: Mitigate excessive agency in Large Language Models (AI/ML Developer)
---

# T4484: Mitigate excessive agency in Large Language Models (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4484](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4484/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# To mitigate and prevent excessive agency in Large Language Models (LLMs), follow these best practices: - Limit the plugins/tools that LLM agents can call to only the minimum necessary functions. - Limit the functions implemented in LLM plugins/tools to the minimum necessary. - Avoid open-ended funct
```

**Success Criteria:**
- The control described by T4484 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
