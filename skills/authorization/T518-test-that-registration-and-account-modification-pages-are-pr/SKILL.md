---
name: t518-test-that-registration-and-account-modification-pages-are-p
description: Follow these steps for both username **registration** and **modification** procedures to make sure they do not lead to user enumeration: 1. Attempt to submit 10 consecutive username registration/modification requests. - This test __fails__ 
---

# T518: Test that registration and account modification pages are protected against user enumeration

**Category:** CODE_FIX  
**SD Elements:** [T518](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T518/)  
**Priority:** 6  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Follow these steps for both username **registration** and **modification** procedures to make sure they do not lead to user enumeration:

1. Attempt to submit 10 consecutive username registration/modification requests.
    - This test __fails__ if:
        - You do not see a **CAPTCHA** (or other **anti-automation** technique).
        - You are not prevented from making further requests.
    - **Note:** If the username is an arbitrary choice of the users instead of email addresses, ignore the rest of these steps.

2. Attempt to create/modify an account with an existing email address and inspect the response. Next, create/modify an account with a unique email address and inspect the response.
    - This test __fails__ if the two **responses differ**.

3. Attempt to create an account with an existing email address.
    - This test __fails__  if the existing account owner does not receive a **warning notification**.

4. Attempt to modify a username with an existing email address. Next, check the inbox for an **email address validation link**.
    - This test __fails__ if there is no such link sent.

5. Click on the **link** and follow the instructions to change the username. Once the new username is successfully set, click the link again within the expiry time window.
    - This test __fails__ if it allows you to update the username again.

6. Repeat step 4. Next, wait until the link's **expiry time window** passes. Then click on the link and attempt to update the username.
    - This test __fails__ if it allows you to update the username.

## Success Criteria

- The control "Test that registration and account modification pages are protected against user enumeration" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
