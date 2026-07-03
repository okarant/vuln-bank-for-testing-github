<!-- SDE-SECURITY-HARDENING-START -->
# Security Hardening (SD Elements)

## Project Overview

| Field | Value |
|-------|-------|
| Application | oleg-vbank-qa2 |
| SD Elements Project | [https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/) |
| Project ID | 31945 |
| Total Countermeasures (selected scope) | 102 |
| Source | Codebase |

## Countermeasure Summary by Category

| Category | Count |
|----------|-------|
| CODE_FIX | 51 |
| ML_CODE | 8 |
| ML_DOC | 5 |
| INFRA | 19 |
| PROCESS | 19 |

### api-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1362 | Perform message throttling in Web APIs | skills/api-security/T1362-perform-message-throttling-in-web-apis/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T166 | Protect against JSON hijacking | skills/api-security/T166-protect-against-json-hijacking/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T2139 | Prevent information exposure through APIs | skills/api-security/T2139-prevent-information-exposure-through-apis/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T2269 | Prevent batching attacks (GraphQL) | skills/api-security/T2269-prevent-batching-attacks-graphql/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T2281 | Secure access control (GraphQL) | skills/api-security/T2281-python/SKILL.md | P8 | CODE_FIX | Pending | LIBRARY:TA8570 |
| T2283 | Configure GraphQL correctly | skills/api-security/T2283-configure-graphql-correctly/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T257 | Secure cross origin resource sharing (CORS) | skills/api-security/T257-secure-cross-origin-resource-sharing-cors/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T2599 | Protect against connection string parameter pollution | skills/api-security/T2599-protect-against-connection-string-parameter-poll/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T2600 | Control the result set size returned by a query | skills/api-security/T2600-control-the-result-set-size-returned-by-a-query/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T281 | Follow best practices when handling access tokens (API tokens) | skills/api-security/T281-follow-best-practices-when-handling-access-token/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T284 | Generate secure access tokens (API tokens) | skills/api-security/T284-generate-secure-access-tokens-api-tokens/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T536 | Restrict the size of incoming messages in services | skills/api-security/T536-restrict-the-size-of-incoming-messages-in-servic/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T66 | Prevent web pages from being loaded inside iFrame | skills/api-security/T66-prevent-web-pages-from-being-loaded-inside-ifram/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T70 | Implement account lockout or authentication throttling for system accounts | skills/api-security/T70-implement-account-lockout-or-authentication-thro/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |

### authentication

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1918 | Integrate with SSO | skills/authentication/T1918-integrate-with-sso/SKILL.md | P9 | CODE_FIX | Skipped | TEMPLATE |
| T1919 | Use JSON Web Token (JWT) securely | skills/authentication/T1919-use-json-web-token-jwt-securely/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T2 | Secure the password reset mechanism | skills/authentication/T2-python/SKILL.md | P9 | CODE_FIX | Pending | LIBRARY:TA8478 |
| T20 | Generate unique session IDs and reset old IDs after authentication | skills/authentication/T20-generate-unique-session-ids-and-reset-old-ids-af/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T338 | Control access to resources through user authentication and authorization | skills/authentication/T338-control-access-to-resources-through-user-authent/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T394 | Secure one-time passwords (OTP) | skills/authentication/T394-secure-one-time-passwords-otp/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T69 | Strong password requirements for server-to-server system accounts | skills/authentication/T69-python/SKILL.md | P8 | CODE_FIX | Pending | LIBRARY:TA8615 |
| T76 | Do not hardcode passwords | skills/authentication/T76-python/SKILL.md | P10 | CODE_FIX | Applied | LIBRARY:TA8509 |

### authorization

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T17 | Do not only rely on client-side authorization | skills/authorization/T17-do-not-only-rely-on-client-side-authorization/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T184 | Perform authorization checks on RESTful web services | skills/authorization/T184-perform-authorization-checks-on-restful-web-serv/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T2598 | Implement query-level access control | skills/authorization/T2598-implement-query-level-access-control/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T378 | Authorize every request for data objects | skills/authorization/T378-authorize-every-request-for-data-objects/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T50 | Use indirect object reference maps if accessing files | skills/authorization/T50-use-indirect-object-reference-maps-if-accessing/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |

### crypto

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1468 | Encrypt sensitive data at rest in the browser | skills/crypto/T1468-encrypt-sensitive-data-at-rest-in-the-browser/SKILL.md | P9 | CODE_FIX | Pending | TEMPLATE |
| T151 | Use cryptographically secure random numbers | skills/crypto/T151-use-cryptographically-secure-random-numbers/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T156 | Validate certificate and its chain of trust properly | skills/crypto/T156-validate-certificate-and-its-chain-of-trust-prop/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T21 | Ensure all data in transit is encrypted using a secure TLS channel | skills/crypto/T21-python/SKILL.md | P8 | INFRA | Pending | LIBRARY:TA8620 |
| T295 | Avoid storing unencrypted confidential data without access control mechanisms | skills/crypto/T295-avoid-storing-unencrypted-confidential-data-with/SKILL.md | P7 | CODE_FIX | Pending | TEMPLATE |
| T59 | Use standard libraries for cryptography | skills/crypto/T59-python/SKILL.md | P8 | CODE_FIX | Pending | LIBRARY:TA8547 |
| T60 | Use correct and approved cryptographic algorithms, parameters, and key lengths | skills/crypto/T60-use-correct-and-approved-cryptographic-algorithm/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |

