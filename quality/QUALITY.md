# Quality audits

**Overall score: 89/100** · 2026-10-05T18:38:52+02:00

| Area | Grade | Score |
|------|-------|------:|
| Security | B+ | 89 |
| Docs | B | 86 |
| Automation | A- | 90 |
| Parity | A- | 93 |
| Secrets hygiene | B+ | 88 |

## Checks

| Check | Result | Detail |
|-------|:------:|--------|
| `sync_board_check` | PASS | pass (before and after scrub) |
| `progress_json_valid` | PASS | version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks |
| `codenames_no_real_repos` | FAIL | 2 private real-name leaks found (IRON-SEAL-38 in a paused-routine slug in today's benchmark files; DRIFT-DEPTH-70 in the 2026-09-23 dated audit) and scrubbed this run; content paths clean after scrub |
| `private_map_absent` | PASS | no repo-codenames.private.json in public tree |
| `secret_scan` | PASS | No live API keys in public progress tree |
| `tracks_present` | PASS | 22 tracks |
| `benchmark_present` | PASS | benchmarks/latest.json present |
| `history_daily` | PASS | 11 history snapshots |
| `public_aliases` | PASS | codenames/PUBLIC_ALIASES.json present |
| `site_board` | PASS | site/index.html present |
| `automation_scripts` | PASS | sync_board + sync_account_inventory present |

## Sync board

`python3 scripts/sync_board.py --check` → **PASS** (pass)

## Leak scan

LEAKS FOUND AND SCRUBBED · 3 paths · 2 private names (shown as codenames: IRON-SEAL-38, DRIFT-DEPTH-70). Leaked strings remain in git history.

## Findings

- **high**: Benchmark routine wrote a real private-repo routine slug into benchmarks/latest.json and benchmarks/history/2026-10-05.json; scrubbed, but the writer will reintroduce it unless it maps routine slugs to codenames
- **medium**: Dated audit 2026-09-23 contained the DRIFT-DEPTH-70 real name since 2026-09-23; earlier scans missed it; scrubbed
- **medium**: sync_board --check passed despite both leaks: its policy check does not catch these strings
- **medium**: Leaked strings still exist in public git history; removal would need a history rewrite and force-push (not done)
- **info**: Audit run of 2026-10-02 failed; no audits 2026-09-30 to 2026-10-02
- **info**: sync_board --check PASS; version=3 overall=96 mean=95.73 tracks=22 (rounding=round(mean)); required id/name/percent/status present on all tracks; codename present on all 12 codenamed (private) tracks

## Prior comparison

Previous overall: **91** (2026-09-29T18:42:28+02:00) → current **89** · gradeDropped=True (Secrets hygiene A → B+)
