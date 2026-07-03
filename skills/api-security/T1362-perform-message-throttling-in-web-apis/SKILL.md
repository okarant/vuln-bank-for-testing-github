---
name: t1362-perform-message-throttling-in-web-apis
description: Perform message throttling in Web APIs
---

# T1362: Perform message throttling in Web APIs

**Category:** CODE_FIX
**SD Elements:** [T1362](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1362/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# To protect APIs against brute-force DoS attacks, use a feature that enforces a set number of failed attempts by a certain IP, API key, or request route during a set period. For example, a web API could allow an IP to have a maximum number of requests within a second, minute, or hour. You should also
```

**Success Criteria:**
- The control described by T1362 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
