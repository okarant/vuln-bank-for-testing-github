---
name: restrict-linux-kernel-capabilities-within-containers-docker
description: Use when Docker or Docker Compose containers run with privileged mode or excessive Linux capabilities; restrict capabilities by dropping all and adding back only what is required.
---

# Restrict Linux Kernel Capabilities within Containers (Docker)

## What This Skill Does
This skill hardens Docker and Docker Compose container runtime settings when containers are given excessive Linux kernel capabilities or run in privileged mode. It fixes the weakness by removing `privileged: true`, dropping all capabilities by default with `cap_drop: - ALL`, and only keeping explicitly justified capabilities when the workload truly requires them.

## Decision Table
| Situation | Action |
|-----------|--------|
| A Docker Compose service sets `privileged: true` | Remove it and set `privileged: false` if explicit intent is helpful |
| A service uses `cap_add: [ALL]` or `- ALL` | Replace with `cap_drop: - ALL` and do not add broad capabilities back |
| A service adds powerful capabilities like `SYS_ADMIN` or `NET_ADMIN` without clear need | Remove them; keep only narrowly required capabilities after testing |
| A service has no capability controls defined | Add `cap_drop: - ALL` as the default hardening step |
| A service already uses `cap_drop: - ALL` and is not privileged | No action needed unless unnecessary `cap_add` entries remain |

## Boundaries

### Can Do
- Remove privileged container settings from Docker Compose service definitions
- Add `cap_drop: - ALL` to services that lack capability restrictions
- Reduce broad `cap_add` usage to a minimal, explicitly justified set

### Cannot Do
- Determine required capabilities for every workload without understanding app behavior
- Guarantee the application will still function after capability reduction without runtime testing
- Fix non-capability container escape risks such as unsafe mounts, host networking, or exposed Docker socket access

## Gotchas
- Dropping capabilities without testing the app: some workloads need specific capabilities, so verify behavior before finalizing
- Setting `privileged: false` but leaving broad `cap_add` entries: this still grants unnecessary kernel powers
- Using `cap_drop: - ALL` in one service but not others: every container must be reviewed individually

## Quick Verification
```bash
# Start the Compose stack
docker compose up -d

# Inspect whether a container is privileged
docker inspect <container_name> --format '{{ .HostConfig.Privileged }}'

# Inspect dropped and added capabilities
docker inspect <container_name> --format '{{ json .HostConfig.CapDrop }}'
docker inspect <container_name> --format '{{ json .HostConfig.CapAdd }}'

# Confirm the app still works after capability restriction
docker compose ps
docker compose logs --tail=100
```