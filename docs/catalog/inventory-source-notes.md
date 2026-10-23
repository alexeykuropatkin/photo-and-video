# Original inventory claims and normalization backlog

This is an **intake note** reflecting equipment reported directly in conversations (not a manufacturer-audited specification list). Before importing a particular device, confirm its precise SKU/revision and manufacturer specs. Treat discussed RED, Nikon and Canon candidates as **not owned**.

## Cameras / stabilization

Reported owned: Sony α7S III, Sony α6700, Blackmagic Pocket Cinema Camera 6K Pro, DJI RS 3 Pro, DJI RS 4 Mini. DJI RS 5, Nikon ZR, RED V-RAPTOR XE, Canon C50/C80/C400 and similar gear are only candidates unless explicitly confirmed later.

## Sony lenses

Full-frame primes reported owned: Sony FE 14mm f/1.8 GM, 24mm f/1.4 GM, 35mm f/1.4 GM, 50mm f/1.4 GM, 85mm f/1.8 (not GM).

Full-frame zooms reported owned: Sony FE 16–35mm f/2.8 GM **I**, FE 24–70mm f/2.8 GM **I / SEL2470GM**, FE 70–200mm f/2.8 GM **I**.

APS-C reported owned: Sony E 10–18mm f/4, E PZ 18–105mm f/4, E PZ 16–50mm pancake. **Do not assume exact generation of the 16–50 until verified.**

An earlier comparison incorrectly attributed a 24–70mm f/4 ZA to the user; the user explicitly corrected this. Never import it as owned.

## Manual and EF cine/photo lenses

Reported owned: Meike FF Cine EF primes at nominal 16, 24, 35, 50, 85, 105, 135 mm. T-stop recollections may be approximate; check each SKU and whether every optic is the same full-frame series. User also reports Canon EF 24–105mm f/4L IS II USM.

## Pending detail capture

Cage/half-cage model/SKU, actual battery makes/models/quantities, monitor, power plates/cables, exact gimbal accessory configurations, exact model revisions, date of purchase and optional serial numbers. Do not fabricate details.

## Migration procedure

Import only unambiguous model IDs first, with `owned` instance records where model is unambiguous. Retain the rest as unresolved intake notes. Once reconciled, migrate them to `catalog/models/` and `catalog/inventory/items.yaml`. Never propagate approximate user recollections to canonical manufacturer specification fields without corroboration.
