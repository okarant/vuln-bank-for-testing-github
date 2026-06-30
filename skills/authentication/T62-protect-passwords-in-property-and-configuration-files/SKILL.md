---
name: t62-protect-passwords-in-property-and-configuration-files
description: Server applications often store plaintext system passwords and keys in configuration files. For example, several frameworks use plaintext configuration files for database connection strings, database encryption keys, Lightweight Directory A
---

# T62: Protect passwords in property and configuration files

**Category:** CODE_FIX  
**SD Elements:** [T62](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T62/)  
**Priority:** 6  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Server applications often store plaintext system passwords and keys in configuration files. For example, several frameworks use plaintext configuration files for database connection strings, database encryption keys, Lightweight Directory Access Protocol (LDAP) connection strings, keystore passwords, and other values. Attackers who are able to exploit separate vulnerabilities may be able to view the contents of these files.

Always encrypt credentials in property files. In particular, __avoid specifying empty password strings__ in connection strings and in configuration files, such as LDAP or database connection parameters.

Unfortunately, the weakness introduced by providing a password or key to decrypt encrypted credentials still exists. While no solution is perfect, use one of the following password and key storage options:

- At the very least, **store a private key** unique to each machine as a binary file that can only be accessed by the application server. 
    - While this control succeeds in preventing attackers from viewing plaintext passwords in configuration files, it does not prevent attackers from first accessing the binary key and then the configuration file using the same exploit. 
- **Store the decryption key or password** in a file, similar to the first option. 
    - Use operating system controls to ensure that the file is only accessible by a separate launching process and not by the application server. 
    - The launching process can then pass the key and password as a command-line argument when launching the application server. 
    - This way, a user who exploits the application server may not necessarily have access to the decryption key itself.
- **Support passphrases** from an environment variable or web form.
    - This solution takes more work and may require manual intervention, but it also greatly reduces the risk of an attacker finding plaintext passwords in configuration files.

## Success Criteria

- The control "Protect passwords in property and configuration files" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Applied
