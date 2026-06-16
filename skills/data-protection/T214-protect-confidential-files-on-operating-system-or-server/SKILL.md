---
name: t214-protect-confidential-files-on-operating-system-or-server
description: Use the following guidelines for protecting confidential files on operating systems and servers: - Use operating system (or server) controls to enforce minimum access rights on any confidential files used by the application. - Restricting a
---

# T214: Protect confidential files on operating system or server

**Category:** INFRA  
**SD Elements:** [T214](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T214/)  
**Priority:** 9  
**Domain:** data-protection

## Affected Areas in This Repository

database.py (virtual_cards.cvv and users.password stored in plaintext; PII in users), static/dashboard.js (JWT in localStorage)

## Why Not Directly Code-Fixable in This Repository

Encrypt sensitive data at rest, never store card CVV, salt+hash passwords, and avoid keeping long-lived secrets in browser storage.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Use the following guidelines for protecting confidential files on operating systems and servers:

- Use operating system (or server) controls to enforce minimum access rights on any confidential files used by the application.
    - Restricting access reduces the risk of a rogue application or malicious user accessing the data.
    - For example, by using a file containing Personally Identifiable Information (PII) or directory listings.

- For confidential files passed to the program as input, enforce this by validating that the file has minimum access as expected before using the content.

- If the access is too wide, such as by allowing public read access, return an error to the user to correct the issue, or apply the correct access rights if the file is to be managed by the application.

- Store files obtained from untrusted sources outside the `webroot`, with limited permissions, and with strong validation.

## Success Criteria

- The requirement "Protect confidential files on operating system or server" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
