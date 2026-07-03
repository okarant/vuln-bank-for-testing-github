---
name: t4468-prevent-large-language-models-denial-of-service-ai-ml-deve
description: Prevent Large Language Models denial of service (AI/ML Developer)
---

# T4468: Prevent Large Language Models denial of service (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4468](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4468/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# To protect a Large Language Model against denial-of-service attacks, ensure the following: - Implement robust input validation and sanitization mechanisms to filter out user inputs. - Set strict input constraints based on your LLM's context window to avoid overloading the system and exhausting its r
```

**Success Criteria:**
- The control described by T4468 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
