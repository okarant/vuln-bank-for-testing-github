---
name: t186-use-recommended-settings-and-the-latest-patches-for-third-p
description: Regularly reviewing and addressing the security vulnerabilities reported for third party software will decrease the risk of a compromise. For any third party libraries or software being used in the system: - Upgrade to the latest version, o
---

# T186: Use recommended settings and the latest patches for third party libraries and software

**Category:** CODE_FIX  
**SD Elements:** [T186](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T186/)  
**Priority:** 10  
**Domain:** dependency-management

## Affected Areas in This Repository

requirements.txt (flask==2.0.1, werkzeug==2.0.1, pyjwt==2.4.0, etc.)

## Required Fix

Pin and patch dependencies to current secure versions, enable automated dependency/vulnerability scanning, and review transitive dependencies.

## Implementation Guidance (SD Elements)

Regularly reviewing and addressing the security vulnerabilities reported for third party software will decrease the risk of a compromise. For any third party libraries or software being used in the system: 

- Upgrade to the latest version, or apply the latest security patches.
- Look for documentation on their security weaknesses and configure them with their most secure settings.
- Modify any of the defaults that need to be changed.
- Avoid using components with known vulnerabilities.

It is essential to review all How-tos for this countermeasure, as each one applies to a different platform or library being used.

Most third party library and framework vendors publish security bulletins for their products directly using their website. Additionally, the following sources can be used to locate security advisories and details about required patch levels for most commonly available products and libraries:

- [Security Focus Vulnerability Database](http://www.securityfocus.com/vulnerabilities)
    - Advisories are categorized by Vendor > Product > Version.
- [National Vulnerability Database (NVD)](http://web.nvd.nist.gov/view/vuln/search)
- [Common Vulnerability Enumerator (by MITRE Foundation)](http://cve.mitre.org/cve/)

## Success Criteria

- The control "Use recommended settings and the latest patches for third party libraries and software" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
