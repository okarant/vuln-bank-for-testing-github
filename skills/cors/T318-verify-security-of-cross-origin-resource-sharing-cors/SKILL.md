---
name: t318-verify-security-of-cross-origin-resource-sharing-cors
description: To test a CORS policy, you will need to send cross-origin requests to the application's backend. The easiest way to achieve this is by using the [Postman tool](https://www.getpostman.com/), or a command line tool such as [HTTPie](https://ht
---

# T318: Verify security of cross origin resource sharing (CORS)

**Category:** CODE_FIX  
**SD Elements:** [T318](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T318/)  
**Priority:** 8  
**Domain:** cors

## Affected Areas in This Repository

app.py L35 `CORS(app)` enables permissive cross-origin access globally

## Required Fix

Scope CORS to an explicit allowlist of trusted origins, methods and headers; never combine a wildcard origin with credentials.

## Implementation Guidance (SD Elements)

To test a CORS policy, you will need to send cross-origin requests to the application's backend. The easiest way to achieve this is by using the [Postman tool](https://www.getpostman.com/), or a command line tool such as [HTTPie](https://httpie.org/). The instructions below assume you are using these tools or similar ones.

Follow these instructions to verify CORS security:

- Verify that the application performs authentication/authorization if the service is not public.
    - Send a CORS request to an application endpoint using an HTTP request tool
	    - Send a custom `Origin` header containing a trusted value, that is also returned in `Access-Control-Allow-Origin` header.
    	- Do not include any authorization state (credentials, cookies, custom headers, ...)
   
    This test __fails__ if you can access protected services without authentication.

- Test that the authentication covers all HTTP verbs.
    - Send requests with different HTTP verbs (such as GET, POST, PUT, DELETE, PATCH, OPTIONS)
	    - Send one set of requests without `Origin` header. These requests mimic same-origin behavior.
	    - Send another set of requests with an `Origin` header with a trusted value. These requests mimic cross-origin behavior. 
	    - Do not include any authorization state (credentials, cookies, custom headers, ...)

    This test __fails__ if you can access a service or page that needs authentication in any of the above cases.

- Test that the origins are properly verified.
   - Send requests with an `Origin` header that contains a non-trusted origin (e.g., `https://evil.com`).
		- Include authorization state on these requests (e.g., a cookie, a custom header, ...) 
   - Make sure you run these tests for various non-trusted domains
   - Look for tricky combinations. For example, to test an application accepting cross-origin requests from `https://www.example.com`, you could use the following values for the `Origin` header:
   		- `https://www-example.com` (bypasses regexes using the `.` as a wildcard)
   		- `https://notexample.com` (bypasses partial matching)
   		- `https://example.com.evil.com` (bypasses partial matching)
   		- `http://example.com` (bypasses partial matching)

    This test __fails__ if you get any response other than the `Invalid CORS request` response.

- Test that the origins are properly verified.

- Work with developers, or analyze the responses, to make sure that you do not return 'Access-Control-Allow-Origin: *' for non-public services.
    - While this is tested in the previous step, due to its prevalence, it is worth being verified again.

- Test that anti-CSRF measures protect CORS requests too.
    - For every endpoint that does not require a CORS preflight, CSRF protection needs to be validated.
	    - Send a trusted cross-origin request with authorization state, but without CSRF tokens

    This test __fails__ if you can access the target service/page without a CSRF error.

	__*Note:*__ Endpoints requiring a preflight (e.g., accepting the `application/json` content type) are protected against CSRF by means of the CORS policy (i.e., malicious origins will not be accepted by the policy)

- Work with developers to make sure that if you use part of the input for calculating the request target, you are validating the input.
    - For more information, see [Input validation issue, XSS with CORS](https://www.owasp.org/index.php/Test_Cross_Origin_Resource_Sharing_(OTG-CLIENT-007)).

## Success Criteria

- The control "Verify security of cross origin resource sharing (CORS)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
