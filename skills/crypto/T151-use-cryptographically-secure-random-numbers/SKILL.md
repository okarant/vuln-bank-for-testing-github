---
name: t151-use-cryptographically-secure-random-numbers
description: Use cryptographically secure random numbers
---

# T151: Use cryptographically secure random numbers

**Category:** CODE_FIX
**SD Elements:** [T151](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T151/)
**Priority:** P7

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Only use cryptographically secure random numbers for security purposes. For example, session ID numbers must be random numbers or strings that cannot be guessed by attackers. Most programming languages come with simple random number tools, such as rand() in C, which don't have enough entropy. In man
```

**Success Criteria:**
- The control described by T151 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
