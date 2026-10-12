# Quality audits

**Overall score: 90/100** · 2026-10-12T18:52:57+02:00

| Area | Grade | Score |
|------|-------|------:|
| Security | A- | 90 |
| Docs | B | 86 |
| Automation | A- | 90 |
| Parity | A | 94 |
| Secrets hygiene | A- | 91 |

## Checks

| Check | Result | Detail |
|-------|:------:|--------|
| `sync_board_check` | PASS | pass (exit 0, no drift; markdown/site not regenerated) |
| `progress_json_valid` | PASS | version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks |
| `codenames_no_real_repos` | PASS | 0 private real-name leaks in the working tree after scrub (38 private names, case-insensitive scan of 65 non-.git files); scrubbed 2 this run; known false positives: public NEXUS-SPIRE-42 host URL/health and GLACIER-FLARE-55 substring inside public launcher repo name |
| `private_map_absent` | PASS | no repo-codenames.private.json in public tree |
| `secret_scan` | PASS | No live API keys or private key blocks in public progress tree |
| `tracks_present` | PASS | 22 tracks |
| `benchmark_present` | PASS | benchmarks/latest.json present (paused routine slug scrubbed to IRON-SEAL-38-agentic-autosync) |
| `history_daily` | PASS | 13 history snapshots, latest history/2026-10-12.json |
| `public_aliases` | PASS | codenames/PUBLIC_ALIASES.json present |
| `site_board` | PASS | site/index.html present; site/progress.json byte-identical to progress.json |
| `automation_scripts` | PASS | sync_board + sync_account_inventory present |
| `account_inventory_private_names` | PASS | data/account-inventory.json lists 60 public repos only; private count 59 published, privateNamesPublished=false |

## Sync board

`python3 scripts/sync_board.py --check` → **PASS** (pass)

## Leak scan

SCRUBBED · 2 occurrence(s): `benchmarks/latest.json` `grok-bot-agentic-autosync` → `IRON-SEAL-38-agentic-autosync`; `benchmarks/history/2026-10-12.json` `grok-bot-agentic-autosync` → `IRON-SEAL-38-agentic-autosync`. Strings leaked before 2026-10-05 remain in git history.

## Findings

- **medium**: Benchmark paused-routines list reintroduced private repo name via routine slug grok-bot-agentic-autosync in benchmarks/latest.json and benchmarks/history/2026-10-12.json; scrubbed to IRON-SEAL-38-agentic-autosync
- **medium**: Strings leaked before 2026-10-05 (IRON-SEAL-38, DRIFT-DEPTH-70) still exist in public git history; removal would need a history rewrite and force-push (not done)
- **medium**: sync_board --check policy still does not scan for real private names; this audit's substring scan is the only guard
- **info**: account inventory completeAccountSync=false (public API + preserved private count)
- **info**: sync_board --check PASS; version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks
- **info**: Catch-up after failed 2026-10-09 routine run; prior published audit was 2026-10-06

## Prior comparison

Previous overall: **90** (2026-10-06T18:40:00+02:00) → current **90** · gradeDropped=False (Parity A- → A)
