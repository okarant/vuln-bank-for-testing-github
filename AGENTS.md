<!-- SDE-SECURITY-HARDENING-START -->
## Security Hardening Execution Contract

## Project Overview

| Property | Value |
|----------|-------|
| Application | vuln-bank-for-testing-github-app-20260616-1404 |
| SD Elements Project | [vuln-bank-for-testing-github-20260616-1404](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/) |
| Project ID | 31909 |
| Total Countermeasures | 368 |

## Countermeasure Summary by Category

| Category | Count | Description |
|----------|-------|-------------|
| CODE_FIX | 178 | Code/config changes in repo |
| ML_CODE | 36 | ML security with code to fix |
| ML_DOC | 13 | ML guidance (no ML code) |
| INFRA | 82 | External infrastructure |
| **FILE-TRACKED TOTAL** | **309** | Countermeasures with local skill files |

> **PROCESS countermeasures (59) are noted in SD Elements only -- not tracked locally.**

## Skill Files

| Domain | Countermeasures |
|--------|----------------|
| api-security | 20 |
| authentication | 30 |
| authorization | 24 |
| backup-recovery | 5 |
| container-security | 73 |
| cors | 2 |
| crypto | 12 |
| csrf | 6 |
| data-protection | 4 |
| database-security | 29 |
| dependency-management | 2 |
| file-handling | 7 |
| general-hardening | 1 |
| injection | 10 |
| input-validation | 3 |
| llm-security | 49 |
| logging-monitoring | 3 |
| network-infra | 7 |
| secrets-config | 6 |
| session-management | 8 |
| ssrf | 2 |
| xss | 6 |

