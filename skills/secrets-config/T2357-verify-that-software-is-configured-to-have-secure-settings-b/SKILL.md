---
name: t2357-verify-that-software-is-configured-to-have-secure-settings
description: Verify that software is configured to have secure settings by default: - Verify that testing is conducted to ensure that the settings, including the default settings, are working as expected. - Verify that the approved configuration is in p
---

# T2357: Verify that software is configured to have secure settings by default

**Category:** CODE_FIX  
**SD Elements:** [T2357](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2357/)  
**Priority:** 8  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Required Fix

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

## Implementation Guidance (SD Elements)

Verify that software is configured to have secure settings by default:

- Verify that testing is conducted to ensure that the settings, including the default settings, are working as expected.
- Verify that the approved configuration is in place for the software.
- Verify that each setting's purpose, options, default value, security relevance, potential operational impact, and relationships with other settings are documented.
- Verify that authoritative programmatic technical mechanisms are used to document how each setting can be implemented and assessed by software administrators.
- Verify that the default configuration is stored in a usable format and follow change control practices for modifying it (e.g., configuration as code).

## Success Criteria

- The control "Verify that software is configured to have secure settings by default" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
