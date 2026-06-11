# Check container health (Docker)

**CM ID:** T31905-T1180
**Classification:** INFRA
**Domain:** docker
**Priority:** 6

## Objective

Harden infrastructure configuration: Check container health (Docker).

## Affected Files

- `Dockerfile` (lines: all): Container security configuration
- `docker-compose.yml` (lines: all): Container orchestration security

## Implementation Steps

1. Review Dockerfile for security best practices
2. Use specific version tags instead of 'latest'
3. Run as non-root user (add USER directive)
4. Minimize image layers and remove unnecessary packages
5. Add health checks and resource limits
6. Scan image for vulnerabilities with trivy/grype

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T1180)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T1180
- Classification: INFRA