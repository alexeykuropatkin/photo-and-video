#!/usr/bin/env python3
"""Produce a deterministic localized JSON view for future static sites."""
import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "catalog"


def read_yml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--locale", choices=("en", "ru"), default="en")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    cfg = read_yml(CAT / "index.yaml")
    registry = read_yml(CAT / cfg["type_registry"])["types"]
    models = []
    for kind in sorted(registry):
        idx = read_yml(CAT / registry[kind]["index"])
        for rel in idx["models"]:
            models.append(read_yml(CAT / rel))
    models.sort(key=lambda x: x["id"])
    labels = read_yml(CAT / cfg["locales"][args.locale])["labels"]
    exported = {
        "catalog_version": cfg["catalog_version"],
        "locale": args.locale,
        "labels": labels,
        "models": models,
    }
    output = ROOT / args.out
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(exported, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{output}: {len(models)} models")


if __name__ == "__main__":
    main()
