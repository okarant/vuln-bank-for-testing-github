---
name: t2611-verify-that-typical-database-and-server-activities-along-w
description: Verify at least the following database and server activities are logged at a minimum: - Startup - Shutdown - Pause - Commit and rollback transactions - Default database logging - All SQL commands - Changes to database and server configurati
---

# T2611: Verify that typical database and server activities, along with related metadata, are logged

**Category:** INFRA  
**SD Elements:** [T2611](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2611/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify at least the following database and server activities are logged at a minimum:

- Startup
- Shutdown
- Pause
- Commit and rollback transactions
- Default database logging
- All SQL commands
- Changes to database and server configurations
- Changes to data

Also, verify that the following information about events is logged for each activity:

- Values
- Names
- IDs

## Success Criteria

- The requirement "Verify that typical database and server activities, along with related metadata, are logged" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
