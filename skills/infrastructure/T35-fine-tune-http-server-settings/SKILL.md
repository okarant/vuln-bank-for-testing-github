### Task T35: Fine-tune HTTP server settings (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T35](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T35/)

**Guidance:** Set limits on incoming HTTP messages, and notify designated administrator roles of a violation. # HTTP request headers and bodies Limit the __number__ and __length__ of HTTP request __headers__ and __bodies__ accepted from the clients to a minimum. Set tighter endpoint-specific restrictions depending on their function to minimize the attack surface. Limit the following request attributes: - Request body size - Number of request header fields - Request header fields size - Request line size - XML

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
