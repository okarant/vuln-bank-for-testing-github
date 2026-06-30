---
name: t2621-use-file-volume-encryption-and-consider-in-database-encryp
description: PostgreSQL does not have built-in encryption. Regulations or business considerations may require at-rest encryption for your data. To satisfy this requirement, you may use these options: - Use Transparent Data Encryption (TDE). This feature
---

# T2621: Use file volume encryption and consider in-database encryption with pgcrypto (PostgreSQL)

**Category:** INFRA  
**SD Elements:** [T2621](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2621/)  
**Priority:** 8  
**Domain:** database-security

## Affected Areas in This Repository

database.py (connection pool authenticates as the Postgres superuser `postgres`), docker-compose.yml (postgres:13 service, POSTGRES_USER=postgres)

## Why Not Directly Code-Fixable in This Repository

Create a dedicated least-privilege application DB role, parameterize queries, bound result-set sizes, validate the connection string, and restrict the application's DB grants to only the tables/operations it needs.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

PostgreSQL does not have built-in encryption. Regulations or business considerations may require at-rest encryption for your data. To satisfy this requirement, you may use these options:

- Use Transparent Data Encryption (TDE). This feature is only available in EnterpriseDB's hosted version of PostgreSQL.
- Encrypt the data volume using operating system features, such as FDE (Full Disk Encryption) in Linux or BitLocker in Windows. This is recommended, but it may not be sufficient to meet security requirements, as users with OS access can bypass OS-level encryption.
- Encrypt data manually using the __pgcrypto__ extension. This adds complexity and requires you to safely store the encryption keys you use.

## Note
To check if `pgcrypto` is installed, use this command:

	SELECT * FROM pg_available_extensions WHERE name='pgcrypto'; 

To enable `pgcrypto`, use this command:

	CREATE EXTENSION pgcrypto;

Once __pgcrypto__ is enabled, you can use the `crypt` and decrypt` functions in your SQL statements. However, __pgcrypto__ is only a viable approach if you securely store and manage the keys that it uses.

## Success Criteria

- The requirement "Use file volume encryption and consider in-database encryption with pgcrypto (PostgreSQL)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
