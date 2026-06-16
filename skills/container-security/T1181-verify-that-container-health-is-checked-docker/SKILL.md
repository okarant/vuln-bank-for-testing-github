---
name: verify-container-health-docker
description: Ensure Docker images define effective HEALTHCHECK instructions and containers expose reliable health status; Use when containers lack health definitions or do not report usable health states.
---

# Verify that container health is checked (Docker)

## What This Skill Does
Ensures Docker images define a `HEALTHCHECK` and that containers expose a fast, deterministic health endpoint so platforms can track `healthy` vs `unhealthy` state. This prevents failing or compromised containers from silently serving traffic by wiring a lightweight in-app `/health` route to the Docker `HEALTHCHECK` and validating that `.State.Health.Status` reflects real service health.

## Decision Table
| Situation | Action |
|-----------|--------|
| Dockerfile has no `HEALTHCHECK` instruction | Add a `HEALTHCHECK` that probes an internal, lightweight `/health` (or similar) endpoint on `localhost` |
| App exposes a simple HTTP endpoint but no dedicated health route | Add a minimal `/health` (or equivalent) route that performs cheap, deterministic checks and returns 200 only when healthy |
| Health endpoint performs heavy or non-deterministic work (DB migrations, long queries, external APIs) | Simplify health logic to fast, bounded checks (e.g., main loop running, essential dependency reachable with quick timeout) |
| Container has `HEALTHCHECK` but uses a shell command that always exits 0 regardless of app state | Replace the `HEALTHCHECK` command with logic that fails (`exit 1`) when the health probe HTTP status is not 200 or on exceptions |
| `docker inspect` shows a healthcheck and `.State.Health.Status` changes with real failures | No action needed; keep health endpoint and `HEALTHCHECK` as-is, only refine if performance or flapping issues exist |

## Boundaries

### Can Do
- Detect missing or trivial `HEALTHCHECK` instructions in Dockerfiles and add a proper one.
- Add or refine lightweight in-app health endpoints (e.g., `/health`) for common web stacks.
- Adjust `HEALTHCHECK` parameters (`--interval`, `--timeout`, `--retries`, `--start-period`) to reasonable defaults for typical services.

### Cannot Do
- Infer app internals or critical dependencies beyond what is visible in the code (must not invent complex health logic).
- Reconfigure orchestrator-level health and readiness probes outside the Dockerfile or app code shown.
- Guarantee performance characteristics under real production load; tuning intervals/timeouts for specific SLAs is out of scope.

## Gotchas
- Using readiness logic in the main request path: placing expensive dependency checks in every `/` request instead of a dedicated `/health` route increases latency and risk of outages.
- Health endpoint returning 200 even when degraded: always-success handlers (e.g., returning 200 while logging errors) stop the container from ever going `unhealthy`, defeating the purpose.
- Overly aggressive `HEALTHCHECK` settings: very low `--interval` or long-running checks can create unnecessary load and cause flapping health status; keep probes fast and moderately frequent.

## Quick Verification
```bash
# 1) Verify image defines a HEALTHCHECK (non-<nil>)
docker inspect --format='{{ .Config.Healthcheck }}' <IMAGE>

# 2) Run a container and check health state
CID=$(docker run -d <IMAGE>)
sleep 20  # allow start-period + a couple of checks
docker inspect --format '{{ .Id }}: Health={{ .State.Health.Status }}' "$CID"

# 3) Probe the in-app health endpoint directly
curl -i http://localhost:8080/health || true

# 4) After inducing a failure inside the container, confirm state moves away from healthy
docker inspect --format '{{ .Id }}: Health={{ .State.Health.Status }}' "$CID"
```