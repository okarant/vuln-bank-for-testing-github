---
name: t2602-log-typical-database-and-server-activities-and-related-met
description: Individual logging requirements will be different depending on the regulatory and compliance requirements, business needs, and other factors that affect your organization. At a minimum, you would typically log these database and server acti
---

# T2602: Log typical database and server activities and related metadata

**Category:** INFRA  
**SD Elements:** [T2602](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2602/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Individual logging requirements will be different depending on the regulatory and compliance requirements, business needs, and other factors that affect your organization. At a minimum, you would typically log these database and server activities:

- Startup
- Shutdown
- Pause
- Commit and rollback transactions
- Default database logging
- All SQL commands
- Changes to database and server configurations
- Changes to data

In addition to logging events, log metadata information about each event. This helps trace an event back to its origin. Logs that only provide summaries are not useful when you audit for suspicious activity. At a minimum, you should log the following information about events in the log:

- Values
- Names
- IDs

## Success Criteria

- The requirement "Log typical database and server activities and related metadata" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
