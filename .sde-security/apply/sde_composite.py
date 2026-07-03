#!/usr/bin/env python3
"""
SD Elements Composite/Batch helper -- CANONICAL REFERENCE (Python 3, stdlib only).

BEHAVIORAL CONTRACT (every runtime/port of this script MUST preserve ALL of it):
  1. AUTH: read SDE_HOST + SDE_API_KEY from the environment. If either is unset,
     read them from the MCP config -- ./.cursor/mcp.json then ~/.cursor/mcp.json --
     at mcpServers.sdelements.env.{SDE_HOST,SDE_API_KEY}. NEVER hardcode the key;
     NEVER print it.
  2. INPUT: read a composite request body (JSON) from --input. Shape:
       { "all_or_none": false, "strict_ref_checking": false,
         "composite_request": [ {"method","path","reference_id","body"?}, ... ] }
  3. SEND: POST it to  https://$SDE_HOST/api/v2/composite/  with header
       Authorization: Token $SDE_API_KEY   (normal TLS verification -- no -k).
  4. OFFLOAD: write the FULL response JSON to --out (the bulk payload stays on
     disk, NOT on stdout / NOT in the agent context window).
  5. RECONCILE: inspect EVERY reference_id in composite_response.
       http_status_code 2xx  => ok
       otherwise             => failed[]
  6. RETRY: re-POST ONLY the failed sub-requests ONCE, as a single follow-up
     composite call (same paths/bodies). Merge the retry outcome back in.
  7. SUMMARY: print ONLY a compact summary to stdout
       (posted / failed counts + the failed reference_ids).
  8. EXIT: non-zero if ANY reference_id is still unresolved after the retry.

Usage:
  SDE_HOST=https://demo.sdelements.com SDE_API_KEY=xxxx \
    python3 sde_composite.py --input body.json --out resp.json
  # or omit the env vars and rely on .cursor/mcp.json

Dependencies: none (urllib, json, os, sys, argparse). Cross-platform (Win/macOS/Linux).
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def _load_from_mcp_json():
    """Return (host, key) from the first mcp.json found, or (None, None)."""
    candidates = [
        os.path.join(os.getcwd(), ".cursor", "mcp.json"),
        os.path.expanduser(os.path.join("~", ".cursor", "mcp.json")),
    ]
    for path in candidates:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                cfg = json.load(fh)
        except (OSError, ValueError):
            continue
        env = (
            cfg.get("mcpServers", {})
            .get("sdelements", {})
            .get("env", {})
        )
        host = env.get("SDE_HOST")
        key = env.get("SDE_API_KEY")
        if host and key:
            return host, key
    return None, None


def load_auth():
    """Resolve (host, key): environment first, then mcp.json. Exit if missing."""
    host = os.environ.get("SDE_HOST")
    key = os.environ.get("SDE_API_KEY")
    if not (host and key):
        m_host, m_key = _load_from_mcp_json()
        host = host or m_host
        key = key or m_key
    if not (host and key):
        sys.stderr.write(
            "[sde_composite] ERROR: SDE_HOST/SDE_API_KEY not found in env or "
            ".cursor/mcp.json (mcpServers.sdelements.env)\n"
        )
        sys.exit(2)
    return host.rstrip("/"), key


def post_composite(host, key, body):
    """POST a composite body; return the parsed JSON response dict."""
    url = host + "/api/v2/composite/"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", "Token " + key)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:  # normal TLS verification
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # The composite endpoint may return a non-2xx OUTER status while still
        # providing per-reference_id detail in the body. Parse it so we can
        # reconcile; only treat as a hard failure when there is no
        # composite_response to inspect.
        raw = exc.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(raw)
        except ValueError:
            parsed = None
        if isinstance(parsed, dict) and "composite_response" in parsed:
            return parsed
        raise


def reconcile(response):
    """Return {reference_id: http_status_code} for every sub-response."""
    out = {}
    for sub in response.get("composite_response", []):
        out[sub.get("reference_id")] = sub.get("http_status_code")
    return out


def main():
    ap = argparse.ArgumentParser(description="SDE composite batch helper")
    ap.add_argument("--input", required=True, help="path to composite body JSON")
    ap.add_argument("--out", required=True, help="path to write the full response JSON")
    args = ap.parse_args()

    host, key = load_auth()

    with open(args.input, "r", encoding="utf-8") as fh:
        body = json.load(fh)

    subs_by_ref = {s.get("reference_id"): s for s in body.get("composite_request", [])}
    total = len(subs_by_ref)

    try:
        response = post_composite(host, key, body)
    except urllib.error.HTTPError as exc:
        sys.stderr.write("[sde_composite] outer HTTP %s\n" % exc.code)
        sys.exit(1)
    except urllib.error.URLError as exc:
        sys.stderr.write("[sde_composite] transport error: %s\n" % exc.reason)
        sys.exit(1)

    statuses = reconcile(response)
    failed = [ref for ref, code in statuses.items() if not (code and 200 <= code < 300)]

    # RETRY the failed subset ONCE, in a single follow-up composite call.
    if failed:
        retry_body = {
            "all_or_none": False,
            "strict_ref_checking": False,
            "composite_request": [subs_by_ref[ref] for ref in failed if ref in subs_by_ref],
        }
        try:
            retry_resp = post_composite(host, key, retry_body)
            merged = {s.get("reference_id"): s for s in response.get("composite_response", [])}
            for s in retry_resp.get("composite_response", []):
                merged[s.get("reference_id")] = s
            response["composite_response"] = list(merged.values())
            statuses = reconcile(response)
            failed = [ref for ref, code in statuses.items() if not (code and 200 <= code < 300)]
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            sys.stderr.write("[sde_composite] retry call failed: %s\n" % exc)

    # OFFLOAD the full response to disk (keep it out of stdout/context).
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(response, fh, indent=2)

    posted = total - len(failed)
    print("[sde_composite] posted=%d failed=%d total=%d" % (posted, len(failed), total))
    if failed:
        print("[sde_composite] failed_reference_ids=%s" % ",".join(str(f) for f in failed))
        print("[sde_composite] full response written to %s" % args.out)
        sys.exit(1)
    print("[sde_composite] full response written to %s" % args.out)
    sys.exit(0)


if __name__ == "__main__":
    main()