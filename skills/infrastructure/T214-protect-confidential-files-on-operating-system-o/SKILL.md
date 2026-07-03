### Task T214: Protect confidential files on operating system or server (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T214](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T214/)

**Guidance:** Use the following guidelines for protecting confidential files on operating systems and servers: - Use operating system (or server) controls to enforce minimum access rights on any confidential files used by the application. - Restricting access reduces the risk of a rogue application or malicious user accessing the data. - For example, by using a file containing Personally Identifiable Information (PII) or directory listings. - For confidential files passed to the program as input, enforce this

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
