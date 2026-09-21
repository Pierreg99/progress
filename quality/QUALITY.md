# Quality audits

**Overall score: 90/100** · 2026-09-21T19:12:30+02:00

| Area | Grade | Score |
|------|-------|------:|
| Security | B+ | 88 |
| Docs | B | 86 |
| Automation | A- | 92 |
| Parity | A- | 90 |
| Secrets hygiene | A | 95 |

## Checks

| Check | Result | Detail |
|-------|:------:|--------|
| `sync_board_check` | PASS | pass |
| `progress_json_valid` | PASS | version=3 overall=95 mean=95 tracks=22 |
| `codenames_no_real_repos` | PASS | clean after scrub |
| `private_map_absent` | PASS | no repo-codenames.private.json in public tree |
| `secret_scan` | PASS | No live API keys in public progress tree |
| `tracks_present` | PASS | 22 tracks |
| `benchmark_present` | PASS | benchmarks/latest.json present |
| `history_daily` | PASS | 4 history snapshots |
| `public_aliases` | PASS | codenames/PUBLIC_ALIASES.json present |
| `site_board` | PASS | site/index.html present |
| `automation_scripts` | PASS | sync_board + sync_account_inventory present |

## Sync board

`python3 scripts/sync_board.py --check` → **PASS** (pass)

## Leak scan

CLEAN (post-scrub) · scrubbed this run: 7 paths

## Prior comparison

Previous overall: **72** (2026-09-05T21:42:40.691479+00:00) → current **90** · gradeDropped=False

Checks: see `audits/latest.json` and `audits/2026-09-21.json`.

Automated by routine **Progress quality audit**.
