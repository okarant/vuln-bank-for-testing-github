---
name: t2258-minimize-host-os-attack-surface
description: Follow the steps below to reduce the host OS attack surface: - Use a container-specific OS as opposed to a general purpose operating system wherever possible. - Harden hosts and keep them up-to-date. - Do not run other apps, like a web serv
---

# T2258: Minimize host OS attack surface

**Category:** INFRA  
**SD Elements:** [T2258](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2258/)  
**Priority:** 7  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Follow the steps below to reduce the host OS attack surface:

- Use a container-specific OS as opposed to a general purpose operating system wherever possible.
- Harden hosts and keep them up-to-date.
- Do not run other apps, like a web server or database, on hosts that run containers.
- Do not run unnecessary system services on hosts that run containers.
- Maintain a schedule to continuously scan hosts and the appropriate lower-level components for vulnerabilities and updates, such as with the kernel. 

For organizations that cannot use a container-specific OS, see NIST's [Guide to General Server Security](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-123.pdf).

## Success Criteria

- The requirement "Minimize host OS attack surface" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
