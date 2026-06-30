---
name: validate-file-contents
description: Validate uploaded file contents by server-side inspection and allowlists instead of trusting filenames/extensions; use when fixing unvalidated or extension-based file upload logic.
---

# Validate file contents

## What This Skill Does
Prevents attackers from uploading malicious or executable files by rejecting decisions based on user-supplied filenames, extensions, or client MIME types. It enforces server-side content-based type detection, strict allowlists, safe server-side filenames, size/sanity checks, and non-executable handling paths for all uploaded files.

## Decision Table
| Situation | Action |
|-----------|--------|
| Upload logic decides “safe” vs “unsafe” files using only `path.extname`, `originalname`, or client MIME | Add server-side content-type detection (magic bytes) and base all decisions on detected type, not user metadata |
| Code accepts any type except a small blocklist (e.g., disallow only `.exe`) | Replace with a strict allowlist of required content types (e.g., limited image/PDF MIME types) and reject all others |
| Uploaded files are stored using client-supplied names or paths (e.g., `file.originalname`, concatenated user paths) | Generate random, opaque filenames and derive extensions from detected content type; never use user paths or names for storage |
| File uploads lack size checks or only rely on web server defaults | Add explicit max-size limits and basic sanity checks on buffers before deeper processing or storage |
| Application routes uploaded content into interpreters (e.g., `eval`, `require`, template engines) or serves from executable paths | Refactor to treat uploads strictly as data: store in non-executable locations and stream bytes back with fixed content headers; never execute or import uploaded content |
| Content is already checked by a robust server-side library and enforced by allowlists and size limits | No action needed beyond confirming settings align with policy |

## Boundaries

### Can Do
- Replace extension-based or client-MIME-based checks with server-side content inspection using magic numbers or file-type libraries.
- Introduce and enforce strict allowlists for permitted MIME types and extensions based on detected content, not user input.
- Generate safe, random server-side filenames and upload paths that ignore client-supplied names and strip unsafe characters.
- Add file size limits and simple structural sanity checks to reduce DoS risk and malformed uploads.
- Refactor application code to serve uploaded files only as non-executable data and avoid routing them into execution engines.

### Cannot Do
- Cannot guarantee detection of every exotic or polyglot file format; deep validation for complex formats (Office docs, archives, media containers) still needs specialized tools.
- Cannot compensate for insecure deployment setups where upload directories are mapped to executable script locations or not restricted at the web server/OS level.
- Cannot retroactively clean or “disinfect” already stored malicious files; only helps prevent new unsafe uploads.
- Cannot enforce organization-wide storage policies (e.g., virus scanning, DLP) without integrating external scanners or services.

## Gotchas
- Trusting client MIME or extension after adding magic-byte checks: If code still allows files when `ext`/client MIME and detected type disagree, attackers can bypass validation. Always treat detected content type as the source of truth and require it to be in the allowlist.
- Using a broad or “anything image/*” allowlist: Overly generic allowlists can admit unexpected formats and malformed content. Keep allowlists narrow (e.g., `image/jpeg`, `image/png`, `image/gif`) and aligned with actual business needs.
- Keeping disk-based storage with multer but skipping memory/content validation: If files are accepted and written to disk based solely on extension, they may already be persisted in an unsafe location before validation occurs. Prefer memory storage, validate buffers, then write to a controlled directory with safe names.

## Quick Verification
```bash
# 1. Run tests or app (Node.js example)
node app_fix_gpt51_code.js example.jpg

# 2. Attempt to upload a disguised script (should be rejected)
# Create a fake "image" with .jpg extension but JS content
echo "<?php echo 'owned'; ?>" > evil.php
cp evil.php evil.jpg
node app_fix_gpt51_code.js evil.jpg  # Expect: not allowed / type_not_allowed

# 3. Test size limits (should be rejected)
# Generate a 50MB file and attempt validation
dd if=/dev/zero of=large.bin bs=1M count=50
node app_fix_gpt51_code.js large.bin  # Expect: size_not_allowed or similar

# 4. Confirm safe serving behavior
# Start the Express app and upload a .js file; check response headers indicate download/data,
# and ensure the file is not executed by the app or server.
```