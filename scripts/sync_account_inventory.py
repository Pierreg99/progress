#!/usr/bin/env python3
"""Sync the GitHub account inventory into public portfolio data.

With ACCOUNT_SYNC_TOKEN the job can read the complete authenticated account.
Without it, only public repositories are queried and the previously published
private count is preserved. Private repository names are never written.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "account-inventory.json"
SITE_OUT = ROOT / "site" / "account.json"
TOKEN = os.environ.get("ACCOUNT_SYNC_TOKEN")
FALLBACK_TOKEN = os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"
OWNER = os.environ.get("GITHUB_OWNER", "Pierreg99")


def api_get(path: str, token: str | None) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Pierreg99-progress-account-sync",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(API + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def public_repositories() -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        query = urllib.parse.urlencode({"per_page": 100, "page": page, "sort": "updated", "direction": "desc"})
        try:
            batch = api_get(f"/users/{urllib.parse.quote(OWNER)}/repos?{query}", FALLBACK_TOKEN)
        except urllib.error.HTTPError as exc:
            print(f"GitHub public API error: HTTP {exc.code}", file=sys.stderr)
            raise
        if not isinstance(batch, list) or not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def all_repositories() -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        query = urllib.parse.urlencode({"per_page": 100, "page": page, "sort": "updated", "direction": "desc"})
        batch = api_get(f"/user/repos?{query}", TOKEN)
        if not isinstance(batch, list) or not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def previous_private_count() -> int:
    for source in (SITE_OUT, OUT):
        try:
            data = json.loads(source.read_text(encoding="utf-8"))
            value = int(data.get("private", 0))
            if value >= 0:
                return value
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            continue
    return 0


def main() -> int:
    complete = bool(TOKEN)
    try:
        repos = all_repositories() if complete else public_repositories()
    except (urllib.error.HTTPError, urllib.error.URLError):
        return 3

    owned = [r for r in repos if r.get("owner", {}).get("login", "").lower() == OWNER.lower()]
    public = [
        {
            "name": r["name"],
            "fullName": r["full_name"],
            "htmlUrl": r["html_url"],
            "defaultBranch": r.get("default_branch"),
            "updatedAt": r.get("updated_at"),
            "archived": bool(r.get("archived")),
        }
        for r in owned if r.get("private") is False
    ]
    private_count = sum(1 for r in owned if r.get("private") is True) if complete else previous_private_count()

    payload = {
        "schemaVersion": 1,
        "owner": OWNER,
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "timezone": "Europe/Berlin",
        "source": "GitHub authenticated account API" if complete else "GitHub public user API + preserved private count",
        "completeAccountSync": complete,
        "total": len(public) + private_count,
        "public": len(public),
        "private": private_count,
        "privateNamesPublished": False,
        "repositories": sorted(public, key=lambda r: (r["archived"], r["name"].lower())),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SITE_OUT.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    OUT.write_text(encoded, encoding="utf-8")
    SITE_OUT.write_text(encoded, encoding="utf-8")
    print(f"synced account total={payload['total']} public={payload['public']} private={payload['private']} complete={complete}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
