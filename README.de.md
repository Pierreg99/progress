# Cryo Progress & Portfolio — Deutsch

Die zentrale Dokumentations-, Fortschritts- und Portfolio-Übersicht für den aktuellen Pierreg99-Projektbestand.

## Einstieg

- [English README](./README.en.md)
- [Portfolio Deutsch](./site/index.de.html)
- [Portfolio English](./site/index.en.html)
- [Aktueller Fortschritt](./PROGRESS.md)
- [Repository-Dokumentationsaudit](./docs/repository-documentation-audit-2026-09-07.md)
- [Deep-Audit-Index](./docs/deep-audit-index-2026-09-07.md)
- [Account-weites GitHub-Sync-Snapshot 12.09.2026](./docs/account-sync-2026-09-12.md)
- [Portfolio-Audit 08.09.2026 Deutsch](./docs/portfolio-audit-2026-09-08.de.md)
- [Portfolio-Audit 08.09.2026 English](./docs/portfolio-audit-2026-09-08.en.md)
- [Notenbenchmark: Innovation · Vision · Wert · Solo vs. Team](./docs/pierreg99-benchmark-grades-2026-09-08.de.md)
- [DE/EN-Dokumentationsstandard](./docs/de-en-documentation-standard.md)

## Account-weite Synchronisierung

`progress` dient als öffentliche Aggregations- und Navigationsschicht für den authentifizierten `Pierreg99`-GitHub-Bestand. Snapshot **12.09.2026**: **99 Repositories insgesamt**, davon **40 öffentlich** und **59 privat**. Private Repository-Namen werden in dieser öffentlichen Oberfläche nicht wiederholt und bleiben der bestehenden Codename-/Redaktionsrichtlinie unterworfen.

Der Account-Sync erfasst Repository-Präsenz und Navigation. Repository-lokale READMEs, Changelogs, Roadmaps, Tests und Agent-Regeln bleiben die maßgeblichen Quellen für Implementierungsstatus.

## Portfolio

Das Portfolio bündelt verifizierte Projekte aus den Bereichen Games, KI/Agentensysteme, Webanwendungen, Creative Technology, Lernen/Dokumentation sowie Infrastruktur und Assets.

Die Projektangaben werden aus den tatsächlich geprüften Repository-Inhalten abgeleitet. Nicht verifizierte Fertigstellungswerte werden nicht als Tatsachen veröffentlicht.

## Notenbenchmark

Die ergänzende Benchmark bewertet **Innovation, Vision, technische Wertarbeit, Solo-Umsetzungsbreite, Systemtiefe, Dokumentation, Produktreife und Portfolio-Wirkung** auf einer Skala von 1–10. Zusätzlich wird die Arbeitsform Solo gegenüber typischen kleinen Dev-Teams nach Vision, Breite, Architektur-Ownership, Parallelisierung, QA, Dokumentation und Time-to-Production eingeordnet.

Die Noten sind redaktionelle Portfolio-/Engineering-Signale und keine objektive Personen- oder Personalbewertung. Repository-Größe allein erzeugt keine bessere Note.

## Dokumentationsprinzip

Bestehende READMEs, historische Änderungsdateien und projektspezifische Agent-Regeln werden erhalten. Neue Dokumente ergänzen sie und schaffen eine einheitliche Navigation.

## Fortschritt

Der öffentliche Fortschrittsstand wird über `progress.json`, History-Snapshots und die vorhandenen Sync-Skripte gepflegt.

```bash
python3 scripts/sync_board.py
python3 scripts/sync_board.py --check
```
