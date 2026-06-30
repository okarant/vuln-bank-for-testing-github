---
name: t105-verify-that-your-application-does-not-have-unnecessary-debu
description: Use the following guidelines for verifying that your application does not have leftover debugging and testing code: _The details of this test may vary based on the type of your application._ 1. Install the application (made for release) and
---

# T105: Verify that your application does not have unnecessary debug capability or leftover test/debug code

**Category:** CODE_FIX  
**SD Elements:** [T105](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T105/)  
**Priority:** 7  
**Domain:** logging-monitoring

## Affected Areas in This Repository

app.py (debug_info with IP/User-Agent returned in responses, `print` statements, Flask debug=True)

## Required Fix

Use structured logging, never return debug/stack data to clients, redact sensitive fields, protect log access, and disable debug mode in production.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying that your application does not have leftover debugging and testing code:

_The details of this test may vary based on the type of your application._

1. Install the application (made for release) and test that debug tools do not return any debug information from the application.

2. Check the application's directories and verify that there is no leftover test or debug code.
    - Look for test data, script, or code in directories and configuration files that will be included in the deployment package.

3. Work with developers to verify the 'annotations' (if applicable) and meta-data in the source code.
    - Verify that the annotations/meta-data do not disclose any unintended information.

### Verify that the debug code is removed from web application before release

For __web applications__, use the following additional guidelines:

- For specific technologies used in the web application, verify if debug capabilities are disabled.
- Browse the web application and make note of any obvious test or debugging data.
    - This includes HTTP parameters with `debug=true`, or pages containing test data.
    
    This test __fails__ if you find this data.

- Create events that trigger server errors.
    - Inspect the errors. 
    - See if any debug information is returned in the response, such as in an error message.
    - See if any SQL statements are passed to the user.
- Look at HTTP headers that are returned.
    - Use Chrome Developer Tools, Firefox Firebug, or proxy software applications such as Burp Suite.
    - Check if any debug information is returned.
        - For example, when you have a number of web servers behind a load balancer, you may want to add an HTTP header to the response with a server identifier to identify which server has processed a specific request.
        - An attacker can use these debug headers to gather information about the web servers and the load balancer itself. 

    This test __fails__ if you can find any debug data and/or components.

__Note:__ This test can only be performed reliably in production, or in an exact replication of production.

## Success Criteria

- The control "Verify that your application does not have unnecessary debug capability or leftover test/debug code" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
