# Cryo Progress & Portfolio — Deutsch

Die zentrale Dokumentations-, Fortschritts- und Portfolio-Übersicht für den aktuellen Pierreg99-Projektbestand.

## Einstieg

- [English README](./README.en.md)
- [Portfolio Deutsch](./site/index.de.html)
- [Portfolio English](./site/index.en.html)
- [Aktueller Fortschritt](./PROGRESS.md)
- [57-Repository-Portfolioaudit Deutsch](./docs/portfolio-audit-2026-09-08.de.md)
- [57-Repository-Portfolioaudit English](./docs/portfolio-audit-2026-09-08.en.md)
- [Repository-Dokumentationsaudit](./docs/repository-documentation-audit-2026-09-07.md)
- [Deep-Audit-Index](./docs/deep-audit-index-2026-09-07.md)
- [DE/EN-Dokumentationsstandard](./docs/de-en-documentation-standard.md)

## Portfolio

Das Portfolio bündelt verifizierte Projekte aus den Bereichen Games, KI/Agentensysteme, Webanwendungen, Creative Technology, Lernen/Dokumentation sowie Infrastruktur und Assets.

Die aktuelle Deep-Audit-Matrix bewertet **57 zugängliche Repositories** nach Engineering-Reife, Dokumentation, Portfolio-Wirkung und Priorität. Die Bewertungen sind redaktionelle Evidenzsignale; nicht ausgeführte Projekte werden nicht als erfolgreich getestet dargestellt.

## Flagship-Fokus

- `agent-memory` — Python-Library, API, Persistenz, Tests, Benchmarks und CI.
- `cryo-unified-agent` — AI-Control-Plane mit Routing, Skills, MCP, Memory, Policies und Governance.
- `Chronicles-of-Lumina-GameRPGwork` — umfangreiche Web-/3D-Game-Plattform mit Tests und Pages.
- `ResidentLovely-Maximum-Hapiness-Game` — interaktives Three.js-Game-Showcase.
- `KiBlox-VoxelGame` — Voxel-/3D-Engineering.
- `Nexo-Jarvis-AI-Futuristic-Assistant-Alpha` — öffentlicher AI/HUD-Showcase.
- `Cryo-Motion-Studio-Concept-Websuite` — öffentlicher Creative-Web-Showcase.

## Dokumentationsprinzip

Bestehende READMEs, historische Änderungsdateien und projektspezifische Agent-Regeln werden erhalten. Neue Dokumente ergänzen sie und schaffen eine einheitliche Navigation.

## Fortschritt

Der öffentliche Fortschrittsstand wird über `progress.json`, History-Snapshots und die vorhandenen Sync-Skripte gepflegt.

```bash
python3 scripts/sync_board.py
python3 scripts/sync_board.py --check
```
