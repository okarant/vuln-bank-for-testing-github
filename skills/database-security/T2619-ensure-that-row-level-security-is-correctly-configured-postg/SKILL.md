---
name: t2619-ensure-that-row-level-security-is-correctly-configured-pos
description: Row-level security restricts users so they can access only a specific subset of the rows in a table. To review which tables use RLS, execute this query: SELECT oid, relname, relrowsecurity FROM pg_class WHERE relrowsecurity IS TRUE; If a ta
---

# T2619: Ensure that row-level security is correctly configured (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2619](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2619/)  
**Priority:** 7  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Row-level security restricts users so they can access only a specific subset of the rows in a table. To review which tables use RLS, execute this query:

	SELECT oid, relname, relrowsecurity FROM pg_class WHERE relrowsecurity IS TRUE;

If a table should have an RLS policy but is not in this list, you will need to `ALTER` the table to apply the policy. To review the details of specific RLS policies, query the `pg_policy` system table.

Additionally, you must review user accounts to ensure that they do not grant `Bypass RLS`, which overrides RLS policy. Use `psql \du+` to check accounts for the `Bypass RLS` attribute. You can remove the `Bypass RLS` attribute with a command like this:

	ALTER ROLE <some-user> NOBYPASSRLS;

## Note
You create RLS policies using the `CREATE POLICY` command. A typical RLS policy restrics row access by matching a field against the name of the current user account. A slightly more elaborate process is to use a function that finds a piece of information related to the current user. This example limits `SELECT` operations to rows that match the current user's organization:

    CREATE POLICY emp_access_policy
    ON employees
    FOR SELECT
    USING (org_id =
    current_setting('app.current_user_org_id')::int);

More details about configuring RLS policies is in the official PostgreSQL documentation at https://www.PostgreSQLql.org/docs/current/ddl-rowsecurity.html

## Success Criteria

- The requirement "Ensure that row-level security is correctly configured (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
