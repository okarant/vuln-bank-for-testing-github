### Task T4746: Ensure container images are secure (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T4746](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4746/)

**Guidance:** Securing container images is crucial as they form the foundation of your containers, containing the code, runtime, system libraries, and settings necessary for your application to function. Ensuring these images are secure helps prevent vulnerabilities from being introduced into your containerized applications. 1. Use images from trusted repositories or create your own to avoid vulnerabilities from untrusted sources. This ensures that the images you use have been vetted for security issues. 2. R

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
