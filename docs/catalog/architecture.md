# Catalog architecture

## Scope and layers

The source of truth is a Git-tracked, typed **file catalog**. `index.yaml` resolves types to JSON Schemas and indexes. Every model is stored in a separate YAML record. Sources, claims and measurements are traceable. Locales provide translated display content. Inventory records refer to model IDs; compatibility edges refer to model IDs or interface standards. Rigs compose instances/models without copying manufacturer specs.

```text
catalog/index.yaml
  -> catalog/types.yaml -> catalog/schemas/*.schema.json
  -> catalog/indexes/*.yaml -> catalog/models/<type>/<id>.yaml
  -> catalog/locales/{en,ru}.yaml
  -> catalog/inventory/items.yaml
  -> catalog/compatibility/*
  -> catalog/rigs/*
assets/<type>/<model-id>/*
docs/catalog/*
```

## Model vs instance vs assembly

- **Model:** manufacturer, SKU, design specifications, measured weights with conditions, supported feature/mode matrices, public documentation, reference photos. Stable `id` independent of localization.
- **Instance:** actual physical item, `model_id`, ownership status and user-confirmation evidence, optional firmware/condition; never copy the model spec. Multiple instances of the same model are legal.
- **Rig:** references exact model or instance IDs and their selected **weight measurement**. Optionally attaches extras; a later evaluation derives the total weight, payload (moving gimbal assembly), and operator-carried weight.
- **Compatibility:** directed/typed relation with separately stated mechanical/electrical/optical/software constraints, test status, firmware, source and optionally recording mode.

## Canonical modeling rules

- Stable IDs use lowercase ASCII kebab-case; no locale in IDs. Keep SKU and variant/generation explicit.
- SI units as numeric values with unit in field names: `weight_g`, `capacity_wh`, `voltage_v`, `width_mm`, `focal_length_min_mm`; no quantities embedded in prose-only strings.
- Use controlled vocabularies for mount, sensor format, power interface, codec, connector and ownership state.
- Avoid universal single-number spec for properties that depend on mode: FPS, bit rate, sensor crop, RAW codec, DR, rolling-shutter readout, AF modes, firmware-dependent functionality.
- Missing/unknown is not `false`; explicit no-feature is `false`. `null` only where schema allows an explicitly unknown state; otherwise omit optional fields and track incomplete status.
- For a specification with inconsistent sources, retain separate attributed observations/measurements; never silently overwrite independent measurement with manufacturer marketing.
- Model metadata can reference many images and source pages; translation strings are not duplicated in specification files.
- Never auto-migrate from `considering` to `owned`; ownership is a separate user-confirmed event.
- External references/images should be stable and lawfully usable; build tools should degrade gracefully when media is unavailable.

## Extensibility

Currently scaffold six types: `camera`, `lens`, `mount_adapter`, `gimbal`, `battery`, `cage`. Add a new type with a schema, type registry entry, collection index, localization labels and tests. Avoid a massive generic object whose meaning depends on free-text fields.

## Battery and power as first-class models

Separate an individual **battery model** (chemistry, Wh, mAh, nominal voltage, voltage range, dimensions, weight, contacts/connector, max continuous power/current) from **camera/gimbal power interface** (slot vs DC input, accepted voltage, connector, draw W) and **connection path** (direct insertion, plate, regulated DC cable, USB-C PD). Compatibility must describe the entire path and electrical constraints, not just a common V-Mount label. Adapter, cable and plate may become separate model types as the catalog expands.

## Rig mass calculation

The computed weight of a rig is the sum of non-overlapping selected physical assemblies. Example: if a camera's operational measured weight already includes its installed NP-FZ100 battery and memory card, do not add the battery and card again. Gimbal “with grip + QR plates, without tripod” must not be mixed with “head only”. Record each measurement's includes/excludes and give the calculation a breakdown. Payload is separate from entire operator-carried weight; a battery/monitor on a fixed handle counts for carried weight but not gimbal motor payload.

Use actual source-backed individual battery weights where available. When unavailable, do not infer body-only mass by subtraction from incompatible configurations.

## Source provenance

Source classes: `manufacturer`, `independent_test`, `user_report`, `calculated`. Suggested evidence levels: `confirmed`, `reported`, `unverified`. URLs and `verified_at` dates are required when claims are taken from external specs. Generated comparison pages should expose a source link and last-verified date, not obscure them in the backend.

## Maintainability

Source YAML is human-authored; JSON builds, comparison tables, indexes and website assets are derived and regenerable. Enforce deterministic ordering, unique IDs, schema validation, no dangling model refs, locale key coverage, and image-license checks in CI. Keep original articles in the repository and link them from model references without rewriting them.
