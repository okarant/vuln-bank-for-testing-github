---
name: t284-generate-secure-access-tokens-api-tokens
description: Generate secure access tokens (API tokens)
---

# T284: Generate secure access tokens (API tokens)

**Category:** CODE_FIX
**SD Elements:** [T284](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T284/)
**Priority:** P7

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Follow these guidelines for generating access/API tokens: - Generate an access token that is long enough to reduce the chances of brute force attacks. - The minimum length is 128 bit, which is 32 characters in base 16, or 22 characters in base 64. - Use a secure random generator for making access to
```

**Success Criteria:**
- The control described by T284 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
