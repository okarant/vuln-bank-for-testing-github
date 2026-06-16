---
name: t259-follow-best-practices-when-storing-data-in-local-or-session
description: Use the following guidelines when using a browser's Local or Session Storage: - Do not store unencrypted sensitive information in Local/Session/IndexDB Storage. - While the specifications describe the APIs, the underlying mechanism used by 
---

# T259: Follow best practices when storing data in Local or Session Storage

**Category:** CODE_FIX  
**SD Elements:** [T259](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T259/)  
**Priority:** 7  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Use the following guidelines when using a browser's Local or Session Storage:

- Do not store unencrypted sensitive information in Local/Session/IndexDB Storage.
    - While the specifications describe the APIs, the underlying mechanism used by browser for storing data locally is unknown.
    - Therefore, if the security of the operating system is compromised the data will be obtained by a hacker or anyone with a privileged access.

- Use `sessionStorage` instead of `localStorage` and `IndexDBStorage`.
    - Data stored using the `sessionStorage` object is available only to that window/tab until the window is closed.
    - On the contrary, `localStorage` and `IndexDBStorage` do not set any expiration date for data, and it will remain in the browser after it is closed.

- Perform strict input validation on data retrieved from Local/Session/IndexDB Storage before using it.
    - A Cross-Site Scripting (XSS) flaw can inject malicious values into the locally stored data.
    - Avoid using `eval()` on the stored data without strict white-listed validation. 

- Avoid placing data from Local/Session/IndexDB Storage into the page's body without proper validation (using `innerHTML` of an element, for example).
    - If the content is manipulated through XSS, this will pose a high risk for unexpected and malicious activities.

- Avoid storing session identifiers in the storage as the data is accessible by JavaScript.
    - Cookies can use the `httpOnly` flag to prevent JavaScript access.

- Avoid hosting multiple applications on the same domain.
    - Use different subdomains instead.
    - Local/Session/IndexDB Storage is shared between all pages of the same origin domain.
    - Therefore, there is no way to restrict the visibility of an object to a specific path like with the attribute path of HTTP Cookies.

__Note__:

- Local/IndexDB Storage allows developers to use JavaScript to store data on the client and in the browser-provided storage.
    - This is also called Web Storage, Offline Storage, or HTML5 Storage.

- Session Storage keeps data until the session ends. 
    -  Both Local and Session Storage store data on the client.
- A session is defined by the top-level browsing context (such as a tab or window) introduced in HTML5.
- Each session lasts as long as its tab/window is open with content coming from the same origin.
- The data will be available only to the pages from that origin.

Given that it can store a much larger amount of data compared to cookies, there is a need for greater care. See [Countermeasure T1468](/library/tasks/T1468/) for more details.

## Success Criteria

- The control "Follow best practices when storing data in Local or Session Storage" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
