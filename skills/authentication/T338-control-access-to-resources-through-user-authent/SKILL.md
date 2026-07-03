---
name: t338-control-access-to-resources-through-user-authentication-and
description: Control access to resources through user authentication and authorization
---

# T338: Control access to resources through user authentication and authorization

**Category:** CODE_FIX
**SD Elements:** [T338](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T338/)
**Priority:** P7

**Code to Fix:**
```python
# auth.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in auth.py:
# Use the following guidelines for controlling access to resources with user authentication and authorization: - Implement a user authentication/authorization system that enforces access control policies. - Users include human, software process, or device. - A typical authentication/authorization syst
```

**Success Criteria:**
- The control described by T338 is enforced in auth.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
