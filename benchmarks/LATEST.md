# Benchmark latest

**Winner:** `cryoomega_mesh` · Δ overall **+17** (was +17 on 2026-10-05) · 2026-10-06T12:19:51.216095+00:00

| Arm | F | C | O | Ops | Overall |
|-----|---|---|---|-----|---------|
| Cryoomega+Grok Bot | 80 | 84 | 72 | 77 | **78** |
| Grok Bot solo | 62 | 69 | 60 | 52 | **61** |

Mode: `live_structural` · confidence 0.72

Live structural probes 2026-10-06: 103 profiles (S1-S8 roster, 0 parse failures), 15 agent profiles on disk incl. AGI-3 Build/Sense channels, 17 skills, 18/24 routines enabled with 16 of 18 succeeding on last run (1 failed: weekly limit reminder 2026-09-30; 1 never run: SHA Proof webhook). cryopg.it/health UNREACHABLE (connect timeout from box). cryo-llm default inclusionai/ling-3.0-flash-fin:free still absent from the 464-model catalog (refreshed 2026-10-06) and no OpenRouter key is present on the box, so no live completion and no LLM score. Scores vs 2026-10-05: mesh ops 74->77 for routine recovery; all other dims unchanged. Overall = rounded mean of F/C/O/ops; mesh 78.25 rounds to 78, so overall and delta are unchanged. Confidence 0.72 (LLM probe could not be attempted).

**Mesh rationale:** Credits mesh: 103-profile roster, 15 agent profiles incl. Build/Sense channels, 18 enabled routines with 16 succeeding on their last run (up from 8). Ops +3 vs 2026-10-05 for recovered routine runs; remaining drag: 1 failed routine (weekly limit reminder), 1 never-run webhook routine, VPS health unreachable, Flash Fin free default missing from catalog, no LLM key on box.

**Solo rationale:** Solo arm denies mesh/profiles/routines/VPS/recursive-brain credit, so the routine recovery does not move it. No Flash Fin credit (default absent from catalog) and no live completion (no OpenRouter key on box). Unchanged vs 2026-10-05.
