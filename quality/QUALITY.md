# Quality audits

**Overall score: 91/100** · 2026-09-29T18:42:28+02:00

| Area | Grade | Score |
|------|-------|------:|
| Security | B+ | 89 |
| Docs | B | 86 |
| Automation | A- | 92 |
| Parity | A- | 93 |
| Secrets hygiene | A | 94 |

## Checks

| Check | Result | Detail |
|-------|:------:|--------|
| `sync_board_check` | PASS | pass |
| `progress_json_valid` | PASS | version=3 overall=95 mean=95 tracks=22 (rounding=round(mean)) |
| `codenames_no_real_repos` | PASS | clean — no private real-name hits in content paths |
| `private_map_absent` | PASS | no repo-codenames.private.json in public tree |
| `secret_scan` | PASS | No live API keys in public progress tree |
| `tracks_present` | PASS | 22 tracks |
| `benchmark_present` | PASS | benchmarks/latest.json present |
| `history_daily` | PASS | 8 history snapshots |
| `public_aliases` | PASS | codenames/PUBLIC_ALIASES.json present |
| `site_board` | PASS | site/index.html present |
| `automation_scripts` | PASS | sync_board + sync_account_inventory present |

## Sync board

`python3 scripts/sync_board.py --check` → **PASS** (pass)

## Leak scan

CLEAN · scrubbed this run: 0 paths · no private-name hits

## Prior comparison

Previous overall: **90** (2026-09-28T18:39:02+02:00) → current **91** · gradeDropped=False

Checks: see `audits/latest.json` and `audits/2026-09-29.json`.

Automated by routine **Progress quality audit**.
