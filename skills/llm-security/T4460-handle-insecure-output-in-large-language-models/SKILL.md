---
name: t4460-handle-insecure-output-in-large-language-models-ai-ml-deve
description: Handle insecure output in Large Language Models (AI/ML Developer)
---

# T4460: Handle insecure output in Large Language Models (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4460](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4460/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# You should ensure the following, no matter what type of vulnerability could result from an insecure output of a Large Language Models (LLM): - Implement strong sanitization measures on LLM output before passing it to backend, privileged, or client-side functions. Always presume the output to be untr
```

**Success Criteria:**
- The control described by T4460 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
