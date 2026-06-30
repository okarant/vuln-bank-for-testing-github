---
name: set-ulimit-appropriately-docker
description: Secure Dockerfiles and container entrypoints by validating and constraining ulimit settings; use when code or comments encourage unsafe ulimit values or fail to check effective limits.
---

# Set ulimit appropriately (Docker)

## What This Skill Does
This skill fixes improper `ulimit` handling in Docker images and container startup code. It removes patterns that encourage excessively high or unlimited resource limits and adds in-container checks that read effective limits (like `nofile` and `nproc`), compare them against configurable safe ranges, and fail fast when limits are too low. It never increases limits beyond the OS/container hard limits and treats any runtime overrides as exceptional, explicit configuration.

## Decision Table
| Situation | Action |
|-----------|--------|
| Dockerfile or comments recommend `--ulimit nofile=655350:655350`, `--ulimit nproc=unlimited`, or similar huge/unlimited values | Remove these recommendations and replace with guidance to use sane, policy-driven defaults (daemon `default-ulimits`) and documented ranges |
| Entrypoint/startup does not read or validate `ulimit` values before running workloads | Add a startup check (e.g., Python `resource.getrlimit`) that logs current limits, compares against required minimums/ideal ranges, and exits non‑zero if below required minimums |
| Code silently increases `nofile`/`nproc` limits to high values inside the container to “make things work” | Remove auto‑increases; at most allow optional tightening (lowering) of overly generous soft limits when explicitly configured, never raising beyond current or hard limits |
| Application sometimes needs stricter limits than daemon defaults for safety | Implement an opt‑in path (e.g., `ULIMIT_TIGHTEN=1`) that only lowers soft limits into documented “ideal” ranges while respecting hard limits and handling failures |
| Effective runtime limits already fall within documented ideal ranges and are checked at startup | No action needed; ensure checks remain, logging is clear, and there are no conflicting recommendations to override limits unsafely |

## Boundaries

### Can Do
- Detect and remove Dockerfile comments or examples that promote unsafe `--ulimit` usage (very high or unlimited).
- Add or modify container startup scripts (Python or shell) to:
  - Read effective resource limits (`RLIMIT_NOFILE`, `RLIMIT_NPROC` where available).
  - Compare against configurable required minimums and ideal ranges via environment variables.
  - Fail fast with clear logs when limits are too low.
- Introduce optional, explicitly configured logic to tighten (lower) overly high soft limits without exceeding hard limits.

### Cannot Do
- Cannot modify Docker daemon or orchestration platform configuration directly (e.g., `daemon.json`, Kubernetes pod security policies); can only document required settings.
- Cannot know the exact safe numeric values for all environments; will propose conservative, configurable defaults and rely on operators to tune them.
- Cannot enforce `ulimit` policies outside the container (e.g., host-wide limits, systemd unit limits); scope is limited to what the containerized process can observe and adjust.

## Gotchas
- Treating low limits as a hint to raise them in code: Raising `nofile`/`nproc` inside the container to “fix” bad configuration hides real problems and can exceed host policy. The fix should fail fast and instruct operators to adjust daemon defaults or runtime flags instead.
- Assuming `RLIMIT_NPROC` exists everywhere: Some container runtimes or platforms do not expose `RLIMIT_NPROC`; code must check `hasattr(resource, "RLIMIT_NPROC")` (or handle shell `ulimit -Su` failures) and degrade gracefully.
- Hard-coding single numeric limits: Hard-wired magic numbers cannot fit all environments. Use environment variables for required minimums and ideal ranges so operators can adjust policies without rebuilding images.

## Quick Verification
```bash
# 1. Build the secure image (example)
docker build -t ulimit-secure .

# 2. Run with intentionally low limits -> expect clear fatal log + non-zero exit
docker run --rm \
  --ulimit nofile=128:256 \
  --ulimit nproc=64:128 \
  ulimit-secure

# 3. Run with acceptable limits -> expect normal startup, no in-process limit changes
docker run --rm \
  --ulimit nofile=2048:4096 \
  --ulimit nproc=512:1024 \
  ulimit-secure

# 4. (Optional) Enable tightening and confirm only soft limits are lowered, never raised
docker run --rm \
  -e ULIMIT_TIGHTEN=1 \
  --ulimit nofile=16384:16384 \
  --ulimit nproc=4096:4096 \
  ulimit-secure
```