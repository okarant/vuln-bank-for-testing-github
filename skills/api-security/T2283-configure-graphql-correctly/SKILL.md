---
name: t2283-configure-graphql-correctly
description: Configure GraphQL correctly
---

# T2283: Configure GraphQL correctly

**Category:** CODE_FIX
**SD Elements:** [T2283](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2283/)
**Priority:** P9

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# GraphQL's default configuration is often insecure for the production environment. Follow the guidelines below to secure a GraphQL application: - Disable GraphiQL and Introspection - Make sure the `NODE_ENV` environment variable has a value. For production use, set `NODE_ENV` to **production**, and f
```

**Success Criteria:**
- The control described by T2283 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
