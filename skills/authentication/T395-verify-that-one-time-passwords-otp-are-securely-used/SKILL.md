---
name: t395-verify-that-one-time-passwords-otp-are-securely-used
description: Verify that the following requirements are met for one-time-passwords (OTPs): - Verify that a __secure random number generator__ is used. - Verify that a __secure hash function__ is used (such as SHA, and not MD5). - Verify that the __valid
---

# T395: Verify that one-time passwords (OTP) are securely used

**Category:** CODE_FIX  
**SD Elements:** [T395](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T395/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Verify that the following requirements are met for one-time-passwords (OTPs):

- Verify that a __secure random number generator__ is used. 
- Verify that a __secure hash function__ is used (such as SHA, and not MD5).
- Verify that the __validity period__ of the OTP is set to the minimum period necessary.
- Verify that a __salt__ is used in password generation.
- Verify that the password is __long__ enough (such as 8 characters or more).
- Verify that __secure channels __ are used for sending OTPs (such as TLS, where possible based on the application/medium).

## Success Criteria

- The control "Verify that one-time passwords (OTP) are securely used" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
