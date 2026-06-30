---
name: t219-avoid-transmitting-confidential-data-through-url-parameters
description: Use the following guidelines for transmitting confidential data in HTTP-based applications: - Do not transmit confidential data as URL parameters, such as passwords and credit card numbers. - Avoid including unnecessary parameters in a requ
---

# T219: Avoid transmitting confidential data through URL parameters

**Category:** CODE_FIX  
**SD Elements:** [T219](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T219/)  
**Priority:** 6  
**Domain:** data-protection

## Affected Areas in This Repository

database.py (virtual_cards.cvv and users.password stored in plaintext; PII in users), static/dashboard.js (JWT in localStorage)

## Required Fix

Encrypt sensitive data at rest, never store card CVV, salt+hash passwords, and avoid keeping long-lived secrets in browser storage.

## Implementation Guidance (SD Elements)

Use the following guidelines for transmitting confidential data in HTTP-based applications:

- Do not transmit confidential data as URL parameters, such as passwords and credit card numbers.
- Avoid including unnecessary parameters in a request, such as hidden fields, Ajax variables, cookies and header values.

- Avoid GET requests when this data is being passed to the server, because GET-style parameter passing puts the information in the URL parameters and can get cached in browser history, proxies, logs, and many other places. 

- Use the POST method to ensure that parameters are stored in the data section of the HTTP request.
    - POST calls can also include parameters in the URL, and avoid using any confidential information to construct the POST URLs.

- Enforce the correct client behavior using server side implementations.
    - To do that, avoid accepting fields that might carry confidential data through URL parameters.
    - Server side enforcement guarantees that the clients and web pages follow the best practice, or they would not function.

- Prevent sensitive data in URLs/form actions, enforce safer submission patterns, and redact leakage in logs/analytics/referrers.

## Success Criteria

- The control "Avoid transmitting confidential data through URL parameters" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
