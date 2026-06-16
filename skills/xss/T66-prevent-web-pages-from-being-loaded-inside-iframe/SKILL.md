---
name: t66-prevent-web-pages-from-being-loaded-inside-iframe
description: Do not allow your application to be loaded in an `iframe` unless you need that functionality. Different strategies can be applied to deny framing. 1. Instruct the browser to prevent framing using HTTP response headers (`X-Frame-Options` and
---

# T66: Prevent web pages from being loaded inside iFrame

**Category:** CODE_FIX  
**SD Elements:** [T66](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T66/)  
**Priority:** 7  
**Domain:** xss

## Affected Areas in This Repository

templates/*.html (Jinja2), static/dashboard.js and static/merchant.js (client-side DOM rendering)

## Required Fix

Keep Jinja2 autoescaping enabled and contextually escape all untrusted output; avoid `innerHTML`/unsafe DOM sinks in JS; send a Content-Security-Policy and `X-Frame-Options: DENY` (or CSP frame-ancestors) to block injection and clickjacking.

## Implementation Guidance (SD Elements)

Do not allow your application to be loaded in an `iframe` unless you need that functionality. Different strategies can be applied to deny framing. 

1. Instruct the browser to prevent framing using HTTP response headers (`X-Frame-Options` and `Content Security Policy`). __This is a current best practice__.
2. Use JavaScript code that detects unwanted framing and prevents abuse. This technique is also known as *frame busting*. It is considered deprecated. More information is available in the JavaScript How-to.

Below you will find different scenarios explaining how to configure the HTTP response headers. 



## Deny framing

Most modern applications do not depend on the framing of their pages. If none of the pages need to be framed, framing can be turned off completely. To do so, the server should send the following two headers on every response with an HTML page that does not need to be framed.

```
X-Frame-Options: DENY
Content-Security-Policy: frame-ancestors 'none'
```

This configuration is supported by all major browsers.



## Allow framing within your origin

When framing is needed, it is often restricted to the application itself. When the page including a framed page is from the same origin, the server should send the following two headers on every response containing an HTML page that should be framed by your origin.

```
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: frame-ancestors 'self'
```

This configuration is supported by all major browsers.


## Allow third-party framing from one origin

When a single origin needs to be able to frame an application page, it needs to be explicitly listed. The server should send the following two headers on every response containing an HTML page that should be framed by the third-party origin.

```
X-Frame-Options: ALLOW-FROM https://example.com
Content-Security-Policy: frame-ancestors https://example.com
```

This configuration allows `https://example.com` to frame the page in the response. 

This configuration is supported by all major browsers.


## Allow third-party framing from multiple origins

When multiple origins need to be able to frame an application page, they all need to be explicitly listed. Unfortunately, the `X-Frame-Options` header only allows a single value to be listed. The more recent `Content-Security-Policy` supports multiple values, __but is not supported by Internet Explorer__. 

The server should send the following header on every response containing an HTML page that should be framed by one of the third-party origins.

```
Content-Security-Policy: frame-ancestors https://one.example.com https://two.example.com
```

This configuration allows `https://one.example.com` and `https://two.example.com` to frame the page in the response. 

This configuration is supported by all major browsers, __except IE__. It is supported in Edge.


### Preventing framing in Internet Explorer ###

If your application needs to support Internet Explorer and needs whitelisting from third-party origins, things get challenging. There are a few options you can follow.

1. Implement a dynamic `X-Frame-Options` header using the `Referer` header to determine who is trying to frame you. This solution requires matching the `Referer` header against a list of approved origins, and sending back the right value in the header.
2. Accept the risk of potential clickjacking attacks against users of Internet Explorer. To mitigate the risk, you can implement short session lifetimes, as well as re-authentication before performing sensitive operations.

Note that JavaScript-based framebusting will not work, since JavaScript cannot read the URL of the parent frame across origins. 


## Add a restrictive Permissions-Policy policy by default, allowing only required browser features and approved origins.

For example, you can disable features such as camera, microphone, geolocation, payment, USB, and fullscreen unless there is a clear business need for them. Where a feature must remain available, scope it as narrowly as possible to `self` or to a specific allowlisted origin instead of permitting broad access.

Keep the policy aligned with the real behavior of your application. As browser features evolve, review and update the header regularly so that newly introduced capabilities are not left unintentionally exposed.


## A Note on Cross-Domain Meta Policy

The content of your website can also be loaded in PDF and Adobe Flash documents. If you want to allow specific domains to embed your content in these documents, specify them correctly in `crossdomain.xml` files on your server. 

Otherwise, disable this feature:

1. Remove all `crossdomain.xml` files from your server.
2. Configure your server to send a ***X-Permitted-Cross-Domain-Policies*** response header with the value ***none*** with each response.

For more information read [this guide on cross domain policy files](https://code.tutsplus.com/tutorials/quick-tip-a-guide-to-cross-domain-policy-files--active-3832).

## Success Criteria

- The control "Prevent web pages from being loaded inside iFrame" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
