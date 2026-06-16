---
name: t457-verify-that-unnecessary-services-and-capabilities-are-disab
description: Follow these instructions to make sure excessive system capabilities are disabled: - Make sure the list of system components and capabilities is complete and updated. - This includes functions, services, protocols, and ports. - Test that an
---

# T457: Verify that unnecessary services and capabilities are disabled

**Category:** CODE_FIX  
**SD Elements:** [T457](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T457/)  
**Priority:** 6  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Required Fix

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

## Implementation Guidance (SD Elements)

Follow these instructions to make sure excessive system capabilities are disabled:

- Make sure the list of system components and capabilities is complete and updated.
    - This includes functions, services, protocols, and ports.

- Test that any capability on the list marked as unnecessary is properly disabled.
    - Otherwise, this test __fails__.

## Success Criteria

- The control "Verify that unnecessary services and capabilities are disabled" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
