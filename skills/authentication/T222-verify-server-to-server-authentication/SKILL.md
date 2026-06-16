---
name: t222-verify-server-to-server-authentication
description: Use the following guidelines for verifying server-to-server authentication: 1. Obtain a list of all servers in-scope for this application along with IP addresses. - For example, a web server, a presentation tier / application server, a midd
---

# T222: Verify server-to-server authentication

**Category:** CODE_FIX  
**SD Elements:** [T222](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T222/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying server-to-server authentication:

1. Obtain a list of all servers in-scope for this application along with IP addresses.
    - For example, a web server, a presentation tier / application server, a middle tier server, or database server.

2. For each pair of servers that communicate with each other, verify that the servers require some form of password, certificate, or other authentication credential to communicate.
    - Alternatively, try to connect directly to the server from a different machine on the same network to determine if the authentication is done by IP.

3. If any machine on the network can connect to a server and access or modify application data without authentication credentials, then this test __fails__.

4. Authenticate WS/SSE during handshake using short-lived credentials bound to origin/session context, and revalidate on reconnect.

## Success Criteria

- The control "Verify server-to-server authentication" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
