---
name: t2613-verify-best-practices-for-data-restoring-operations-are-fo
description: Verify the following steps are taken to minimize the risk of corruption. - Verify that the recovery procedures are tested regularly to ensure that data can be restored without any issues. - Verify that a comprehensive restoration checklist 
---

# T2613: Verify best practices for data-restoring operations are followed

**Category:** INFRA  
**SD Elements:** [T2613](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2613/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Why Not Directly Code-Fixable in This Repository

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify the following steps are taken to minimize the risk of corruption. 

- Verify that the recovery procedures are tested regularly to ensure that data can be restored without any issues.

- Verify that a comprehensive restoration checklist is provided to ensure that everything is in place for data restoration.

- Verify that backup verification tools are used to test the size and integrity of backups. Ensure that if any of these tests uncover an anomaly, the administrators are alerted immediately.

- Verify that the data restoration plan is shared with relevant personnel in the company to ensure that whoever is in charge in the event of failure knows the procedure and can follow it easily.

## Success Criteria

- The requirement "Verify best practices for data-restoring operations are followed" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
