---
name: t1541-decide-on-the-best-csrf-defense-for-your-application
description: To analyze if your application is vulnerable to CSRF, follow these steps: 1. Does your application perform state-changing operations on the backend (e.g., login, store data)? * __*Yes*__: Continue with the next step * __*No*__: Your applica
---

# T1541: Decide on the best CSRF defense for your application

**Category:** CODE_FIX  
**SD Elements:** [T1541](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1541/)  
**Priority:** 7  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

To analyze if your application is vulnerable to CSRF, follow these steps:

1. Does your application perform state-changing operations on the backend (e.g., login, store data)?
    * __*Yes*__: Continue with the next step
    * __*No*__: Your application does not need protection against CSRF attacks.
2. Does your application rely on authentication or session management mechanism that is automatically handled by the browser (e.g., cookies, HTTP Basic authentication)?
    *  __*Yes*__: You need protection against CSRF attacks
    *  __*No*__: Your application does not need protection against CSRF attacks.


To select the proper CSRF defense, follow these steps:

1. Does your application generate dynamic pages on the server (e.g., PHP, JSP)?
    * __*Yes*__: Continue with step 2
    * __*No*__: Continue with step 3
2. Does your application handle a small number of concurrent users (< 1000)?
    * __*Yes*__: Use a *Synchronizer Token* pattern, as described in [Countermeasure 29](/library/tasks/T29/) and continue with step 5.
    * __*No*__: Continue with step 3
3. Does your application accept requests that can be sent from an HTML element (e.g., a form), or without a CORS preflight request?
    * __*Yes*__: Continue with step 4
    * __*No*__: Use a *secure CORS policy*, as described in [Countermeasure 257](/library/tasks/T257/).
4. Are your application's frontend and backend deployed on the same origin?
    * __*Yes*__: Use a *Double Submit Cookie*, as described in [Countermeasure 29](/library/tasks/T29/) and continue with step 5.
    * __*No*__: Use a *secure CORS policy*, as described in [Countermeasure 257](/library/tasks/T257/).
5. Does your backend only need to accept requests coming from the same domain (e.g., from `www.example.com` to `api.example.com` falls within `example.com`)?
    * __*Yes*__: Consider using the *SameSite* cookie attribute, as described in [Countermeasure 557](/library/tasks/T557/).
    * __*No*__: No additional security measures need to be taken.

For every application, you need to analyze if weaknesses that introduce Cross-Site Request Forgery (CSRF) exist or not. When it is, you need to select one of four currently available defense strategies. This guideline guides you through the process and refers to other guidelines containing more details about implementing defenses.

![CSRF Flowchart](https://cd.sdelements.com/static/screenshots/CSRF_defense_flowchart_v2.png)

## Success Criteria

- The control "Decide on the best CSRF defense for your application" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
