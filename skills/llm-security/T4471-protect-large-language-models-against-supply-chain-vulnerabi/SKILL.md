---
name: t4471-protect-large-language-models-against-supply-chain-vulnera
description: To protect Large Language Models (LLMs) against supply chain vulnerabilities, ensure the following: - Verify third-party components, base images, and service suppliers, ensuring they are updated and free from vulnerabilities. Also, avoid us
---

# T4471: Protect Large Language Models against supply chain vulnerabilities (MLOps Engineer)

**Category:** ML_CODE  
**SD Elements:** [T4471](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4471/)  
**Priority:** 8  
**Domain:** llm-security

## Affected Areas in This Repository

ai_agent_deepseek.py (system_prompt explicitly instructs the model to obey injected instructions and expose the database; _get_database_context runs DB queries from user text; no output filtering), app.py /api/ai/chat and /api/ai/chat/anonymous

## Required Fix

For code-applicable LLM risks: rewrite the system prompt to refuse injected/override instructions, sanitize and bound user input, filter/escape model output before returning or rendering it, run the agent with a least-privilege read-only DB role, and rate-limit. For risks tied to model training/fine-tuning/vector-stores/model-theft: the app calls an external DeepSeek API and does not train, host, fine-tune or vector-index models, so these are documented as not code-fixable in this repository.

## Implementation Guidance (SD Elements)

To protect Large Language Models (LLMs) against supply chain vulnerabilities, ensure the following:

- Verify third-party components, base images, and service suppliers, ensuring they are updated and free from vulnerabilities. Also, avoid using deprecated components.

- Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to detect and alert for new, zero-day vulnerabilities.

More details on Software Bill of Materials (SBOM) can be found in [this article from NIST](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-software-1).

### Implement automated integrity checks and provenance tracking (RAG)

- Automate pipeline stages to verify the integrity of third-party components and datasets.  

- Implement provenance tracking for model inputs and parameters to ensure data integrity and transparency in the RAG framework.

## Success Criteria

- The control "Protect Large Language Models against supply chain vulnerabilities (MLOps Engineer)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
