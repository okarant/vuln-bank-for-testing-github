---
name: t1918-integrate-with-sso
description: Integrate with SSO
---

# T1918: Integrate with SSO

**Category:** CODE_FIX
**SD Elements:** [T1918](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1918/)
**Priority:** P9

**Code to Fix:**
```python
# auth.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in auth.py:
# Use the following guidelines for secure Single Sign-On (SSO) integrations: - Verify that the identity directory is accurate - Use modern authentication protocols - Secure all the components of the SSO system - Require Multi-Factor Authentication (MFA) - Enforce session timeouts - Enforce frequent pa
```

**Success Criteria:**
- The control described by T1918 is enforced in auth.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Skipped
