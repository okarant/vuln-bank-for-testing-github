---
name: t604-implement-a-consent-withdrawal-mechanism
description: Implement a consent withdrawal mechanism
---

# T604: Implement a consent withdrawal mechanism

**Category:** CODE_FIX
**SD Elements:** [T604](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T604/)
**Priority:** P10

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Act on the consent withdrawal if you are a [controller](/library/glossary/G33/) or a [processor](/library/glossary/G34/) assigned to act on behalf of the controller. Communicate the withdrawal mechanism to your processors or sub-processors. If your application needs to collect personal information t
```

**Success Criteria:**
- The control described by T604 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
