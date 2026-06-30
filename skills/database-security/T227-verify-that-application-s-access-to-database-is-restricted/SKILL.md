---
name: t227-verify-that-application-s-access-to-database-is-restricted
description: Use the following guidelines to verify that an application's access to the database is restricted: 1. Review source code to determine the account that the application uses to connect to its database at runtime. - For example, the applicatio
---

# T227: Verify that application's access to database is restricted

**Category:** CODE_FIX  
**SD Elements:** [T227](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T227/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

Use the following guidelines to verify that an application's access to the database is restricted:

1. Review source code to determine the account that the application uses to connect to its database at runtime. 
    - For example, the application has an id 'bank_app' that it uses to connect to the database.

    This test __fails__ if the application uses a database super-user account, such as 'sa' (System Administrator).

2. Review the database permissions for the user identified in step 1.

    This test __fails__ if the user has more permissions than it requires.
        - Common examples of excessive permissions include the ability to drop tables, alter the database schema, or execute unnecessary prepared statements.

__Note__: This verification countermeasure requires access to source code and a fair understanding of the source code structure.

## Success Criteria

- The control "Verify that application's access to database is restricted" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
