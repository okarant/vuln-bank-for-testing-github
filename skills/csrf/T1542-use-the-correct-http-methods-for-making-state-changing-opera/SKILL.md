---
name: t1542-use-the-correct-http-methods-for-making-state-changing-ope
description: The HTTP specification defines several different methods to send requests. Each of the methods has an intended purpose. Use the following guide to decide on which method to use for each request: * `GET / HEAD`: Fetch information from the se
---

# T1542: Use the correct HTTP methods for making state-changing operations

**Category:** CODE_FIX  
**SD Elements:** [T1542](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1542/)  
**Priority:** 7  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

The HTTP specification defines several different methods to send requests. Each of the methods has an intended purpose. Use the following guide to decide on which method to use for each request:

* `GET / HEAD`: Fetch information from the server. These requests should never trigger a server-side state change. Note that this includes logout features, which are often mistakenly implemented as a `GET` operation.
* `POST`: Submit information to the server. In a REST context, used to create a new resource.
* `PUT / PATCH / DELETE`: Used in a REST context to manipulate the resource at the given URL (create, update and delete).

__Not respecting these methods might violate implicit security assumptions__. For example, CSRF defenses assume that `GET` requests never change state. Hence, `GET` requests do not require CSRF protection (See [Countermeasure 1541](/library/tasks/T1541/) for more information).

## Success Criteria

- The control "Use the correct HTTP methods for making state-changing operations" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
