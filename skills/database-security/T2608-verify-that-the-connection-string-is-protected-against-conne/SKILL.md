---
name: t2608-verify-that-the-connection-string-is-protected-against-con
description: Verify the following: - Connection strings are not hard-coded into the application or web pages. - Connection strings are not constructed based on user input. - Ensure the connection strings are not visible in the URLs. - Verify that incomi
---

# T2608: Verify that the connection string is protected against connection string parameter pollution

**Category:** CODE_FIX  
**SD Elements:** [T2608](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2608/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

Verify the following:

- Connection strings are not hard-coded into the application or web pages.

- Connection strings are not constructed based on user input.

- Ensure the connection strings are not visible in the URLs.

- Verify that incoming connection strings are validated before use. The semicolon character is filtered out and potentially malicious characters are escaped.

- Verify that the application does not log connection strings. 

- Verify that configuration files or other resources on the file system containing connection strings are secure, and proper access control is set for them.

## Success Criteria

- The control "Verify that the connection string is protected against connection string parameter pollution" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
