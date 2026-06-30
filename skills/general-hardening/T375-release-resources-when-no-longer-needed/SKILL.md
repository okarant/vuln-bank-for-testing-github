---
name: t375-release-resources-when-no-longer-needed
description: Release the following resources properly when you no longer need them: * Files * Network Sockets * Database Connections * I/O Devices (such as camera, microphone, speaker, or sensor) * Memory (for unmanaged languages) __Note:__ Newer versio
---

# T375: Release resources when no longer needed

**Category:** CODE_FIX  
**SD Elements:** [T375](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T375/)  
**Priority:** 6  
**Domain:** general-hardening

## Affected Areas in This Repository

database.py (connection pool checkout/return)

## Required Fix

Ensure resources (DB connections, file handles) are released promptly in finally blocks to prevent exhaustion.

## Implementation Guidance (SD Elements)

Release the following resources properly when you no longer need them:

* Files
* Network Sockets
* Database Connections
* I/O Devices (such as camera, microphone, speaker, or sensor)
* Memory (for unmanaged languages)

__Note:__ Newer versions of many programming languages introduce the ***with*** statement for ***try*** blocks, which lets you open and close multiple resources easier and with fewer errors. Use this feature for error handling where applicable.

## Success Criteria

- The control "Release resources when no longer needed" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
