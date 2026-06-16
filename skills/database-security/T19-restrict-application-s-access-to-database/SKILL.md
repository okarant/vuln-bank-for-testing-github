---
name: restrict-applications-access-to-database
description: Limit an application’s database privileges (schemas, tables, actions, routines) to least privilege; use when code uses over-privileged DB accounts or can reach non-application data.
---

# Restrict Application's Access to Database

## What This Skill Does
Enforces least privilege between an application and its database. It helps the assistant detect when an app uses over-privileged or generic DB accounts, touches non-application tables/schemas, performs DDL or admin operations at runtime, or can call arbitrary stored routines. The skill then steers fixes toward using a restricted app account, separating runtime vs. migration/admin access, whitelisting tables and routines, and making critical tables append/read-only from application code.

## Decision Table
| Situation | Action |
|-----------|--------|
| App connects with a generic/admin DB user (e.g., `root`, `sa`, `dbo`, shared service account) for normal requests | Introduce an application-specific low-privilege account; verify DB username in code and fail fast if it’s not the expected app user; separate runtime and migration/admin connections |
| Same DB connection or ORM context can read/write tables outside the app’s core schema (e.g., `admin_audit`, system or other app tables) | Restrict ORM mappings to an app-specific schema; add a whitelist of allowed tables; refactor code to stop accessing non-application tables; in some cases separate into distinct databases |
| Application code executes DDL or admin operations at runtime (e.g., `CREATE/DROP/ALTER`, role/permission changes) | Move schema/admin operations into migration tooling or dedicated admin services; ensure runtime code and its DB user lack DDL/admin privileges; replace generic “run any SQL” helpers with narrow repositories/DAOs |
| Stored procedures/functions are called with dynamic names or from generic “execute arbitrary routine” helpers | Introduce a whitelist/registry of allowed routines; block dynamic routine dispatch from user input; avoid or refactor wrappers that can invoke arbitrary DB/system routines |
| App reads or modifies highly sensitive/audit tables with full CRUD | Encapsulate access in append-only or read-only components; remove `UPDATE`/`DELETE` operations from application behavior; ensure the app account has only the minimal rights (often `SELECT` or `INSERT` only) on those tables |

## Boundaries

### Can Do
- Detect and refactor code that uses over-privileged DB accounts into separate runtime vs. migration/admin connections, with explicit checks on the effective DB user.
- Guide creation of table/schema whitelists and repository/DAO layers so only approved tables and CRUD operations are exposed to application code.
- Help wrap or replace generic SQL/stored-procedure execution helpers with narrow, business-focused functions and append-only patterns for critical data.

### Cannot Do
- Cannot actually change DB roles, GRANT/REVOKE permissions, or server configuration; it can only produce code/config changes and SQL examples for humans/DBAs to apply.
- Cannot infer the correct minimal privilege set without some human/domain input (which tables/actions are truly required); it can only make conservative recommendations based on code usage.
- Cannot guarantee full isolation when the physical DB topology is fixed (e.g., mandatory shared schema in a legacy system); it can only approximate least privilege within those limits.

## Gotchas
- Mixing migration/admin logic with runtime code: Keeping migrations or admin utilities in the same process or connection pool tempts developers to reuse admin credentials in normal paths; always separate processes/config and verify the effective DB user in runtime code.
- Relying on “parameterized queries” alone: Parameterization prevents injection, but if the DB user is over-privileged, an attacker who reaches a query still gains excessive power; fix requires both safe queries and restricted privileges.
- Whitelists that silently fall back: Implementing a table/routine whitelist but falling back to a default or “best guess” on miss defeats the protection; lookups must fail hard (exceptions) for anything not explicitly allowed.

## Quick Verification
```bash
# 1. Run vulnerable example and observe over-privileged behavior
python app_vulnerable_code.py
# Expect: normal notes output + actual contents of admin_audit exported

# 2. Run fixed example and confirm restricted access
python app_fix_human_code.py
# Expect: normal notes output + message like:
# "admin_audit export is not available to the application account"

# 3. Simulate an attack trying to access non-application data (conceptual)
# For real DBs (e.g., PostgreSQL/MySQL), try a query as the app user:
psql "$APP_RUNTIME_DSN" -c "SELECT * FROM admin_audit;" || echo "Access correctly denied"

# 4. Grep for risky patterns (project-level hygiene)
grep -R --line-number -E "CREATE TABLE|DROP TABLE|ALTER TABLE|GRANT |REVOKE |admin_audit|xp_cmdshell" .
```