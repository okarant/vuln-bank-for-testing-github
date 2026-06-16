---
name: t61-disable-default-accounts-or-change-all-default-passwords
description: Use the following guidelines to disable or delete default accounts, or change all default passwords that are shipped with the product or created as part of the installation process: - Delete user accounts that are not needed as part of the 
---

# T61: Disable default accounts or change all default passwords

**Category:** CODE_FIX  
**SD Elements:** [T61](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T61/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines to disable or delete default accounts, or change all default passwords that are shipped with the product or created as part of the installation process:

- Delete user accounts that are not needed as part of the installation process, after installation, after deployment, or manually.

- Some application frameworks and other third-party packages contain databases and configuration files with default accounts and passwords. 
    - For user accounts that are needed for continuous administration or functioning of the application, ensure that all of the libraries have default passwords changed to strong alternatives.
    - Administrators may miss changing some passwords prior to deployment because configuration files aren't covered in a typical hardening process.

- The application must change, or remove, development and test accounts and passwords before they become active. 
    - Initiate a procedure through the installer that forces administrative users to change all default passwords for any accounts created and managed during or after installation.

- Don't use default authentication credentials or keys for built-in accounts to protect the storage and transmission of sensitive data.

- Implement mechanisms to prevent unauthorized access, exposure, or modification of critical assets, where limiting access is not possible. For example, due to the architecture of the solution or the execution environment in which the software is executed.

## Success Criteria

- The control "Disable default accounts or change all default passwords" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
