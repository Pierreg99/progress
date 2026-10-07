#!/usr/bin/env python3
"""Regenerate PROGRESS.md + README.md + site/ from progress.json (Europe/Berlin).

Usage:
  python3 scripts/sync_board.py           # rewrite markdown + site
  python3 scripts/sync_board.py --check   # exit 1 if stale or policy broken
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
PROGRESS = ROOT / "progress.json"
PROGRESS_MD = ROOT / "PROGRESS.md"
README = ROOT / "README.md"
TZ = ZoneInfo("Europe/Berlin")
CONTENT_DIRS = ("history", "quality", "benchmarks", "codenames", "site", "tracks", "assets")
CONTENT_FILES = ("progress.json", "PROGRESS.md", "README.md", "LICENSE")
# obfuscated deny fragments (decoded only at runtime)
_DENY_B64 = "Q3J5by1vbWVnYVRPUFRJRVIKM3RvNUQtSHlwZXJzY2FsZQpDcnlHYW1lLVNPVkVSRUlHTlRZCmNyeW9wZy12cHMKY3J5by1hdmF0YXItc29jaWFscwpDcnlvT1MtQXNzZXRzLUNvbXBsZXRlCkNyeW9PUy1BTEwtQVNTRVRTCkNyeW9Bc3NldHMtRXhhbXBsZQ=="


def denylist() -> list[str]:
    return base64.b64decode(_DENY_B64).decode().splitlines()


def load() -> dict:
    data = json.loads(PROGRESS.read_text(encoding="utf-8"))
    tracks = data.get("tracks") or []
    if not tracks:
        raise SystemExit("progress.json: no tracks")
    for t in tracks:
        if "percent" not in t or "name" not in t or "id" not in t:
            raise SystemExit(f"track missing fields: {t}")
        pct = t["percent"]
        if not isinstance(pct, (int, float)) or pct < 0 or pct > 100:
            raise SystemExit(f"bad percent on {t.get('id')}: {pct}")
    percents = [float(t["percent"]) for t in tracks]
    overall = round(sum(percents) / len(percents))
    data["overallPercent"] = overall
    data.setdefault("timezone", "Europe/Berlin")
    data.setdefault("version", 3)
    data.setdefault("orgRepo", "Pierreg99/progress")
    data.setdefault(
        "syncPolicy",
        "after-every-task (sync-progress-after-task) + weekday catch-up (progress-percent-auto)",
    )
    data.setdefault(
        "codenamePolicy",
        "Private repos: display name IS the secret codename only.",
    )
    return data


def render_progress_md(data: dict) -> str:
    iso = data.get("updatedAt") or datetime.now(TZ).isoformat(timespec="seconds")
    overall = data["overallPercent"]
    lines = [
        f"# Progress — {overall}%",
        "",
        f"Updated: {iso} (Europe/Berlin)",
        "",
        "| Track | % | Status |",
        "|---|---:|---|",
    ]
    for t in sorted(
        data["tracks"], key=lambda x: (-float(x.get("percent", 0)), x.get("name", ""))
    ):
        lines.append(
            f"| {t.get('name')} | {t.get('percent')} | {t.get('status', '')} |"
        )
    lines.append("")
    return "\n".join(lines)


def _badge(label: str, msg: str, color: str) -> str:
    from urllib.parse import quote

    def e(x: str) -> str:
        return quote(x.replace("-", "--").replace("_", "__"), safe="")

    return (
        f'<img alt="{label}: {msg}" '
        f'src="https://img.shields.io/badge/{e(label)}-{e(msg)}-{color}?style=for-the-badge">'
    )


def render_readme(data: dict) -> str:
    overall = data["overallPercent"]
    iso = data.get("updatedAt") or ""
    tracks = data["tracks"]
    done = sum(1 for t in tracks if float(t.get("percent", 0)) >= 100)
    rows = []
    for t in sorted(
        tracks, key=lambda x: (-float(x.get("percent", 0)), x.get("name", ""))
    ):
        rows.append(
            f"| {t.get('percent')}% | `{t.get('name')}` | {t.get('status', '')} |"
        )
    below = [t for t in tracks if float(t.get("percent", 0)) < 100]
    open_md = ""
    if below:
        open_md = (
            "\n## Offen\n\n"
            + "\n".join(
                f"- **{t.get('name')}**: {t.get('percent')}% ({t.get('status')})"
                + (f", {t.get('notes')}" if t.get("notes") else "")
                for t in sorted(below, key=lambda x: float(x.get("percent", 0)))
            )
            + "\n"
        )
    color = "2E7D32" if overall >= 90 else ("F59F00" if overall >= 60 else "C92A2A")
    badges = "\n".join(
        [
            _badge("Gesamt", f"{overall}%", color),
            _badge("Tracks", f"{done}/{len(tracks)} fertig", "0B7285"),
            _badge("Python", "3.12", "3776AB"),
            _badge("Lizenz", "MIT", "495057"),
        ]
    )
    wf = "\n".join(
        f'<a href="https://github.com/Pierreg99/progress/actions/workflows/{w}">'
        f'<img alt="{w}" src="https://github.com/Pierreg99/progress/actions/workflows/{w}/badge.svg"></a>'
        for w in ("validate.yml", "pages.yml", "account-sync.yml")
    )
    mermaid = "\n".join(
        [
            "```mermaid",
            "flowchart LR",
            '    J[("progress.json")] --> S["scripts/sync_board.py"]',
            '    S --> R["README.md"]',
            '    S --> P["PROGRESS.md"]',
            '    S --> W["site/"]',
            '    S --> C{"Leak-Policy und --check"}',
            '    C --> V[["validate.yml"]]',
            '    W --> G[["pages.yml"]]',
            "```",
        ]
    )
    return f"""<div align="center">

