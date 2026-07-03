---
name: t257-secure-cross-origin-resource-sharing-cors
description: Secure cross origin resource sharing (CORS)
---

# T257: Secure cross origin resource sharing (CORS)

**Category:** CODE_FIX
**SD Elements:** [T257](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T257/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use the following guidelines for securing CORS: - __Do not__ rely on the `Origin:` header for access control. - Enforce a normal authentication/authorization process. - Same-origin requests and non-browser requests are not subject to a CORS policy - See the related How-to for this countermeasure on 
```

**Success Criteria:**
- The control described by T257 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
