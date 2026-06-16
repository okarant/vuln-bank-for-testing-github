---
name: t2607-verify-query-level-access-control-is-implemented
description: Verify that access to your database is limited to users, roles, processes, or systems that require it, and ensure that they only have access to the specific databases, tables, columns, and stored procedures they need.
---

# T2607: Verify query-level access control is implemented

**Category:** CODE_FIX  
**SD Elements:** [T2607](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2607/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

Verify that access to your database is limited to users, roles, processes, or systems that require it, and ensure that they only have access to the specific databases, tables, columns, and stored procedures they need.

## Success Criteria

- The control "Verify query-level access control is implemented" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
