---
name: t536-restrict-the-size-of-incoming-messages-in-services
description: Restrict the size of incoming messages in services
---

# T536: Restrict the size of incoming messages in services

**Category:** CODE_FIX
**SD Elements:** [T536](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T536/)
**Priority:** P8

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Use the following guidelines for restricting the size of incoming messages in services: - Limit the size of input messages that services accept to protect them against Denial of Service (DoS) attacks. - If services call other services as part of their operation, make sure the message sizes are withi
```

**Success Criteria:**
- The control described by T536 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
