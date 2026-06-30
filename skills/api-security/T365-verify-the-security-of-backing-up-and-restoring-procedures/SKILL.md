---
name: t365-verify-the-security-of-backing-up-and-restoring-procedures
description: Follow these guidelines to verify that backup/restore procedures are reliable and secure: - Create backups with different types of data. - For example, system data, user data, and so on. - Restore the data/system, and test if the system wor
---

# T365: Verify the security of backing up and restoring procedures

**Category:** INFRA  
**SD Elements:** [T365](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T365/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Why Not Directly Code-Fixable in This Repository

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Follow these guidelines to verify that backup/restore procedures are reliable and secure:

- Create backups with different types of data.
    - For example, system data, user data, and so on.
    - Restore the data/system, and test if the system works properly and the data is restored.
    - This test __fails__ if the system does not work as intended, or the data is not restored.
 
- Interrupt the backing up process and check if it can be resumed/restarted.
    - This simulates an uncontrolled abrupt interruption, such as a power failure.
    - This test __fails__ if the backing up process cannot resume or restart.

- Verify that the same rules are applied to backup data as the original data.
    - For example, make sure that confidential data in the backups are treated in the same way as the original data (such as passwords, credit card numbers, and social insurance numbers). 

- Work with developers to verify that confidential data in transit is only sent over a secure communication channel.
    - For example, use the TLS protocol to send data securely.

- Work with developers to verify that the backup/restore server is authenticated before a data transfer.

## Success Criteria

- The requirement "Verify the security of backing up and restoring procedures" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
