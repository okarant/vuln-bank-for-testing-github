---
name: t2601-use-transparent-data-encryption-with-enterprise-databases
description: Enterprise databases like Oracle, Microsoft SQL Server, and IBM employ Transparent Data Encryption (TDE) to safeguard sensitive data. TDE allows for seamless decryption during access, managed through the database's administrative interface.
---

# T2601: Use Transparent Data Encryption with Enterprise Databases

**Category:** INFRA  
**SD Elements:** [T2601](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2601/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Enterprise databases like Oracle, Microsoft SQL Server, and IBM employ Transparent Data Encryption (TDE) to safeguard sensitive data. TDE allows for seamless decryption during access, managed through the database's administrative interface. It protects against network attacks and theft of storage media by ensuring data remains encrypted until accessed by authorized users, enhancing overall security.

- Enable TDE for entire tables, columns within a table, and or individual cells within a table when appropriate. 

Note: TDE is implemented differently in each enterprise database product. Check the documentation to find out how to implement it in your environment.

## Success Criteria

- The requirement "Use Transparent Data Encryption with Enterprise Databases" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
