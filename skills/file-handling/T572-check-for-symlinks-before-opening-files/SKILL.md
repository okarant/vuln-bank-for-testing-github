---
name: check-for-symlinks-before-opening-files
description: Prevents link-following vulnerabilities by checking for symlinks and hard links plus base-directory containment before file access; use when untrusted paths are opened, created, or deleted
---

# Check for symlinks before opening files

## What This Skill Does
Prevents Improper Link Resolution / link-following vulnerabilities (CWE-59) by ensuring code does not blindly follow symbolic links or hard links when accessing files. It guides you to add `lstat`-based link checks, canonical path validation, and base-directory containment so that user-controlled paths cannot escape a trusted directory or hijack file operations.

## Decision Table
| Situation | Action |
|-----------|--------|
| Code opens/creates/deletes files with user-controlled or external input paths (e.g., HTTP, CLI, config) and no explicit symlink checks | Insert `lstat`/equivalent before access; reject symlinks and unexpected hard links |
| Application must never follow symlinks for security-sensitive files (config, keys, auth data, logs) | Add a guard that uses `lstat` to detect any symlink and fail closed on detection |
| Application intentionally uses symlinks (shared resources, alias dirs) | Resolve with `realpath`, canonicalize, and enforce that final target is under an allowed base directory before access |
| Paths are intended to be confined to a “home” or sandbox directory but only `path.join` / string concatenation is used | Add base-directory canonicalization and containment checks (`realpath` + `relative`) and reject any escaping path |
| Code already uses `lstat`/equivalent, `realpath`, and enforces containment under a trusted base before using the path or file descriptor | No action needed (ensure checks cover both read and write/delete paths) |

## Boundaries

### Can Do
- Detect and remediate missing symlink and hard-link checks before file open/create/delete.
- Add race-resistant, descriptor-based open patterns (e.g., exclusive create, `lstat` on existing paths, then operate via descriptor).
- Enforce canonical path containment under a trusted base directory to prevent directory traversal via symlinks or `..`.

### Cannot Do
- Cannot fully eliminate OS-level TOCTOU races where the language/runtime lacks atomic, link-safe primitives beyond basic flags.
- Cannot infer application-specific policy for when symlinks *should* be allowed; requires hints from surrounding code or comments.
- Cannot protect against vulnerabilities introduced by other components (e.g., misconfigured container volumes, privileged helper tools) that bypass the application’s path checks.

## Gotchas
- Assuming `stat`/default file API is enough: `stat` usually follows symlinks; use `lstat` (or equivalent) when deciding whether to reject a path, so you examine the link itself, not its target.
- Relying only on `path.join` / string checks: normalization alone does not prevent symlink-based escapes; always combine with `realpath` and base-directory containment checks for the final target.
- Treating single-link regular files as always safe: hard links share the same inode; any regular file with `nlink > 1` must be evaluated against policy (often rejected) before writes or deletes.

## Quick Verification
```bash
# 1) Prepare environment
mkdir -p user_files
echo "SECRET" > secret.txt
ln -s "$(pwd)/secret.txt" user_files/evil_link

# 2) Run vulnerable version (should incorrectly overwrite secret.txt)
node app_vulnerable_code.js evil_link
cat secret.txt   # In vulnerable code, contents are modified

# 3) Run fixed version (should reject the symlink/hardlink path)
node app_fix_gpt51_code.js evil_link || echo "blocked as unsafe"

# 4) Verify secret.txt was not modified by the fixed app
cat secret.txt
```