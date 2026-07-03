---
name: t295-avoid-storing-unencrypted-confidential-data-without-access
description: Avoid storing unencrypted confidential data without access control mechanisms
---

# T295: Avoid storing unencrypted confidential data without access control mechanisms

**Category:** CODE_FIX
**SD Elements:** [T295](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T295/)
**Priority:** P7

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Consider the following guidelines for saving confidential data on mobile/client devices or in shared locations on the server: - Generally there are two types of confidential data that you may identify: 1. Application's secrets such as keys, proprietary data and other information that belongs to you 
```

**Success Criteria:**
- The control described by T295 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
