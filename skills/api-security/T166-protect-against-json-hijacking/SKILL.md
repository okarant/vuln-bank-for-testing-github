---
name: t166-protect-against-json-hijacking
description: Protect against JSON hijacking
---

# T166: Protect against JSON hijacking

**Category:** CODE_FIX
**SD Elements:** [T166](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T166/)
**Priority:** P7

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use the following guidelines to reduce the risk of JSON hijacking attacks, especially when dealing with older web browsers: * Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session. * On the server side, use a hard to guess random nonce that is uniqu
```

**Success Criteria:**
- The control described by T166 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
