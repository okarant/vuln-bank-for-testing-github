---
name: t2599-protect-against-connection-string-parameter-pollution
description: Protect against connection string parameter pollution
---

# T2599: Protect against connection string parameter pollution

**Category:** CODE_FIX
**SD Elements:** [T2599](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2599/)
**Priority:** P9

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# This is an attack where an attacker finds out what's in a connection string and then appends their own parameters to the string. Using this technique, an attacker may be able to connect to a different data source, such as another database on your network, and in the process completely bypass your au
```

**Success Criteria:**
- The control described by T2599 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
