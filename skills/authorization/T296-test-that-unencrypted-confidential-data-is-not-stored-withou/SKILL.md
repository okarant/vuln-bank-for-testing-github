---
name: t296-test-that-unencrypted-confidential-data-is-not-stored-witho
description: Use the following guidelines for testing that confidential data is not stored on a client, or in shared locations on a server, in an unencrypted format: ## For client applications: - Install the application on a client, such as a mobile dev
---

# T296: Test that unencrypted confidential data is not stored without access control mechanisms

**Category:** CODE_FIX  
**SD Elements:** [T296](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T296/)  
**Priority:** 7  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Use the following guidelines for testing that confidential data is not stored on a client, or in shared locations on a server, in an unencrypted format:

## For client applications:

- Install the application on a client, such as a mobile device.
    - If the device is protected, root or jailbreak the device, or use an emulator that simulates this.

- Locate the data-files and local databases, and then copy them.
    - It is usually possible to do so on rooted mobile devices through a USB cable.
    - For mobile devices, check the data storage folders belonging to the application on the shared storage as well.

- Inspect the contents of the files and the databases.

    This test __fails__ if sensitive data such as application secrets or sensitive user data is stored without encryption.

## For server applications:

- Browse and analyze the directory structure on the server.

- Inspect the contents of the files and the databases.
    
    This test __fails__ if sensitive data such as application secrets or sensitive user data is stored without encryption.

### Test serialized objects

Locate the folders that hold application data especially 'serialized objects' (consult the developers). Check the content of those files/streams to test that confidential data is not stored in serialized objects without encryption.

## Success Criteria

- The control "Test that unencrypted confidential data is not stored without access control mechanisms" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