### general-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T19 | Restrict Application's Access to Database | skills/general-security/T19-python/SKILL.md | P8 | INFRA | Pending | LIBRARY:TA8571 |

### infrastructure

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T214 | Protect confidential files on operating system or server | skills/infrastructure/T214-protect-confidential-files-on-operating-system-o/SKILL.md | P9 | INFRA | Pending | TEMPLATE |
| T35 | Fine-tune HTTP server settings | skills/infrastructure/T35-fine-tune-http-server-settings/SKILL.md | P9 | INFRA | Pending | TEMPLATE |
| T374 | Offload HTTP request handling to dedicated modules | skills/infrastructure/T374-offload-http-request-handling-to-dedicated-modul/SKILL.md | P7 | INFRA | Pending | TEMPLATE |
| T4746 | Ensure container images are secure | skills/infrastructure/T4746-ensure-container-images-are-secure/SKILL.md | P10 | INFRA | Pending | TEMPLATE |
| T4751 | Reduce the attack surface of container images | skills/infrastructure/T4751-reduce-the-attack-surface-of-container-images/SKILL.md | P10 | INFRA | Pending | TEMPLATE |
| T558 | Authenticate all other components before any network communication with them | skills/infrastructure/T558-authenticate-all-other-components-before-any-net/SKILL.md | P9 | INFRA | Pending | TEMPLATE |
| T573 | Prevent UDDI/ebXML spoofing | skills/infrastructure/T573-prevent-uddi-ebxml-spoofing/SKILL.md | P8 | INFRA | Pending | TEMPLATE |

### injection

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| CT435 | Bind variables in SQL statements - Oleg Test | skills/injection/CT435-bind-variables-in-sql-statements-oleg-test/SKILL.md | P10 | CODE_FIX | Applied | TEMPLATE |
| T1144 | Prevent Server-Side Template Injection (SSTI) | skills/injection/T1144-prevent-server-side-template-injection-ssti/SKILL.md | P8 | CODE_FIX | Documented | TEMPLATE |
| T1365 | Mitigate Server Side Request Forgery | skills/injection/T1365-python/SKILL.md | P8 | CODE_FIX | Applied | LIBRARY:TA8521 |
| T279 | Avoid dynamically loading any code without proper security considerations | skills/injection/T279-avoid-dynamically-loading-any-code-without-prope/SKILL.md | P8 | CODE_FIX | Documented | TEMPLATE |
| T29 | Use anti-Cross-Site Request Forgery (CSRF) tokens | skills/injection/T29-use-anti-cross-site-request-forgery-csrf-tokens/SKILL.md | P7 | CODE_FIX | Documented | TEMPLATE |
| T36 | Escape untrusted data in HTML, HTML attributes, CSS, and JavaScript | skills/injection/T36-javascript/SKILL.md | P8 | CODE_FIX | Documented | LIBRARY:TA8479 |
| T37 | Avoid DOM-based Cross-Site Scripting (XSS) | skills/injection/T37-python/SKILL.md | P8 | CODE_FIX | Documented | LIBRARY:TA8540 |
| T38 | Bind variables in SQL statements | skills/injection/T38-bind-variables-in-sql-statements/SKILL.md | P10 | CODE_FIX | Applied | TEMPLATE |
| T42 | Avoid relying on untrusted data for server-side selection | skills/injection/T42-avoid-relying-on-untrusted-data-for-server-side/SKILL.md | P10 | CODE_FIX | Documented | TEMPLATE |

