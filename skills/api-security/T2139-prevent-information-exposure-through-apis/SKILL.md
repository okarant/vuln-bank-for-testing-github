---
name: t2139-prevent-information-exposure-through-apis
description: Prevent information exposure through APIs
---

# T2139: Prevent information exposure through APIs

**Category:** CODE_FIX
**SD Elements:** [T2139](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2139/)
**Priority:** P7

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use the following guidelines to avoid exposing information with APIs: - Remove unused API endpoints. - Never return unrequested sensitive data in API responses, and never rely on the client-side filtering. Attackers can call the API directly and receive sensitive data that the client would filter ou
```

**Success Criteria:**
- The control described by T2139 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
