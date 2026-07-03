---
name: t38-bind-variables-in-sql-statements
description: Bind variables in SQL statements
---

# T38: Bind variables in SQL statements

**Category:** CODE_FIX
**SD Elements:** [T38](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T38/)
**Priority:** P10

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# Use the following guidelines for binding variables in SQL statements: - Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data. - Most persistence frameworks provide a feature to bind runtime variables with pre-generated SQL statements. -
```

**Success Criteria:**
- The control described by T38 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Applied
