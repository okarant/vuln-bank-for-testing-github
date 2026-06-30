---
name: t2664-create-dedicated-database-user-accounts-with-minimum-privi
description: Ensure that applications and users connect to the database with appropriately limited user accounts. Follow these guidelines: - Use a different database user account for each application and use. Every account should serve only one purpose.
---

# T2664: Create dedicated database user accounts with minimum privileges (Database Server)

**Category:** INFRA  
**SD Elements:** [T2664](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2664/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Ensure that applications and users connect to the database with appropriately limited user accounts. Follow these guidelines:

- Use a different database user account for each application and use. Every account should serve only one purpose.
- Give each account the permissions for just those databases that it needs to interact with.
- Do not grant permissions for data definition and data manipulation operations the application does not use.
- Do not use root, superuser, or administrator accounts for application access.
- If the database supports role-based authorization, apply permissions with roles rather than on individual users.

## Success Criteria

- The requirement "Create dedicated database user accounts with minimum privileges (Database Server)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
