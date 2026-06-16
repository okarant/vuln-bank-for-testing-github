---
name: t70-implement-account-lockout-or-authentication-throttling-for-s
description: Use a feature to lock out users after a configurable number of failed authentication attempts. This protects against brute-forcing for system accounts. Alternatively, consider a mechanism to throttle multiple authentication attempts for the
---

# T70: Implement account lockout or authentication throttling for system accounts

**Category:** CODE_FIX  
**SD Elements:** [T70](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T70/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use a feature to lock out users after a configurable number of failed authentication attempts. This protects against brute-forcing for system accounts. 

Alternatively, consider a mechanism to throttle multiple authentication attempts for the same user ID, or originating from the same user ID. This has the benefit of not locking out legitimate user accounts, while decreasing the likelihood of a brute-force attack.

Exponentially increase the amount of time a user has to wait between authentication attempts until it reaches a point that makes brute-forcing impractical. For example, increasing the wait period by 24 hours would discourage brute-force attacks.

## Success Criteria

- The control "Implement account lockout or authentication throttling for system accounts" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
