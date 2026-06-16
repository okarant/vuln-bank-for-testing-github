---
name: t285-restrict-use-of-access-tokens-api-tokens
description: If the application has services that must authenticate or authorize access using tokens, or API tokens, follow these guidelines: - __Use access tokens for services that are used most frequently__ - Use access tokens instead of username and 
---

# T285: Restrict use of access tokens (API tokens)

**Category:** CODE_FIX  
**SD Elements:** [T285](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T285/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

If the application has services that must authenticate or authorize access using tokens, or API tokens, follow these guidelines:

- __Use access tokens for services that are used most frequently__

    - Use access tokens instead of username and passwords.
    - Access tokens have advantages that include convenience and rotation. 
    - Access tokens do not disclose any private information about the user, and only need moderate protection.


- __Do not use access tokens for critical functions__

    - Do not use access tokens for enabling anything beyond their own security level.
    - Do not use access tokens for changing passwords, or information related to password-reset (such as email addresses and security questions). 
    - Do not assign default access tokens to services unless the user explicitly requests them, such as by clicking a button.
    - Do not use access tokens to change data fields related to a user's identity: 

        - username
        - phone number
        - date of birth
        - mailing address 
        - security questions

## Success Criteria

- The control "Restrict use of access tokens (API tokens)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