### api-security
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1148 | Validate JSON files | [skills/api-security/T1148-validate-json-files/SKILL.md](./skills/api-security/T1148-validate-json-files/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T1149 | Test if JSON files are validated against malicious inputs | [skills/api-security/T1149-test-if-json-files-are-validated-against-malicious-inputs/SKILL.md](./skills/api-security/T1149-test-if-json-files-are-validated-against-malicious-inputs/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T166 | Protect against JSON hijacking | [skills/api-security/T166-protect-against-json-hijacking/SKILL.md](./skills/api-security/T166-protect-against-json-hijacking/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T167 | Test that the application is not vulnerable to JSON Hijacking | [skills/api-security/T167-test-that-the-application-is-not-vulnerable-to-json-hijackin/SKILL.md](./skills/api-security/T167-test-that-the-application-is-not-vulnerable-to-json-hijackin/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T2139 | Prevent information exposure through APIs | [skills/api-security/T2139-prevent-information-exposure-through-apis/SKILL.md](./skills/api-security/T2139-prevent-information-exposure-through-apis/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T2140 | Test that APIs do not expose sensitive information | [skills/api-security/T2140-test-that-apis-do-not-expose-sensitive-information/SKILL.md](./skills/api-security/T2140-test-that-apis-do-not-expose-sensitive-information/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T2269 | Prevent batching attacks (GraphQL) | [skills/api-security/T2269-prevent-batching-attacks-graphql/SKILL.md](./skills/api-security/T2269-prevent-batching-attacks-graphql/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T228 | Test that application restricts HTTP message size | [skills/api-security/T228-test-that-application-restricts-http-message-size/SKILL.md](./skills/api-security/T228-test-that-application-restricts-http-message-size/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2283 | Configure GraphQL correctly | [skills/api-security/T2283-configure-graphql-correctly/SKILL.md](./skills/api-security/T2283-configure-graphql-correctly/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2284 | Prevent DoS attacks (GraphQL) | [skills/api-security/T2284-prevent-dos-attacks-graphql/SKILL.md](./skills/api-security/T2284-prevent-dos-attacks-graphql/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2604 | Follow best practices for data restoring operations | [skills/api-security/T2604-follow-best-practices-for-data-restoring-operations/SKILL.md](./skills/api-security/T2604-follow-best-practices-for-data-restoring-operations/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2613 | Verify best practices for data-restoring operations are followed | [skills/api-security/T2613-verify-best-practices-for-data-restoring-operations-are-foll/SKILL.md](./skills/api-security/T2613-verify-best-practices-for-data-restoring-operations-are-foll/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T364 | Enable secure backup and restore capabilities | [skills/api-security/T364-enable-secure-backup-and-restore-capabilities/SKILL.md](./skills/api-security/T364-enable-secure-backup-and-restore-capabilities/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T365 | Verify the security of backing up and restoring procedures | [skills/api-security/T365-verify-the-security-of-backing-up-and-restoring-procedures/SKILL.md](./skills/api-security/T365-verify-the-security-of-backing-up-and-restoring-procedures/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T536 | Restrict the size of incoming messages in services | [skills/api-security/T536-restrict-the-size-of-incoming-messages-in-services/SKILL.md](./skills/api-security/T536-restrict-the-size-of-incoming-messages-in-services/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T537 | Test that the size of incoming messages in services is restricted | [skills/api-security/T537-test-that-the-size-of-incoming-messages-in-services-is-restr/SKILL.md](./skills/api-security/T537-test-that-the-size-of-incoming-messages-in-services-is-restr/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T553 | Design secure RESTful web services | [skills/api-security/T553-design-secure-restful-web-services/SKILL.md](./skills/api-security/T553-design-secure-restful-web-services/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T554 | Verify that REST web services are securely designed | [skills/api-security/T554-verify-that-rest-web-services-are-securely-designed/SKILL.md](./skills/api-security/T554-verify-that-rest-web-services-are-securely-designed/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T573 | Prevent UDDI/ebXML spoofing | [skills/api-security/T573-prevent-uddi-ebxml-spoofing/SKILL.md](./skills/api-security/T573-prevent-uddi-ebxml-spoofing/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T576 | Verify that UDDI/ebXML spoofing is prevented | [skills/api-security/T576-verify-that-uddi-ebxml-spoofing-is-prevented/SKILL.md](./skills/api-security/T576-verify-that-uddi-ebxml-spoofing-is-prevented/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |

### authentication
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T10 | Use server-to-server authentication | [skills/authentication/T10-use-server-to-server-authentication/SKILL.md](./skills/authentication/T10-use-server-to-server-authentication/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T114 | Test system-to-system authentication lockout or throttling | [skills/authentication/T114-test-system-to-system-authentication-lockout-or-throttling/SKILL.md](./skills/authentication/T114-test-system-to-system-authentication-lockout-or-throttling/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1362 | Perform message throttling in Web APIs | [skills/authentication/T1362-perform-message-throttling-in-web-apis/SKILL.md](./skills/authentication/T1362-perform-message-throttling-in-web-apis/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1363 | Verify if message throttling is properly performed in Web APIs | [skills/authentication/T1363-verify-if-message-throttling-is-properly-performed-in-web-ap/SKILL.md](./skills/authentication/T1363-verify-if-message-throttling-is-properly-performed-in-web-ap/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1918 | Integrate with SSO | [skills/authentication/T1918-integrate-with-sso/SKILL.md](./skills/authentication/T1918-integrate-with-sso/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T1919 | Use JSON Web Token (JWT) securely | [skills/authentication/T1919-use-json-web-token-jwt-securely/SKILL.md](./skills/authentication/T1919-use-json-web-token-jwt-securely/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2 | Secure the password reset mechanism | [skills/authentication/T2-secure-the-password-reset-mechanism/SKILL.md](./skills/authentication/T2-secure-the-password-reset-mechanism/SKILL.md) | 9 | CODE_FIX | Pending | LIBRARY:TA8478 |
| T220 | Verify that user password is salted and hashed | [skills/authentication/T220-verify-that-user-password-is-salted-and-hashed/SKILL.md](./skills/authentication/T220-verify-that-user-password-is-salted-and-hashed/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T222 | Verify server-to-server authentication | [skills/authentication/T222-verify-server-to-server-authentication/SKILL.md](./skills/authentication/T222-verify-server-to-server-authentication/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T2276 | Test to confirm that authorization and authentication controls are in place for access to resources | [skills/authentication/T2276-test-to-confirm-that-authorization-and-authentication-contro/SKILL.md](./skills/authentication/T2276-test-to-confirm-that-authorization-and-authentication-contro/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T2277 | Test to confirm the use of an account and identity management system | [skills/authentication/T2277-test-to-confirm-the-use-of-an-account-and-identity-managemen/SKILL.md](./skills/authentication/T2277-test-to-confirm-the-use-of-an-account-and-identity-managemen/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T230 | Test that server-to-server system accounts meet minimum password requirements | [skills/authentication/T230-test-that-server-to-server-system-accounts-meet-minimum-pass/SKILL.md](./skills/authentication/T230-test-that-server-to-server-system-accounts-meet-minimum-pass/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2652 | Consider adding plugins for stronger authentication protocols and stricter password complexity rules (MariaDB) | [skills/authentication/T2652-consider-adding-plugins-for-stronger-authentication-protocol/SKILL.md](./skills/authentication/T2652-consider-adding-plugins-for-stronger-authentication-protocol/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T281 | Follow best practices when handling access tokens (API tokens) | [skills/authentication/T281-follow-best-practices-when-handling-access-tokens-api-tokens/SKILL.md](./skills/authentication/T281-follow-best-practices-when-handling-access-tokens-api-tokens/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T284 | Generate secure access tokens (API tokens) | [skills/authentication/T284-generate-secure-access-tokens-api-tokens/SKILL.md](./skills/authentication/T284-generate-secure-access-tokens-api-tokens/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T285 | Restrict use of access tokens (API tokens) | [skills/authentication/T285-restrict-use-of-access-tokens-api-tokens/SKILL.md](./skills/authentication/T285-restrict-use-of-access-tokens-api-tokens/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T3 | Require old passwords when users change passwords | [skills/authentication/T3-require-old-passwords-when-users-change-passwords/SKILL.md](./skills/authentication/T3-require-old-passwords-when-users-change-passwords/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T323 | Test that default accounts are disabled or default passwords are changed | [skills/authentication/T323-test-that-default-accounts-are-disabled-or-default-passwords/SKILL.md](./skills/authentication/T323-test-that-default-accounts-are-disabled-or-default-passwords/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T338 | Control access to resources through user authentication and authorization | [skills/authentication/T338-control-access-to-resources-through-user-authentication-and/SKILL.md](./skills/authentication/T338-control-access-to-resources-through-user-authentication-and/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T340 | Use an account and identity management system | [skills/authentication/T340-use-an-account-and-identity-management-system/SKILL.md](./skills/authentication/T340-use-an-account-and-identity-management-system/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T394 | Secure one-time passwords (OTP) | [skills/authentication/T394-secure-one-time-passwords-otp/SKILL.md](./skills/authentication/T394-secure-one-time-passwords-otp/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T395 | Verify that one-time passwords (OTP) are securely used | [skills/authentication/T395-verify-that-one-time-passwords-otp-are-securely-used/SKILL.md](./skills/authentication/T395-verify-that-one-time-passwords-otp-are-securely-used/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T61 | Disable default accounts or change all default passwords | [skills/authentication/T61-disable-default-accounts-or-change-all-default-passwords/SKILL.md](./skills/authentication/T61-disable-default-accounts-or-change-all-default-passwords/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T62 | Protect passwords in property and configuration files | [skills/authentication/T62-protect-passwords-in-property-and-configuration-files/SKILL.md](./skills/authentication/T62-protect-passwords-in-property-and-configuration-files/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T69 | Strong password requirements for server-to-server system accounts | [skills/authentication/T69-strong-password-requirements-for-server-to-server-system-acc/SKILL.md](./skills/authentication/T69-strong-password-requirements-for-server-to-server-system-acc/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8615 |
| T7 | Salt and hash stored passwords | [skills/authentication/T7-salt-and-hash-stored-passwords/SKILL.md](./skills/authentication/T7-salt-and-hash-stored-passwords/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8548 |
| T70 | Implement account lockout or authentication throttling for system accounts | [skills/authentication/T70-implement-account-lockout-or-authentication-throttling-for-s/SKILL.md](./skills/authentication/T70-implement-account-lockout-or-authentication-throttling-for-s/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T76 | Do not hardcode passwords | [skills/authentication/T76-do-not-hardcode-passwords/SKILL.md](./skills/authentication/T76-do-not-hardcode-passwords/SKILL.md) | 10 | CODE_FIX | Pending | LIBRARY:TA8509 |
| T78 | Test strength of password reset mechanism | [skills/authentication/T78-test-strength-of-password-reset-mechanism/SKILL.md](./skills/authentication/T78-test-strength-of-password-reset-mechanism/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T79 | Test password change functions | [skills/authentication/T79-test-password-change-functions/SKILL.md](./skills/authentication/T79-test-password-change-functions/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### authorization
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T106 | Test that site is not vulnerable to direct object access attacks | [skills/authorization/T106-test-that-site-is-not-vulnerable-to-direct-object-access-att/SKILL.md](./skills/authorization/T106-test-that-site-is-not-vulnerable-to-direct-object-access-att/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T128 | Test for access control bypass through user-controlled keys | [skills/authorization/T128-test-for-access-control-bypass-through-user-controlled-keys/SKILL.md](./skills/authorization/T128-test-for-access-control-bypass-through-user-controlled-keys/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T14 | Enforce the principle of least privilege | [skills/authorization/T14-enforce-the-principle-of-least-privilege/SKILL.md](./skills/authorization/T14-enforce-the-principle-of-least-privilege/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T15 | Centralize authorization | [skills/authorization/T15-centralize-authorization/SKILL.md](./skills/authorization/T15-centralize-authorization/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T16 | Authorize every non-public page | [skills/authorization/T16-authorize-every-non-public-page/SKILL.md](./skills/authorization/T16-authorize-every-non-public-page/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T17 | Do not only rely on client-side authorization | [skills/authorization/T17-do-not-only-rely-on-client-side-authorization/SKILL.md](./skills/authorization/T17-do-not-only-rely-on-client-side-authorization/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T18 | Make authorization decisions using full context | [skills/authorization/T18-make-authorization-decisions-using-full-context/SKILL.md](./skills/authorization/T18-make-authorization-decisions-using-full-context/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T184 | Perform authorization checks on RESTful web services | [skills/authorization/T184-perform-authorization-checks-on-restful-web-services/SKILL.md](./skills/authorization/T184-perform-authorization-checks-on-restful-web-services/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2141 | Perform function level authorization in API | [skills/authorization/T2141-perform-function-level-authorization-in-api/SKILL.md](./skills/authorization/T2141-perform-function-level-authorization-in-api/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8555 |
| T2142 | Verify that function level authorization is implemented in API | [skills/authorization/T2142-verify-that-function-level-authorization-is-implemented-in-a/SKILL.md](./skills/authorization/T2142-verify-that-function-level-authorization-is-implemented-in-a/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T226 | Verify that authorization is centralized | [skills/authorization/T226-verify-that-authorization-is-centralized/SKILL.md](./skills/authorization/T226-verify-that-authorization-is-centralized/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2274 | Test to confirm that the principle of least privilege is strongly implemented | [skills/authorization/T2274-test-to-confirm-that-the-principle-of-least-privilege-is-str/SKILL.md](./skills/authorization/T2274-test-to-confirm-that-the-principle-of-least-privilege-is-str/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2281 | Secure access control (GraphQL) | [skills/authorization/T2281-secure-access-control-graphql/SKILL.md](./skills/authorization/T2281-secure-access-control-graphql/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8570 |
| T2282 | Test to confirm that unauthenticated parts of the application are accessible | [skills/authorization/T2282-test-to-confirm-that-unauthenticated-parts-of-the-applicatio/SKILL.md](./skills/authorization/T2282-test-to-confirm-that-unauthenticated-parts-of-the-applicatio/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T295 | Avoid storing unencrypted confidential data without access control mechanisms | [skills/authorization/T295-avoid-storing-unencrypted-confidential-data-without-access-c/SKILL.md](./skills/authorization/T295-avoid-storing-unencrypted-confidential-data-without-access-c/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T296 | Test that unencrypted confidential data is not stored without access control mechanisms | [skills/authorization/T296-test-that-unencrypted-confidential-data-is-not-stored-withou/SKILL.md](./skills/authorization/T296-test-that-unencrypted-confidential-data-is-not-stored-withou/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T349 | Protect audit information and logs against unauthorized access | [skills/authorization/T349-protect-audit-information-and-logs-against-unauthorized-acce/SKILL.md](./skills/authorization/T349-protect-audit-information-and-logs-against-unauthorized-acce/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T373 | Design and regulate access to unauthenticated parts of the application | [skills/authorization/T373-design-and-regulate-access-to-unauthenticated-parts-of-the-a/SKILL.md](./skills/authorization/T373-design-and-regulate-access-to-unauthenticated-parts-of-the-a/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T378 | Authorize every request for data objects | [skills/authorization/T378-authorize-every-request-for-data-objects/SKILL.md](./skills/authorization/T378-authorize-every-request-for-data-objects/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T50 | Use indirect object reference maps if accessing files | [skills/authorization/T50-use-indirect-object-reference-maps-if-accessing-files/SKILL.md](./skills/authorization/T50-use-indirect-object-reference-maps-if-accessing-files/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T517 | Protect user registration and account modification pages against user enumeration | [skills/authorization/T517-protect-user-registration-and-account-modification-pages-aga/SKILL.md](./skills/authorization/T517-protect-user-registration-and-account-modification-pages-aga/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T518 | Test that registration and account modification pages are protected against user enumeration | [skills/authorization/T518-test-that-registration-and-account-modification-pages-are-pr/SKILL.md](./skills/authorization/T518-test-that-registration-and-account-modification-pages-are-pr/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T84 | Test page-level authorization | [skills/authorization/T84-test-page-level-authorization/SKILL.md](./skills/authorization/T84-test-page-level-authorization/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T85 | Test server-side enforcement of authorization | [skills/authorization/T85-test-server-side-enforcement-of-authorization/SKILL.md](./skills/authorization/T85-test-server-side-enforcement-of-authorization/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |

### backup-recovery
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T2477 | Test the re-deployment routines | [skills/backup-recovery/T2477-test-the-re-deployment-routines/SKILL.md](./skills/backup-recovery/T2477-test-the-re-deployment-routines/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T2478 | Manage re-deployment routines | [skills/backup-recovery/T2478-manage-re-deployment-routines/SKILL.md](./skills/backup-recovery/T2478-manage-re-deployment-routines/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T2603 | Protect backup archive bits | [skills/backup-recovery/T2603-protect-backup-archive-bits/SKILL.md](./skills/backup-recovery/T2603-protect-backup-archive-bits/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2612 | Verify backup archive bits are protected | [skills/backup-recovery/T2612-verify-backup-archive-bits-are-protected/SKILL.md](./skills/backup-recovery/T2612-verify-backup-archive-bits-are-protected/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T3990 | Schedule regular backups | [skills/backup-recovery/T3990-schedule-regular-backups/SKILL.md](./skills/backup-recovery/T3990-schedule-regular-backups/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |

### container-security
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1150 | Configure container networks properly (Docker) | [skills/container-security/T1150-configure-container-networks-properly-docker/SKILL.md](./skills/container-security/T1150-configure-container-networks-properly-docker/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8476 |
| T1151 | Verify that container networks are configured properly (Docker) | [skills/container-security/T1151-verify-that-container-networks-are-configured-properly-docke/SKILL.md](./skills/container-security/T1151-verify-that-container-networks-are-configured-properly-docke/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8469 |
| T1154 | Secure Docker registries (Docker) | [skills/container-security/T1154-secure-docker-registries-docker/SKILL.md](./skills/container-security/T1154-secure-docker-registries-docker/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8474 |
| T1155 | Verify that Docker registries are secure (Docker) | [skills/container-security/T1155-verify-that-docker-registries-are-secure-docker/SKILL.md](./skills/container-security/T1155-verify-that-docker-registries-are-secure-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1156 | Do not use the aufs storage driver (Docker) | [skills/container-security/T1156-do-not-use-the-aufs-storage-driver-docker/SKILL.md](./skills/container-security/T1156-do-not-use-the-aufs-storage-driver-docker/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8473 |
| T1157 | Verify that the aufs storage driver is not used (Docker) | [skills/container-security/T1157-verify-that-the-aufs-storage-driver-is-not-used-docker/SKILL.md](./skills/container-security/T1157-verify-that-the-aufs-storage-driver-is-not-used-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1158 | Configure TLS authentication for the Docker daemon (Docker) | [skills/container-security/T1158-configure-tls-authentication-for-the-docker-daemon-docker/SKILL.md](./skills/container-security/T1158-configure-tls-authentication-for-the-docker-daemon-docker/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8472 |
| T1159 | Verify that TLS authentication is configured for the Docker daemon (Docker) | [skills/container-security/T1159-verify-that-tls-authentication-is-configured-for-the-docker/SKILL.md](./skills/container-security/T1159-verify-that-tls-authentication-is-configured-for-the-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1160 | Set ulimit appropriately (Docker) | [skills/container-security/T1160-set-ulimit-appropriately-docker/SKILL.md](./skills/container-security/T1160-set-ulimit-appropriately-docker/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8471 |
| T1161 | Verify that ulimit is set appropriately (Docker) | [skills/container-security/T1161-verify-that-ulimit-is-set-appropriately-docker/SKILL.md](./skills/container-security/T1161-verify-that-ulimit-is-set-appropriately-docker/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T1166 | Encrypt data exchanged between containers on different nodes on the overlay network (Docker) | [skills/container-security/T1166-encrypt-data-exchanged-between-containers-on-different-nodes/SKILL.md](./skills/container-security/T1166-encrypt-data-exchanged-between-containers-on-different-nodes/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8467 |
| T1167 | Verify that data exchanged between containers on different nodes on the overlay network is encrypted (Docker) | [skills/container-security/T1167-verify-that-data-exchanged-between-containers-on-different-n/SKILL.md](./skills/container-security/T1167-verify-that-data-exchanged-between-containers-on-different-n/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1172 | Secure daemon configuration files (Docker) | [skills/container-security/T1172-secure-daemon-configuration-files-docker/SKILL.md](./skills/container-security/T1172-secure-daemon-configuration-files-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1173 | Verify that daemon configuration files are secured (Docker) | [skills/container-security/T1173-verify-that-daemon-configuration-files-are-secured-docker/SKILL.md](./skills/container-security/T1173-verify-that-daemon-configuration-files-are-secured-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1174 | Create non-root users for containers (Docker) | [skills/container-security/T1174-create-non-root-users-for-containers-docker/SKILL.md](./skills/container-security/T1174-create-non-root-users-for-containers-docker/SKILL.md) | 9 | CODE_FIX | Pending | LIBRARY:TA8448 |
| T1175 | Verify that containers are not run as root (Docker) | [skills/container-security/T1175-verify-that-containers-are-not-run-as-root-docker/SKILL.md](./skills/container-security/T1175-verify-that-containers-are-not-run-as-root-docker/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T1176 | Use trusted base images and include the latest security patches (Docker) | [skills/container-security/T1176-use-trusted-base-images-and-include-the-latest-security-patc/SKILL.md](./skills/container-security/T1176-use-trusted-base-images-and-include-the-latest-security-patc/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8447 |
| T1177 | Verify that secure and updated images are used (Docker) | [skills/container-security/T1177-verify-that-secure-and-updated-images-are-used-docker/SKILL.md](./skills/container-security/T1177-verify-that-secure-and-updated-images-are-used-docker/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8477 |
| T1180 | Check container health (Docker) | [skills/container-security/T1180-check-container-health-docker/SKILL.md](./skills/container-security/T1180-check-container-health-docker/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8445 |
| T1181 | Verify that container health is checked (Docker) | [skills/container-security/T1181-verify-that-container-health-is-checked-docker/SKILL.md](./skills/container-security/T1181-verify-that-container-health-is-checked-docker/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8465 |
| T1186 | Do not store secrets in Dockerfiles (Docker) | [skills/container-security/T1186-do-not-store-secrets-in-dockerfiles-docker/SKILL.md](./skills/container-security/T1186-do-not-store-secrets-in-dockerfiles-docker/SKILL.md) | 10 | CODE_FIX | Pending | LIBRARY:TA8441 |
| T1187 | Test if secrets are stored in Dockerfiles (Docker) | [skills/container-security/T1187-test-if-secrets-are-stored-in-dockerfiles-docker/SKILL.md](./skills/container-security/T1187-test-if-secrets-are-stored-in-dockerfiles-docker/SKILL.md) | 10 | CODE_FIX | Pending | LIBRARY:TA8466 |
| T1188 | Configure Linux Security Modules (Docker) | [skills/container-security/T1188-configure-linux-security-modules-docker/SKILL.md](./skills/container-security/T1188-configure-linux-security-modules-docker/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8458 |
| T1189 | Test if Linux Security Modules are securely configured (Docker) | [skills/container-security/T1189-test-if-linux-security-modules-are-securely-configured-docke/SKILL.md](./skills/container-security/T1189-test-if-linux-security-modules-are-securely-configured-docke/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8462 |
| T1190 | Restrict Linux Kernel Capabilities within containers (Docker) | [skills/container-security/T1190-restrict-linux-kernel-capabilities-within-containers-docker/SKILL.md](./skills/container-security/T1190-restrict-linux-kernel-capabilities-within-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8457 |
| T1191 | Test if Linux Kernel Capabilities are restricted within containers (Docker) | [skills/container-security/T1191-test-if-linux-kernel-capabilities-are-restricted-within-cont/SKILL.md](./skills/container-security/T1191-test-if-linux-kernel-capabilities-are-restricted-within-cont/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8461 |
| T1192 | Do not expose unnecessary host resources (Docker) | [skills/container-security/T1192-do-not-expose-unnecessary-host-resources-docker/SKILL.md](./skills/container-security/T1192-do-not-expose-unnecessary-host-resources-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8439 |
| T1193 | Test if unnecessary host resources are exposed (Docker) | [skills/container-security/T1193-test-if-unnecessary-host-resources-are-exposed-docker/SKILL.md](./skills/container-security/T1193-test-if-unnecessary-host-resources-are-exposed-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1194 | Do not run SSH within containers (Docker) | [skills/container-security/T1194-do-not-run-ssh-within-containers-docker/SKILL.md](./skills/container-security/T1194-do-not-run-ssh-within-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8460 |
| T1195 | Test if SSH is running within containers (Docker) | [skills/container-security/T1195-test-if-ssh-is-running-within-containers-docker/SKILL.md](./skills/container-security/T1195-test-if-ssh-is-running-within-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1196 | Open only needed ports on the containers (Docker) | [skills/container-security/T1196-open-only-needed-ports-on-the-containers-docker/SKILL.md](./skills/container-security/T1196-open-only-needed-ports-on-the-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8442 |
| T1197 | Test if only needed ports are open on the containers (Docker) | [skills/container-security/T1197-test-if-only-needed-ports-are-open-on-the-containers-docker/SKILL.md](./skills/container-security/T1197-test-if-only-needed-ports-are-open-on-the-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1198 | Do not share the host's network namespace (Docker) | [skills/container-security/T1198-do-not-share-the-host-s-network-namespace-docker/SKILL.md](./skills/container-security/T1198-do-not-share-the-host-s-network-namespace-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8456 |
| T1199 | Test that the host's network namespace is not shared (Docker) | [skills/container-security/T1199-test-that-the-host-s-network-namespace-is-not-shared-docker/SKILL.md](./skills/container-security/T1199-test-that-the-host-s-network-namespace-is-not-shared-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1200 | Limit resources used by containers (Docker) | [skills/container-security/T1200-limit-resources-used-by-containers-docker/SKILL.md](./skills/container-security/T1200-limit-resources-used-by-containers-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8455 |
| T1201 | Test that resources used by containers are limited (Docker) | [skills/container-security/T1201-test-that-resources-used-by-containers-are-limited-docker/SKILL.md](./skills/container-security/T1201-test-that-resources-used-by-containers-are-limited-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1202 | Set container CPU priority appropriately (Docker) | [skills/container-security/T1202-set-container-cpu-priority-appropriately-docker/SKILL.md](./skills/container-security/T1202-set-container-cpu-priority-appropriately-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8454 |
| T1203 | Test if container CPU priority is appropriately set (Docker) | [skills/container-security/T1203-test-if-container-cpu-priority-is-appropriately-set-docker/SKILL.md](./skills/container-security/T1203-test-if-container-cpu-priority-is-appropriately-set-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1204 | Mount container's root file system as read-only (Docker) | [skills/container-security/T1204-mount-container-s-root-file-system-as-read-only-docker/SKILL.md](./skills/container-security/T1204-mount-container-s-root-file-system-as-read-only-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8453 |
| T1205 | Test if the container's root file system is mounted as read-only (Docker) | [skills/container-security/T1205-test-if-the-container-s-root-file-system-is-mounted-as-read/SKILL.md](./skills/container-security/T1205-test-if-the-container-s-root-file-system-is-mounted-as-read/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1206 | Set the 'on-failure' container restart policy to 5 (Docker) | [skills/container-security/T1206-set-the-on-failure-container-restart-policy-to-5-docker/SKILL.md](./skills/container-security/T1206-set-the-on-failure-container-restart-policy-to-5-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8452 |
| T1207 | Test that the 'on-failure' container restart policy is set to 5 (Docker) | [skills/container-security/T1207-test-that-the-on-failure-container-restart-policy-is-set-to/SKILL.md](./skills/container-security/T1207-test-that-the-on-failure-container-restart-policy-is-set-to/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1208 | Do not set mount propagation mode to 'shared' (Docker) | [skills/container-security/T1208-do-not-set-mount-propagation-mode-to-shared-docker/SKILL.md](./skills/container-security/T1208-do-not-set-mount-propagation-mode-to-shared-docker/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8451 |
| T1209 | Verify that mount propagation mode is not set to 'shared' (Docker) | [skills/container-security/T1209-verify-that-mount-propagation-mode-is-not-set-to-shared-dock/SKILL.md](./skills/container-security/T1209-verify-that-mount-propagation-mode-is-not-set-to-shared-dock/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T1210 | Configure seccomp profile (Docker) | [skills/container-security/T1210-configure-seccomp-profile-docker/SKILL.md](./skills/container-security/T1210-configure-seccomp-profile-docker/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8450 |
| T1211 | Verify that seccomp profile is enabled (Docker) | [skills/container-security/T1211-verify-that-seccomp-profile-is-enabled-docker/SKILL.md](./skills/container-security/T1211-verify-that-seccomp-profile-is-enabled-docker/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1212 | Confirm cgroup usage (Docker) | [skills/container-security/T1212-confirm-cgroup-usage-docker/SKILL.md](./skills/container-security/T1212-confirm-cgroup-usage-docker/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8440 |
| T1213 | Verify that cgroup usage is confirmed (Docker) | [skills/container-security/T1213-verify-that-cgroup-usage-is-confirmed-docker/SKILL.md](./skills/container-security/T1213-verify-that-cgroup-usage-is-confirmed-docker/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T1214 | Restrict containers from acquiring additional privileges (Docker) | [skills/container-security/T1214-restrict-containers-from-acquiring-additional-privileges-doc/SKILL.md](./skills/container-security/T1214-restrict-containers-from-acquiring-additional-privileges-doc/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8449 |
| T1215 | Verify that containers are restricted from acquiring additional privileges (Docker) | [skills/container-security/T1215-verify-that-containers-are-restricted-from-acquiring-additio/SKILL.md](./skills/container-security/T1215-verify-that-containers-are-restricted-from-acquiring-additio/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1232 | Create a separate partition for containers (Docker) | [skills/container-security/T1232-create-a-separate-partition-for-containers-docker/SKILL.md](./skills/container-security/T1232-create-a-separate-partition-for-containers-docker/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T1233 | Test that containers are on a separate partition (Docker) | [skills/container-security/T1233-test-that-containers-are-on-a-separate-partition-docker/SKILL.md](./skills/container-security/T1233-test-that-containers-are-on-a-separate-partition-docker/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T1234 | Only allow trusted users to control the Docker daemon (Docker) | [skills/container-security/T1234-only-allow-trusted-users-to-control-the-docker-daemon-docker/SKILL.md](./skills/container-security/T1234-only-allow-trusted-users-to-control-the-docker-daemon-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1235 | Test that only trusted users can control the Docker daemon (Docker) | [skills/container-security/T1235-test-that-only-trusted-users-can-control-the-docker-daemon-d/SKILL.md](./skills/container-security/T1235-test-that-only-trusted-users-can-control-the-docker-daemon-d/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1236 | Audit the Docker daemon and its files (Docker) | [skills/container-security/T1236-audit-the-docker-daemon-and-its-files-docker/SKILL.md](./skills/container-security/T1236-audit-the-docker-daemon-and-its-files-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1237 | Test that the Docker daemon and its files are audited (Docker) | [skills/container-security/T1237-test-that-the-docker-daemon-and-its-files-are-audited-docker/SKILL.md](./skills/container-security/T1237-test-that-the-docker-daemon-and-its-files-are-audited-docker/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T1923 | Disable swarm mode if not needed | [skills/container-security/T1923-disable-swarm-mode-if-not-needed/SKILL.md](./skills/container-security/T1923-disable-swarm-mode-if-not-needed/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T1924 | Verify that swarm mode is disabled | [skills/container-security/T1924-verify-that-swarm-mode-is-disabled/SKILL.md](./skills/container-security/T1924-verify-that-swarm-mode-is-disabled/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T2105 | Enforce the use of client certificate bundles for unprivileged users to access UCP (Docker) | [skills/container-security/T2105-enforce-the-use-of-client-certificate-bundles-for-unprivileg/SKILL.md](./skills/container-security/T2105-enforce-the-use-of-client-certificate-bundles-for-unprivileg/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2106 | Verify that the use of client certificate bundles for unprivileged users is enforced (Docker) | [skills/container-security/T2106-verify-that-the-use-of-client-certificate-bundles-for-unpriv/SKILL.md](./skills/container-security/T2106-verify-that-the-use-of-client-certificate-bundles-for-unpriv/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2109 | Enable signed image enforcement (Docker) | [skills/container-security/T2109-enable-signed-image-enforcement-docker/SKILL.md](./skills/container-security/T2109-enable-signed-image-enforcement-docker/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2110 | Verify that signed image enforcement is enabled (Docker) | [skills/container-security/T2110-verify-that-signed-image-enforcement-is-enabled-docker/SKILL.md](./skills/container-security/T2110-verify-that-signed-image-enforcement-is-enabled-docker/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2115 | Enable image vulnerability scanning (Docker) | [skills/container-security/T2115-enable-image-vulnerability-scanning-docker/SKILL.md](./skills/container-security/T2115-enable-image-vulnerability-scanning-docker/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2116 | Verify that image vulnerability scanning is enabled (Docker) | [skills/container-security/T2116-verify-that-image-vulnerability-scanning-is-enabled-docker/SKILL.md](./skills/container-security/T2116-verify-that-image-vulnerability-scanning-is-enabled-docker/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2256 | Authenticate and log all access to registries containing sensitive or proprietary images | [skills/container-security/T2256-authenticate-and-log-all-access-to-registries-containing-sen/SKILL.md](./skills/container-security/T2256-authenticate-and-log-all-access-to-registries-containing-sen/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2257 | Regularly update and patch containerization systems | [skills/container-security/T2257-regularly-update-and-patch-containerization-systems/SKILL.md](./skills/container-security/T2257-regularly-update-and-patch-containerization-systems/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T2258 | Minimize host OS attack surface | [skills/container-security/T2258-minimize-host-os-attack-surface/SKILL.md](./skills/container-security/T2258-minimize-host-os-attack-surface/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T4746 | Ensure container images are secure | [skills/container-security/T4746-ensure-container-images-are-secure/SKILL.md](./skills/container-security/T4746-ensure-container-images-are-secure/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T4747 | Limit container privileges | [skills/container-security/T4747-limit-container-privileges/SKILL.md](./skills/container-security/T4747-limit-container-privileges/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T4748 | Implement Role-Based Access Control (RBAC) for container orchestration | [skills/container-security/T4748-implement-role-based-access-control-rbac-for-container-orche/SKILL.md](./skills/container-security/T4748-implement-role-based-access-control-rbac-for-container-orche/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T4749 | Monitor containers in real-time | [skills/container-security/T4749-monitor-containers-in-real-time/SKILL.md](./skills/container-security/T4749-monitor-containers-in-real-time/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T4750 | Isolate container networks | [skills/container-security/T4750-isolate-container-networks/SKILL.md](./skills/container-security/T4750-isolate-container-networks/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T4751 | Reduce the attack surface of container images | [skills/container-security/T4751-reduce-the-attack-surface-of-container-images/SKILL.md](./skills/container-security/T4751-reduce-the-attack-surface-of-container-images/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |

### cors
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T257 | Secure cross origin resource sharing (CORS) | [skills/cors/T257-secure-cross-origin-resource-sharing-cors/SKILL.md](./skills/cors/T257-secure-cross-origin-resource-sharing-cors/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T318 | Verify security of cross origin resource sharing (CORS) | [skills/cors/T318-verify-security-of-cross-origin-resource-sharing-cors/SKILL.md](./skills/cors/T318-verify-security-of-cross-origin-resource-sharing-cors/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |

### crypto
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1468 | Encrypt sensitive data at rest in the browser | [skills/crypto/T1468-encrypt-sensitive-data-at-rest-in-the-browser/SKILL.md](./skills/crypto/T1468-encrypt-sensitive-data-at-rest-in-the-browser/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T151 | Use cryptographically secure random numbers | [skills/crypto/T151-use-cryptographically-secure-random-numbers/SKILL.md](./skills/crypto/T151-use-cryptographically-secure-random-numbers/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T156 | Validate certificate and its chain of trust properly | [skills/crypto/T156-validate-certificate-and-its-chain-of-trust-properly/SKILL.md](./skills/crypto/T156-validate-certificate-and-its-chain-of-trust-properly/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T175 | Test that the client validates digital certificates | [skills/crypto/T175-test-that-the-client-validates-digital-certificates/SKILL.md](./skills/crypto/T175-test-that-the-client-validates-digital-certificates/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T21 | Ensure all data in transit is encrypted using a secure TLS channel | [skills/crypto/T21-ensure-all-data-in-transit-is-encrypted-using-a-secure-tls-c/SKILL.md](./skills/crypto/T21-ensure-all-data-in-transit-is-encrypted-using-a-secure-tls-c/SKILL.md) | 8 | INFRA | Pending | LIBRARY:TA8620 |
| T2665 | Protect sensitive data at rest with encryption | [skills/crypto/T2665-protect-sensitive-data-at-rest-with-encryption/SKILL.md](./skills/crypto/T2665-protect-sensitive-data-at-rest-with-encryption/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T445 | Verify that only approved cryptographic algorithms and key lengths are used | [skills/crypto/T445-verify-that-only-approved-cryptographic-algorithms-and-key-l/SKILL.md](./skills/crypto/T445-verify-that-only-approved-cryptographic-algorithms-and-key-l/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T446 | Verify that only standard libraries are used for cryptography | [skills/crypto/T446-verify-that-only-standard-libraries-are-used-for-cryptograph/SKILL.md](./skills/crypto/T446-verify-that-only-standard-libraries-are-used-for-cryptograph/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T587 | Verify that cryptographically secure algorithms are used for random number generation | [skills/crypto/T587-verify-that-cryptographically-secure-algorithms-are-used-for/SKILL.md](./skills/crypto/T587-verify-that-cryptographically-secure-algorithms-are-used-for/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T59 | Use standard libraries for cryptography | [skills/crypto/T59-use-standard-libraries-for-cryptography/SKILL.md](./skills/crypto/T59-use-standard-libraries-for-cryptography/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8547 |
| T60 | Use correct and approved cryptographic algorithms, parameters, and key lengths | [skills/crypto/T60-use-correct-and-approved-cryptographic-algorithms-parameters/SKILL.md](./skills/crypto/T60-use-correct-and-approved-cryptographic-algorithms-parameters/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T87 | Verify that all data in transit is encrypted using a secure TLS channel | [skills/crypto/T87-verify-that-all-data-in-transit-is-encrypted-using-a-secure/SKILL.md](./skills/crypto/T87-verify-that-all-data-in-transit-is-encrypted-using-a-secure/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |

### csrf
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T113 | Test that site is not vulnerable to HTTP verb tampering | [skills/csrf/T113-test-that-site-is-not-vulnerable-to-http-verb-tampering/SKILL.md](./skills/csrf/T113-test-that-site-is-not-vulnerable-to-http-verb-tampering/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T1541 | Decide on the best CSRF defense for your application | [skills/csrf/T1541-decide-on-the-best-csrf-defense-for-your-application/SKILL.md](./skills/csrf/T1541-decide-on-the-best-csrf-defense-for-your-application/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T1542 | Use the correct HTTP methods for making state-changing operations | [skills/csrf/T1542-use-the-correct-http-methods-for-making-state-changing-opera/SKILL.md](./skills/csrf/T1542-use-the-correct-http-methods-for-making-state-changing-opera/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T29 | Use anti-Cross-Site Request Forgery (CSRF) tokens | [skills/csrf/T29-use-anti-cross-site-request-forgery-csrf-tokens/SKILL.md](./skills/csrf/T29-use-anti-cross-site-request-forgery-csrf-tokens/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T65 | Restrict accepted HTTP verbs | [skills/csrf/T65-restrict-accepted-http-verbs/SKILL.md](./skills/csrf/T65-restrict-accepted-http-verbs/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T96 | Test if your site is vulnerable to CSRF | [skills/csrf/T96-test-if-your-site-is-vulnerable-to-csrf/SKILL.md](./skills/csrf/T96-test-if-your-site-is-vulnerable-to-csrf/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |

### data-protection
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1539 | Clear browser data on user logout | [skills/data-protection/T1539-clear-browser-data-on-user-logout/SKILL.md](./skills/data-protection/T1539-clear-browser-data-on-user-logout/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1540 | Verify that browser data is cleared upon user logout | [skills/data-protection/T1540-verify-that-browser-data-is-cleared-upon-user-logout/SKILL.md](./skills/data-protection/T1540-verify-that-browser-data-is-cleared-upon-user-logout/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T214 | Protect confidential files on operating system or server | [skills/data-protection/T214-protect-confidential-files-on-operating-system-or-server/SKILL.md](./skills/data-protection/T214-protect-confidential-files-on-operating-system-or-server/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T219 | Avoid transmitting confidential data through URL parameters | [skills/data-protection/T219-avoid-transmitting-confidential-data-through-url-parameters/SKILL.md](./skills/data-protection/T219-avoid-transmitting-confidential-data-through-url-parameters/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### database-security
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T19 | Restrict Application's Access to Database | [skills/database-security/T19-restrict-application-s-access-to-database/SKILL.md](./skills/database-security/T19-restrict-application-s-access-to-database/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8571 |
| T227 | Verify that application's access to database is restricted | [skills/database-security/T227-verify-that-application-s-access-to-database-is-restricted/SKILL.md](./skills/database-security/T227-verify-that-application-s-access-to-database-is-restricted/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2597 | Implement RBAC instead of individual accounts | [skills/database-security/T2597-implement-rbac-instead-of-individual-accounts/SKILL.md](./skills/database-security/T2597-implement-rbac-instead-of-individual-accounts/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T2598 | Implement query-level access control | [skills/database-security/T2598-implement-query-level-access-control/SKILL.md](./skills/database-security/T2598-implement-query-level-access-control/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2599 | Protect against connection string parameter pollution | [skills/database-security/T2599-protect-against-connection-string-parameter-pollution/SKILL.md](./skills/database-security/T2599-protect-against-connection-string-parameter-pollution/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2600 | Control the result set size returned by a query | [skills/database-security/T2600-control-the-result-set-size-returned-by-a-query/SKILL.md](./skills/database-security/T2600-control-the-result-set-size-returned-by-a-query/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T2601 | Use Transparent Data Encryption with Enterprise Databases | [skills/database-security/T2601-use-transparent-data-encryption-with-enterprise-databases/SKILL.md](./skills/database-security/T2601-use-transparent-data-encryption-with-enterprise-databases/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2602 | Log typical database and server activities and related metadata | [skills/database-security/T2602-log-typical-database-and-server-activities-and-related-metad/SKILL.md](./skills/database-security/T2602-log-typical-database-and-server-activities-and-related-metad/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2605 | Validate database traffic | [skills/database-security/T2605-validate-database-traffic/SKILL.md](./skills/database-security/T2605-validate-database-traffic/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2606 | Verify RBAC implemented instead of individual accounts | [skills/database-security/T2606-verify-rbac-implemented-instead-of-individual-accounts/SKILL.md](./skills/database-security/T2606-verify-rbac-implemented-instead-of-individual-accounts/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T2607 | Verify query-level access control is implemented | [skills/database-security/T2607-verify-query-level-access-control-is-implemented/SKILL.md](./skills/database-security/T2607-verify-query-level-access-control-is-implemented/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2608 | Verify that the connection string is protected against connection string parameter pollution | [skills/database-security/T2608-verify-that-the-connection-string-is-protected-against-conne/SKILL.md](./skills/database-security/T2608-verify-that-the-connection-string-is-protected-against-conne/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T2609 | Verify that the result set size returned by queries are controlled | [skills/database-security/T2609-verify-that-the-result-set-size-returned-by-queries-are-cont/SKILL.md](./skills/database-security/T2609-verify-that-the-result-set-size-returned-by-queries-are-cont/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8583 |
| T2610 | Verify that Transparent Data Encryption is utilized with Enterprise Databases | [skills/database-security/T2610-verify-that-transparent-data-encryption-is-utilized-with-ent/SKILL.md](./skills/database-security/T2610-verify-that-transparent-data-encryption-is-utilized-with-ent/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2611 | Verify that typical database and server activities, along with related metadata, are logged | [skills/database-security/T2611-verify-that-typical-database-and-server-activities-along-wit/SKILL.md](./skills/database-security/T2611-verify-that-typical-database-and-server-activities-along-wit/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2614 | Verify database traffic is validated | [skills/database-security/T2614-verify-database-traffic-is-validated/SKILL.md](./skills/database-security/T2614-verify-database-traffic-is-validated/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2615 | Limit network access by blocking connections from unknown IP addresses (PostgreSQL) | [skills/database-security/T2615-limit-network-access-by-blocking-connections-from-unknown-ip/SKILL.md](./skills/database-security/T2615-limit-network-access-by-blocking-connections-from-unknown-ip/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2616 | Use a secure authentication mechanism for database connections (PostgreSQL) | [skills/database-security/T2616-use-a-secure-authentication-mechanism-for-database-connectio/SKILL.md](./skills/database-security/T2616-use-a-secure-authentication-mechanism-for-database-connectio/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2617 | Create dedicated database user accounts with minimum privileges (PostgreSQL) | [skills/database-security/T2617-create-dedicated-database-user-accounts-with-minimum-privile/SKILL.md](./skills/database-security/T2617-create-dedicated-database-user-accounts-with-minimum-privile/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2618 | Remove unnecessary superuser accounts (PostgreSQL) | [skills/database-security/T2618-remove-unnecessary-superuser-accounts-postgresql/SKILL.md](./skills/database-security/T2618-remove-unnecessary-superuser-accounts-postgresql/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T2619 | Ensure that row-level security is correctly configured (PostgreSQL) | [skills/database-security/T2619-ensure-that-row-level-security-is-correctly-configured-postg/SKILL.md](./skills/database-security/T2619-ensure-that-row-level-security-is-correctly-configured-postg/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T2620 | Protect data in transit with TLS (PostgreSQL) | [skills/database-security/T2620-protect-data-in-transit-with-tls-postgresql/SKILL.md](./skills/database-security/T2620-protect-data-in-transit-with-tls-postgresql/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2621 | Use file volume encryption and consider in-database encryption with pgcrypto (PostgreSQL) | [skills/database-security/T2621-use-file-volume-encryption-and-consider-in-database-encrypti/SKILL.md](./skills/database-security/T2621-use-file-volume-encryption-and-consider-in-database-encrypti/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2623 | Schedule regular database backups to protect availability (PostgreSQL) | [skills/database-security/T2623-schedule-regular-database-backups-to-protect-availability-po/SKILL.md](./skills/database-security/T2623-schedule-regular-database-backups-to-protect-availability-po/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T2662 | Restrict network access to the database server | [skills/database-security/T2662-restrict-network-access-to-the-database-server/SKILL.md](./skills/database-security/T2662-restrict-network-access-to-the-database-server/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T2663 | Use a secure authentication mechanism for database connections | [skills/database-security/T2663-use-a-secure-authentication-mechanism-for-database-connectio/SKILL.md](./skills/database-security/T2663-use-a-secure-authentication-mechanism-for-database-connectio/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T2664 | Create dedicated database user accounts with minimum privileges (Database Server) | [skills/database-security/T2664-create-dedicated-database-user-accounts-with-minimum-privile/SKILL.md](./skills/database-security/T2664-create-dedicated-database-user-accounts-with-minimum-privile/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2666 | Protect data in transit with TLS (Database Server) | [skills/database-security/T2666-protect-data-in-transit-with-tls-database-server/SKILL.md](./skills/database-security/T2666-protect-data-in-transit-with-tls-database-server/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T2667 | Schedule regular database backups to protect availability (Database Server) | [skills/database-security/T2667-schedule-regular-database-backups-to-protect-availability-da/SKILL.md](./skills/database-security/T2667-schedule-regular-database-backups-to-protect-availability-da/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |

### dependency-management
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1364 | Verify that third party software libraries/modules and open source/COTS components are used securely | [skills/dependency-management/T1364-verify-that-third-party-software-libraries-modules-and-open/SKILL.md](./skills/dependency-management/T1364-verify-that-third-party-software-libraries-modules-and-open/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T186 | Use recommended settings and the latest patches for third party libraries and software | [skills/dependency-management/T186-use-recommended-settings-and-the-latest-patches-for-third-pa/SKILL.md](./skills/dependency-management/T186-use-recommended-settings-and-the-latest-patches-for-third-pa/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |

### file-handling
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T129 | Test for reliance on file name or extension of externally-supplied file | [skills/file-handling/T129-test-for-reliance-on-file-name-or-extension-of-externally-su/SKILL.md](./skills/file-handling/T129-test-for-reliance-on-file-name-or-extension-of-externally-su/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T157 | Temporary files must be cleaned up after the resource is used | [skills/file-handling/T157-temporary-files-must-be-cleaned-up-after-the-resource-is-use/SKILL.md](./skills/file-handling/T157-temporary-files-must-be-cleaned-up-after-the-resource-is-use/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T2167 | Secure file storage | [skills/file-handling/T2167-secure-file-storage/SKILL.md](./skills/file-handling/T2167-secure-file-storage/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T300 | Test that temporary files are cleaned up after the resource is used | [skills/file-handling/T300-test-that-temporary-files-are-cleaned-up-after-the-resource/SKILL.md](./skills/file-handling/T300-test-that-temporary-files-are-cleaned-up-after-the-resource/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T54 | Validate file contents | [skills/file-handling/T54-validate-file-contents/SKILL.md](./skills/file-handling/T54-validate-file-contents/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8493 |
| T572 | Check for symlinks before opening files | [skills/file-handling/T572-check-for-symlinks-before-opening-files/SKILL.md](./skills/file-handling/T572-check-for-symlinks-before-opening-files/SKILL.md) | 6 | CODE_FIX | Pending | LIBRARY:TA8484 |
| T595 | Test that your application checks for symlinks before opening files | [skills/file-handling/T595-test-that-your-application-checks-for-symlinks-before-openin/SKILL.md](./skills/file-handling/T595-test-that-your-application-checks-for-symlinks-before-openin/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### general-hardening
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T375 | Release resources when no longer needed | [skills/general-hardening/T375-release-resources-when-no-longer-needed/SKILL.md](./skills/general-hardening/T375-release-resources-when-no-longer-needed/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### injection
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| CT435 | Bind variables in SQL statements - Oleg Test | [skills/injection/CT435-bind-variables-in-sql-statements-oleg-test/SKILL.md](./skills/injection/CT435-bind-variables-in-sql-statements-oleg-test/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T101 | Test that application is not vulnerable to SQL injection | [skills/injection/T101-test-that-application-is-not-vulnerable-to-sql-injection/SKILL.md](./skills/injection/T101-test-that-application-is-not-vulnerable-to-sql-injection/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T1144 | Prevent Server-Side Template Injection (SSTI) | [skills/injection/T1144-prevent-server-side-template-injection-ssti/SKILL.md](./skills/injection/T1144-prevent-server-side-template-injection-ssti/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T1145 | Verify if web page template is vulnerable to SSTI | [skills/injection/T1145-verify-if-web-page-template-is-vulnerable-to-ssti/SKILL.md](./skills/injection/T1145-verify-if-web-page-template-is-vulnerable-to-ssti/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T122 | Test for remote file include | [skills/injection/T122-test-for-remote-file-include/SKILL.md](./skills/injection/T122-test-for-remote-file-include/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T279 | Avoid dynamically loading any code without proper security considerations | [skills/injection/T279-avoid-dynamically-loading-any-code-without-proper-security-c/SKILL.md](./skills/injection/T279-avoid-dynamically-loading-any-code-without-proper-security-c/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T305 | Verify that your application dynamically loads code only from secure locations | [skills/injection/T305-verify-that-your-application-dynamically-loads-code-only-fro/SKILL.md](./skills/injection/T305-verify-that-your-application-dynamically-loads-code-only-fro/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T38 | Bind variables in SQL statements | [skills/injection/T38-bind-variables-in-sql-statements/SKILL.md](./skills/injection/T38-bind-variables-in-sql-statements/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T420 | Prevent Client-Side Template Injection (CSTI) | [skills/injection/T420-prevent-client-side-template-injection-csti/SKILL.md](./skills/injection/T420-prevent-client-side-template-injection-csti/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T421 | Verify if web page template is vulnerable to client side template injection (CSTI) | [skills/injection/T421-verify-if-web-page-template-is-vulnerable-to-client-side-tem/SKILL.md](./skills/injection/T421-verify-if-web-page-template-is-vulnerable-to-client-side-tem/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### input-validation
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T32 | Always perform input validation on a server | [skills/input-validation/T32-always-perform-input-validation-on-a-server/SKILL.md](./skills/input-validation/T32-always-perform-input-validation-on-a-server/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T42 | Avoid relying on untrusted data for server-side selection | [skills/input-validation/T42-avoid-relying-on-untrusted-data-for-server-side-selection/SKILL.md](./skills/input-validation/T42-avoid-relying-on-untrusted-data-for-server-side-selection/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T98 | Test for input validation on a server | [skills/input-validation/T98-test-for-input-validation-on-a-server/SKILL.md](./skills/input-validation/T98-test-for-input-validation-on-a-server/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |

### llm-security
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T4455 | Prevent prompt injection in Large Language Models (Project Manager) | [skills/llm-security/T4455-prevent-prompt-injection-in-large-language-models-project-ma/SKILL.md](./skills/llm-security/T4455-prevent-prompt-injection-in-large-language-models-project-ma/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4456 | Prevent prompt injection in Large Language Models (MLOps Engineer) | [skills/llm-security/T4456-prevent-prompt-injection-in-large-language-models-mlops-engi/SKILL.md](./skills/llm-security/T4456-prevent-prompt-injection-in-large-language-models-mlops-engi/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4457 | Prevent prompt injection in Large Language Models (AI/ML Developer) | [skills/llm-security/T4457-prevent-prompt-injection-in-large-language-models-ai-ml-deve/SKILL.md](./skills/llm-security/T4457-prevent-prompt-injection-in-large-language-models-ai-ml-deve/SKILL.md) | 7 | ML_CODE | Pending | LIBRARY:TA8621 |
| T4458 | Prevent prompt injection in Large Language Models (Data Scientist) | [skills/llm-security/T4458-prevent-prompt-injection-in-large-language-models-data-scien/SKILL.md](./skills/llm-security/T4458-prevent-prompt-injection-in-large-language-models-data-scien/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4459 | Prevent prompt injection in Large Language Models (QA Analyst) | [skills/llm-security/T4459-prevent-prompt-injection-in-large-language-models-qa-analyst/SKILL.md](./skills/llm-security/T4459-prevent-prompt-injection-in-large-language-models-qa-analyst/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4460 | Handle insecure output in Large Language Models (AI/ML Developer) | [skills/llm-security/T4460-handle-insecure-output-in-large-language-models-ai-ml-develo/SKILL.md](./skills/llm-security/T4460-handle-insecure-output-in-large-language-models-ai-ml-develo/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4461 | Handle insecure output in Large Language Models (MLOps Engineer) | [skills/llm-security/T4461-handle-insecure-output-in-large-language-models-mlops-engine/SKILL.md](./skills/llm-security/T4461-handle-insecure-output-in-large-language-models-mlops-engine/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4462 | Prevent training data poisoning in Large Language Models (Project Manager) | [skills/llm-security/T4462-prevent-training-data-poisoning-in-large-language-models-pro/SKILL.md](./skills/llm-security/T4462-prevent-training-data-poisoning-in-large-language-models-pro/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4463 | Prevent training data poisoning in Large Language Models (MLOps Engineer) | [skills/llm-security/T4463-prevent-training-data-poisoning-in-large-language-models-mlo/SKILL.md](./skills/llm-security/T4463-prevent-training-data-poisoning-in-large-language-models-mlo/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4464 | Prevent training data poisoning in Large Language Models (Data Scientist) | [skills/llm-security/T4464-prevent-training-data-poisoning-in-large-language-models-dat/SKILL.md](./skills/llm-security/T4464-prevent-training-data-poisoning-in-large-language-models-dat/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4465 | Prevent training data poisoning in Large Language Models (AI/ML Developer) | [skills/llm-security/T4465-prevent-training-data-poisoning-in-large-language-models-ai/SKILL.md](./skills/llm-security/T4465-prevent-training-data-poisoning-in-large-language-models-ai/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4466 | Prevent Large Language Model denial of service (Project Manager) | [skills/llm-security/T4466-prevent-large-language-model-denial-of-service-project-manag/SKILL.md](./skills/llm-security/T4466-prevent-large-language-model-denial-of-service-project-manag/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4467 | Prevent Large Language Model denial of service (MLOps Engineer) | [skills/llm-security/T4467-prevent-large-language-model-denial-of-service-mlops-enginee/SKILL.md](./skills/llm-security/T4467-prevent-large-language-model-denial-of-service-mlops-enginee/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4468 | Prevent Large Language Models denial of service (AI/ML Developer) | [skills/llm-security/T4468-prevent-large-language-models-denial-of-service-ai-ml-develo/SKILL.md](./skills/llm-security/T4468-prevent-large-language-models-denial-of-service-ai-ml-develo/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4469 | Prevent Large Language Model denial of service (QA Analyst) | [skills/llm-security/T4469-prevent-large-language-model-denial-of-service-qa-analyst/SKILL.md](./skills/llm-security/T4469-prevent-large-language-model-denial-of-service-qa-analyst/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4470 | Protect Large Language Models against supply chain vulnerabilities (Project Manager) | [skills/llm-security/T4470-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md](./skills/llm-security/T4470-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4471 | Protect Large Language Models against supply chain vulnerabilities (MLOps Engineer) | [skills/llm-security/T4471-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md](./skills/llm-security/T4471-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4472 | Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer) | [skills/llm-security/T4472-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md](./skills/llm-security/T4472-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4473 | Protect Large Language Models against supply chain vulnerabilities (Data Scientist) | [skills/llm-security/T4473-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md](./skills/llm-security/T4473-protect-large-language-models-against-supply-chain-vulnerabi/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4474 | Prevent sensitive information disclosure in Large Language Models (Project Manager) | [skills/llm-security/T4474-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md](./skills/llm-security/T4474-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4475 | Prevent sensitive information disclosure in Large Language Models (MLOps Engineer) | [skills/llm-security/T4475-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md](./skills/llm-security/T4475-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4476 | Prevent sensitive information disclosure in Large Language Models (AI/ML Developer) | [skills/llm-security/T4476-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md](./skills/llm-security/T4476-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4477 | Prevent sensitive information disclosure in Large Language Models (Data Scientist) | [skills/llm-security/T4477-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md](./skills/llm-security/T4477-prevent-sensitive-information-disclosure-in-large-language-m/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4478 | Design secure plugins for Large Language Models (Project Manager) | [skills/llm-security/T4478-design-secure-plugins-for-large-language-models-project-mana/SKILL.md](./skills/llm-security/T4478-design-secure-plugins-for-large-language-models-project-mana/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4479 | Design secure plugins for Large Language Models (AI/ML Developer) | [skills/llm-security/T4479-design-secure-plugins-for-large-language-models-ai-ml-develo/SKILL.md](./skills/llm-security/T4479-design-secure-plugins-for-large-language-models-ai-ml-develo/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4480 | Design secure plugins for Large Language Models (MLOps Engineer) | [skills/llm-security/T4480-design-secure-plugins-for-large-language-models-mlops-engine/SKILL.md](./skills/llm-security/T4480-design-secure-plugins-for-large-language-models-mlops-engine/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4481 | Design secure plugins for Large Language Models (QA Analyst) | [skills/llm-security/T4481-design-secure-plugins-for-large-language-models-qa-analyst/SKILL.md](./skills/llm-security/T4481-design-secure-plugins-for-large-language-models-qa-analyst/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4482 | Mitigate excessive agency in Large Language Models (Project Manager) | [skills/llm-security/T4482-mitigate-excessive-agency-in-large-language-models-project-m/SKILL.md](./skills/llm-security/T4482-mitigate-excessive-agency-in-large-language-models-project-m/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4483 | Mitigate excessive agency in Large Language Models (MLOps Engineer) | [skills/llm-security/T4483-mitigate-excessive-agency-in-large-language-models-mlops-eng/SKILL.md](./skills/llm-security/T4483-mitigate-excessive-agency-in-large-language-models-mlops-eng/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4484 | Mitigate excessive agency in Large Language Models (AI/ML Developer) | [skills/llm-security/T4484-mitigate-excessive-agency-in-large-language-models-ai-ml-dev/SKILL.md](./skills/llm-security/T4484-mitigate-excessive-agency-in-large-language-models-ai-ml-dev/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4485 | Mitigate excessive agency in Large Language Models (QA Analyst) | [skills/llm-security/T4485-mitigate-excessive-agency-in-large-language-models-qa-analys/SKILL.md](./skills/llm-security/T4485-mitigate-excessive-agency-in-large-language-models-qa-analys/SKILL.md) | 7 | ML_CODE | Pending | TEMPLATE |
| T4486 | Mitigate overreliance in Large Language Models (Project Manager) | [skills/llm-security/T4486-mitigate-overreliance-in-large-language-models-project-manag/SKILL.md](./skills/llm-security/T4486-mitigate-overreliance-in-large-language-models-project-manag/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4487 | Mitigate overreliance in Large Language Models (MLOps Engineer) | [skills/llm-security/T4487-mitigate-overreliance-in-large-language-models-mlops-enginee/SKILL.md](./skills/llm-security/T4487-mitigate-overreliance-in-large-language-models-mlops-enginee/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4488 | Mitigate overreliance in Large Language Models (AI/ML Developer) | [skills/llm-security/T4488-mitigate-overreliance-in-large-language-models-ai-ml-develop/SKILL.md](./skills/llm-security/T4488-mitigate-overreliance-in-large-language-models-ai-ml-develop/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4489 | Mitigate overreliance in Large Language Models (Data Scientist) | [skills/llm-security/T4489-mitigate-overreliance-in-large-language-models-data-scientis/SKILL.md](./skills/llm-security/T4489-mitigate-overreliance-in-large-language-models-data-scientis/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4490 | Mitigate overreliance in Large Language Models (QA Analyst) | [skills/llm-security/T4490-mitigate-overreliance-in-large-language-models-qa-analyst/SKILL.md](./skills/llm-security/T4490-mitigate-overreliance-in-large-language-models-qa-analyst/SKILL.md) | 6 | ML_CODE | Pending | TEMPLATE |
| T4491 | Prevent model theft in Large Language Models (Project Manager) | [skills/llm-security/T4491-prevent-model-theft-in-large-language-models-project-manager/SKILL.md](./skills/llm-security/T4491-prevent-model-theft-in-large-language-models-project-manager/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4492 | Prevent model theft in Large Language Models (MLOps Engineer) | [skills/llm-security/T4492-prevent-model-theft-in-large-language-models-mlops-engineer/SKILL.md](./skills/llm-security/T4492-prevent-model-theft-in-large-language-models-mlops-engineer/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4493 | Prevent model theft in Large Language Models (AI/ML Developer) | [skills/llm-security/T4493-prevent-model-theft-in-large-language-models-ai-ml-developer/SKILL.md](./skills/llm-security/T4493-prevent-model-theft-in-large-language-models-ai-ml-developer/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4494 | Prevent model theft in Large Language Models (Data Scientist) | [skills/llm-security/T4494-prevent-model-theft-in-large-language-models-data-scientist/SKILL.md](./skills/llm-security/T4494-prevent-model-theft-in-large-language-models-data-scientist/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4495 | Prevent model theft in Large Language Models (QA Analyst) | [skills/llm-security/T4495-prevent-model-theft-in-large-language-models-qa-analyst/SKILL.md](./skills/llm-security/T4495-prevent-model-theft-in-large-language-models-qa-analyst/SKILL.md) | 7 | ML_DOC | Pending | TEMPLATE |
| T4830 | Ensure aligned training of generative AI models | [skills/llm-security/T4830-ensure-aligned-training-of-generative-ai-models/SKILL.md](./skills/llm-security/T4830-ensure-aligned-training-of-generative-ai-models/SKILL.md) | 8 | ML_DOC | Pending | TEMPLATE |
| T4833 | Test fine-tuning alignement of generative AI models | [skills/llm-security/T4833-test-fine-tuning-alignement-of-generative-ai-models/SKILL.md](./skills/llm-security/T4833-test-fine-tuning-alignement-of-generative-ai-models/SKILL.md) | 8 | ML_DOC | Pending | TEMPLATE |
| T4834 | Implement protection against system prompt leakage | [skills/llm-security/T4834-implement-protection-against-system-prompt-leakage/SKILL.md](./skills/llm-security/T4834-implement-protection-against-system-prompt-leakage/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4835 | Implement defenses against vector and embedding weaknesses | [skills/llm-security/T4835-implement-defenses-against-vector-and-embedding-weaknesses/SKILL.md](./skills/llm-security/T4835-implement-defenses-against-vector-and-embedding-weaknesses/SKILL.md) | 8 | ML_DOC | Pending | TEMPLATE |
| T4836 | Implement verification and fact-checking to mitigate misinformation | [skills/llm-security/T4836-implement-verification-and-fact-checking-to-mitigate-misinfo/SKILL.md](./skills/llm-security/T4836-implement-verification-and-fact-checking-to-mitigate-misinfo/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4837 | Test effectiveness of protections against system prompt leakage | [skills/llm-security/T4837-test-effectiveness-of-protections-against-system-prompt-leak/SKILL.md](./skills/llm-security/T4837-test-effectiveness-of-protections-against-system-prompt-leak/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |
| T4838 | Test effectiveness of defenses against vector and embedding weaknesses | [skills/llm-security/T4838-test-effectiveness-of-defenses-against-vector-and-embedding/SKILL.md](./skills/llm-security/T4838-test-effectiveness-of-defenses-against-vector-and-embedding/SKILL.md) | 8 | ML_DOC | Pending | TEMPLATE |
| T4839 | Test effectiveness of misinformation mitigatation | [skills/llm-security/T4839-test-effectiveness-of-misinformation-mitigatation/SKILL.md](./skills/llm-security/T4839-test-effectiveness-of-misinformation-mitigatation/SKILL.md) | 8 | ML_CODE | Pending | TEMPLATE |

### logging-monitoring
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T105 | Verify that your application does not have unnecessary debug capability or leftover test/debug code | [skills/logging-monitoring/T105-verify-that-your-application-does-not-have-unnecessary-debug/SKILL.md](./skills/logging-monitoring/T105-verify-that-your-application-does-not-have-unnecessary-debug/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T350 | Verify that audit information is sufficiently protected | [skills/logging-monitoring/T350-verify-that-audit-information-is-sufficiently-protected/SKILL.md](./skills/logging-monitoring/T350-verify-that-audit-information-is-sufficiently-protected/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T49 | Disable and remove debug capabilities and code/data, and prepare application for release | [skills/logging-monitoring/T49-disable-and-remove-debug-capabilities-and-code-data-and-prep/SKILL.md](./skills/logging-monitoring/T49-disable-and-remove-debug-capabilities-and-code-data-and-prep/SKILL.md) | 7 | CODE_FIX | Pending | LIBRARY:TA8625 |

### network-infra
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T2596 | Prevent HTTP Request Smuggling | [skills/network-infra/T2596-prevent-http-request-smuggling/SKILL.md](./skills/network-infra/T2596-prevent-http-request-smuggling/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T35 | Fine-tune HTTP server settings | [skills/network-infra/T35-fine-tune-http-server-settings/SKILL.md](./skills/network-infra/T35-fine-tune-http-server-settings/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T374 | Offload HTTP request handling to dedicated modules | [skills/network-infra/T374-offload-http-request-handling-to-dedicated-modules/SKILL.md](./skills/network-infra/T374-offload-http-request-handling-to-dedicated-modules/SKILL.md) | 7 | INFRA | Pending | TEMPLATE |
| T4600 | Establish Out-of-Band Communications Channel | [skills/network-infra/T4600-establish-out-of-band-communications-channel/SKILL.md](./skills/network-infra/T4600-establish-out-of-band-communications-channel/SKILL.md) | 10 | INFRA | Pending | TEMPLATE |
| T4601 | Prioritize static network configuration | [skills/network-infra/T4601-prioritize-static-network-configuration/SKILL.md](./skills/network-infra/T4601-prioritize-static-network-configuration/SKILL.md) | 8 | INFRA | Pending | TEMPLATE |
| T558 | Authenticate all other components before any network communication with them | [skills/network-infra/T558-authenticate-all-other-components-before-any-network-communi/SKILL.md](./skills/network-infra/T558-authenticate-all-other-components-before-any-network-communi/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T589 | Verify that all the components are authenticated explicitly | [skills/network-infra/T589-verify-that-all-the-components-are-authenticated-explicitly/SKILL.md](./skills/network-infra/T589-verify-that-all-the-components-are-authenticated-explicitly/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |

### secrets-config
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T2349 | Configure software to have secure settings by default | [skills/secrets-config/T2349-configure-software-to-have-secure-settings-by-default/SKILL.md](./skills/secrets-config/T2349-configure-software-to-have-secure-settings-by-default/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T2357 | Verify that software is configured to have secure settings by default | [skills/secrets-config/T2357-verify-that-software-is-configured-to-have-secure-settings-b/SKILL.md](./skills/secrets-config/T2357-verify-that-software-is-configured-to-have-secure-settings-b/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T241 | Verify that third party libraries use secure settings and the latest patches | [skills/secrets-config/T241-verify-that-third-party-libraries-use-secure-settings-and-th/SKILL.md](./skills/secrets-config/T241-verify-that-third-party-libraries-use-secure-settings-and-th/SKILL.md) | 10 | CODE_FIX | Pending | TEMPLATE |
| T2661 | Change insecure configuration defaults and remove unnecessary features | [skills/secrets-config/T2661-change-insecure-configuration-defaults-and-remove-unnecessar/SKILL.md](./skills/secrets-config/T2661-change-insecure-configuration-defaults-and-remove-unnecessar/SKILL.md) | 9 | INFRA | Pending | TEMPLATE |
| T456 | Change default security settings to the most stringent ones and disable unnecessary services and modules | [skills/secrets-config/T456-change-default-security-settings-to-the-most-stringent-ones/SKILL.md](./skills/secrets-config/T456-change-default-security-settings-to-the-most-stringent-ones/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T457 | Verify that unnecessary services and capabilities are disabled | [skills/secrets-config/T457-verify-that-unnecessary-services-and-capabilities-are-disabl/SKILL.md](./skills/secrets-config/T457-verify-that-unnecessary-services-and-capabilities-are-disabl/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### session-management
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T20 | Generate unique session IDs and reset old IDs after authentication | [skills/session-management/T20-generate-unique-session-ids-and-reset-old-ids-after-authenti/SKILL.md](./skills/session-management/T20-generate-unique-session-ids-and-reset-old-ids-after-authenti/SKILL.md) | 9 | CODE_FIX | Pending | TEMPLATE |
| T259 | Follow best practices when storing data in Local or Session Storage | [skills/session-management/T259-follow-best-practices-when-storing-data-in-local-or-session/SKILL.md](./skills/session-management/T259-follow-best-practices-when-storing-data-in-local-or-session/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T26 | Expire sessions on logout | [skills/session-management/T26-expire-sessions-on-logout/SKILL.md](./skills/session-management/T26-expire-sessions-on-logout/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T27 | Turn off session rewriting | [skills/session-management/T27-turn-off-session-rewriting/SKILL.md](./skills/session-management/T27-turn-off-session-rewriting/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T321 | Verify that Local and Session Storage are securely used | [skills/session-management/T321-verify-that-local-and-session-storage-are-securely-used/SKILL.md](./skills/session-management/T321-verify-that-local-and-session-storage-are-securely-used/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T4597 | Break and inspect SSL/TLS sessions | [skills/session-management/T4597-break-and-inspect-ssl-tls-sessions/SKILL.md](./skills/session-management/T4597-break-and-inspect-ssl-tls-sessions/SKILL.md) | 6 | INFRA | Pending | TEMPLATE |
| T93 | Test that sessions expire upon logout | [skills/session-management/T93-test-that-sessions-expire-upon-logout/SKILL.md](./skills/session-management/T93-test-that-sessions-expire-upon-logout/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |
| T94 | Test that session IDs are not leaked through URLs | [skills/session-management/T94-test-that-session-ids-are-not-leaked-through-urls/SKILL.md](./skills/session-management/T94-test-that-session-ids-are-not-leaked-through-urls/SKILL.md) | 6 | CODE_FIX | Pending | TEMPLATE |

### ssrf
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1365 | Mitigate Server Side Request Forgery | [skills/ssrf/T1365-mitigate-server-side-request-forgery/SKILL.md](./skills/ssrf/T1365-mitigate-server-side-request-forgery/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8521 |
| T1392 | Test for Server Side Request Forgery | [skills/ssrf/T1392-test-for-server-side-request-forgery/SKILL.md](./skills/ssrf/T1392-test-for-server-side-request-forgery/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |

### xss
| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T119 | Test for clickjacking | [skills/xss/T119-test-for-clickjacking/SKILL.md](./skills/xss/T119-test-for-clickjacking/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T169 | Test that the site is not vulnerable to DOM-based XSS | [skills/xss/T169-test-that-the-site-is-not-vulnerable-to-dom-based-xss/SKILL.md](./skills/xss/T169-test-that-the-site-is-not-vulnerable-to-dom-based-xss/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |
| T36 | Escape untrusted data in HTML, HTML attributes, CSS, and JavaScript | [skills/xss/T36-escape-untrusted-data-in-html-html-attributes-css-and-javasc/SKILL.md](./skills/xss/T36-escape-untrusted-data-in-html-html-attributes-css-and-javasc/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8479 |
| T37 | Avoid DOM-based Cross-Site Scripting (XSS) | [skills/xss/T37-avoid-dom-based-cross-site-scripting-xss/SKILL.md](./skills/xss/T37-avoid-dom-based-cross-site-scripting-xss/SKILL.md) | 8 | CODE_FIX | Pending | LIBRARY:TA8540 |
| T66 | Prevent web pages from being loaded inside iFrame | [skills/xss/T66-prevent-web-pages-from-being-loaded-inside-iframe/SKILL.md](./skills/xss/T66-prevent-web-pages-from-being-loaded-inside-iframe/SKILL.md) | 7 | CODE_FIX | Pending | TEMPLATE |
| T89 | Test that site is not vulnerable to XSS | [skills/xss/T89-test-that-site-is-not-vulnerable-to-xss/SKILL.md](./skills/xss/T89-test-that-site-is-not-vulnerable-to-xss/SKILL.md) | 8 | CODE_FIX | Pending | TEMPLATE |

## Completion Requirements

**ALL 309 file-tracked countermeasures must be addressed. No exceptions.**

### Progress Tracking

| Domain | Total | Applied | Documented | Remaining |
|--------|-------|---------|------------|-----------|
| api-security | 20 | 0 | 0 | 20 |
| authentication | 30 | 0 | 0 | 30 |
| authorization | 24 | 0 | 0 | 24 |
| backup-recovery | 5 | 0 | 0 | 5 |
| container-security | 73 | 0 | 0 | 73 |
| cors | 2 | 0 | 0 | 2 |
| crypto | 12 | 0 | 0 | 12 |
| csrf | 6 | 0 | 0 | 6 |
| data-protection | 4 | 0 | 0 | 4 |
| database-security | 29 | 0 | 0 | 29 |
| dependency-management | 2 | 0 | 0 | 2 |
| file-handling | 7 | 0 | 0 | 7 |
| general-hardening | 1 | 0 | 0 | 1 |
| injection | 10 | 0 | 0 | 10 |
| input-validation | 3 | 0 | 0 | 3 |
| llm-security | 49 | 0 | 0 | 49 |
| logging-monitoring | 3 | 0 | 0 | 3 |
| network-infra | 7 | 0 | 0 | 7 |
| secrets-config | 6 | 0 | 0 | 6 |
| session-management | 8 | 0 | 0 | 8 |
| ssrf | 2 | 0 | 0 | 2 |
| xss | 6 | 0 | 0 | 6 |
| **TOTAL** | **309** | **0** | **0** | **309** |

**Remaining MUST reach 0 before completion.**

## Verification Checklist

- [ ] All CODE_FIX countermeasures have fixes applied
- [ ] All fixes are in ORIGINAL files (no *_secure.* alternatives)
- [ ] All non-code items documented with justification
- [ ] Total addressed = 309
<!-- SDE-SECURITY-HARDENING-END -->
