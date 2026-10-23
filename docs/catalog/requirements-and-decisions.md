# Equipment catalog — requirements and decisions

**Decision record date:** 2026-10-23.  
**Status:** agreed architecture; initial scaffold / partial sample data; not a complete populated catalog.  
**Existing repository:** `alexeykuropatkin/photo-and-video`.

This document preserves the discussions and product goals that preceded the structured catalog.

## Purpose

Establish one source of truth for specifications, original manufacturer references, product photography, owned gear, candidate gear, compatibility, and calculated shooting-rig weight. Both humans and AI agents should be able to find exact models and avoid repeated lookup or confusion between similar generations. Later reuse the same repository as a content source for a public bilingual equipment website.

## Accepted decisions

1. Reuse this repository; retain existing `sony.md` and `apple-iphone-pro.md` articles.
2. Prefer **YAML** for hand-authored model records, type registry, indexes, and curated facts; **JSON Schema Draft 2020-12** for structure/validation. Derived JSON and UI pages are generated, not canonical.
3. `catalog/index.yaml` is the canonical entry point for agents; `catalog/types.yaml` enumerates extensible device types.
4. Separate **product model** from **owned device instance**. Inventory may be public; do not expose serial numbers, receipts, exact whereabouts, or credentials by default.
5. Base language is **English (`en`)**, with **Russian (`ru`)** fully supported and first-class. Identifiers and enum codes are language-neutral. Internationalized labels, descriptions, and alt text are separate from machine values.
6. Initial equipment types: **camera, lens, mount adapter, gimbal, battery**; include **cage** now as a sixth scaffolded type because camera cages and their mounting geometry matter for gimbals.
7. Preserve **measurement conditions**, included/excluded accessories, firmware version where meaningful, source URL, date of verification, and source kind (manufacturer / measurement / user report).
8. Support compatibility by **specific model, function, and configuration**, not just by matching mounts. Examples: optical image circle vs recording format; electronic aperture, AF tracking, OIS, and firmware; external power topology; mechanical rig fit.
9. Store product images as small licensed WebP assets when redistribution is permitted; keep attribution/license metadata. Otherwise save an original URL and do not copy the file.
10. The website is a **future phase**, not a dependency of the catalog. Candidate domains include `filmmaking.roadblog.com`, an equipment-focused subdomain of `roadblog.com`, and `kurapatkin.com`; **no domain selected**.
11. Initial tools should be simple, file-first, Git-friendly, with no database/backend requirement. Can later generate an API/static content feed and public site.
12. Proposed default comparison filters: only `owned` equipment, while `considering`, `planned`, `sold` or external models can be explicitly included.

## Current user-provided equipment notes (not yet all normalized)

User explicitly reports owning Sony A7S III, Sony a6700, BMPCC 6K Pro, Sony FE 14/1.8 GM, 24/1.4 GM, 35/1.4 GM, 50/1.4 GM, FE 85/1.8 (not GM), Sony 16–35/2.8 GM **first generation**, 24–70/2.8 GM **first generation**, 70–200/2.8 GM **first generation**, APS-C E 10–18/4, E PZ 18–105/4, and an E PZ 16–50 pancake (exact revision to confirm). The user also reports owning Meike full-frame manual cine EF primes nominally 16, 24, 35, 50, 85, 105, 135 mm (exact models/T-stops to confirm), Canon EF 24–105 f/4L IS II USM, DJI RS 3 Pro, and DJI RS 4 Mini. Exact cage/half-cage product IDs and batteries have not yet been provided.

Prior discussion also mentions additional production gear; it must only be added to verified inventory after checking precise model/revision.

**Do not mark as owned:** Nikon ZR, Nikon Z lenses, RED V-RAPTOR XE/X, Canon C50/C80/C400, RED KOMODO-X, or other products considered for future purchases.

## Use cases to implement

- Answer “which lenses/cameras/stabilizers do I own?” without inventing versions.
- Compare bodies/lenses by native sensor format, RAW capability, 10-bit 4:2:2 modes, focus tracking, rolling/global shutter, low-light ability, stabilization, mass, dimensions, battery/power requirements, and links to official sources.
- Compute weight of camera + lens + battery + cage + mount adapter + gimbal + plates + monitor/filter as a reproducible configuration with components and measurement conditions.
- Check compatibility between mount adapters, lenses, bodies, batteries/power connectors, and gimbals; distinguish physical mount, electrical control, image circle, AF performance, and actual axis clearance.
- Serve image-backed device pages, bilingual EN/RU search/filter interfaces, side-by-side comparisons, compatible configurations, and source citations.
- Keep manufacturer claims and independent tests distinct; explicitly record uncertainty, variance and firmware dependencies.

## Deferred / open items

- Precise inventory reconciliation (variants of Sony pancake, Meike lenses, cages, all battery models).
- Actual manufacturer citations for every spec/record; product images with verified redistribution rights.
- Choice of website host/subdomain, framework, search/indexing, and public navigation.
- Future product types: tripod/head, monitor, microphone, media card, filter/ND, power plate/cable, drone, recorder, lighting.
- Whether personal ownership is exposed on the eventual public website by default (public repository does not imply publishing a personal collection view).
