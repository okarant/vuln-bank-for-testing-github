---
name: t2610-verify-that-transparent-data-encryption-is-utilized-with-e
description: Verify that Transparent Data Encryption (TDE) is enabled for entire tables, columns within a table, and/or individual cells within a table where appropriate. Note: TDE is implemented differently in each enterprise database product. Check th
---

# T2610: Verify that Transparent Data Encryption is utilized with Enterprise Databases

**Category:** INFRA  
**SD Elements:** [T2610](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2610/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that Transparent Data Encryption (TDE) is enabled for entire tables, columns within a table, and/or individual cells within a table where appropriate.

Note: TDE is implemented differently in each enterprise database product. Check the documentation to find out how to implement it in your environment.

## Success Criteria

- The requirement "Verify that Transparent Data Encryption is utilized with Enterprise Databases" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
