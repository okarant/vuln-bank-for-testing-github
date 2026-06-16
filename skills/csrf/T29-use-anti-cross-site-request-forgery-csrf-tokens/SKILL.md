---
name: t29-use-anti-cross-site-request-forgery-csrf-tokens
description: Use the following guidelines for anti-CSRF tokens: - Use a library that creates anti-CSRF tokens. - The code usually creates a token based on a secret parameter and a salt, then places parts of the information in cookies on the client. - Pl
---

# T29: Use anti-Cross-Site Request Forgery (CSRF) tokens

**Category:** CODE_FIX  
**SD Elements:** [T29](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T29/)  
**Priority:** 7  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

Use the following guidelines for anti-CSRF tokens:

- Use a library that creates anti-CSRF tokens.
    - The code usually creates a token based on a secret parameter and a salt, then places parts of the information in cookies on the client.

- Place the library-generated token in the request.
    - For example, use the token as a hidden input in the form, or query string in a URL on the page or headers.

- Use the verification function when you receive data, and check if the token is valid.
    - The verification function verifies the token against the cookie values received with the request.
    - Some libraries automatically perform verification for all pages and do not require calling the verification function.

- Where applicable, use **standard headers** (e.g. `Origin`, `Referer`) to verify that the request originates from the expected site as a supplementary check; do not rely on these headers alone for access control.
- For **privileged or sensitive actions**, consider requiring **user interaction** (e.g. re-authentication, CAPTCHA, or one-time confirmation) so actions are not triggered solely by following a link or automatic request.
- Prefer a **trusted web application framework** that provides built-in CSRF protections (e.g. synchronizer token, double-submit cookie) so mitigations are applied consistently.

# About Anti-CSRF Tokens

An anti-CSRF token is a session- or transaction-specific string of random characters attached to important transactions, such as purchasing a stock on a brokerage site. In most cases, generating one CSRF token per session is enough, but the token should be independent of the session-id. When handling the client's request, the server ensures that the anti-CSRF token is the value expected for that session or transaction. If the token is not correct, then the application denies the transaction. This helps protect against CSRF because each request will have at least one unique parameter that an attacker cannot know ahead of time.

For more information about CSRF tokens, see the [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) or [OWASP CSRF page](https://owasp.org/www-community/attacks/csrf).

## Success Criteria

- The control "Use anti-Cross-Site Request Forgery (CSRF) tokens" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
