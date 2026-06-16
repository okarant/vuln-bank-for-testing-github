---
name: t241-verify-that-third-party-libraries-use-secure-settings-and-t
description: Complete the following steps to ensure that there are no outstanding security patches for third party libraries, and that the libraries and tools are configured for the most secure settings: 1. Obtain a list of all third party libraries use
---

# T241: Verify that third party libraries use secure settings and the latest patches

**Category:** CODE_FIX  
**SD Elements:** [T241](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T241/)  
**Priority:** 10  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Required Fix

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

## Implementation Guidance (SD Elements)

Complete the following steps to ensure that there are no outstanding security patches for third party libraries, and that the libraries and tools are configured for the most secure settings:

1. Obtain a list of all third party libraries used by the application, including version numbers.
    - If you are not familiar with the code structure, you might need to ask a developer to compile this list for you.

2. Research vendor pages for the third party libraries to see if there are any outstanding security vulnerabilities.

    This test __fails__ if there are outstanding security vulnerabilities without any workarounds.

3.  Research vendor pages for the most secure settings of the libraries, or any weaknesses reported caused by misconfiguration of the tools/software.
    - Check the system settings.

    This test __fails__ if they are different from recommended settings.

__Note__: If vulnerability information is unavailable from the vendor, consider using a third party service such as the Common Vulnerability Exposures (CVE) database to research if there are known vulnerabilities for the third party libraries. The following sources can be used to locate security advisories and details about required patch levels for most commonly available products/libraries:

- [Security Focus Vulnerability Database](http://www.securityfocus.com/vulnerabilities) (where advisories are categorized by vendor > Product > Version)
- [National Vulnerability Database (NVD)](http://web.nvd.nist.gov/view/vuln/search).
- [Common Vulnerability Enumerator (by MITRE Foundation)](http://cve.mitre.org/cve/).

## Success Criteria

- The control "Verify that third party libraries use secure settings and the latest patches" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
