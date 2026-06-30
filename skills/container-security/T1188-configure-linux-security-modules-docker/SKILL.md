---
name: configure-linux-security-modules-docker
description: Use when Docker Compose services disable AppArmor, omit an explicit AppArmor profile, or need consistent kernel confinement via security_opt.
---

# Configure Linux Security Modules (Docker)

## What This Skill Does
This skill fixes Docker Compose configurations that weaken Linux Security Module enforcement by disabling AppArmor or leaving it implicit. It updates in-scope services to declare an explicit AppArmor profile in `security_opt`, rejects `apparmor=unconfined`, and standardizes on `docker-default` or another intended named profile so containers keep kernel-enforced confinement.

## Decision Table
| Situation | Action |
|-----------|--------|
| A Compose service sets `security_opt` with `apparmor=unconfined` or `apparmor:unconfined` | Replace it with an explicit confined profile such as `apparmor=docker-default` or the approved named profile |
| A Compose service has no explicit AppArmor entry | Add `security_opt` with an explicit AppArmor profile for that service |
| A Compose service already declares `apparmor=docker-default` or another intended named profile | No action needed |
| The file uses mixed AppArmor settings across services | Normalize all in-scope services to explicit confined profiles and remove unconfined entries |
| The target is not Docker Compose service configuration | Do not apply this skill |

## Boundaries

### Can Do
- Update Docker Compose service definitions to add explicit AppArmor settings
- Replace unconfined AppArmor settings with `docker-default` or another intended named profile
- Flag services that rely on implicit behavior instead of explicit AppArmor configuration

### Cannot Do
- Create or validate custom AppArmor profiles on the host
- Guarantee AppArmor is installed, enabled, or enforced by the host kernel
- Prove runtime confinement from static YAML alone without deployment-time inspection

## Gotchas
- Using `apparmor=unconfined`: this disables kernel confinement and is the unsafe pattern this skill must remove
- Relying on implicit defaults: this is inconsistent across environments and does not meet the requirement for explicit service-level declaration
- Mixing `=` and `:` forms carelessly: Compose examples vary, so preserve a valid project style and confirm the final `security_opt` value is actually parsed as an AppArmor setting

## Quick Verification
```bash
# Find insecure or missing AppArmor settings in Compose files
grep -RniE 'apparmor[=:]unconfined|security_opt' docker-compose.yml compose.yml . 2>/dev/null

# Render the final Compose config and inspect security options
docker compose config

# Check a running container's AppArmor profile
docker inspect --format '{{ .Name }} {{ .AppArmorProfile }}' <container_name>

# Confirm no running container is unconfined
docker ps -q | xargs -r docker inspect --format '{{ .Name }} {{ .AppArmorProfile }}' | grep -v ' unconfined$'
```