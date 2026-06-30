---
name: t2662-restrict-network-access-to-the-database-server
description: To reduce the attack surface of your system, limit network access to the database server. Potential measures include: - Configuring firewall rules to allow traffic only for authorized IP addresses and ports - Using network segmentation to p
---

# T2662: Restrict network access to the database server

**Category:** INFRA  
**SD Elements:** [T2662](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2662/)  
**Priority:** 10  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To reduce the attack surface of your system, limit network access to the database server. Potential measures include:
- Configuring firewall rules to allow traffic only for authorized IP addresses and ports
- Using network segmentation to place the database server in a more secure environment
- Applying product-specific features in your database that limit network connectivity
- Using features like Private Link to isolate database services in a cloud environment

## Success Criteria

- The requirement "Restrict network access to the database server" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
