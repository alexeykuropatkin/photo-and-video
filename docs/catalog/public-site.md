# Potential public equipment catalog website — product vision

**Status: proposed, no domain or stack selected.** Candidate locations: `filmmaking.roadblog.com`, an equipment-specific subdomain of `roadblog.com` (e.g. `gear.roadblog.com`), or `kurapatkin.com`. Naming and DNS are intentionally undecided. The catalog repository remains the source of truth whichever domain is chosen.

## Audience and scope

Public EN/RU reference for photographers, cinematographers, travel filmmakers and small crews. Capabilities:

- Browse device pages with licensed photographs, first-party specifications and citations.
- Filter cameras by sensor size, 6K/8K, RAW codec, bit depth, in-camera recording, shutter type, frame-rate/mode, AF tracking; filter lenses by coverage/image circle, focal length, f/T aperture, thread size, internal zoom and weight.
- Compare two or more bodies/lenses/gimbals side by side, with clearly identified measurement conditions.
- Compose a rig, add camera, lens, adapter, cage, battery, gimbal, plates, monitor/ND, calculate carried mass and moving-axis payload separately; distinguish estimated vs tested fit.
- Trace lens/sensor coverage, adapter mechanics/electronics, power interfaces and compatibility confidence; show unknowns rather than invented approval.
- Per-locale search aliases, descriptions, labels, formatting, shareable comparison URLs.
- Optional personal `owned` inventory view; repository publicness does not imply that the consumer UI needs to highlight personal ownership.

## Architecture direction

Start with **static-site generation** from validated YAML, a deterministic JSON export and localized UI. No database or account backend required until there is a demonstrated use case. A later API can consume the same versioned normalized catalog. Avoid embedding product specs directly in UI code; schema is the contract.

## Quality attributes

Fast mobile UX and simple navigation, reproducible builds, source transparency, SEO per locale, image licensing, accessibility, cacheable static assets, deterministic comparison algorithms, and clear unknown/untested states.
