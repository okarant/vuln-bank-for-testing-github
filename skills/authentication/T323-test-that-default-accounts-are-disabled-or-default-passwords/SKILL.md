---
name: t323-test-that-default-accounts-are-disabled-or-default-password
description: Use the following guidelines to test that default passwords are changed or default accounts are disabled: - Identify all third party libraries/software that are used by your application and their default accounts. - Identify all default use
---

# T323: Test that default accounts are disabled or default passwords are changed

**Category:** CODE_FIX  
**SD Elements:** [T323](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T323/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines to test that default passwords are changed or default accounts are disabled:

- Identify all third party libraries/software that are used by your application and their default accounts.

- Identify all default user accounts that are created by your application.

- Test that accounts that are unnecessary after installation/deployment are deleted or disabled.
    - Work with system administrators to check if those accounts are removed.
    - This test __fails__ if these accounts are not removed.

- Test the default passwords for third party library/software or application accounts.

- This test __fails__ if any of the default passwords work.
    - There are some cases in which permitting the use of default passwords could be acceptable.
    - For example, a wireless modem may be shipped with a default admin username and password.

## Success Criteria

- The control "Test that default accounts are disabled or default passwords are changed" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
