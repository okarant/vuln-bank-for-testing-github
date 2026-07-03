---
name: t1919-use-json-web-token-jwt-securely
description: Use JSON Web Token (JWT) securely
---

# T1919: Use JSON Web Token (JWT) securely

**Category:** CODE_FIX
**SD Elements:** [T1919](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1919/)
**Priority:** P9

**Code to Fix:**
```python
# auth.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in auth.py:
# Secure [JSON Web Token (JWT)](/library/glossary/G112/) with JavaScript Object Signing and Encryption (JOSE). Use proper JOSE cryptographic function that serves your purpose: - **HMAC** (Hashed Message Authentication Code): is an efficient hash that requires a **secret key** and provides authenticity
```

**Success Criteria:**
- The control described by T1919 is enforced in auth.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
