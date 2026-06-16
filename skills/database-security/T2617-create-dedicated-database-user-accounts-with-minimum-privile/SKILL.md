---
name: t2617-create-dedicated-database-user-accounts-with-minimum-privi
description: Ensure that applications connect to the database with an appropriately limited user account. - Use a different database user account for each application and use. Every account should serve only one purpose. - Give each account the permissi
---

# T2617: Create dedicated database user accounts with minimum privileges (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2617](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2617/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Ensure that applications connect to the database with an appropriately limited user account.

- Use a different database user account for each application and use. Every account should serve only one purpose.
- Give each account the permissions for just those databases that it needs to interact with.
- Never use the `PostgreSQL` superuser account for application access or give an application a role with the `SUPERUSER` attribute.
- Do not grant permissions to an application account that it does not require. For example, an application will commonly need `SELECT`, `INSERT`, and `UPDATE` permissions, but not `DELETE` (for records) and `CREATE`, `DROP`, and `ALTER` (for database objects).
- Do not make the application account the owner of any database objects.
- Create roles to apply minimum permissions to multiple users.
- Use the PostgreSQL predefined roles to assign common permission sets for back-end tasks. For example, `pg_read_all_data` gives permission to read all tables for all databases. This allows certain types of reporting and analysis tasks without encouraging the use of a more powerful (and therefore dangerous) administrative account. The complete list of PostgreSQL predefined roles is in the documentation at https://www.PostgreSQLql.org/docs/current/predefined-roles.html

## Note
Consider auditing all database user accounts to ensure they use the correct permissions. You can retrieve a list of users with the role information for each one using the `psql \du+` command.

## Success Criteria

- The requirement "Create dedicated database user accounts with minimum privileges (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
