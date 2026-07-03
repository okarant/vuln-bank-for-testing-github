---
name: t1468-encrypt-sensitive-data-at-rest-in-the-browser
description: Encrypt sensitive data at rest in the browser
---

# T1468: Encrypt sensitive data at rest in the browser

**Category:** CODE_FIX
**SD Elements:** [T1468](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1468/)
**Priority:** P9

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Avoid using browser-based storage mechanisms to store sensitive data. However, if you can justify storing data in the browser, that data needs to be encrypted. The mechanism for encrypting data in the browser is driven by the requirement to gain access to the data while the application is offline (i
```

**Success Criteria:**
- The control described by T1468 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
