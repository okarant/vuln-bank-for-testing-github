---
name: t1363-verify-if-message-throttling-is-properly-performed-in-web
description: Write a brief script that makes HTTP requests to the API endpoint every *n* milliseconds. The script can have different inputs such as: - Set **IP** where requests are made from - **API key** by which the requests are made with - **n** the 
---

# T1363: Verify if message throttling is properly performed in Web APIs

**Category:** CODE_FIX  
**SD Elements:** [T1363](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1363/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Write a brief script that makes HTTP requests to the API endpoint every *n* milliseconds. The script can have different inputs such as:

- Set **IP** where requests are made from
- **API key** by which the requests are made with
- **n** the frequency by which you send to the endpoint

This test checks if a message throttling mechanism has been properly implemented for the API endpoint.

## Success Criteria

- The control "Verify if message throttling is properly performed in Web APIs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Applied