### llm-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T4457 | Prevent prompt injection in Large Language Models (AI/ML Developer) | skills/llm-security/T4457-python/SKILL.md | P7 | ML_CODE | Pending | LIBRARY:TA8621 |
| T4458 | Prevent prompt injection in Large Language Models (Data Scientist) | skills/llm-security/T4458-prevent-prompt-injection-in-large-language-model/SKILL.md | P7 | ML_DOC | Pending | TEMPLATE |
| T4460 | Handle insecure output in Large Language Models (AI/ML Developer) | skills/llm-security/T4460-handle-insecure-output-in-large-language-models/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4464 | Prevent training data poisoning in Large Language Models (Data Scientist) | skills/llm-security/T4464-prevent-training-data-poisoning-in-large-languag/SKILL.md | P7 | ML_DOC | Pending | TEMPLATE |
| T4465 | Prevent training data poisoning in Large Language Models (AI/ML Developer) | skills/llm-security/T4465-prevent-training-data-poisoning-in-large-languag/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4468 | Prevent Large Language Models denial of service (AI/ML Developer) | skills/llm-security/T4468-prevent-large-language-models-denial-of-service/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4472 | Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer) | skills/llm-security/T4472-protect-large-language-models-against-supply-cha/SKILL.md | P8 | ML_CODE | Pending | TEMPLATE |
| T4473 | Protect Large Language Models against supply chain vulnerabilities (Data Scientist) | skills/llm-security/T4473-protect-large-language-models-against-supply-cha/SKILL.md | P8 | ML_DOC | Pending | TEMPLATE |
| T4476 | Prevent sensitive information disclosure in Large Language Models (AI/ML Developer) | skills/llm-security/T4476-prevent-sensitive-information-disclosure-in-larg/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4477 | Prevent sensitive information disclosure in Large Language Models (Data Scientist) | skills/llm-security/T4477-prevent-sensitive-information-disclosure-in-larg/SKILL.md | P7 | ML_DOC | Pending | TEMPLATE |
| T4484 | Mitigate excessive agency in Large Language Models (AI/ML Developer) | skills/llm-security/T4484-mitigate-excessive-agency-in-large-language-mode/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4493 | Prevent model theft in Large Language Models (AI/ML Developer) | skills/llm-security/T4493-prevent-model-theft-in-large-language-models-ai/SKILL.md | P7 | ML_CODE | Pending | TEMPLATE |
| T4494 | Prevent model theft in Large Language Models (Data Scientist) | skills/llm-security/T4494-prevent-model-theft-in-large-language-models-dat/SKILL.md | P7 | ML_DOC | Pending | TEMPLATE |

### logging-monitoring

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T1539 | Clear browser data on user logout | skills/logging-monitoring/T1539-clear-browser-data-on-user-logout/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T2602 | Log typical database and server activities and related metadata | skills/logging-monitoring/T2602-log-typical-database-and-server-activities-and-r/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T349 | Protect audit information and logs against unauthorized access | skills/logging-monitoring/T349-protect-audit-information-and-logs-against-unaut/SKILL.md | P7 | INFRA | Pending | TEMPLATE |
| T49 | Disable and remove debug capabilities and code/data, and prepare application for release | skills/logging-monitoring/T49-python/SKILL.md | P7 | CODE_FIX | Pending | LIBRARY:TA8625 |

### privacy

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T178 | Obtain consent from users prior to collecting personal information | skills/privacy/T178-obtain-consent-from-users-prior-to-collecting-pe/SKILL.md | P10 | CODE_FIX | Pending | TEMPLATE |
| T544 | Anonymize (de-identify) identifying information before using it for a secondary purpose | skills/privacy/T544-anonymize-de-identify-identifying-information-be/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T604 | Implement a consent withdrawal mechanism | skills/privacy/T604-implement-a-consent-withdrawal-mechanism/SKILL.md | P10 | CODE_FIX | Pending | TEMPLATE |
| T744 | Protect pseudonymized personal information | skills/privacy/T744-protect-pseudonymized-personal-information/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |
| T754 | Enable the restriction of processing personal information of an individual for a specific purpose | skills/privacy/T754-enable-the-restriction-of-processing-personal-in/SKILL.md | P8 | CODE_FIX | Pending | TEMPLATE |

### supply-chain

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T186 | Use recommended settings and the latest patches for third party libraries and software | skills/supply-chain/T186-use-recommended-settings-and-the-latest-patches/SKILL.md | P10 | CODE_FIX | Pending | TEMPLATE |
| T3903 | Implement application and webhook security strategies (GitHub) | skills/supply-chain/T3903-implement-application-and-webhook-security-strat/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3905 | Ensure pipeline efficiency and security (GitHub) | skills/supply-chain/T3905-ensure-pipeline-efficiency-and-security-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3906 | Implement secure build worker management (GitHub) | skills/supply-chain/T3906-implement-secure-build-worker-management-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3907 | Ensure pipeline definition and security (GitHub) | skills/supply-chain/T3907-ensure-pipeline-definition-and-security-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3908 | Enforce artifact signing (GitHub) | skills/supply-chain/T3908-enforce-artifact-signing-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3909 | Ensure third-party artifact security (GitHub) | skills/supply-chain/T3909-ensure-third-party-artifact-security-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3910 | Implement dependency management strategy (GitHub) | skills/supply-chain/T3910-implement-dependency-management-strategy-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3912 | Enforce artifact certification and uploading rules (GitHub) | skills/supply-chain/T3912-enforce-artifact-certification-and-uploading-rul/SKILL.md | P8 | INFRA | Pending | TEMPLATE |
| T3913 | Implement package registry security (GitHub) | skills/supply-chain/T3913-implement-package-registry-security-github/SKILL.md | P8 | INFRA | Pending | TEMPLATE |

## Progress Tracking

| Metric | Value |
|--------|-------|
| Total skill files | 83 |
| Applied | 0 |
| Pending | 83 |

## Verification Checklist

- [ ] All CODE_FIX/ML_CODE countermeasures applied
- [ ] All ML_DOC/INFRA countermeasures documented
- [ ] All PROCESS countermeasures noted in SD Elements

<!-- SDE-SECURITY-HARDENING-END -->
