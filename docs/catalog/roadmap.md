# Equipment catalog implementation roadmap

## Phase 0 — preserve design decisions (current PR)

Capture requirements, model-vs-instance distinction, public inventory choice, battery/power modeling, measurement conditions, i18n-first architecture, future website vision, photo licensing, agent rules and explicit known/unknown inventory. Create initial file-first machine-readable skeleton.

## Phase 1 — schema-first foundation

Finalize the six device schemas (`camera`, `lens`, `mount_adapter`, `gimbal`, `battery`, `cage`), shared IDs/source/measurement rules and controlled vocabularies. Introduce JSON Schema validator and tests for malformed values, unsupported enum labels, dangling refs, duplicate IDs and missing locale strings.

## Phase 2 — accurate model import

Import known equipment model-by-model using official manufacturer specs. Explicitly distinguish generations (SEL2470GM vs SEL2470GM2, Sony 16–50 I/II, Meike cine variants). Include camera recording modes and sensor-specific crops separately. Record official/independent source, date and measurement conditions. Collect **licensed** or self-shot product photos.

## Phase 3 — inventory, batteries, rigs, compatibility

Resolve user-owned physical instances, battery models, compatible interfaces, cages, adapted lenses, and representative rigs with repeatable weight/fit logic. Model native-slot power and remote battery/DC-input path separately. Produce generated accurate comparisons; test gimbal geometry in person.

## Phase 4 — outputs and bilingual site

Build deterministic JSON indices and English/Russian documentation exports. Prototype static product pages and a compare/configure UI, with canonical localized URLs and media attribution. Select a domain and hosting only after UX prototype; deployment requires an explicit decision.

## Non-goals of this initial foundation

No automatic scraping of images or specs, no public deployment, no GitHub inventory with serial numbers or receipts, no attempt to populate every desired camera/lens immediately, and no claims that a mount match proves full-function compatibility.

## Definition of done for each imported model

Valid schema and stable ID; source-backed spec values; correct generation; measurement conditions; cross-references resolved; i18n keys covered; missing/uncertain traits documented; photos licensed or remote-only; tested status explicitly declared.
