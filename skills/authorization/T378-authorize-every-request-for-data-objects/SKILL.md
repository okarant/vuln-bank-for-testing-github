---
name: t378-authorize-every-request-for-data-objects
description: Every direct object reference should be governed by session authentication and a permission check. Where objects (e.g. files) are served via the web, prefer using a web application framework to host and manage them instead of serving direct
---

# T378: Authorize every request for data objects

**Category:** CODE_FIX  
**SD Elements:** [T378](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T378/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Every direct object reference should be governed by session authentication and a permission check. Where objects (e.g. files) are served via the web, prefer using a web application framework to host and manage them instead of serving directly from the web server.

Follow these implementation steps:

**Identify access points:**
- Identify parts of the code or pages that enable users to access data objects (e.g. database rows, files, or other data objects)

**Session and permission:**
- Base authorization on the authenticated session (e.g. use the identity or ID from the session object), not on the identifier supplied by the user in the request
- Check permission for both the requested object and the requested action or properties before granting access
- Do not rely only on interface-level or page-level authorization; verify access for each requested object (e.g. each file, database row). It is not enough to authorize access to a page when a user can manually manipulate the object references; the application should properly authorize each access request

**No alternate paths:**
- Verify that there are no alternative, less secure access paths to the same objects or files

**Framework hosting and file types:**
- Prefer using a web application framework to host and serve files instead of serving directly from the web server
- When using a framework, have all file types associated with the application (.txt, .pdf, documents, etc.) hosted and managed by the framework so access control and safe handling apply consistently

**Unknown file types:**
- Refuse to serve or return an error when the server receives a request for a file type it does not know how to handle (e.g. after directory traversal, to prevent downloading or executing unauthorized content such as password files from the application server)

Note: This countermeasure applies to web applications that expose direct or indirect object references (e.g. files, database rows). 

Example: If User A is authorized to see a page that shows their account information (e.g. `https://somedomain.com/showmyaccount?id=52`), User A should not be allowed to see User B's information by changing the link to `id=53`, even if User A has logged in as a valid user.

## Success Criteria

- The control "Authorize every request for data objects" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
