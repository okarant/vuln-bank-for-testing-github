---
name: t220-verify-that-user-password-is-salted-and-hashed
description: Complete the following steps for verifying that passwords are salted and hashed: 1. Review the source code for where authentication occurs. 2. Ensure that the code appends a salt to the user-supplied password and hashes prior to comparing i
---

# T220: Verify that user password is salted and hashed

**Category:** CODE_FIX  
**SD Elements:** [T220](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T220/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Complete the following steps for verifying that passwords are salted and hashed:

1. Review the source code for where authentication occurs.

2. Ensure that the code appends a salt to the user-supplied password and hashes prior to comparing it with the stored password.
    - If the code hashes but does not append a salt, or the code does not hash, then this test __fails__.

3. Ensure that the salts are unique for each user and has enough entropy:
    - This test __fails__ if the same salt is used for multiple users.
    - This test __fails__ if the generated salt is predictable, such as being derived from other fields like username. 
    - This test __fails__ if the salt is too short (shorter than 8 bytes).

4. This test __fails__ if the password is hashed with a weak algorithm, such as MD5.

## Success Criteria

- The control "Verify that user password is salted and hashed" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
