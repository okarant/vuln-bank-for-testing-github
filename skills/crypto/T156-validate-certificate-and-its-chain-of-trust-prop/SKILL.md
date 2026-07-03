---
name: t156-validate-certificate-and-its-chain-of-trust-properly
description: Validate certificate and its chain of trust properly
---

# T156: Validate certificate and its chain of trust properly

**Category:** CODE_FIX
**SD Elements:** [T156](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T156/)
**Priority:** P7

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Validate all certificates and their chains of trust, such as X509 certificates. Any application using __SSL__ or __public key infrastructure (PKI)__ based authentication must do the following at the very least: * Follow the chain of trust for certificate validation. * Verify that each node in the ch
```

**Success Criteria:**
- The control described by T156 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
