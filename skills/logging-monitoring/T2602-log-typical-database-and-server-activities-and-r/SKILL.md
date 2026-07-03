---
name: t2602-log-typical-database-and-server-activities-and-related-met
description: Log typical database and server activities and related metadata
---

# T2602: Log typical database and server activities and related metadata

**Category:** CODE_FIX
**SD Elements:** [T2602](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2602/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Individual logging requirements will be different depending on the regulatory and compliance requirements, business needs, and other factors that affect your organization. At a minimum, you would typically log these database and server activities: - Startup - Shutdown - Pause - Commit and rollback t
```

**Success Criteria:**
- The control described by T2602 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
