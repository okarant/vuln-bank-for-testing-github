---
name: t2614-verify-database-traffic-is-validated
description: To protect against protocol vulnerabilities: - Verify that all database traffic is parsed and validated to ensure it is well-formed and matches the expected format. Ensure that anything that does not match what should be coming is blocked. 
---

# T2614: Verify database traffic is validated

**Category:** INFRA  
**SD Elements:** [T2614](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2614/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To protect against protocol vulnerabilities:

- Verify that all database traffic is parsed and validated to ensure it is well-formed and matches the expected format. Ensure that anything that does not match what should be coming is blocked.

- Verify that the network and servers are configured to use more secure variants of protocols, such as IPsec instead of IP, DNSsec instead of DNS, and SBGP instead of BGP.


The use of firewalls:

- Verify if the development, testing, and production databases are separated, hosted on separate servers, and each one is firewalled from the other. If this is not possible, at minimum, testing and development are separated from production via an internal firewall. This firewall should be different from the one screening incoming requests from the Internet to the production server.

## Success Criteria

- The requirement "Verify database traffic is validated" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
