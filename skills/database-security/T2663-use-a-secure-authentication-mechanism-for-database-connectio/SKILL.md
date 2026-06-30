---
name: t2663-use-a-secure-authentication-mechanism-for-database-connect
description: When a user or application connects to the database, they must authenticate over a secure protocol that: - Does not risk revealing account credentials - Is not subject to common exploit types, such as brute force password guessing or on-pat
---

# T2663: Use a secure authentication mechanism for database connections

**Category:** INFRA  
**SD Elements:** [T2663](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2663/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

When a user or application connects to the database, they must authenticate over a secure protocol that:
- Does not risk revealing account credentials
- Is not subject to common exploit types, such as brute force password guessing or on-path attacks

## Success Criteria

- The requirement "Use a secure authentication mechanism for database connections" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
