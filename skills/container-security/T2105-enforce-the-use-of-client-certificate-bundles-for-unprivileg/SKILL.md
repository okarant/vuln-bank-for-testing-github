---
name: t2105-enforce-the-use-of-client-certificate-bundles-for-unprivil
description: Provide unprivileged users with client certificate bundles for connecting to UCP manager nodes and communicating with a UCP cluster so that their access rights are controlled via the built-in role-based access control (RBAC) model. With the
---

# T2105: Enforce the use of client certificate bundles for unprivileged users to access UCP (Docker)

**Category:** INFRA  
**SD Elements:** [T2105](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2105/)  
**Priority:** 7  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Provide unprivileged users with client certificate bundles for connecting to UCP manager nodes and communicating with a UCP cluster so that their access rights are controlled via the built-in role-based access control (RBAC) model.

With the use of UCP client certificate bundles, you do not need to include standard users in the "docker" security group and instead, you can facilitate user access to the cluster via RBAC.

## Success Criteria

- The requirement "Enforce the use of client certificate bundles for unprivileged users to access UCP (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
