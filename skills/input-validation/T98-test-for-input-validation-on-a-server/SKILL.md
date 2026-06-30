---
name: t98-test-for-input-validation-on-a-server
description: Use the following guidelines to test input validation on your server: 1. Find HTTP parameters and cookies that appear to be validated correctly. 2. For each input, enter a valid value. 3. Using an HTTP-proxy tool, convert the value to inval
---

# T98: Test for input validation on a server

**Category:** CODE_FIX  
**SD Elements:** [T98](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T98/)  
**Priority:** 7  
**Domain:** input-validation

## Affected Areas in This Repository

app.py request handlers (JSON/form/query input used without validation)

## Required Fix

Validate and normalize all server-side input against strict allowlists/schemas before use; never trust client-supplied values for security decisions.

## Implementation Guidance (SD Elements)

Use the following guidelines to test input validation on your server:

1. Find HTTP parameters and cookies that appear to be validated correctly. 

2. For each input, enter a valid value. 

3. Using an HTTP-proxy tool, convert the value to invalid. 

This test __fails__ if the input is no longer validated.

## Success Criteria

- The control "Test for input validation on a server" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
