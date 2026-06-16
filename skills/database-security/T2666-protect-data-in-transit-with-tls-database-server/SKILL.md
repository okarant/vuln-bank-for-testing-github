---
name: t2666-protect-data-in-transit-with-tls-database-server
description: Transport Layer Security (TLS, sometimes known as SSL), encrypts network communication between a client and the database. To ensure a secure deployment, follow these guidelines: - TLS must be __required__ for all remote database connections
---

# T2666: Protect data in transit with TLS (Database Server)

**Category:** INFRA  
**SD Elements:** [T2666](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2666/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Transport Layer Security (TLS, sometimes known as SSL), encrypts network communication between a client and the database. To ensure a secure deployment, follow these guidelines:
- TLS must be __required__ for all remote database connections (not just enabled).
- TLS connections should require a minimum version of TLS 1.2, as earlier versions have known weaknesses.
- It must not be possible to circumvent TLS by connecting with an alternate, less secure protocol.

## Success Criteria

- The requirement "Protect data in transit with TLS (Database Server)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
