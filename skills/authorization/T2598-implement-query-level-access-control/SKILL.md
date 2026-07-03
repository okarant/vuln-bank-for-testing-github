---
name: t2598-implement-query-level-access-control
description: Implement query-level access control
---

# T2598: Implement query-level access control

**Category:** CODE_FIX
**SD Elements:** [T2598](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2598/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Query-level access control helps you restrict access to query operations, stored procedures, tables, rows, columns, and other database objects. Essentially, it allows users, roles, and groups to access database objects by configuring permissions for the objects themselves, rather than for the user a
```

**Success Criteria:**
- The control described by T2598 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
