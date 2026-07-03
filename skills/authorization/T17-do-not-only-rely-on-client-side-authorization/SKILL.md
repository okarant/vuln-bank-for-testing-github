---
name: t17-do-not-only-rely-on-client-side-authorization
description: Do not only rely on client-side authorization
---

# T17: Do not only rely on client-side authorization

**Category:** CODE_FIX
**SD Elements:** [T17](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T17/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Do not only rely on client-side code to authorize users, such as a JavaScript library, because users can bypass client-side security controls. Authorization checks on a user should be done on the server itself, or users can forcibly browse or guess the URL of a page that normally requires authorizat
```

**Success Criteria:**
- The control described by T17 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
