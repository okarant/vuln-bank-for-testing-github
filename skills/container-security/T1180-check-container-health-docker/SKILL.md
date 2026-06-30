---
name: check-container-health-docker
description: Use when Docker images or docker run paths lack a real container health check and need an explicit HEALTHCHECK or --health-cmd.
---

# Check container health (Docker)

## What This Skill Does
This skill fixes Docker containers that have no meaningful health signal, where Docker treats a merely running process as healthy even if the application is hung, returning errors, or not serving requests. It adds a real container health check with either a `HEALTHCHECK` instruction in the image or a runtime `--health-cmd`, using a lightweight local probe and explicit timing values so Docker can mark the container `unhealthy` when the service is not actually working.

## Decision Table
| Situation | Action |
|-----------|--------|
| Dockerfile has no `HEALTHCHECK` and the container runs a long-lived service | Add a `HEALTHCHECK` that probes a real local endpoint or command and set explicit `--interval`, `--timeout`, `--retries`, and `--start-period` |
| Image cannot be changed but container startup uses `docker run` | Add `--health-cmd` plus explicit `--health-interval`, `--health-timeout`, `--health-retries`, and `--health-start-period` |
| Health check only verifies the process exists | Replace it with a probe that confirms the app’s core function, such as a local HTTP endpoint returning a healthy response |
| Health check depends on slow, flaky, or external network calls | Replace it with a lightweight deterministic local probe |
| Dockerfile or runtime config already defines a meaningful health check with explicit timing | No action needed |

## Boundaries

### Can Do
- Add a Docker `HEALTHCHECK` instruction for service containers
- Add or improve `docker run` health check flags when image changes are not possible
- Choose a simple local probe that fails on error, timeout, or non-healthy responses

### Cannot Do
- Guarantee the selected endpoint fully represents all business-critical dependencies
- Invent application-specific health semantics that are not visible from the code or config
- Fix orchestrator restart policies or deployment behavior outside Docker health check settings

## Gotchas
- Checking only that the process is running: this misses hung apps and erroring services because PID existence is not real health
- Probing an external dependency or remote URL: this makes health status flaky and can mark a healthy container unhealthy for network reasons unrelated to the container itself
- Omitting timing values: Docker defaults may not match startup or response behavior, causing false failures or slow detection

## Quick Verification
```bash
# Build and run the image
docker build -t app-healthcheck .
docker run -d --name app -p 8080:80 app-healthcheck

# Inspect health status
docker inspect --format '{{json .State.Health}}' app

# Watch status changes
docker ps

# Force the local health endpoint to fail or stop responding, then confirm Docker marks it unhealthy
docker inspect --format '{{.State.Health.Status}}' app
```