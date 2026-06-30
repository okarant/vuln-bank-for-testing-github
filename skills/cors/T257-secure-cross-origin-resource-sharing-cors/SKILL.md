---
name: t257-secure-cross-origin-resource-sharing-cors
description: Use the following guidelines for securing CORS: - __Do not__ rely on the `Origin:` header for access control. - Enforce a normal authentication/authorization process. - Same-origin requests and non-browser requests are not subject to a CORS
---

# T257: Secure cross origin resource sharing (CORS)

**Category:** CODE_FIX  
**SD Elements:** [T257](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T257/)  
**Priority:** 8  
**Domain:** cors

## Affected Areas in This Repository

app.py L35 `CORS(app)` enables permissive cross-origin access globally

## Required Fix

Scope CORS to an explicit allowlist of trusted origins, methods and headers; never combine a wildcard origin with credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for securing CORS:

- __Do not__ rely on the `Origin:` header for access control.
    - Enforce a normal authentication/authorization process.
        - Same-origin requests and non-browser requests are not subject to a CORS policy
        - See the related How-to for this countermeasure on CORS and access control.
    - Perform authentication/authorization for all request types such as GET and POST, except OPTIONS.
    - Make sure no part of the functionality that is not public is exposed without authentication.

- Use standard procedures to block cross-site request forgery (CSRF).
    - See the related How-to for this countermeasure.

- Use the following guidelines to develop a secure CORS policy, using a whitelist for trusted origins.
    - Do not send CORS response headers on private resources that are not intended to be used across origins
    - Send the wildcard value (`Access-Control-Allow-Origin: *`) in a response containing publicly accessible resources
        - It is recommended to enable this for all public resources, including JavaScript files, stylesheets, and images. Doing so enables features such as [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) and [HTML5 canvas exports](https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_enabled_image).
        - As a precaution, the wildcard cannot be used with credentials (cookies, client certificates).
    - For shareable resources, check the exact value of the incoming `Origin: ` header against a whitelist, along with the HTTP method and headers used. If a match is found, return appropriate `Access-Control-Allow-...` headers.
        - Do not use partial whitelist matching (e.g., `contains()`, `startsWith()`, `endsWith()`) to avoid bypass attacks

Additionally, take the following considerations into account.

- Use the response header `Access-Control-Max-Age:` to enforce a time limit on the caching of the CORS policy in the browser (in seconds).
- Send the `Access-Control-Allow-Credentials: true` header on all requests that require credentials (e.g., cookies, client certificates). 
- If the request is sent from the browser over a plain HTTP channel, but the origin shows an HTTPS prefix, do **not** process the message or return an error.
- If you are building an isolated application, consider moving frontend and API into the same origin to benefit from same-origin requests.

In all cases, fail securely, and return a minimum amount of information.

## Success Criteria

- The control "Secure cross origin resource sharing (CORS)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
