---
name: t4465-prevent-training-data-poisoning-in-large-language-models-a
description: Prevent training data poisoning in Large Language Models (AI/ML Developer)
---

# T4465: Prevent training data poisoning in Large Language Models (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4465](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4465/)
**Priority:** P7

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# To ensure the integrity of the training data and protect the model against poisoning attacks, use the following strategy: - Design separate models for different use cases to ensure accurate AI output.
```

**Success Criteria:**
- The control described by T4465 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
