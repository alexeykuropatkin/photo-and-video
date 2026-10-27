# Instructions for agents

This repository contains technical documentation and a structured photography/cinema equipment catalog.

## Entry point and read order

1. Read `catalog/index.yaml`.
2. Resolve a category through `catalog/types.yaml` and its JSON Schema.
3. Read only the relevant model index and model files.
4. For ownership claims, read `catalog/inventory/items.yaml` and `docs/catalog/inventory-source-notes.md`.
5. For rig comparisons, read `docs/catalog/measurements-and-rigs.md` and the rig configuration.
6. Verify any disputed, missing, firmware-dependent, or fast-changing values against a cited manufacturer source.

## Invariants

- Never infer that a product is owned merely because it was discussed, recommended, searched for, or compared.
- Do not substitute product generations. In particular, the user's Sony 24–70/2.8 GM is **SEL2470GM generation 1**, not SEL2470GM2 or Sony Zeiss 24–70/4.
- Distinguish the mass of a bare body, an operational camera with battery/card, a bare gimbal, and a gimbal with grip and QR plates. Never count an already included battery or plate twice.
- A nominal mount match does not prove autofocus performance, electronic functions, lens coverage, or physical gimbal fit.
- Unknown values stay absent/unknown; do not set `false` unless absence is confirmed.
- RAW bit depth is not chroma subsampling; RAW is not 4:2:2.
- Use stable English-language identifiers and SI units. Translate labels/descriptions, never IDs.
- Store claims with provenance and verification date where possible; label calculations and user recollections distinctly from official published specifications.
- Do not scrape/copy product photos into the repository without verified redistribution rights. External references may be kept with copyright/license metadata.
- The planned web domain is **not decided**. Do not deploy or create DNS without explicit approval.
- The documentation in `sony.md` and `apple-iphone-pro.md` must remain intact unless explicitly editing those documents.

## Working practices

Work directly on `main`, as requested by the repository owner. Do not create additional branches or pull requests unless explicitly requested. Run catalog validation, keep schemas and indexes in sync, and update the architectural docs when a design decision changes.
