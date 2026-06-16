---
name: t32-always-perform-input-validation-on-a-server
description: Perform input validation on the server-side *in addition to* the client. Attackers can bypass input validation on the client, which is commonly seen in JavaScript validation. In case of an input validation failure, log the following informa
---

# T32: Always perform input validation on a server

**Category:** CODE_FIX  
**SD Elements:** [T32](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T32/)  
**Priority:** 7  
**Domain:** input-validation

## Affected Areas in This Repository

app.py request handlers (JSON/form/query input used without validation)

## Required Fix

Validate and normalize all server-side input against strict allowlists/schemas before use; never trust client-supplied values for security decisions.

## Implementation Guidance (SD Elements)

Perform input validation on the server-side *in addition to* the client. Attackers can bypass input validation on the client, which is commonly seen in JavaScript validation.

In case of an input validation failure, log the following information:

- Timestamp
- Source IP
- Description of event
- Error codes (if applicable)

Use a __general error message__ for failed checks that do not reveal any information about the system or the process of validation.

### Use client-side validation to detect malicious behavior

Since client-side validation mechanisms are easy to bypass, they cannot be relied upon for security. However, it is recommended to ensure that client-side validation procedures and server-side validation procedures enforce identical rules. In doing so, you can expect that server-side validation should not fail.

Under these conditions, a server-side input validation failure can be used as a signal of data tampering. __Such a failure should be seen as a security-relevant incident__, and should be logged appropriately.

Additionally, the system can decide to enforce further security restrictions. For example, the account can be locked, or the associated privileges revoked.

For more details on detecting suspicious behavior and acting upon such events, see the [OWASP AppSensor project](https://www.owasp.org/index.php/OWASP_AppSensor_Project).

## Success Criteria

- The control "Always perform input validation on a server" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
