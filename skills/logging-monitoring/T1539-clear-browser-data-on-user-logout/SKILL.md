---
name: t1539-clear-browser-data-on-user-logout
description: Clear browser data on user logout
---

# T1539: Clear browser data on user logout

**Category:** CODE_FIX
**SD Elements:** [T1539](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1539/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Configure your application to send the `Clear-Site-Data` header when the user logs out. Configure the header using the following directives: * `"cache"`: clear all cached files for this origin * `"cookies"`: clear all cookies for the domain (both HTTP and HTTPS) * `"storage"`: clear all locally stor
```

**Success Criteria:**
- The control described by T1539 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
