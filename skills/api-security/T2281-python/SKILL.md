---
name: secure-access-control-graphql
description: 'Secure coding guidance for weakness Improper Access Control (Authorization)
  (P182). Use when implementing or reviewing: Secure access control (GraphQL).'
---

# Secure access control (GraphQL)

## What This Skill Does
Ensures GraphQL APIs enforce proper authorization on all queries, mutations, nodes, and edges. This skill guides you to centralize access control (RBAC or similar), route resolvers through business logic that performs checks, and shape the schema so different permission levels cannot accidentally expose sensitive fields.

## Decision Table
| Situation | Action |
|-----------|--------|
| Resolver reads or mutates sensitive data and only uses `user_id`/args without checking caller identity or roles | Introduce a central authorization helper (RBAC-style) and call it from that resolver before data access/mutation |
| Authorization is done ad hoc in some resolvers but missing on nested fields or relationship traversals | Add per-node and per-edge checks and ensure all field resolvers invoke the central helper with resource IDs/owners |
| Business logic is spread across resolvers and other callers (CLI, jobs, REST) with duplicated or inconsistent auth | Move authorization rules into business/service layer methods and have all resolvers delegate to them |
| Schema currently exposes one “fat” type with sensitive fields that are just nullable for low-privilege users | Split into interface/union types (e.g., `PublicUser` vs `PrivateUser`) and only include sensitive fields on privileged types |
| Code already derives a principal from context and consistently checks permissions in a single helper or service for all paths | No action needed; keep pattern and just verify node/edge traversal paths also use the same checks |

## Boundaries

### Can Do
- Identify GraphQL resolvers that lack authorization checks before accessing or mutating sensitive resources.
- Propose or implement centralized RBAC-style helpers and integrate them into resolvers and business services.
- Add node- and edge-level checks to prevent unauthorized graph traversal to other users’ data.
- Refactor examples to delegate authorization to a business layer and use schema types (interfaces/unions) to separate privileged vs limited views.

### Cannot Do
- Infer your application’s full role/permission model or business rules without human input; you must define roles and allowed actions.
- Automatically detect every GraphQL entry point if the framework wiring is hidden or meta-programmed beyond what’s shown in code.
- Guarantee performance or caching behavior of added checks; you must profile and optimize (e.g., batching, dataloaders).
- Replace or configure external identity providers (OIDC, SSO); this skill assumes authentication is already in place and focuses on authorization.

## Gotchas
- Relying only on top-level query/mutation checks: This is wrong because nested resolvers (e.g., `user.orders`, `team.members`) can still expose unauthorized data if they don’t re-check access per node/edge.
- Using operation name alone for authorization (e.g., “if query == getUser, allow”): This is wrong because attackers can vary arguments (different `user_id`, tenant, etc.); checks must use the current principal plus resource ownership/tenant information.
- Returning null for sensitive fields on a single type instead of using separate types: This is risky because schema suggests the field is always requestable; clients may discover presence/absence patterns, and developers may accidentally re-enable exposure. Prefer separate interface/union member types with no sensitive field on low-privilege variants.

## Quick Verification
```bash
# 1. Run vulnerable example: confirm unauthorized access is currently possible
python app_vulnerable_code.py 2             # Logged in as user "1", can read user "2" (incorrect)
python app_vulnerable_code.py 2 newemail@x  # Logged in as user "1", can edit user "2" (incorrect)

# 2. Run fixed example: confirm unauthorized attempts are blocked
python app_fix_original_code.py 2           # Expect PermissionError in output for non-admin "1"
python app_fix_original_code.py 2 newemail@x  # Expect PermissionError, email not changed

# 3. Optional: simulate authorized admin access by editing fixture to make current_user_id admin
# Then rerun and ensure admin can read/edit others while normal user cannot.
```