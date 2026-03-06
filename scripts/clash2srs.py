#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

import yaml


def normalize_domain(value: str) -> str:
    value = value.strip().lower()
    value = value.lstrip(".")
    return value


def main(input_yaml: str, output_json: str) -> None:
    data = yaml.safe_load(Path(input_yaml).read_text(encoding="utf-8"))

    payload = data.get("payload", [])
    if not isinstance(payload, list):
        raise SystemExit("Expected YAML with key: payload: [...]")

    domain_suffix = []
    domain = []
    domain_keyword = []
    domain_regex = []

    for item in payload:
        if not isinstance(item, str):
            continue

        s = item.strip()
        if not s or s.startswith("#"):
            continue

        m = re.match(r"^(DOMAIN-SUFFIX|DOMAIN|DOMAIN-KEYWORD|DOMAIN-REGEX)\s*,\s*(.+)$", s, re.I)
        if not m:
            continue

        kind = m.group(1).upper()
        value = m.group(2).strip()

        if kind == "DOMAIN-SUFFIX":
            domain_suffix.append(normalize_domain(value))
        elif kind == "DOMAIN":
            domain.append(normalize_domain(value))
        elif kind == "DOMAIN-KEYWORD":
            domain_keyword.append(value)
        elif kind == "DOMAIN-REGEX":
            domain_regex.append(value)

    rule = {}
    if domain_suffix:
        rule["domain_suffix"] = sorted(set(domain_suffix))
    if domain:
        rule["domain"] = sorted(set(domain))
    if domain_keyword:
        rule["domain_keyword"] = sorted(set(domain_keyword))
    if domain_regex:
        rule["domain_regex"] = sorted(set(domain_regex))

    rule_set = {
        "version": 4,
        "rules": [rule],
    }

    Path(output_json).write_text(
        json.dumps(rule_set, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {output_json}")
    for key in ("domain_suffix", "domain", "domain_keyword", "domain_regex"):
        if key in rule:
            print(f"{key}: {len(rule[key])}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: clash2srs.py <input_yaml> <output_json>")
        sys.exit(2)

    main(sys.argv[1], sys.argv[2])
