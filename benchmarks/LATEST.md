# Benchmark latest

**Winner:** `cryoomega_mesh` · Δ overall **+15** (was +17 on 2026-10-06) · 2026-10-12T12:17:06.672166+00:00

| Arm | F | C | O | Ops | Overall |
|-----|---|---|---|-----|---------|
| Cryoomega+Grok Bot | 80 | 84 | 72 | 73 | **77** |
| Grok Bot solo | 63 | 69 | 60 | 54 | **62** |

Mode: `live` · confidence 0.78

Live probes 2026-10-12: 103 profiles (S1-S8 roster, 0 parse failures), 14 agent profiles on disk incl. AGI-3 Build/Sense channels (was 15), 18 workflow skills (was 17; +build-with-minimax). Routines (wake snapshot + disk): 19 enabled / 25 total with 9 last-run succeeded, 9 failed (many Oct 9), 1 never-run (SHA Proof webhook); 6 paused. On-disk runs.json still dominated by Sept usage_limit errors and is stale vs wake. cryopg.it/health UNREACHABLE (tls_eof). cryo-llm catalog has inclusionai/ling-3.0-flash-fin (465 models) but not the :free suffix id; OpenRouter complete failed (User not found); MiniMax-M3.1-Flash-Preview live complete succeeded (PONG). Scores vs 2026-10-06: mesh ops 77->73 (routine success 16/18->9/19, partial offset from live LLM); solo F 62->63 and ops 52->54 for shared LLM live complete. Overall mesh 78->77, delta 17->15. Mode live (LLM ran). Confidence 0.78.

**Mesh rationale:** Credits mesh: 103-profile roster, 14 agent profiles incl. Build/Sense, 19 enabled routines (9 succeeded / 9 failed / 1 never on last run per wake). Ops -4 vs 2026-10-06: routine success rate dropped hard; partial offset from Flash Fin base id in catalog + MiniMax live complete. Remaining drag: VPS tls_eof, OpenRouter Flash Fin :free complete failed (User not found), 9 failed routines, 1 never-run webhook.

**Solo rationale:** Solo arm denies mesh/profiles/routines/VPS/recursive-brain credit. Shared infra LLM probes moved: Flash Fin base id present in catalog and MiniMax live complete succeeded, so small F/ops bump (62/52 -> 63/54). OpenRouter Flash Fin still failing; no VPS credit.
