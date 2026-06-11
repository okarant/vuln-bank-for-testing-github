# Do not store secrets in Dockerfiles (Docker)

**CM ID:** T31905-T1186
**Classification:** INFRA
**Domain:** docker
**Priority:** 10

## Objective

Harden infrastructure configuration: Do not store secrets in Dockerfiles (Docker).

## Affected Files

- `Dockerfile` (lines: all): Container security configuration
- `docker-compose.yml` (lines: all): Container orchestration security

## Implementation Steps

1. Audit Dockerfile and docker-compose.yml for hardcoded secrets
2. Move all secrets to environment variables or Docker secrets
3. Use .env files (excluded from git) for local development
4. Add secret scanning to CI pipeline
5. Verify no secrets remain in image layers using `docker history`

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T1186)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T1186
- Classification: INFRA