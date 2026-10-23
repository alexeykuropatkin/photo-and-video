# Machine-readable equipment catalog

Read `index.yaml` first. Paths in model indexes and `types.yaml` are relative to this `catalog/` directory (not the index's own subdirectory). All model specification files are validated against a type-specific JSON Schema. Inventory and rigs reference model IDs; battery power compatibility is expressed as a separate directed relation.

### Quick start

```bash
python -m pip install -r scripts/requirements-catalog.txt
python scripts/validate_catalog.py
python scripts/export_catalog.py --locale en --out generated/catalog.en.json
python scripts/export_catalog.py --locale ru --out generated/catalog.ru.json
```

The sample rig should calculate 3100 grams (A7S III + owned GM first-gen 24–70/2.8 + RS 3 Pro without tripod). This is **not** proof of physical fit. `generated/` can be created in a build; it is not the editable source of truth.

Device type source: `types.yaml`; label translations: `locales/en.yaml`, `locales/ru.yaml`; provenance/ownership rules and roadmap: `../docs/catalog/`.
