---
name: t70-implement-account-lockout-or-authentication-throttling-for-s
description: Implement account lockout or authentication throttling for system accounts
---

# T70: Implement account lockout or authentication throttling for system accounts

**Category:** CODE_FIX
**SD Elements:** [T70](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T70/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use a feature to lock out users after a configurable number of failed authentication attempts. This protects against brute-forcing for system accounts. Alternatively, consider a mechanism to throttle multiple authentication attempts for the same user ID, or originating from the same user ID. This ha
```

**Success Criteria:**
- The control described by T70 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
