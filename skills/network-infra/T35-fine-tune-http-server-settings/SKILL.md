---
name: t35-fine-tune-http-server-settings
description: Set limits on incoming HTTP messages, and notify designated administrator roles of a violation. # HTTP request headers and bodies Limit the __number__ and __length__ of HTTP request __headers__ and __bodies__ accepted from the clients to a 
---

# T35: Fine-tune HTTP server settings

**Category:** INFRA  
**SD Elements:** [T35](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T35/)  
**Priority:** 9  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Set limits on incoming HTTP messages, and notify designated administrator roles of a violation.

# HTTP request headers and bodies

Limit the __number__ and __length__ of HTTP request __headers__ and __bodies__ accepted from the clients to a minimum. Set tighter endpoint-specific restrictions depending on their function to minimize the attack surface.

Limit the following request attributes:

- Request body size
- Number of request header fields
- Request header fields size
- Request line size
- XML request body size

# Server timeout

Tune the connection __timeout__ settings of the server. A higher connection timeout gives the server more time to engage with the application. This increases the likelihood for various types of server attacks, such as [Slowloris](http://en.wikipedia.org/wiki/Slowloris_%28software%29).

__Note:__ A small value may introduce issues with the legitimate users with slow connections. Set timeout values based on your normal connection statistics.

Tune the following timeout settings:

- Request read timeout
- Keep-alive timeout

# Server connections and backlog capacity

Tune the maximum number of __simultaneous connections__, and increase the capacity of the backlog of pending connections where possible.

__Note:__ The backlog prolongs a denial of service (DoS) attack because it holds incomplete requests (including malicious ones), but reduces the impact of small attacks.

Most web and application servers provide a configuration option for each of these limits. See the server-specific documentation, and review your application needs when adjusting each of these settings.

## Considerations

The meaning of "reasonable" varies according to a system's available resources and an application's features and needs. Consider the following:

- A maximum URL size of 2000 characters is considered reasonable and supported by most browsers. 
    - Smaller values (256) might interfere with features such as single sign-on.

- While a 1 MB limit on HTTP request sizes is reasonable for most applications, it might restrict file upload speeds where applicable.

- Maximum number of concurrent connections:
    - Carefully review the operational environment, hardware, and software resources, such as system memory available to the HTTP server.
    - There is no common value that works for all environments.

- Decreasing the keep-alive time-out might have a small performance impact. 
    - A value above 60 seconds is not recommended according to [Apache Performance Tuning](http://httpd.apache.org/docs/2.2/misc/perf-tuning.html).

For more information about web server security, see [Apache Security Tips](http://httpd.apache.org/docs/trunk/misc/security_tips.html).

## Success Criteria

- The requirement "Fine-tune HTTP server settings" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
