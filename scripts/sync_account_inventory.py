#!/usr/bin/env python3
"""Sync the authenticated GitHub account inventory into public portfolio data.

Writes:
  data/account-inventory.json
  site/account.json

The script prefers ACCOUNT_SYNC_TOKEN (a PAT/app token stored as a GitHub
Actions secret). Without it, GITHUB_TOKEN is used and the repository's public
inventory is still updated safely; private repository names are never written.
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
TOKEN = os.environ.get("ACCOUNT_SYNC_TOKEN") or os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"
OWNER = os.environ.get("GITHUB_OWNER", "Pierreg99")


def api_get(path: str) -> object:
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Pierreg99-progress-account-sync",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def main() -> int:
    if not TOKEN:
        print("Missing GITHUB_TOKEN/ACCOUNT_SYNC_TOKEN", file=sys.stderr)
        return 2

    repos: list[dict] = []
    page = 1
    while True:
        query = urllib.parse.urlencode({
            "per_page": 100,
            "page": page,
            "sort": "updated",
            "direction": "desc",
        })
        try:
            batch = api_get(f"/user/repos?{query}")
        except urllib.error.HTTPError as exc:
            print(f"GitHub API error: HTTP {exc.code}", file=sys.stderr)
            return 3
        if not isinstance(batch, list) or not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    public = [
        {
            "name": r["name"],
            "fullName": r["full_name"],
            "htmlUrl": r["html_url"],
            "defaultBranch": r.get("default_branch"),
            "updatedAt": r.get("updated_at"),
            "archived": bool(r.get("archived")),
        }
        for r in repos
        if r.get("private") is False
        and r.get("owner", {}).get("login", "").lower() == OWNER.lower()
    ]
    private_count = sum(
        1 for r in repos
        if r.get("private") is True
        and r.get("owner", {}).get("login", "").lower() == OWNER.lower()
    )

    payload = {
        "schemaVersion": 1,
        "owner": OWNER,
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "timezone": "Europe/Berlin",
        "source": "GitHub /user/repos",
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
    print(f"synced account total={payload['total']} public={payload['public']} private={payload['private']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
