---
name: t394-secure-one-time-passwords-otp
description: Secure one-time passwords (OTP)
---

# T394: Secure one-time passwords (OTP)

**Category:** CODE_FIX
**SD Elements:** [T394](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T394/)
**Priority:** P7

**Code to Fix:**
```python
# auth.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in auth.py:
# When generating OTPs, follow these guidelines to ensure their security: #### OTP Generation - Use a **secure random number generator** for making OTPs. - Consult the documentation for the random function that you use. - Avoid predictable or weak random number generators. - Implement __Time-based OTP
```

**Success Criteria:**
- The control described by T394 is enforced in auth.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
