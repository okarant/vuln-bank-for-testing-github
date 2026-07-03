---
name: t378-authorize-every-request-for-data-objects
description: Authorize every request for data objects
---

# T378: Authorize every request for data objects

**Category:** CODE_FIX
**SD Elements:** [T378](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T378/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Every direct object reference should be governed by session authentication and a permission check. Where objects (e.g. files) are served via the web, prefer using a web application framework to host and manage them instead of serving directly from the web server. Follow these implementation steps: *
```

**Success Criteria:**
- The control described by T378 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
