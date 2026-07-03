---
name: t184-perform-authorization-checks-on-restful-web-services
description: Perform authorization checks on RESTful web services
---

# T184: Perform authorization checks on RESTful web services

**Category:** CODE_FIX
**SD Elements:** [T184](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T184/)
**Priority:** P9

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Consider the following points when performing authorization checks on RESTful web services: - Ensure that the user accessing the web service has sufficient permissions to access the URL and uses the HTTP verb. - For example, a user may have access to GET a resource, but may not have permission to DE
```

**Success Criteria:**
- The control described by T184 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
