---
name: t79-test-password-change-functions
description: Search each page of the application for password change features after authentication. For each page, attempt to reset a password. This test __fails__ if: - The password can be reset without entering the old password first. - The password c
---

# T79: Test password change functions

**Category:** CODE_FIX  
**SD Elements:** [T79](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T79/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Search each page of the application for password change features after authentication. For each page, attempt to reset a password.

This test __fails__ if:

- The password can be reset without entering the old password first.
- The password can be reset by entering a false old password.

## Success Criteria

- The control "Test password change functions" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
