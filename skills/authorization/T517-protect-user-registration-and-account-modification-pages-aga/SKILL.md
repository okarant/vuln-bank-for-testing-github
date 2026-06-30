---
name: t517-protect-user-registration-and-account-modification-pages-ag
description: When a user tries to **modify his/her username** or **create a new account**, the application needs to check if the username already exists. However, giving away this information allows attackers to build a list of valid usernames (user enu
---

# T517: Protect user registration and account modification pages against user enumeration

**Category:** CODE_FIX  
**SD Elements:** [T517](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T517/)  
**Priority:** 6  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

When a user tries to **modify his/her username** or **create a new account**, the application needs to check if the username already exists. However, giving away this information allows attackers to build a list of valid usernames (user enumeration). Follow these steps to protect the application against user enumeration:

1. Include an anti-automation technique, such as a **CAPTCHA** image to slow down attacks. Use accessibility options for visually impaired users.
    - **Note:** If usernames are not user email addresses, but arbitrary choices, ignore the rest of these steps.

2. For usernames that are email addresses, display a message informing the user that a validation email has been sent to their inbox. Display a similar message **regardless of whether the entered email address exists**. 

3. If an account is associated with the selected email address, send a **warning message** to that address. Also send an **abnormal behavior alert** to system admin.

4. If the submitted email address is unique in the system, send a one-time-use email address validation link to that address.  Expire the link if it is not used within a predefined period.

## Success Criteria

- The control "Protect user registration and account modification pages against user enumeration" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
