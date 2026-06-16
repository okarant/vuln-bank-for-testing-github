---
name: t4601-prioritize-static-network-configuration
description: - Configure hosts and devices to use static IP addresses and network settings, where feasible. Although configuring hosts and devices to use static IP addresses and network settings is a security best practice that enhances network stabilit
---

# T4601: Prioritize static network configuration

**Category:** INFRA  
**SD Elements:** [T4601](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4601/)  
**Priority:** 8  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

- Configure hosts and devices to use static IP addresses and network settings, where feasible.

Although configuring hosts and devices to use static IP addresses and network settings is a security best practice that enhances network stability, prevents unauthorized DHCP attacks, improves network visibility and control, mitigates IP address spoofing risks, and reduces the risk of service disruptions, it is essential to evaluate its feasibility based on network architecture, device limitations, and operational requirements.

Considerations and Limitations
- Scalability: Managing static IPs in large networks can be complex and may require centralized IP management solutions.
- Operational Constraints: Some environments, such as cloud-based infrastructures or highly dynamic networks, may require DHCP for flexibility and automation.
- Hybrid Approach: In cases where static IPs are impractical, organizations should implement additional DHCP security measures (e.g., DHCP snooping, IP-MAC binding) to mitigate risks.

## Success Criteria

- The requirement "Prioritize static network configuration" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
