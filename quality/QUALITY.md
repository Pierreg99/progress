# Quality audits

**Overall score: 90/100** · 2026-10-06T18:40:00+02:00

| Area | Grade | Score |
|------|-------|------:|
| Security | A- | 90 |
| Docs | B | 86 |
| Automation | A- | 90 |
| Parity | A- | 93 |
| Secrets hygiene | A- | 91 |

## Checks

| Check | Result | Detail |
|-------|:------:|--------|
| `sync_board_check` | PASS | pass (exit 0, no drift; markdown/site not regenerated) |
| `progress_json_valid` | PASS | version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks |
| `codenames_no_real_repos` | PASS | 0 private real-name leaks in the working tree (37 private names, case-insensitive substring scan of all non-.git files); only known false positives: the public NEXUS-SPIRE-42 host in URL/health contexts and the GLACIER-FLARE-55 substring inside a public launcher repo name and an agent name |
| `private_map_absent` | PASS | no repo-codenames.private.json in public tree |
| `secret_scan` | PASS | No live API keys or private key blocks in public progress tree |
| `tracks_present` | PASS | 22 tracks |
| `benchmark_present` | PASS | benchmarks/latest.json present (2026-10-06 run uses codename IRON-SEAL-38 for the routine slug) |
| `history_daily` | PASS | 12 history snapshots, latest history/2026-10-06.json |
| `public_aliases` | PASS | codenames/PUBLIC_ALIASES.json present |
| `site_board` | PASS | site/index.html present; site/progress.json byte-identical to progress.json |
| `automation_scripts` | PASS | sync_board + sync_account_inventory present |
| `account_inventory_private_names` | PASS | data/account-inventory.json lists 76 public repos only; private count 59 published, privateNamesPublished=false |

## Sync board

`python3 scripts/sync_board.py --check` → **PASS** (pass)

## Leak scan

CLEAN · 0 private real names in the working tree; nothing scrubbed this run. Strings leaked before 2026-10-05 remain in git history.

## Findings

- **medium**: Strings leaked before 2026-10-05 (IRON-SEAL-38, DRIFT-DEPTH-70) still exist in public git history; removal would need a history rewrite and force-push (not done)
- **medium**: sync_board --check policy still does not scan for real private names; this audit's substring scan is the only guard
- **info**: Benchmark writer no longer emits the real routine slug: 2026-10-06 benchmark files use the codename (prior high finding resolved)
- **info**: account inventory completeAccountSync=false (public API + preserved private count)
- **info**: sync_board --check PASS; version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks

## Prior comparison

Previous overall: **89** (2026-10-05T18:38:52+02:00) → current **90** · gradeDropped=False (Secrets hygiene B+ → A-, Security B+ → A-)
