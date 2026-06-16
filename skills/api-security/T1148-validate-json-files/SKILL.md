---
name: t1148-validate-json-files
description: It's important to never build JSON dynamically from user input without sufficient validation because this increases the chances of XSS. Validate JSON files for example by using a JSON schema. A JSON schema is written in JSON and its structu
---

# T1148: Validate JSON files

**Category:** CODE_FIX  
**SD Elements:** [T1148](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1148/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

It's important to never build JSON dynamically from user input without sufficient validation because this increases the chances of XSS.

Validate JSON files for example by using a JSON schema. A JSON schema is written in JSON and its structural validation makes it ideal for automated testing and input validation. Below is an example of JSON schema:

````
{
	"type" : "string",
	"minLength" : 6 ,
	"maxLength" : 12
}
````

This schema checks if an input is a string and its length is between 6 to 12 characters. There are many JSON validators written in different languages, like C, C++, Java, JavaScript, and Python. For more information, refer to [JSON Schema](http://json-schema.org/).

## Success Criteria

- The control "Validate JSON files" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
