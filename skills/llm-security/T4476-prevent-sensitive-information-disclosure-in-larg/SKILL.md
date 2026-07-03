---
name: t4476-prevent-sensitive-information-disclosure-in-large-language
description: Prevent sensitive information disclosure in Large Language Models (AI/ML Developer)
---

# T4476: Prevent sensitive information disclosure in Large Language Models (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4476](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4476/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# To prevent information disclosure in Large Language Models (LLMs), opt for the following steps: - Avoid using any sensitive information that, if disclosed, could pose a risk to users or the system.
```

**Success Criteria:**
- The control described by T4476 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
