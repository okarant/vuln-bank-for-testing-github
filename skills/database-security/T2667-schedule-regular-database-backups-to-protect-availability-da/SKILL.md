---
name: t2667-schedule-regular-database-backups-to-protect-availability
description: Backups are a key aspect of disaster recovery. Configure your database to regularly back up all data, including database schema, the actual records, transaction logs, encryption keys, and metadata (such as user lists and configuration infor
---

# T2667: Schedule regular database backups to protect availability (Database Server)

**Category:** INFRA  
**SD Elements:** [T2667](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2667/)  
**Priority:** 6  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Backups are a key aspect of disaster recovery. Configure your database to regularly back up all data, including database schema, the actual records, transaction logs, encryption keys, and metadata (such as user lists and configuration information). 

Additionally, follow these best practices:
- Validate your backup. Follow a documented process to test that the backup process works correctly and a backup can be successfully restored to a new server.
- Ensure backup data is encrypted.
- Use a dedicated database user account for backup operations, with appropriately limited permissions (for example, no ability to modify records). Protect the credentials of this account.
- Protect backup files in their new location (for example, with file access permissions).
- Have a documented disaster recovery plan, which may include backups and other measures to protect availability, like replication.

## Success Criteria

- The requirement "Schedule regular database backups to protect availability (Database Server)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
