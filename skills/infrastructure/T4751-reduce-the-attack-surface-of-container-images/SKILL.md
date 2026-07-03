### Task T4751: Reduce the attack surface of container images (DOCUMENTATION ONLY)

**Category:** INFRA
**SD Elements:** [T4751](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4751/)

**Guidance:** Reducing the attack surface is crucial for minimizing the potential entry points for attackers into your container environment. By limiting the components and functionalities within your container images, you can significantly decrease the risk of unauthorized access and improve overall security. This approach not only enhances security but also optimizes performance by eliminating unnecessary elements. 1. **Remove Unnecessary Software, Libraries, and Services**: Begin by auditing your container

**Why Not Code-Fixable:**
- Searched: application source (Dockerfile) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
