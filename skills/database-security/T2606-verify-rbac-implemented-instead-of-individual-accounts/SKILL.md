---
name: t2606-verify-rbac-implemented-instead-of-individual-accounts
description: Verify that RBAC (Role-Based Access Control) is implemented for accessing your databases instead of using individual accounts, and ensure that the following guidelines are followed: - By default, the Deny Access rule is set for all accounts
---

# T2606: Verify RBAC implemented instead of individual accounts

**Category:** INFRA  
**SD Elements:** [T2606](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2606/)  
**Priority:** 10  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that RBAC (Role-Based Access Control) is implemented for accessing your databases instead of using individual accounts, and ensure that the following guidelines are followed:

- By default, the Deny Access rule is set for all accounts, services, and processes.

-  Access is granted on an as-needed basis using the principle of least privilege. This means that access is granted only when necessary for the user, system, or process to perform a specific task.
- Privileges for roles are set as granularly as possible

## Success Criteria

- The requirement "Verify RBAC implemented instead of individual accounts" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