# Cryo Progress ({overall}%)

<p><strong>Öffentlicher Fortschritts- und Qualitätsstand von Cryo Omega, private Projekte nur unter Codenamen.</strong></p>

<p>
{badges}
</p>
<p>
{wf}
</p>

<p><a href="#tracks">Tracks</a> · <a href="#schnellstart">Schnellstart</a> · <a href="#english-summary">English</a></p>

</div>

---

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Features](#features)
- [Tracks](#tracks)
- [Schnellstart](#schnellstart)
- [Architektur](#architektur)
- [Projektstruktur](#projektstruktur)
- [Richtlinien](#richtlinien)
- [Dokumentation](#dokumentation)
- [English summary](#english-summary)

## Überblick

**Gesamt: {overall}%** · Stand: `{iso}` · Zeitzone: Europe/Berlin

Synchronisiert nach jeder relevanten Aufgabe (Skill `sync-progress-after-task`) sowie werktags über die Routine **Progress percent auto** (18:00 Berlin, Mo–Fr). Private Tracks erscheinen ausschließlich unter ihrem **Codenamen**.

## Features

- Eine Datenquelle: `progress.json` enthält alle Tracks; der Gesamtwert ist der Mittelwert aller Track-Prozente.
- `scripts/sync_board.py` erzeugt `README.md`, `PROGRESS.md` und die Seiten unter `site/`.
- Eingebaute Leak-Prüfung: Inhalte werden vor dem Schreiben auf private Repository-Namen geprüft.
- `--check` erkennt veraltete Artefakte; `validate.yml` prüft jeden Pull Request.
- Historie unter `history/`, Qualitäts-Audits unter `quality/audits/`, Benchmarks unter `benchmarks/`.
- Live-Board über GitHub Pages (`pages.yml`).

## Tracks

| % | Name | Status |
|---|------|--------|
{chr(10).join(rows)}
{open_md}
## Schnellstart

```bash
git clone https://github.com/Pierreg99/progress.git
cd progress
python3 scripts/sync_board.py          # regenerate PROGRESS.md + README.md + site/
python3 scripts/sync_board.py --check  # CI / pre-push policy check
```

## Architektur

{mermaid}

## Projektstruktur

```text
progress/
├── .github/workflows/   account-sync.yml, pages.yml, validate.yml
├── benchmarks/          Benchmark-Snapshots
├── codenames/           Öffentliche Aliase
├── data/                Account-Inventar und Meilensteine
├── docs/                Audits und Dokumentationsstandard
├── history/             Tägliche Fortschritts-Snapshots
├── quality/             QUALITY.md und Audits
├── scripts/             sync_board.py, sync_account_inventory.py
├── site/                Live-Board (GitHub Pages)
├── progress.json        Datenquelle
├── PROGRESS.md          Generierte Übersicht
├── README.de.md / README.en.md
└── LICENSE
```

## Richtlinien

- Niemals private Codename-Zuordnungen oder echte private Repository-Namen in Inhaltsdateien committen.
- Öffentliche Aliase liegen in [`codenames/PUBLIC_ALIASES.json`](./codenames/PUBLIC_ALIASES.json).
- Historien-Snapshots: [`history/`](./history/).
- Live-Board (GitHub Pages): `site/index.html`

## Dokumentation

- [README.de.md](./README.de.md) · [README.en.md](./README.en.md)
- [PROGRESS.md](./PROGRESS.md)
- [Qualität: quality/QUALITY.md](./quality/QUALITY.md)
- [Benchmarks: benchmarks/LATEST.md](./benchmarks/LATEST.md)
- [docs/](./docs/)

## English summary

Public Cryo Omega progress and quality audits. Overall progress is **{overall}%** across {len(tracks)} tracks ({done} complete); private tracks appear by codename only. Everything is generated from `progress.json` by `scripts/sync_board.py`, which also enforces the private-name leak policy and powers the GitHub Pages board.
"""

def iter_content_files():
    for name in CONTENT_FILES:
        p = ROOT / name
        if p.is_file():
            yield p
    for d in CONTENT_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file():
                yield path


def scan_leaks() -> list[str]:
    hits = []
    deny = denylist()
    for path in iter_content_files():
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for name in deny:
            if name and name in text:
                hits.append(f"{path.relative_to(ROOT)}: blocked fragment")
    return hits


def write_site(data: dict) -> None:
    site = ROOT / "site"
    site.mkdir(exist_ok=True)
    (site / "progress.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    overall = data["overallPercent"]
    rows = "".join(
        f"<tr><td>{t.get('percent')}</td><td>{t.get('name')}</td><td>{t.get('status','')}</td></tr>"
        for t in sorted(
            data["tracks"],
            key=lambda x: (-float(x.get("percent", 0)), x.get("name", "")),
        )
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Cryo Progress — {overall}%</title>
  <style>
    :root {{ color-scheme: dark; font-family: ui-sans-serif, system-ui, sans-serif; }}
    body {{ margin: 2rem auto; max-width: 52rem; padding: 0 1rem; background: #0b1020; color: #e8eefc; }}
    h1 {{ font-size: 1.6rem; }}
    .bar {{ height: 10px; background: #1c2744; border-radius: 999px; overflow: hidden; margin: 1rem 0 1.5rem; }}
    .bar > span {{ display: block; height: 100%; width: {overall}%; background: linear-gradient(90deg,#5aa9ff,#7c4dff); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; }}
    th, td {{ text-align: left; padding: 0.45rem 0.35rem; border-bottom: 1px solid #243056; }}
    th {{ color: #9fb3d9; font-weight: 600; }}
    td:first-child {{ width: 4rem; font-variant-numeric: tabular-nums; }}
    a {{ color: #8ec5ff; }}
    .meta {{ color: #9fb3d9; font-size: 0.9rem; }}
  </style>
</head>
<body>
  <h1>Cryo Progress — {overall}%</h1>
  <p class="meta">Updated {data.get('updatedAt','')} · Europe/Berlin · <a href="https://github.com/Pierreg99/progress">source</a></p>
  <div class="bar" aria-label="Overall {overall}%"><span></span></div>
  <table>
    <thead><tr><th>%</th><th>Track</th><th>Status</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <p class="meta">Private tracks shown by codename only.</p>
</body>
</html>
"""
    (site / "index.html").write_text(html, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--touch-updated", action="store_true")
    args = ap.parse_args()
    data = load()
    if args.touch_updated:
        data["updatedAt"] = datetime.now(TZ).isoformat(timespec="seconds")
    progress_md = render_progress_md(data)
    readme = render_readme(data)
    leaks = scan_leaks()
    if leaks:
        print("POLICY FAIL — private name leak in content:", file=sys.stderr)
        for h in leaks:
            print(" ", h, file=sys.stderr)
        return 2
    if args.check:
        ok = True
        if PROGRESS_MD.read_text(encoding="utf-8") != progress_md:
            print("PROGRESS.md stale", file=sys.stderr)
            ok = False
        if f"({data['overallPercent']}%)" not in README.read_text(encoding="utf-8"):
            print("README.md overall stale", file=sys.stderr)
            ok = False
        stored = json.loads(PROGRESS.read_text(encoding="utf-8")).get("overallPercent")
        if stored != data["overallPercent"]:
            print("progress.json overallPercent mismatch vs mean", file=sys.stderr)
            ok = False
        if not (ROOT / "site" / "index.html").exists():
            print("site/index.html missing", file=sys.stderr)
            ok = False
        return 0 if ok else 1
    PROGRESS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PROGRESS_MD.write_text(progress_md, encoding="utf-8")
    README.write_text(readme, encoding="utf-8")
    write_site(data)
    print(f"synced overall={data['overallPercent']}% tracks={len(data['tracks'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
