---
name: t364-enable-secure-backup-and-restore-capabilities
description: Follow these guidelines to develop or set up secure backup and restore capabilities: - Decide on the __types of data__ that need to be included in the backups. - Such as user data, system data, and so on. - Apply the same rules to backup da
---

# T364: Enable secure backup and restore capabilities

**Category:** INFRA  
**SD Elements:** [T364](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T364/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Why Not Directly Code-Fixable in This Repository

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Follow these guidelines to develop or set up secure backup and restore capabilities:

- Decide on the __types of data__ that need to be included in the backups.
    - Such as user data, system data, and so on.

- Apply the same rules to backup data as the original data.
    - For example, make sure that confidential data (passwords, credit card numbers and social insurance numbers) in the backups are treated in the same way as the original data.

- Decide on the location of the backup data (usually a server if applicable) and secure the communication channel to the server (use secure protocols such as TLS).
    - __Authenticate__ the backup server before sending backup data to and loading data from it.

- If system recovery is implemented, restore the system to a __secure state__ after a failure.
    - Identify the minimum data, system parameters, security parameters, and security patches to achieve this goal.

- Devise a means to __resume or restart backup__ when the process fails.
    - Because of a power failure, for example.

## Success Criteria

- The requirement "Enable secure backup and restore capabilities" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
