---
name: t2106-verify-that-the-use-of-client-certificate-bundles-for-unpr
description: UCP cluster administrators can audit client certificate bundles on a per-user basis. You can verify that a user's client certificate bundle has been created by navigating to the `USER MANAGEMENT | USERS` interface in UCP, selecting the user
---

# T2106: Verify that the use of client certificate bundles for unprivileged users is enforced (Docker)

**Category:** INFRA  
**SD Elements:** [T2106](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2106/)  
**Priority:** 7  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

UCP cluster administrators can audit client certificate bundles on a per-user basis. You can verify that a user's client certificate bundle has been created by navigating to the `USER MANAGEMENT | USERS` interface in UCP, selecting the user from the list, clicking on the "Configure" button from the right-hand navigation menu, and selecting "Client Bundle" from the drop-down. From there, a list of client bundles assigned to the user will appear.

## Success Criteria

- The requirement "Verify that the use of client certificate bundles for unprivileged users is enforced (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
