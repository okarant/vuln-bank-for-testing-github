---
name: t96-test-if-your-site-is-vulnerable-to-csrf
description: Use either of the following methods to test your site for a CSRF vulnerability: ## Method One 1. Log into the application. 2. Determine which transactions are considered "high-value" according to your business. - For example, transactions w
---

# T96: Test if your site is vulnerable to CSRF

**Category:** CODE_FIX  
**SD Elements:** [T96](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T96/)  
**Priority:** 7  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

Use either of the following methods to test your site for a CSRF vulnerability:

## Method One

1. Log into the application.

2. Determine which transactions are considered "high-value" according to your business.
    - For example, transactions with personal safety, monetary, or brand reputation impact. 

3. Choose one transaction.
    - Repeat the rest of the test for all those transactions, or make sure the entire application uses the same safeguards for CSRF.

4. Determine how the transaction is requested.
    - For example, it may use a request form with input values, which is submitted to a destination page to process the request. This is called a POST method.
    - Alternatively, the transaction may be enabled by a single hyperlink. This is possible through a GET method with a query string containing parameters.   

5. Use an HTTP proxy or HTML inspecting tool to save the content of the HTTP request sent to the target page that processes the transaction. 
    - You can use a tool such as Burp Suite, Chrome Developers Tools, or Firefox FireBug/TamperData.

6. Record the entire request including headers.

7. Delete the browser's history, and log in again as the same user.

8. Go to the same page again, but intercept the request before sending it to the target.
    - Replace the unpredictable parts of this request with some random values with a tool such as TamperData or Burp Suite. 
        - Parts that cannot be predicted include random tokens you see in the request.
    - Do not replace cookies.

This test __fails__ if you can perform the transaction successfully.

## Method Two

1. Find the transaction that you would like to test.

2. Create an HTML page to initiate the request.
    - For GET requests, the transaction could be initiated simply with a hyperlink with parameters.
    - For a POST method, create a form with all the values that the request page sends including the hidden inputs.
        - Replace the unpredictable values with some random values or values that an attacker can guess. 

3. Clear your browsing history and log into the application.

4. Use the page in step 2 to send the request.

This test __fails__ if you can perform the transaction successfully.

## Success Criteria

- The control "Test if your site is vulnerable to CSRF" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
