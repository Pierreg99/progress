# Benchmark latest

**Winner:** `cryoomega_mesh` · Δ overall **+17** (was +18 on 2026-09-29) · 2026-10-05T12:21:43.715378+00:00

| Arm | F | C | O | Ops | Overall |
|-----|---|---|---|-----|---------|
| Cryoomega+Grok Bot | 80 | 84 | 72 | 74 | **78** |
| Grok Bot solo | 62 | 69 | 60 | 52 | **61** |

Mode: `live_structural` · confidence 0.74

Live structural probes 2026-10-05: 103 profiles (S1-S8 roster, 0 parse failures), 15 agent profiles on disk incl. AGI-3 Build/Sense channels, 18/24 routines enabled but only 8 of the 18 enabled had a succeeded last run (9 failed, mostly 2026-10-02; 1 never run). cryopg.it/health UNREACHABLE (TLS wrong version number from box). cryo-llm default inclusionai/ling-3.0-flash-fin:free is absent from the 466-model catalog and live OpenRouter completion failed (user_not_found), so no LLM score. Scores vs 2026-09-29: both arms F and ops -2 for stale Flash Fin default; mesh ops a further -4 for routine last-run failures; C/O unchanged (no new probe evidence). Overall = rounded mean of F/C/O/ops. Confidence lowered to 0.74.
