<div align="center">

<img src="./assets/readme-banner.svg" alt="progress" width="100%">

# progress

Public Cryo Omega progress % + quality audits (private projects by secret codename only)

[![branch](https://img.shields.io/badge/branch-main-7EB8C9?style=flat-square)](https://github.com/Pierreg99/progress)
[![sichtbarkeit](https://img.shields.io/badge/sichtbarkeit-öffentlich-141414?style=flat-square&labelColor=0A0A0A)](https://github.com/Pierreg99/progress)
[![sprache](https://img.shields.io/badge/sprache-HTML-2A2A28?style=flat-square&labelColor=0A0A0A)](https://github.com/Pierreg99/progress)

</div>

<table>
<tr>
<td width="58%" valign="top">

### Bestand

Public Cryo Omega progress % + quality audits (private projects by secret codename only)

Der Default-Branch `main` ist die Fläche, die zählt. Was nicht in diesem Baum liegt, ist kein Feature dieses Repos.

</td>
<td width="42%" valign="top">

### Fakten

| Feld | Wert |
| --- | --- |
| Owner | Pierreg99 |
| Branch | `main` |
| Sichtbarkeit | öffentlich |
| Sprache | HTML |
| Archiv | nein |

</td>
</tr>
</table>

## Lesen

1. Default-Branch öffnen.
2. Nur Dateien in diesem Baum als Beleg nehmen.
3. Issues und Diskussionen nur nutzen, wenn sie im Repo eingeschaltet sind.

## Grenze

Keine Qualitätszahl, kein Paketstand und keine Runtime, die nicht als Datei in diesem Repo steht.

<p align="center"><sub>Fläche nach Cryo Core Lite v1.5 · Tokens #0A0A0A / #141414 / #7EB8C9</sub></p>


<details>
<summary>Bisheriger README-Text</summary>

# Cryo Progress (96%)

Public automatic progress + quality audits for Cryofreee / Cryo Omega.

**Overall: 96%** · Updated: `2026-10-06T18:10:00+02:00` · Timezone: Europe/Berlin

Synced after every material task (`sync-progress-after-task` skill) plus weekday catch-up routine **Progress percent auto** (18:00 Berlin, Mon–Fri). Private tracks = **codename only**.

## Tracks

| % | Name | Status |
|---|------|--------|
| 100% | `AURORA-PANEL-27` | live |
| 100% | `Blender 5.2 LTS install` | live |
| 100% | `CRYO-ARC-14` | live |
| 100% | `Castle 30s immersive render` | live |
| 100% | `Chronicles of Lumina` | live |
| 100% | `CryAIPulse public viz` | live |
| 100% | `Cryoplane Polygonal Flight` | live |
| 100% | `Cyberdash Rhythm Platformer` | live |
| 100% | `DRIFT-MIRROR-11` | live |
| 100% | `IRON-SEAL-38` | live |
| 100% | `KiBlox VoxelGame` | live |
| 100% | `Master prompts fan bundle` | live |
| 100% | `NEXUS-SPIRE-42` | live |
| 100% | `OBSIDIAN-ORBIT-66` | live |
| 100% | `POLAR-BLADE-62` | live |
| 100% | `POLAR-BLADE-62` | live |
| 100% | `POLAR-BLADE-62` | live |
| 100% | `Resident Lovely` | live |
| 100% | `SPECTRE-LENS-37` | live |
| 100% | `agent-memory library` | live |
| 96% | `NEXUS-CORE-81` | active |
| 10% | `CIPHER-ARC-15` | user_action |


## Open

- **CIPHER-ARC-15** — 10% (user_action) — Secret rotation still deferred (codename only).
- **NEXUS-CORE-81** — 96% (active) — main at 5297cea (README surfaces + OmniSurface CLI/TUI dispatcher, Termux:API catalog, skin registry, LSP host probe on top of 4c0a0b4); pytest 52 passed on 5297cea (2026-10-05). The botult branch no longer exists on the remote; 7 PRs open (checked 2026-10-06, main unchanged). Still no debugger or git panel in the IDE or APK and no live language-server session (kotlin-lsp binary not in the tree), so the percent stays 96.

## Quality

See [`quality/QUALITY.md`](./quality/QUALITY.md).

## Sync

```bash
python3 scripts/sync_board.py          # regenerate PROGRESS.md + README.md + site/
python3 scripts/sync_board.py --check  # CI / pre-push policy check
```

## Policy

- Never commit private codename maps or real private repo names into content files.
- Public aliases live in [`codenames/PUBLIC_ALIASES.json`](./codenames/PUBLIC_ALIASES.json).
- History snapshots: [`history/`](./history/).
- Live board (GitHub Pages): `site/index.html`

</details>
