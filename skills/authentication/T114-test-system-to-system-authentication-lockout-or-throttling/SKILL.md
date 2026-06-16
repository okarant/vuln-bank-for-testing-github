---
name: t114-test-system-to-system-authentication-lockout-or-throttling
description: Use the following guidelines to test for system-to-system authentication lockout and throttling: 1. Obtain the user ID of a system account. 2. Attempt to authenticate with a valid user ID and incorrect password. 3. Repeat this 5 times. This
---

# T114: Test system-to-system authentication lockout or throttling

**Category:** CODE_FIX  
**SD Elements:** [T114](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T114/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines to test for system-to-system authentication lockout and throttling:

1. Obtain the user ID of a system account.

2. Attempt to authenticate with a valid user ID and incorrect password. 

3. Repeat this 5 times.

This test __fails__ if both of the following are true:

- You are able to log in with the correct password on the 6th try without having to wait (throttling).
- You do not face any other restriction that prevents you from authenticating (lockout).

## Success Criteria

- The control "Test system-to-system authentication lockout or throttling" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Applied
