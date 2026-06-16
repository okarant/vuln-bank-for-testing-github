---
name: t4600-establish-out-of-band-communications-channel
description: Have alternative methods to support communication requirements during communication failures and data integrity attacks. 1. Identify critical communication channels and data flows essential for operations. 2. Determine acceptable downtime a
---

# T4600: Establish Out-of-Band Communications Channel

**Category:** INFRA  
**SD Elements:** [T4600](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4600/)  
**Priority:** 10  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Have alternative methods to support communication requirements during communication failures and data integrity attacks. 

1. Identify critical communication channels and data flows essential for operations.
2. Determine acceptable downtime and data integrity thresholds for different systems.
3. Design redundant communication channels: 

    - Physical redundancy: Deploy backup communication infrastructure, such as secondary networks (e.g., satellite links, cellular data, or alternative wired connections).
    - Protocol redundancy: Use alternative communication protocols (e.g., MQTT, Zigbee, LoRaWAN) in case primary ones are compromised.

4. Implement fallback mechanisms, such as offline data storage or batch processing.

## Success Criteria

- The requirement "Establish Out-of-Band Communications Channel" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
