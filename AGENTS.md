# AGENTS.md

<!-- SDE-SECURITY-HARDENING:BEGIN -->

## Security Hardening Plan

Generated: 20260611-2019
Project: vuln-bank-for-testing (SD Elements Project ID: 31905)
Branch: security-hardening/vuln-bank-for-testing-20260611-2019

### Summary

| Classification | Count | Action |
|---|---|---|
| CODE_FIX | 32 | Fix existing vulnerable code |
| ML_CODE | 9 | Implement new security features |
| INFRA | 28 | Infrastructure/deployment hardening |
| PROCESS | 31 | Organizational process tasks (noted in SDE) |

### Execution Ledger

Each entry below links to a skill file containing fix instructions.

| # | CM ID | Domain | Title | Status |
|---|---|---|---|---|
| 1 | T1187 | docker | [Test if secrets are stored in Dockerfiles (Docker)](.sde-security/skills/docker/t1187-test-if-secrets-are-stored-in-dockerfile/SKILL.md) | pending |
| 2 | T1186 | docker | [Do not store secrets in Dockerfiles (Docker)](.sde-security/skills/docker/t1186-do-not-store-secrets-in-dockerfiles-doc/SKILL.md) | pending |
| 3 | T3916 | github | [Ensure automated and secure deployment (GitHub)](.sde-security/skills/github/t3916-ensure-automated-and-secure-deployment/SKILL.md) | pending |
| 4 | T3903 | github | [Implement application and webhook security strateg](.sde-security/skills/github/t3903-implement-application-and-webhook-securi/SKILL.md) | pending |
| 5 | T3906 | github | [Implement secure build worker management (GitHub)](.sde-security/skills/github/t3906-implement-secure-build-worker-management/SKILL.md) | pending |
| 6 | T4484 | ai-ml | [Mitigate excessive agency in Large Language Models](.sde-security/skills/ai-ml/t4484-mitigate-excessive-agency-in-large-langu/SKILL.md) | pending |
| 7 | T50 | file-security | [Use indirect object reference maps if accessing fi](.sde-security/skills/file-security/t50-use-indirect-object-reference-maps-if-ac/SKILL.md) | pending |
| 8 | T2139 | web-security | [Prevent information exposure through APIs](.sde-security/skills/web-security/t2139-prevent-information-exposure-through-api/SKILL.md) | pending |
| 9 | T2606 | authentication | [Verify RBAC implemented instead of individual acco](.sde-security/skills/authentication/t2606-verify-rbac-implemented-instead-of-indiv/SKILL.md) | pending |
| 10 | T1213 | docker | [Verify that cgroup usage is confirmed (Docker)](.sde-security/skills/docker/t1213-verify-that-cgroup-usage-is-confirmed-d/SKILL.md) | pending |
| 11 | T1180 | docker | [Check container health (Docker)](.sde-security/skills/docker/t1180-check-container-health-docker/SKILL.md) | pending |
| 12 | T323 | cryptography | [Test that default accounts are disabled or default](.sde-security/skills/cryptography/t323-test-that-default-accounts-are-disabled/SKILL.md) | pending |
| 13 | T220 | cryptography | [Verify that user password is salted and hashed](.sde-security/skills/cryptography/t220-verify-that-user-password-is-salted-and/SKILL.md) | pending |
| 14 | T65 | web-security | [Restrict accepted HTTP verbs](.sde-security/skills/web-security/t65-restrict-accepted-http-verbs/SKILL.md) | pending |
| 15 | T36 | input-validation | [Escape untrusted data in HTML, HTML attributes, CS](.sde-security/skills/input-validation/t36-escape-untrusted-data-in-html-html-attr/SKILL.md) | pending |
| 16 | T17 | authentication | [Do not only rely on client-side authorization](.sde-security/skills/authentication/t17-do-not-only-rely-on-client-side-authoriz/SKILL.md) | pending |
| 17 | T1159 | docker | [Verify that TLS authentication is configured for t](.sde-security/skills/docker/t1159-verify-that-tls-authentication-is-config/SKILL.md) | pending |
| 18 | T4466 | ai-ml | [Prevent Large Language Model denial of service (Pr](.sde-security/skills/ai-ml/t4466-prevent-large-language-model-denial-of-s/SKILL.md) | pending |
| 19 | T119 | web-security | [Test for clickjacking](.sde-security/skills/web-security/t119-test-for-clickjacking/SKILL.md) | pending |
| 20 | T338 | authentication | [Control access to resources through user authentic](.sde-security/skills/authentication/t338-control-access-to-resources-through-user/SKILL.md) | pending |
| 21 | T62 | cryptography | [Protect passwords in property and configuration fi](.sde-security/skills/cryptography/t62-protect-passwords-in-property-and-config/SKILL.md) | pending |
| 22 | T375 | resource-management | [Release resources when no longer needed](.sde-security/skills/resource-management/t375-release-resources-when-no-longer-needed/SKILL.md) | pending |
| 23 | T2614 | general-security | [Verify database traffic is validated](.sde-security/skills/general-security/t2614-verify-database-traffic-is-validated/SKILL.md) | pending |
| 24 | T1203 | docker | [Test if container CPU priority is appropriately se](.sde-security/skills/docker/t1203-test-if-container-cpu-priority-is-approp/SKILL.md) | pending |
| 25 | T4452 | shell-security | [Test environmental vulnerabilities (Bash/Shell)](.sde-security/skills/shell-security/t4452-test-environmental-vulnerabilities-bash/SKILL.md) | pending |
| 26 | T3901 | github | [Enforce repository management and security strateg](.sde-security/skills/github/t3901-enforce-repository-management-and-securi/SKILL.md) | pending |
| 27 | T545 | data-privacy | [Verify that personal information is anonymized bef](.sde-security/skills/data-privacy/t545-verify-that-personal-information-is-anon/SKILL.md) | pending |
| 28 | T2257 | docker | [Regularly update and patch containerization system](.sde-security/skills/docker/t2257-regularly-update-and-patch-containerizat/SKILL.md) | pending |
| 29 | T2601 | cryptography | [Use Transparent Data Encryption with Enterprise Da](.sde-security/skills/cryptography/t2601-use-transparent-data-encryption-with-ent/SKILL.md) | pending |
| 30 | T4448 | shell-security | [Test prevention against input file attacks (Bash/S](.sde-security/skills/shell-security/t4448-test-prevention-against-input-file-attac/SKILL.md) | pending |
| 31 | T4480 | ai-ml | [Design secure plugins for Large Language Models (M](.sde-security/skills/ai-ml/t4480-design-secure-plugins-for-large-language/SKILL.md) | pending |
| 32 | T4440 | shell-security | [Enforce access controls (Bash/Shell)](.sde-security/skills/shell-security/t4440-enforce-access-controls-bash-shell/SKILL.md) | pending |
| 33 | T754 | data-privacy | [Enable the restriction of processing personal info](.sde-security/skills/data-privacy/t754-enable-the-restriction-of-processing-per/SKILL.md) | pending |
| 34 | T4835 | ai-ml | [Implement defenses against vector and embedding we](.sde-security/skills/ai-ml/t4835-implement-defenses-against-vector-and-em/SKILL.md) | pending |
| 35 | T1177 | docker | [Verify that secure and updated images are used (Do](.sde-security/skills/docker/t1177-verify-that-secure-and-updated-images-ar/SKILL.md) | pending |
| 36 | T1210 | docker | [Configure seccomp profile (Docker)](.sde-security/skills/docker/t1210-configure-seccomp-profile-docker/SKILL.md) | pending |
| 37 | T2258 | deployment | [Minimize host OS attack surface](.sde-security/skills/deployment/t2258-minimize-host-os-attack-surface/SKILL.md) | pending |
| 38 | T87 | network-security | [Verify that all data in transit is encrypted using](.sde-security/skills/network-security/t87-verify-that-all-data-in-transit-is-encry/SKILL.md) | pending |
| 39 | T179 | data-privacy | [Allow access for users to remove their personal in](.sde-security/skills/data-privacy/t179-allow-access-for-users-to-remove-their-p/SKILL.md) | pending |
| 40 | T1156 | docker | [Do not use the aufs storage driver (Docker)](.sde-security/skills/docker/t1156-do-not-use-the-aufs-storage-driver-dock/SKILL.md) | pending |
| 41 | T1212 | docker | [Confirm cgroup usage (Docker)](.sde-security/skills/docker/t1212-confirm-cgroup-usage-docker/SKILL.md) | pending |
| 42 | T4456 | ai-ml | [Prevent prompt injection in Large Language Models ](.sde-security/skills/ai-ml/t4456-prevent-prompt-injection-in-large-langua/SKILL.md) | pending |
| 43 | T1194 | docker | [Do not run SSH within containers (Docker)](.sde-security/skills/docker/t1194-do-not-run-ssh-within-containers-docker/SKILL.md) | pending |
| 44 | T70 | authentication | [Implement account lockout or authentication thrott](.sde-security/skills/authentication/t70-implement-account-lockout-or-authenticat/SKILL.md) | pending |
| 45 | T2141 | authentication | [Perform function level authorization in API](.sde-security/skills/authentication/t2141-perform-function-level-authorization-in/SKILL.md) | pending |
| 46 | T60 | cryptography | [Use correct and approved cryptographic algorithms,](.sde-security/skills/cryptography/t60-use-correct-and-approved-cryptographic-a/SKILL.md) | pending |
| 47 | T2661 | deployment | [Change insecure configuration defaults and remove ](.sde-security/skills/deployment/t2661-change-insecure-configuration-defaults-a/SKILL.md) | pending |
| 48 | T2256 | authentication | [Authenticate and log all access to registries cont](.sde-security/skills/authentication/t2256-authenticate-and-log-all-access-to-regis/SKILL.md) | pending |
| 49 | T2478 | deployment | [Manage re-deployment routines](.sde-security/skills/deployment/t2478-manage-re-deployment-routines/SKILL.md) | pending |
| 50 | T4447 | shell-security | [Test directory writing and reading (Bash/Shell)](.sde-security/skills/shell-security/t4447-test-directory-writing-and-reading-bash/SKILL.md) | pending |
| 51 | T1160 | docker | [Set ulimit appropriately (Docker)](.sde-security/skills/docker/t1160-set-ulimit-appropriately-docker/SKILL.md) | pending |
| 52 | T4475 | ai-ml | [Prevent sensitive information disclosure in Large ](.sde-security/skills/ai-ml/t4475-prevent-sensitive-information-disclosure/SKILL.md) | pending |
| 53 | T4459 | ai-ml | [Prevent prompt injection in Large Language Models ](.sde-security/skills/ai-ml/t4459-prevent-prompt-injection-in-large-langua/SKILL.md) | pending |
| 54 | T85 | authentication | [Test server-side enforcement of authorization](.sde-security/skills/authentication/t85-test-server-side-enforcement-of-authoriz/SKILL.md) | pending |
| 55 | T219 | general-security | [Avoid transmitting confidential data through URL p](.sde-security/skills/general-security/t219-avoid-transmitting-confidential-data-thr/SKILL.md) | pending |
| 56 | T279 | general-security | [Avoid dynamically loading any code without proper ](.sde-security/skills/general-security/t279-avoid-dynamically-loading-any-code-witho/SKILL.md) | pending |
| 57 | T2110 | docker | [Verify that signed image enforcement is enabled (D](.sde-security/skills/docker/t2110-verify-that-signed-image-enforcement-is/SKILL.md) | pending |
| 58 | T2604 | general-security | [Follow best practices for data restoring operation](.sde-security/skills/general-security/t2604-follow-best-practices-for-data-restoring/SKILL.md) | pending |
| 59 | T1158 | docker | [Configure TLS authentication for the Docker daemon](.sde-security/skills/docker/t1158-configure-tls-authentication-for-the-doc/SKILL.md) | pending |
| 60 | T93 | authentication | [Test that sessions expire upon logout](.sde-security/skills/authentication/t93-test-that-sessions-expire-upon-logout/SKILL.md) | pending |
| 61 | T2612 | deployment | [Verify backup archive bits are protected](.sde-security/skills/deployment/t2612-verify-backup-archive-bits-are-protected/SKILL.md) | pending |
| 62 | T2282 | authentication | [Test to confirm that unauthenticated parts of the ](.sde-security/skills/authentication/t2282-test-to-confirm-that-unauthenticated-par/SKILL.md) | pending |
| 63 | T421 | input-validation | [Verify if web page template is vulnerable to clien](.sde-security/skills/input-validation/t421-verify-if-web-page-template-is-vulnerabl/SKILL.md) | pending |
| 64 | T114 | authentication | [Test system-to-system authentication lockout or th](.sde-security/skills/authentication/t114-test-system-to-system-authentication-loc/SKILL.md) | pending |
| 65 | T1235 | docker | [Test that only trusted users can control the Docke](.sde-security/skills/docker/t1235-test-that-only-trusted-users-can-control/SKILL.md) | pending |
| 66 | T79 | cryptography | [Test password change functions](.sde-security/skills/cryptography/t79-test-password-change-functions/SKILL.md) | pending |
| 67 | T2613 | general-security | [Verify best practices for data-restoring operation](.sde-security/skills/general-security/t2613-verify-best-practices-for-data-restoring/SKILL.md) | pending |
| 68 | T3902 | github | [Ensure regular review and inactive users removal (](.sde-security/skills/github/t3902-ensure-regular-review-and-inactive-users/SKILL.md) | pending |
| 69 | T222 | authentication | [Verify server-to-server authentication](.sde-security/skills/authentication/t222-verify-server-to-server-authentication/SKILL.md) | pending |

### PROCESS CMs (noted in SD Elements, not code-actionable)

| CM ID | Title |
|---|---|
| T1387 | Ensure the security of products acquired through the supply  |
| T2353 | Verify that proper criteria for software security checks are |
| T4492 | Prevent model theft in Large Language Models (MLOps Engineer |
| T3926 | Test third-party artifact security (GitHub) |
| T1370 | Identify and track common software weaknesses and threats |
| T4482 | Mitigate excessive agency in Large Language Models (Project  |
| T3924 | Test pipeline definition and security (GitHub) |
| T3927 | Test dependency management strategy (GitHub) |
| T1540 | Verify that browser data is cleared upon user logout |
| T2331 | Verify whether any plan exists for data privacy incident res |
| T2140 | Test that APIs do not expose sensitive information |
| T2296 | Securely install and configure all software components |
| T2516 | Verify that common software weaknesses and threats are ident |
| T2670 | Verify that applicable compliance regulations are identified |
| T4476 | Prevent sensitive information disclosure in Large Language M |
| T4833 | Test fine-tuning alignement of generative AI models |
| T3925 | Test artifact signing (GitHub) |
| T240 | Test whether users can remove their data from the system |
| T756 | Verify if personal data processing activities are recorded a |
| T2474 | Include security constraints in all user stories and feature |
| T1921 | Track and manage usage of third-party and commercial off the |
| T2352 | Verify that supporting toolchains are properly implemented |
| T3932 | Test separation of deployment configuration files (GitHub) |
| T2501 | Perform cybersecurity planning |
| T2676 | Verify that a bi-directional communication channel is establ |
| T2506 | Verify the cybersecurity assessment report |
| T2170 | Ensure that personal information processed by the applicatio |
| T1892 | Perform a Threat and Risk Assessment (TRA) |
| T573 | Prevent UDDI/ebXML spoofing |
| T1369 | Perform security testing using DAST tools |
| T1368 | Perform security testing using SAST tools |

<!-- SDE-SECURITY-HARDENING:END -->