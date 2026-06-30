---
name: t2277-test-to-confirm-the-use-of-an-account-and-identity-managem
description: Test to confirm that the account management system is capable of organizing user and service accounts (service accounts are used for software processes and devices). This test __fails__ if the answer to any of following questions is no: - C
---

# T2277: Test to confirm the use of an account and identity management system

**Category:** INFRA  
**SD Elements:** [T2277](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2277/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Why Not Directly Code-Fixable in This Repository

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Test to confirm that the account management system is capable of organizing user and service accounts (service accounts are used for software processes and devices). This test __fails__ if the answer to any of following questions is no:

- Can the system add, remove, disable, modify, and activate accounts in accordance with the organization's requirements and procedures?
- Can the system identify and select the types of accounts in use when there is an organizational need?
- Does the system assign account managers for each account?
- Does the system control and manage authenticators that can be any combination of passwords, tokens, and cryptographic keys?
- Can the system create conditions for accounts, assign roles to them, and create groups of accounts? 
- Can the system give permissions to accounts, roles, or groups of accounts? 
- Can the system verify account creation requests based on organizational roles?
- Does the system keep track of account usage and notify account managers within a proper period of time when:
    - Accounts are no longer required.
    - Users are terminated or transferred.
    - Knowledge of individual information system usage or individual account changes is needed.
- Does the system support information access authorization based upon:
    - Valid access authorization.
    - Intended system usage.
    - Attributes as required by the organization, associated missions or other business functions.
- Can the system analyze accounts for compliance with account management requirements that adhere to an organization-defined policy? 
- Can the system create a process for reissuing shared/group account credentials (if deployed) when accounts are removed from the group?
- Are default authenticators or passwords modified after the first installation of the system?
- Are default accounts that are only used for installation removed after the installation of the system?

## Success Criteria

- The requirement "Test to confirm the use of an account and identity management system" is documented with an owner and an infrastructure/process plan.

**Status:** Documented
