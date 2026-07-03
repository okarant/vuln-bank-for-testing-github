---
name: t744-protect-pseudonymized-personal-information
description: Protect pseudonymized personal information
---

# T744: Protect pseudonymized personal information

**Category:** CODE_FIX
**SD Elements:** [T744](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T744/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# If you are a [controller](/library/glossary/G33/) or a service provider, implement pseudonymization before giving the data to the [processor](/library/glossary/G34/). If your application pseudonymizes personal information, follow these guidelines to protect the identity of individuals associated wit
```

**Success Criteria:**
- The control described by T744 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
