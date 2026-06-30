---
name: t2616-use-a-secure-authentication-mechanism-for-database-connect
description: To ensure a secure configuration, verify that the access rules in __pg.hba.conf__ follow these guidelines: - Do not use the authentication methods `trust`, `password`, or `ident`. - Prefer `scram-sha-256` to `md5` for password-based authent
---

# T2616: Use a secure authentication mechanism for database connections (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2616](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2616/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To ensure a secure configuration, verify that the access rules in __pg.hba.conf__ follow these guidelines:
- Do not use the authentication methods `trust`, `password`, or `ident`.
- Prefer `scram-sha-256` to `md5` for password-based authentication, because MD5 is vulnerable to packet replay attacks. However, if you change an existing database, you must first update the `password_encryption` setting in the __PostgreSQLql.conf__ file and require all users to create new passwords.
- Do not allow remote access to the administration account unless required.

## Success Criteria

- The requirement "Use a secure authentication mechanism for database connections (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
