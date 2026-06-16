---
name: t230-test-that-server-to-server-system-accounts-meet-minimum-pas
description: Use the following guidelines to test the minimum password requirements for server-to-server system accounts: Attempt to create a new server account with a simple password that does not meet minimum password standards. For example, less than
---

# T230: Test that server-to-server system accounts meet minimum password requirements

**Category:** CODE_FIX  
**SD Elements:** [T230](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T230/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines to test the minimum password requirements for server-to-server system accounts:

Attempt to create a new server account with a simple password that does not meet minimum password standards. For example, less than 5 characters, uses dictionary words, and so on.

This test __fails__ if you are able to successfully create this account with a weak password.

__Note__: The same test can be done by attempting to change the password for an existing account. However, using an existing system account might result in the interruption of service of the production environment and must be avoided.

## Success Criteria

- The control "Test that server-to-server system accounts meet minimum password requirements" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
