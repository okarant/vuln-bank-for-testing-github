---
name: t2600-control-the-result-set-size-returned-by-a-query
description: Control the result set size returned by a query
---

# T2600: Control the result set size returned by a query

**Category:** CODE_FIX
**SD Elements:** [T2600](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2600/)
**Priority:** P7

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# - Control the size of the result set returned from the database to the application for sensitive queries and stored procedures. - Program your application to display an error message or roll back a transaction if a query produces more results than the limit. Refer to your database documentation for 
```

**Success Criteria:**
- The control described by T2600 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
