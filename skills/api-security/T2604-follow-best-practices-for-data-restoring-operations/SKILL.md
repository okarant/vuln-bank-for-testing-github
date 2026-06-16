---
name: t2604-follow-best-practices-for-data-restoring-operations
description: Service-level agreements and disaster recovery plans should include the details of how long each database should take to be restored, and the measures taken to ensure no corruption has taken place. Following are steps you can take to minimi
---

# T2604: Follow best practices for data restoring operations

**Category:** INFRA  
**SD Elements:** [T2604](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2604/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Why Not Directly Code-Fixable in This Repository

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Service-level agreements and disaster recovery plans should include the details of how long each database should take to be restored, and the measures taken to ensure no corruption has taken place.

Following are steps you can take to minimize the risk of corruption. 

- Test your recovery procedures regularly to ensure that data can be restored without a glitch. Testing will also provide you with a timeline for how long it takes to do a full recovery.

- Provide a restoration checklist to ensure that everything is in place for a data restoration, including the operating system level, database software level, and any ancillary utilities used to monitor the system.

- Use backup verification tools to test the size and integrity of backups. If any of these tests uncover an anomaly, the administrator should be alerted immediately.

- Be cautious about rushing the restoration which may lead to errors. because when a system goes down, there is often extreme pressure to get it back up and running quickly but be cautious about how you perform each step. also , when a system appears to be fully restored, be cautious about its integrity until it is fully checked and tested.

- Keep the data recovery plan simple and clear.

- Share your data restoration plan with relevant personnel in your company so that whoever is in charge in the event of failure will know the procedure and will be able to follow it easily.
 
Note: If you use Oracle, you can check for corrupt data using the RMAN utility, which can also repair the damaged data.

## Success Criteria

- The requirement "Follow best practices for data restoring operations" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
