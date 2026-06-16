---
name: t1364-verify-that-third-party-software-libraries-modules-and-ope
description: Follow the guidelines below to check whether security risks for using third-party and commercial off the shelf (COTS) components are mitigated: - Verify that there is a process for choosing a reliable vendor. If not, then this test __fails_
---

# T1364: Verify that third party software libraries/modules and open source/COTS components are used securely

**Category:** CODE_FIX  
**SD Elements:** [T1364](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1364/)  
**Priority:** 6  
**Domain:** dependency-management

## Affected Areas in This Repository

requirements.txt (flask==2.0.1, werkzeug==2.0.1, pyjwt==2.4.0, etc.)

## Required Fix

Pin and patch dependencies to current secure versions, enable automated dependency/vulnerability scanning, and review transitive dependencies.

## Implementation Guidance (SD Elements)

Follow the guidelines below to check whether security risks for using third-party and commercial off the shelf (COTS) components are mitigated:

- Verify that there is a process for choosing a reliable vendor. If not, then this test __fails__.

- Verify that all the software and hardware components are checked against known vulnerabilities, they are acquired from reliable sources, and their digital signatures are checked. If not, then this test __fails__.

- Verify there is a process for conducting risk assessments and threat modeling for third-party solutions. If not, then this test __fails__.

- Verify that there is a least privilege mechanism for restricting third-party component access to resources of your company. If not, then this test __fails__.

- Verify that third-party component communication and performance are being monitored and audited. If not, then this test __fails__.

- Verify that third-party components are configured securely such as by ensuring that all pre-configured defaults are not being used, and all unnecessary accounts and features are disabled. If not, then this test __fails__.

- Verify that there is a list of all components with all necessary information that is kept up to date. If not, then this test __fails__.

- Verify that open source component licensing is properly checked. If not, then this test __fails__.

- Verify that well-maintained code from a master branch is being used. If not, then this test __fails__.

- Verify that open source components are scanned for potential vulnerabilities before using them. If not, then this test __fails__.

- Verify third-party services are authenticated and communicating through a secure channel. If not, then this test __fails__.

### Verify if vulnerable javascript dependencies are detected

Check whether a scanning tool such as **Retire.js** or **NSP** is installed and can detect javascript vulnerable libraries:

- Prepare a testing environment and use an unpatched javascript library on your application. 

- Check whether the unpatched library can be detected by running the installed scanner.

If the unpatched javascript library was not detected using the scanner, this test __fails__.

## Success Criteria

- The control "Verify that third party software libraries/modules and open source/COTS components are used securely" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
