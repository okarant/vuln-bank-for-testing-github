---
name: t340-use-an-account-and-identity-management-system
description: Develop, set up, or use an account management system that enables the organization of user accounts, as well as service accounts (non-human accounts for software processes and devices that use the system). Such a system provides the capabil
---

# T340: Use an account and identity management system

**Category:** INFRA  
**SD Elements:** [T340](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T340/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Why Not Directly Code-Fixable in This Repository

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Develop, set up, or use an account management system that enables the organization of user accounts, as well as service accounts (non-human accounts for software processes and devices that use the system).

Such a system provides the capability to:

- Add, remove, disable, modify and activate accounts in accordance with organization-defined procedures or conditions.
- Identify and select the types of accounts used to support organizational mission/business functions.
- Assign account managers for accounts.
- Manage authenticators and combinations of authenticators, such as passwords, tokens, symmetric keys, private keys, biometrics, physical keys, and key cards.
- Define roles or groups of accounts (if applicable), and establish conditions for membership.
- Assign permissions to individual accounts, to roles, or to groups of accounts.
- Manage approvals by organization-defined personnel or roles when a request to create accounts is received.
- Monitor the use of accounts.
    - Verify the user identity before modifying any authentication factor.
- Notify account managers within a time-period proper for each situation when:
    - Accounts are no longer required.
    - Users are terminated or transferred.
    - Individual information system usage or need-to-know changes for an individual.
- Authorize access to the information system based on:
    - A valid access authorization.
    - Intended system usage.
    - Other attributes as required by the organization or associated missions/business functions.
- Review accounts for compliance with account management requirements with a frequency mandated by your organization.
    - Implementing an automatic report generation mechanism may help with the reviewing process.
- Establish a process for reissuing shared/group account credentials (if deployed) when accounts are removed from the group.
- Train users about security practices that will keep their accounts safe. This includes choosing strong authentication factors, protecting passwords, avoiding password reuse, and avoiding phishing attacks.

- Deny all access by __default__.

__Note__: Default authenticators (passwords) that are used for installation of the system should be modified after the first installation. Unused default accounts that are only necessary for installation should be removed after the first installation of the system.

## Success Criteria

- The requirement "Use an account and identity management system" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
