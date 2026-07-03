### Task T3908: Enforce artifact signing (GitHub) (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T3908](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T3908/)

**Guidance:** Ensure all artifacts in releases are securely signed. Additionally, ensure the generation and signing of a Software Bill of Materials (SBOM) during the build process.

**Why Not Code-Fixable:**
- Searched: application source (requirements.txt) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
