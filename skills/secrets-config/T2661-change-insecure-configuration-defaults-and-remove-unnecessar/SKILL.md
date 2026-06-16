---
name: t2661-change-insecure-configuration-defaults-and-remove-unnecess
description: In most cases, the default configuration of a database product or its official Docker image is suitable for development purposes only. Additional steps are necessary to strengthen the security of a new deployment before it is considered pro
---

# T2661: Change insecure configuration defaults and remove unnecessary features

**Category:** INFRA  
**SD Elements:** [T2661](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2661/)  
**Priority:** 9  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Why Not Directly Code-Fixable in This Repository

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

In most cases, the default configuration of a database product or its official Docker image is suitable for development purposes only. Additional steps are necessary to strengthen the security of a new deployment before it is considered production ready. These may include:

- Disabling unnecessary features or plugins
- Restricting unnecessary connectivity (such as ports)
- Removing test databases
- Removing or renaming the default administrator or superuser accounts
- Configuring (and requiring) secure authentication
- Creating database users with limited permissions
- Modifying miscellaneous permissive settings

## Success Criteria

- The requirement "Change insecure configuration defaults and remove unnecessary features" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
