# Cryo Progress & Portfolio — English

Central documentation, progress, and portfolio overview for the current Pierreg99 project landscape.

## Start here

- [Deutsch README](./README.de.md)
- [Portfolio German](./site/index.de.html)
- [Portfolio English](./site/index.en.html)
- [Current progress](./PROGRESS.md)
- [Repository documentation audit](./docs/repository-documentation-audit-2026-09-07.md)
- [Deep-audit index](./docs/deep-audit-index-2026-09-07.md)
- [Account-wide GitHub sync — 2026-09-12](./docs/account-sync-2026-09-12.md)
- [Portfolio Audit 2026-09-08 — German](./docs/portfolio-audit-2026-09-08.de.md)
- [Portfolio Audit 2026-09-08 — English](./docs/portfolio-audit-2026-09-08.en.md)
- [Grade Benchmark: Innovation · Vision · Value · Solo vs. Team](./docs/pierreg99-benchmark-grades-2026-09-08.en.md)
- [DE/EN documentation standard](./docs/de-en-documentation-standard.md)

## Account-wide synchronization

`progress` is synchronized against the authenticated `Pierreg99` GitHub repository inventory. Snapshot **2026-09-12**: **99 repositories total**, including **40 public** and **59 private**. Private repository names are intentionally redacted here and remain governed by the existing codename policy.

The account-wide sync is an inventory and navigation layer. Repository-local READMEs, changelogs, roadmaps, tests, and agent instructions remain authoritative for implementation status.

## Portfolio

The portfolio groups verified projects across games, AI/agent systems, web applications, creative technology, learning/documentation, and infrastructure/assets.

Project statements are derived from verified repository content. Unsupported completion percentages are not presented as facts.

## Grade benchmark

The complementary benchmark rates **innovation, vision, technical value/workmanship, solo implementation breadth, systems depth, documentation, product maturity, and portfolio impact** on a 1–10 scale. It also compares solo work with typical small development teams across vision, breadth, architecture ownership, parallelization, QA, documentation, and time-to-production.

The grades are editorial portfolio/engineering signals, not objective personnel or personality evaluations. Repository size alone does not increase a grade.

## Documentation policy

Existing READMEs, historical change files, project roadmaps, and repository-specific agent instructions are preserved. New files provide consistent navigation and bilingual access rather than replacing project history.

## Progress

The public progress board is maintained from `progress.json`, history snapshots, and the repository sync scripts.

```bash
python3 scripts/sync_board.py
python3 scripts/sync_board.py --check
```
