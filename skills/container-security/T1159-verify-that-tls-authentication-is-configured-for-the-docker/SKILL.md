---
name: t1159-verify-that-tls-authentication-is-configured-for-the-docke
description: Run the following command: ```ps -ef | grep dockerd``` Ensure that the below parameters are present: * '--tlsverify' * '--tlscacert' * '--tlscert' * '--tlskey'
---

# T1159: Verify that TLS authentication is configured for the Docker daemon (Docker)

**Category:** INFRA  
**SD Elements:** [T1159](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1159/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Run the following command:

```ps -ef | grep dockerd``` 

Ensure that the below parameters are present:

* '--tlsverify'
* '--tlscacert'
* '--tlscert'
* '--tlskey'

## Success Criteria

- The requirement "Verify that TLS authentication is configured for the Docker daemon (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
