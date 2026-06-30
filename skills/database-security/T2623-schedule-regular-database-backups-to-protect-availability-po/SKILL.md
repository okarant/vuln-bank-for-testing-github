---
name: t2623-schedule-regular-database-backups-to-protect-availability
description: PostgreSQL includes the __pg_dump__ utility for creating backups. Ensure that you are using a tool like __crontab__ to schedule __pg_dump__ or another utility to make regular backups. ## Note Backups are a key aspect of disaster recovery. Y
---

# T2623: Schedule regular database backups to protect availability (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2623](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2623/)  
**Priority:** 6  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

PostgreSQL includes the __pg_dump__ utility for creating backups. Ensure that you are using a tool like __crontab__ to schedule __pg_dump__ or another utility to make regular backups.

## Note
Backups are a key aspect of disaster recovery. You should also follow these best practices:
- Validate your backup. Follow a documented process to test that the backup process works correctly and a backup can be successfully restored to a new server.
- Use a dedicated database user account for backup operations, with appropriately limited permissions (for example, no ability to modify records). Protect the credentials of this account.
- Protect backup files in their new location (for example, with file access permissions and file system encryption).
- Have a documented disaster recovery plan, which may include backups and other measures to protect availability.

## Success Criteria

- The requirement "Schedule regular database backups to protect availability (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
