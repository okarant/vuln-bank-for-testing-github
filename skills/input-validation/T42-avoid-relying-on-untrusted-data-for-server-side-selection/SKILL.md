---
name: t42-avoid-relying-on-untrusted-data-for-server-side-selection
description: Do not use untrusted data such as user-supplied settings for the selection of a page, view, or template on the server side. These settings may allow the user to run code on the server side, or access server-side files. Validate all input us
---

# T42: Avoid relying on untrusted data for server-side selection

**Category:** CODE_FIX  
**SD Elements:** [T42](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T42/)  
**Priority:** 10  
**Domain:** input-validation

## Affected Areas in This Repository

app.py request handlers (JSON/form/query input used without validation)

## Required Fix

Validate and normalize all server-side input against strict allowlists/schemas before use; never trust client-supplied values for security decisions.

## Implementation Guidance (SD Elements)

Do not use untrusted data such as user-supplied settings for the selection of a page, view, or template on the server side.

These settings may allow the user to run code on the server side, or access server-side files. Validate all input using a strict whitelist that only allows certain input, such as alphanumeric characters.

__Note:__ In addition to validating the format of input, check that the input value is within a valid range, or set of values. Very large input that happens to be valid may cause resource exhaustion denial of service (DoS). This is especially true if user input is used as a loop counter, or to allocate resources.

## Success Criteria

- The control "Avoid relying on untrusted data for server-side selection" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
