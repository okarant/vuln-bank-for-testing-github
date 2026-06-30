---
name: t2597-implement-rbac-instead-of-individual-accounts
description: Role-based access control (or RBAC) assigns permissions to the role rather than to individual accounts. Users or accounts that are added to a role inherit permissions assigned to that role. Role-based access control helps you manage your ap
---

# T2597: Implement RBAC instead of individual accounts

**Category:** INFRA  
**SD Elements:** [T2597](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2597/)  
**Priority:** 10  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Role-based access control (or RBAC) assigns permissions to the role rather than to individual accounts. Users or accounts that are added to a role inherit permissions assigned to that role. Role-based access control helps you manage your applications, users, and database security.

Best practices for assigning permissions include:

- Deny access by default to all accounts, services, and processes.
- Grant access on an as-needed basis using the principle of least privilege. That is, only grant whatever access is needed for the user, system, or process to perform the task.
- Set privileges for roles as granularly as possible.

## Success Criteria

- The requirement "Implement RBAC instead of individual accounts" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
