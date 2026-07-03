### Task T573: Prevent UDDI/ebXML spoofing (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T573](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T573/)

**Guidance:** Use the following guidelines for preventing UDDI and ebXML spoofing: __For applications that rely on registry/discovery services:__ - Only trust messages from *Universal Description, Discovery and Integration (UDDI)*, *Electronic Business XML(ebXML)*, or similar discovery/registry services that are signed and verified by a trusted party. - This prevents spoofing attacks in which attackers can craft malicious UDDI entries to reference harmful web services. __For registry/discovery services:__ - P

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
