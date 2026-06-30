---
name: t1918-integrate-with-sso
description: Use the following guidelines for secure Single Sign-On (SSO) integrations: - Verify that the identity directory is accurate - Use modern authentication protocols - Secure all the components of the SSO system - Require Multi-Factor Authentic
---

# T1918: Integrate with SSO

**Category:** INFRA  
**SD Elements:** [T1918](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1918/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Why Not Directly Code-Fixable in This Repository

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Use the following guidelines for secure Single Sign-On (SSO) integrations:

- Verify that the identity directory is accurate
- Use modern authentication protocols
- Secure all the components of the SSO system
- Require Multi-Factor Authentication (MFA)
- Enforce session timeouts
- Enforce frequent password changes
- Put restrictions on the devices with which a user can leverage SSO

## Success Criteria

- The requirement "Integrate with SSO" is documented with an owner and an infrastructure/process plan.

**Status:** Documented
