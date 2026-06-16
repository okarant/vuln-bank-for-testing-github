---
name: t10-use-server-to-server-authentication
description: Use the following guidelines for server-to-server authentication: - The application must have a feature that authenticates servers. - For example, a middle-tier server may need to authenticate a presentation-tier server. - This control redu
---

# T10: Use server-to-server authentication

**Category:** CODE_FIX  
**SD Elements:** [T10](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T10/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for server-to-server authentication:

- The application must have a feature that authenticates servers.
    - For example, a middle-tier server may need to authenticate a presentation-tier server. 

- This control reduces the risk of attackers connecting directly to a server from the internal network.

- Server-to-server authentication is commonly done using __X509 certificate mutual authentication__.

## Success Criteria

- The control "Use server-to-server authentication" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
