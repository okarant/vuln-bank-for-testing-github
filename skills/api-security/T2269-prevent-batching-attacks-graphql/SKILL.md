---
name: t2269-prevent-batching-attacks-graphql
description: Prevent batching attacks (GraphQL)
---

# T2269: Prevent batching attacks (GraphQL)

**Category:** CODE_FIX
**SD Elements:** [T2269](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T2269/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Limit incoming requests at the code level so the code will apply the limitation for each batching request. Batching requests or query batching is supported in GraphQL to batch multiple queries or batch requests for various object instances in a single network call. To limit requests and thereby redu
```

**Success Criteria:**
- The control described by T2269 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
