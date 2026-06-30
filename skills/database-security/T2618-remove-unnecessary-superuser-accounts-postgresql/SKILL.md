---
name: t2618-remove-unnecessary-superuser-accounts-postgresql
description: To identify roles that have the `SUPERUSER` attribute _and_ can be used to log in, use this query: SELECT rolname FROM pg_authid WHERE rolsuper and rolcanlogin; Remove unnecessary superuser permissions as follows: ALTER USER <some-user> NOS
---

# T2618: Remove unnecessary superuser accounts (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2618](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2618/)  
**Priority:** 6  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To identify roles that have the `SUPERUSER` attribute _and_ can be used to log in, use this query:

	SELECT rolname FROM pg_authid WHERE rolsuper and rolcanlogin;

Remove unnecessary superuser permissions as follows:

	ALTER USER <some-user> NOSUPERUSER;

Or if a user is granted `SUPERUSER` permissions through another role, revoke it:

	REVOKE <some-role> FROM <some-user>;

## Note
An optional best practice is to implement a privilege escalation pattern with the `set_user` extension. The idea is to:
- Remove the `LOGIN` attribute from all superuser accounts, including `PostgreSQL`.
- Give database administrators the ability to escalate to a superuser.
- Log all privilege escalation for auditing purposes.

## Success Criteria

- The requirement "Remove unnecessary superuser accounts (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
