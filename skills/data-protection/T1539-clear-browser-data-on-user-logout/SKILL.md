---
name: t1539-clear-browser-data-on-user-logout
description: Configure your application to send the `Clear-Site-Data` header when the user logs out. Configure the header using the following directives: * `"cache"`: clear all cached files for this origin * `"cookies"`: clear all cookies for the domain
---

# T1539: Clear browser data on user logout

**Category:** CODE_FIX  
**SD Elements:** [T1539](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1539/)  
**Priority:** 8  
**Domain:** data-protection

## Affected Areas in This Repository

database.py (virtual_cards.cvv and users.password stored in plaintext; PII in users), static/dashboard.js (JWT in localStorage)

## Required Fix

Encrypt sensitive data at rest, never store card CVV, salt+hash passwords, and avoid keeping long-lived secrets in browser storage.

## Implementation Guidance (SD Elements)

Configure your application to send the `Clear-Site-Data` header when the user logs out. Configure the header using the following directives:

* `"cache"`: clear all cached files for this origin
* `"cookies"`: clear all cookies for the domain (both HTTP and HTTPS)
* `"storage"`: clear all locally stored data, including *ServiceWorker* registrations and *appCache* data

For example, the header shown below clears cookies and Local Storage.

```
Clear-Site-Data: "cookies", "storage"
```

The browser is not a secure storage area. Therefore, it is recommended to clear client-side application data when the user logs out.

## Success Criteria

- The control "Clear browser data on user logout" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
