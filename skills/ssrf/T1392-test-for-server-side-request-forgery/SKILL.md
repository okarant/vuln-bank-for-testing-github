---
name: t1392-test-for-server-side-request-forgery
description: Use Burp Suite to craft requests containing `URL` payloads to launch an SSRF attack: 1. Try `http://127.0.0.1:80` as a URL (convert http://127.0.0.1:80 to base64 aHR0cDovLzEyNy4wLjAuMTo4MA== and run it on Burp repeater). This forces the vul
---

# T1392: Test for Server Side Request Forgery

**Category:** CODE_FIX  
**SD Elements:** [T1392](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1392/)  
**Priority:** 8  
**Domain:** ssrf

## Affected Areas in This Repository

app.py /upload_profile_picture_url (fetches an attacker-supplied URL), the emulated /latest/meta-data/* IMDS routes

## Required Fix

Validate and allowlist outbound destinations, reject internal/link-local/metadata IP ranges, restrict URL scheme to http(s), and disable following redirects to private hosts.

## Implementation Guidance (SD Elements)

Use Burp Suite to craft requests containing `URL` payloads to launch an SSRF attack:

1. Try `http://127.0.0.1:80` as a URL (convert http://127.0.0.1:80 to base64 aHR0cDovLzEyNy4wLjAuMTo4MA== and run it on Burp repeater). This forces the vulnerable application to make a request on behalf of the attacker via its loopback network interface (localhost). If the response contains some information about the hosting (i.e. server banner), then the attack has been successful. This attack can be repeated using other URL payloads such as `http://169.254.169.254/latest/meta-data/` for fetching cloud meta-data, `http://localhost/server-status` for Apache HTTP Servers' status and so on.

2. Try other URL schemes in the URL, such as Gopher, DICT and SFTP. Set up a virtual private server (VPS) and use its IP when crafting these URLs. When you receive a request (on your VPS), the SSRF attack has been successfully launched. This is because the vulnerable application has made a request to your VPS on your behalf. Alternatively, you can try the `file:///etc/passwd` URI payload and see if `passwd` is relayed back to you by the vulnerable application.

For a comprehensive list of SSRF attacks, see the [SSRF Bible Cheatsheet](https://github.com/jivoi/offsec_pdfs/blob/master/SSRF-Bible-Cheatsheet.pdf).

### Blind Server Side Request Forgery (SSRF)

SSRF attacks do not often trigger a response directly back to the web application but still may be vulnerable to SSRF. Blind SSRF occurs when an application can be forced to trigger a back-end HTTP request, but as a tester or attacker you have no knowledge of the response. To test for blind SSRF, it is a best practice to utilize an out-of-band technique that requires  an external server capable of receiving HTTP requests be set up. This server should be under your control.

1. Configure a public-facing web server with an IP address and domain name. If using Burp, the tool Burp Collaborator may be used to set this up quickly.

2. Identify an injection point in the web application to test for blind SSRF (similar to testing for regular SSRF). Enter your IP address or domain name as the server.

3. View the logs in your server and search for requests coming from the target application. If you see log entries that are aligned with the vulnerable application, it is susceptible to blind SSRF and further scans can begin to enumerate the internal network or load a malicious file from your server.

## Success Criteria

- The control "Test for Server Side Request Forgery" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
