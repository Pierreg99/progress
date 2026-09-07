# DE/EN Documentation Standard — 2026-09-07

## Purpose

Provide a consistent bilingual documentation layer across the Pierreg99 repository portfolio without replacing project-specific documentation.

## Required language surfaces

For projects selected for bilingual expansion:

- `README.md` — canonical project overview; both languages may be linked here.
- `README.de.md` — German project guide.
- `README.en.md` — English project guide.
- `CHANGELOG.md` — canonical release/change index.
- `CHANGELOG.de.md` / `CHANGELOG.en.md` — optional when the changelog is substantial.
- `PROGRESS.md` — evidence-based status.
- `PROGRESS.de.md` / `PROGRESS.en.md` — optional language views for substantial projects.

## Existing documentation preservation

Do not delete or rewrite existing `CHANGES.md`, `HISTORY.md`, `ROADMAP.md`, `PLAN.md`, agent instructions, release notes, or domain-specific documents merely to match this standard.

## Translation policy

Translated files must describe only information supported by the repository. Do not add unverified features, deployment claims, test claims, completion percentages, or security guarantees.

## Current rollout

Bilingual README companions have been added to:

- `Cryo-Card-V2-Cardgame`
- `CryoMediaPro-MediaSuite`
- `CryoPCBuilderSuite`

The broader portfolio audit identifies further candidates for language expansion without fabricating absent evidence.

## Progress semantics

Use labels such as `verified`, `present`, `partial`, `blocked`, and `needs verification`. Percentages are allowed only where generated from explicit repository evidence or an existing authoritative progress system.
