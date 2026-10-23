#!/usr/bin/env python3
"""Validate model schemas, references, sources, translations and assembled rig weights."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "catalog"
SCHEMAS = CAT / "schemas"
errors: list[str] = []


def y(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def problem(msg: str) -> None:
    errors.append(msg)


def flatten_keys(obj, parent=""):
    out = set()
    for key, val in obj.items():
        p = f"{parent}.{key}" if parent else str(key)
        if isinstance(val, dict):
            out |= flatten_keys(val, p)
        else:
            out.add(p)
    return out


def validate_json(instance, schema_file: Path, registry: Registry, label: str):
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    for issue in sorted(validator.iter_errors(instance), key=lambda e: str(e.path)):
        problem(f"{label} [{'.'.join(map(str, issue.path))}]: {issue.message}")


def main():
    paths = sorted(SCHEMAS.glob("*.schema.json"))
    resources = [(p.name, Resource.from_contents(json.loads(p.read_text(encoding="utf-8")))) for p in paths]
    registry = Registry().with_resources(resources)
    for p in paths:
        Draft202012Validator.check_schema(json.loads(p.read_text(encoding="utf-8")))

    entry = y(CAT / "index.yaml")
    types = y(CAT / entry["type_registry"])["types"]
    model_by_id: dict[str, dict] = {}
    indexed: set[str] = set()

    for typ, cfg in types.items():
        index_path = CAT / cfg["index"]
        schema_path = CAT / cfg["schema"]
        index = y(index_path)
        for path_string in index["models"]:
            p = CAT / path_string
            if not p.exists():
                problem(f"Missing indexed model: {p}")
                continue
            record = y(p)
            validate_json(record, schema_path, registry, str(p.relative_to(ROOT)))
            model_id = record.get("id", "")
            if model_id in model_by_id:
                problem(f"Duplicate model ID: {model_id}")
            model_by_id[model_id] = record
            indexed.add(str(p.relative_to(CAT)))
            if record.get("type") != typ:
                problem(f"Model type does not match index: {p}")
            if p.stem != model_id:
                problem(f"Model filename/id mismatch: {p} vs {model_id}")
            src_ids = {s.get("id") for s in record.get("sources", [])}
            if len(src_ids) != len(record.get("sources", [])):
                problem(f"Duplicate source ID in {model_id}")
            ids = set()
            for m in record.get("measurements", []):
                if m["id"] in ids:
                    problem(f"Duplicate weight measurement in {model_id}: {m['id']}")
                ids.add(m["id"])
                if m["source_id"] not in src_ids:
                    problem(f"Unresolved weight source {model_id}.{m['id']}")
                overlap = set(m.get("includes", [])) & set(m.get("excludes", []))
                if overlap:
                    problem(f"Included and excluded overlap {model_id}.{m['id']}: {overlap}")
            for pic in record.get("media", []):
                if pic.get("file"):
                    if pic.get("license") == "unverified":
                        problem(f"Cannot commit unlicensed media: {model_id}.{pic['id']}")
                    if not (ROOT / pic["file"]).is_file():
                        problem(f"Missing local image file: {pic['file']}")

    # Every imported YAML file must be in the corresponding model index.
    for typ, cfg in types.items():
        for p in (CAT / cfg["models_dir"]).glob("*.yaml"):
            if str(p.relative_to(CAT)) not in indexed:
                problem(f"Unindexed model file: {p.relative_to(ROOT)}")

    mounts = set(y(CAT / entry["vocabularies"]["mounts"])["values"])
    sensor_formats = set(y(CAT / entry["vocabularies"]["sensor_formats"])["values"])
    codecs = set(y(CAT / entry["vocabularies"]["codecs"])["values"])
    power_interfaces = set(y(CAT / entry["vocabularies"]["power_interfaces"])["values"])
    for mid, m in model_by_id.items():
        spec = m.get("specs", {})
        for k in ("mount_id", "lens_mount_id", "camera_mount_id"):
            if k in spec and spec[k] not in mounts:
                problem(f"Unknown mount {mid}: {k}={spec[k]}")
        fmt = spec.get("sensor", {}).get("format_id") or spec.get("sensor_format_id")
        if fmt and fmt not in sensor_formats:
            problem(f"Unknown sensor format {mid}: {fmt}")
        for mode in spec.get("recording_modes", []):
            if mode["codec_id"] not in codecs:
                problem(f"Unknown codec {mid}: {mode['codec_id']}")
            if mode["raw"] and mode.get("chroma_subsampling") not in (None,):
                problem(f"RAW must not carry 4:2:2/4:2:0 tag: {mid}:{mode['id']}")
            if not mode["raw"] and mode.get("chroma_subsampling") is None:
                problem(f"Non-RAW recording mode missing chroma sampling: {mid}:{mode['id']}")
        interface_ids = spec.get("battery_interface_ids", []) + spec.get("power", {}).get("native_battery_interface_ids", [])
        for interface in interface_ids:
            if interface not in power_interfaces:
                problem(f"Unknown power interface {mid}: {interface}")

    inventory = y(CAT / entry["inventory"])
    validate_json(inventory, SCHEMAS / "inventory.schema.json", registry, "inventory/items.yaml")
    instance_ids = set()
    for item in inventory.get("items", []):
        if item["instance_id"] in instance_ids:
            problem(f"Duplicate instance ID: {item['instance_id']}")
        instance_ids.add(item["instance_id"])
        if item["model_id"] not in model_by_id:
            problem(f"Unknown inventory model: {item['model_id']}")

    en = y(CAT / entry["locales"]["en"])
    ru = y(CAT / entry["locales"]["ru"])
    if en.get("locale") != "en" or ru.get("locale") != "ru":
        problem("Locale identifiers must be en and ru")
    ek, rk = flatten_keys(en["labels"]), flatten_keys(ru["labels"])
    if ek != rk:
        problem(f"Missing RU translation keys: {sorted(ek-rk)}; missing EN keys: {sorted(rk-ek)}")
    for typ in types:
        if typ not in en["labels"]["types"]:
            problem(f"No translation for type {typ}")

    relations = y(CAT / "compatibility/battery-power.yaml")["relations"]
    for e in relations:
        battery = model_by_id.get(e["battery_model_id"])
        target = model_by_id.get(e["camera_model_id"])
        if not battery or battery["type"] != "battery":
            problem(f"Unknown battery relation model: {e['battery_model_id']}")
        if not target or target["type"] != "camera":
            problem(f"Unknown camera relation model: {e['camera_model_id']}")
        if e["interface_id"] not in power_interfaces:
            problem(f"Unknown relation power interface: {e['interface_id']}")
        if battery and e["interface_id"] not in battery["specs"].get("battery_interface_ids", []):
            problem(f"Battery does not expose relation interface: {e['battery_model_id']}")
        if target and e["interface_id"] not in target["specs"].get("power", {}).get("native_battery_interface_ids", []):
            problem(f"Camera does not accept relation interface: {e['camera_model_id']}")

    for path in sorted((CAT / entry["rigs_dir"]).glob("*.yaml")):
        rig = y(path)
        validate_json(rig, SCHEMAS / "rig.schema.json", registry, str(path.relative_to(ROOT)))
        weight = 0
        payload = 0
        for c in rig["components"]:
            m = model_by_id.get(c["model_id"])
            if not m:
                problem(f"Unknown rig component: {c['model_id']}")
                continue
            matches = [v for v in m.get("measurements", []) if v["id"] == c["measurement_id"]]
            if len(matches) != 1:
                problem(f"Missing or duplicate measurement: {m['id']}.{c['measurement_id']}")
                continue
            grams = matches[0]["weight_g"] * c.get("quantity", 1)
            weight += grams
            if c["placement"] == "moving":
                payload += grams
        print(f"{rig['id']}: carried={weight:g}g, gimbal-payload={payload:g}g (physical fit NOT verified)")

    if errors:
        for line in errors:
            print("ERROR:", line, file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: {len(model_by_id)} models across {len(types)} types; EN/RU labels, inventory, sources and rigs validated.")


if __name__ == "__main__":
    main()
