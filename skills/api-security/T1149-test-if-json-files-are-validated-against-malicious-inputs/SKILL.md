---
name: t1149-test-if-json-files-are-validated-against-malicious-inputs
description: Use the following guidelines to test for JSON input validation: 1. Locate a JSON input and identify the requirements for the fields included in it or locate the relative JSON schema if one is used for its validation. JSON schema would look 
---

# T1149: Test if JSON files are validated against malicious inputs

**Category:** CODE_FIX  
**SD Elements:** [T1149](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1149/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines to test for JSON input validation:

1. Locate a JSON input and identify the requirements for the fields included in it or locate the relative JSON schema if one is used for its validation. JSON schema would look like:

        {
        	"type" : "string",
	        "minLength" : 6 ,
        	"maxLength" : 12
        }

2. Create a JSON input that breaks the validation or the requirements in the schema. For example, the following JSON breaks the above schema by providing a short value for the `username` field:


        {
	        "username": "123",	
        }

2. Submit the crafted JSON input to the application.

The application should validate the input. This test __fails__ if the invalid input does not result in an error message or a prompt.

## Success Criteria

- The control "Test if JSON files are validated against malicious inputs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
