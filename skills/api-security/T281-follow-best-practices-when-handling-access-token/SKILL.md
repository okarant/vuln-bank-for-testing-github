---
name: t281-follow-best-practices-when-handling-access-tokens-api-token
description: Follow best practices when handling access tokens (API tokens)
---

# T281: Follow best practices when handling access tokens (API tokens)

**Category:** CODE_FIX
**SD Elements:** [T281](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T281/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use the following guidelines for authenticating/authorizing an application's services through access/API tokens: - Avoid allowing and requiring users to provide API tokens in query parameters because they are cached. - Receive the tokens in the headers or body of a message, and over secure protocols
```

**Success Criteria:**
- The control described by T281 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
