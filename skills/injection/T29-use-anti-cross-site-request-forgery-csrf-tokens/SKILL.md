---
name: t29-use-anti-cross-site-request-forgery-csrf-tokens
description: Use anti-Cross-Site Request Forgery (CSRF) tokens
---

# T29: Use anti-Cross-Site Request Forgery (CSRF) tokens

**Category:** CODE_FIX
**SD Elements:** [T29](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T29/)
**Priority:** P7

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# Use the following guidelines for anti-CSRF tokens: - Use a library that creates anti-CSRF tokens. - The code usually creates a token based on a secret parameter and a salt, then places parts of the information in cookies on the client. - Place the library-generated token in the request. - For exampl
```

**Success Criteria:**
- The control described by T29 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Documented
