---
name: ct435-bind-variables-in-sql-statements-oleg-test
description: Bind variables in SQL statements - Oleg Test
---

# CT435: Bind variables in SQL statements - Oleg Test

**Category:** CODE_FIX
**SD Elements:** [CT435](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-CT435/)
**Priority:** P10

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# - **Bind variables and avoid dynamic concatenation:** Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data. - **Use parameterized queries:** Pass untrusted values as bound parameters, never via string concatenation, formatting, or templ
```

**Success Criteria:**
- The control described by CT435 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Applied
