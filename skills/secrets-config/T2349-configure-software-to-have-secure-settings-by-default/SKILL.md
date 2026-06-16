---
name: t2349-configure-software-to-have-secure-settings-by-default
description: Define and implement secure default settings for the software baseline by determining how to configure each setting that has an effect on security so that the default settings are secure and do not weaken the security functions provided by 
---

# T2349: Configure software to have secure settings by default

**Category:** CODE_FIX  
**SD Elements:** [T2349](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2349/)  
**Priority:** 8  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Required Fix

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

## Implementation Guidance (SD Elements)

Define and implement secure default settings for the software baseline by determining how to configure each setting that has an effect on security so that the default settings are secure and do not weaken the security functions provided by the platform, network infrastructure, or services.

- Conduct testing to ensure that the settings, including the default settings, are working as expected and are not inadvertently causing any security weaknesses, operational issues, or other problems.
- Verify that the approved configuration is in place for the software.
- Document each setting's purpose, options, default value, security relevance, potential operational impact, and relationships with other settings.
- Use authoritative programmatic technical mechanisms to document how each setting can be implemented and assessed by software administrators.
- Store the default configuration in a usable format and follow change control practices for modifying it (e.g., configuration as code).

## Success Criteria

- The control "Configure software to have secure settings by default" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
