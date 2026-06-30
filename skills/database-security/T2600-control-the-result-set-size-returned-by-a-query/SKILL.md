---
name: t2600-control-the-result-set-size-returned-by-a-query
description: - Control the size of the result set returned from the database to the application for sensitive queries and stored procedures. - Program your application to display an error message or roll back a transaction if a query produces more resul
---

# T2600: Control the result set size returned by a query

**Category:** CODE_FIX  
**SD Elements:** [T2600](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2600/)  
**Priority:** 7  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

- Control the size of the result set returned from the database to the application for sensitive queries and stored procedures.

- Program your application to display an error message or roll back a transaction if a query produces more results than the limit.

Refer to your database documentation for guidance on how to manage the size of result sets

## Success Criteria

- The control "Control the result set size returned by a query" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
