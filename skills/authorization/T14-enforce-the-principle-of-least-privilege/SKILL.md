---
name: t14-enforce-the-principle-of-least-privilege
description: The principle of least privilege is the concept that all subjects of a computing environment are restricted from accessing resources that are not essential to their purpose. This includes application components, users, and processes. Follow
---

# T14: Enforce the principle of least privilege

**Category:** CODE_FIX  
**SD Elements:** [T14](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T14/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

The principle of least privilege is the concept that all subjects of a computing environment are restricted from accessing resources that are not essential to their purpose. This includes application components, users, and processes. Following this principle, additional processes, roles, and accounts should only be created as necessary.

To enforce the fewest privileges on a subject, all privileges must be:

- Restricted as much as possible.
- Granted as late as possible.
- Revoked as soon as possible.

Define an access control model (to support a consistent and uniform way of allocating access) that grants access to the users as follows:

- Define appropriate access depending on each user's business and access needs.
- Define access to system components and data resources that are based on users' job classification and functions.
- Enforce the fewest privileges (for example, user, administrator) to perform a job function.

Access is assigned to users, including privileged users, based on:

- Job classification and function.
- Least privileges necessary to perform job responsibilities.

Define, assign, and manage access privileges for application and system accounts as follows:

- Based on the least privileges necessary for the operability of the system or application.
- Access is limited to the systems, applications, or processes that specifically require their use.

##### Note
The principle of least privilege can be applied in many different contexts. For example:

- Create an account for the sole purpose of running a particular background process.
    - Run Server/daemon processes under restricted user accounts.

- Use accounts with access restricted to the required features and resources of a service.
    - The code interacts with a service, such as a database, that supports user accounts and access controls.
    - Multiple accounts may be required to use different parts of the code, and to work with different sets of data.

## Success Criteria

- The control "Enforce the principle of least privilege" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
