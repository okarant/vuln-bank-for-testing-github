---
name: t321-verify-that-local-and-session-storage-are-securely-used
description: Use the following guidelines for verifying the security of Local and Session Storage: - Find tools or plugins that allow for the inspection of Local/Session Storage's contents. - Chrome offers a strong tool under Developer Tools > Resources
---

# T321: Verify that Local and Session Storage are securely used

**Category:** CODE_FIX  
**SD Elements:** [T321](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T321/)  
**Priority:** 7  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying the security of Local and Session Storage:

- Find tools or plugins that allow for the inspection of Local/Session Storage's contents.
    - Chrome offers a strong tool under Developer Tools > Resources.
    - The Firefox Firebug plugin could also be helpful.

- Use the web application normally.
    - Make sure to launch the pages that you know may store data in Local Storage or Session Storage.
        - You may need input from developers.

- Open the tabs for Local Storage and Session Storage in the plugin/inspection tool and examine the items.

- This test __fails__ if:

    - Unencrypted application secrets are stored in Local/Session Storage (such as keys).

    - Unencrypted sensitive user data is stored in the Local/Session Storage.

    - User data that does not need to be persisted is stored in Local Storage instead of Session Storage.

    - Session identifiers are stored in Local/Session Storage instead of cookies.

- Open various applications hosted on the same domain.
    - Inspect the storage.
    - This test __fails__ if data specific to one application that needs to be protected from other applications on the same domain is stored in the Local/Session Storage.

Work with developers to verify these items:

- Data from Local/Session Storage is not used by the JavaScript method `eval()`, in the `innerHTML` of nodes, or through similar methods to construct a web page without proper validation.
    - This test __fails__ if the data is not properly validated.

- If the data in Local/Session Storage is encrypted, verify that the key for encryption is not shared among different users.
    - This test __fails__ if a shared key is sent to the client or stored locally.

## Success Criteria

- The control "Verify that Local and Session Storage are securely used" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
