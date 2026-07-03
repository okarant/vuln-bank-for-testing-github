### Task T349: Protect audit information and logs against unauthorized access (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T349](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T349/)

**Guidance:** Protect audit information against unauthorized deletion or modification. This countermeasure is as crucial as logging important events itself. Follow these guidelines to protect audit records: - Identify, classify and collect required audit information: - Audit information includes not only audit data, but audit settings and audit reports. - Design and develop extra safeguards: - Give audit data a higher level of attention/security, prevent any modification to such data, or at a minimum, record 

**Why Not Code-Fixable:**
- Searched: application source (app.py) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
