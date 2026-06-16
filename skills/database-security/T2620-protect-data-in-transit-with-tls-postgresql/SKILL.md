---
name: t2620-protect-data-in-transit-with-tls-postgresql
description: Verify that TLS is enabled for PostgreSQL by running this query: SELECT * FROM pg_stat_ssl; If TLS is not enabled, all rows will be `null`, except `ssl`, which will be `f` (false). Enabling TLS requires several steps, including creating cer
---

# T2620: Protect data in transit with TLS (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2620](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2620/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that TLS is enabled for PostgreSQL by running this query:

	SELECT * FROM pg_stat_ssl;

If TLS is not enabled, all rows will be `null`, except `ssl`, which will be `f` (false).

Enabling TLS requires several steps, including creating certificates and setting the following properties in the __PostgreSQLql.conf__ file:
- `ssl = on`
- `ssl_min_protocol_version = 'TLSv1.3'` (to force clients to use TLS v1.3 or newer, as older versions are deprecated as insecure)
- `ssl_cert_file` and `ssl_key_file` to point to your server certificate and key file

A full walkthrough of TLS configuration instructions is available in the PostgreSQL documentation at https://www.PostgreSQLql.org/docs/current/ssl-tcp.html.

## Note
TLS is recommended to protect all connections, even over internal networks.

## Success Criteria

- The requirement "Protect data in transit with TLS (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
