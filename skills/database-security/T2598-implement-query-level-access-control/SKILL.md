---
name: t2598-implement-query-level-access-control
description: Query-level access control helps you restrict access to query operations, stored procedures, tables, rows, columns, and other database objects. Essentially, it allows users, roles, and groups to access database objects by configuring permis
---

# T2598: Implement query-level access control

**Category:** CODE_FIX  
**SD Elements:** [T2598](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2598/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

Query-level access control helps you restrict access to query operations, stored procedures, tables, rows, columns, and other database objects. Essentially, it allows users, roles, and groups to access database objects by configuring permissions for the objects themselves, rather than for the user accounts or roles.

- Create a chart listing all users, roles, processes, or systems that may require access to your database.
- List the resources each of these accounts will need from your application, including specific databases, tables, columns, and stored procedures they need to access.
- Determine read, write, delete, and update permissions for databases, tables, and other objects, even cells containing sensitive information needed for each role, and deny excessive privileges.

## Success Criteria

- The control "Implement query-level access control" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
