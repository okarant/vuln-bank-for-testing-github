### Task T374: Offload HTTP request handling to dedicated modules (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T374](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T374/)

**Guidance:** Follow these guidelines to protect your HTTP server against external attacks: 1. Offload parts of the request handling processes onto the operating system if supported. - Some operating systems provide the web server with specific optimization capabilities for a listening socket. - For example, not sending HTTP requests to the server until the entire request is received. 2. Configure available server-specific modules to protect the HTTP server against resource exhaustion attacks. - For example, 

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
