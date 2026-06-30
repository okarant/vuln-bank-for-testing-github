---
name: t2605-validate-database-traffic
description: To protect against protocol vulnerabilities: - Parse and validate all database traffic to make sure it's well-formed and is what you're expecting. Block anything that doesn't match what should be coming. This way, you can mitigate the effec
---

# T2605: Validate database traffic

**Category:** INFRA  
**SD Elements:** [T2605](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2605/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To protect against protocol vulnerabilities:

- Parse and validate all database traffic to make sure it's well-formed and is what you're expecting. Block anything that doesn't match what should be coming. This way, you can mitigate the effects of forged packets and other attacks.
- Configure your network and servers to use more secure variants of protocols, such as IPsec instead of IP, DNSsec instead of DNS, and SBGP instead of BGP.


Use multiple firewalls:

- One way to help protect your databases is to separate your development, testing, and production databases, is to host them on separate servers, each firewalled from the other. If this is not possible you should, at minimum, separate testing and development from production via an internal firewall. This is a different firewall from the one screening incoming requests from the Internet to the production server.

## Success Criteria

- The requirement "Validate database traffic" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
