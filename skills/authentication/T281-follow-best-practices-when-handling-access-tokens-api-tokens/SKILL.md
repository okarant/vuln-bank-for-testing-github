---
name: t281-follow-best-practices-when-handling-access-tokens-api-token
description: Use the following guidelines for authenticating/authorizing an application's services through access/API tokens: - Avoid allowing and requiring users to provide API tokens in query parameters because they are cached. - Receive the tokens in
---

# T281: Follow best practices when handling access tokens (API tokens)

**Category:** CODE_FIX  
**SD Elements:** [T281](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T281/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for authenticating/authorizing an application's services through access/API tokens:

- Avoid allowing and requiring users to provide API tokens in query parameters because they are cached.
    - Receive the tokens in the headers or body of a message, and over secure protocols, such as TLS.

- Log all access and activity using access tokens and allow users to review those logs.

- Do not include access token values in the logs.
    - Mask, sanitize, hash, or encrypt the value as suggested in the [OWASP logging instructions](https://www.owasp.org/index.php/Logging_Cheat_Sheet).

- Display messages to educate users about, and make them aware of:
    - Displaying access tokens.
    - Sending email notifications about the security of access tokens.

## Success Criteria

- The control "Follow best practices when handling access tokens (API tokens)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Applied
