---
name: t2599-protect-against-connection-string-parameter-pollution
description: This is an attack where an attacker finds out what's in a connection string and then appends their own parameters to the string. Using this technique, an attacker may be able to connect to a different data source, such as another database o
---

# T2599: Protect against connection string parameter pollution

**Category:** CODE_FIX  
**SD Elements:** [T2599](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2599/)  
**Priority:** 9  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Required Fix

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

## Implementation Guidance (SD Elements)

This is an attack where an attacker finds out what's in a connection string and then appends their own parameters to the string. Using this technique, an attacker may be able to connect to a different data source, such as another database on your network, and in the process completely bypass your authentication mechanisms, turn off encryption, and more.

Databases such as MySQL do not include built-in functionality for creating secure connection strings. To prevent parameter pollution, use other techniques on the web server, such as:

1. Avoid hardcoding the connection string into your application or web pages.
2. Don't construct connection strings based on user input. If you're using an enterprise database such as Oracle or Microsoft SQL Server, you can use built-in functionality to create connections securely. In Oracle, use the Integrated Security functionality. In Microsoft environments, you can use connection builder classes like the ones for .NET
3. Ensure the connection string is not visible in the URL.
4. Validate incoming connection strings
4. Filter out the semicolon character, which could be used to append new parameters at the end of the string, and escape potentially malicious characters
3. Ensure that the application does not log connection strings. If they are logged for debugging or troubleshooting purposes, remove them.
4. If connection strings are stored in configuration files or other resources on the file system, set proper permissions and restrict access to them.

Consult your product documentation for specific steps to build secure connection strings.

## Success Criteria

- The control "Protect against connection string parameter pollution" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
