---
name: t284-generate-secure-access-tokens-api-tokens
description: Follow these guidelines for generating access/API tokens: - Generate an access token that is long enough to reduce the chances of brute force attacks. - The minimum length is 128 bit, which is 32 characters in base 16, or 22 characters in b
---

# T284: Generate secure access tokens (API tokens)

**Category:** CODE_FIX  
**SD Elements:** [T284](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T284/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Follow these guidelines for generating access/API tokens: 

- Generate an access token that is long enough to reduce the chances of brute force attacks.
    - The minimum length is 128 bit, which is 32 characters in base 16, or 22 characters in base 64.

- Use a secure random generator for making access tokens to reduce the predictability of the tokens.

- Define an expiry date for tokens if they are used to protect sensitive services.

- Implement a way to revoke access tokens.

- When an account gets a new access token, send an email to inform the user.

- Alternatively, only display the access token at the time it is generated
    - Afterwards, mask the access token, such as by hiding the token's values except for the last few digits.
    - Allow users to regenerate the token if they need to, such as in the case they won't remember it.

## Success Criteria

- The control "Generate secure access tokens (API tokens)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
