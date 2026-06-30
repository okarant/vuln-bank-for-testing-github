---
name: t2652-consider-adding-plugins-for-stronger-authentication-protoc
description: The default configuration of MariaDB authentication uses the `mysql_native_password` plugin. It provides moderately strong password hashes using `SHA-1`. However, additional steps are recommended to increase authentication security: - Repla
---

# T2652: Consider adding plugins for stronger authentication protocols and stricter password complexity rules (MariaDB)

**Category:** INFRA  
**SD Elements:** [T2652](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2652/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Why Not Directly Code-Fixable in This Repository

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

The default configuration of MariaDB authentication uses the `mysql_native_password` plugin. It provides moderately strong password hashes using `SHA-1`. However, additional steps are recommended to increase authentication security:

- Replace the default __mysql_native_password__ plugin with MariaDB's __ed25519__, or another plugin for a specific authentication protocol. Authentication plugins are set in the __mariadb.cnf__ configuration file, but you must also use `ALTER USER` to configure user accounts to use the correct authentication plugin. The full configuration process is detailed at https://mariadb.com/kb/en/pluggable-authentication-overview/
- Enforce password complexity rules with MariaDB's 
__simple_password_check__ and __cracklib_password_check__ plugins. They add common password weakness checks (rejecting known compromised passwords, passwords that repeat a single character or match a dictionary word, and so on). You can check if these plugins are active with the `SHOW PLUGINS;` query or review all your password settings with this query:


	SHOW VARIABLES LIKE '%pass%';

- Consider applying a password timeout by setting `default_password_lifetime` to a value other than `0`. For example, a value of `365` requires a new password after one year.
- Manually lock old or temporarily unused user accounts using a command like this:


	ALTER USER 'sondra'@'localhost' ACCOUNT LOCK;

## Success Criteria

- The requirement "Consider adding plugins for stronger authentication protocols and stricter password complexity rules (MariaDB)" is documented with an owner and an infrastructure/process plan.

**Status:** Documented
