#!/usr/bin/env python3
"""
Build the node attribute catalog from a Katapult model_attributes export.

Usage:
    python build_attribute_catalog.py model_attributes.json [--entity node] [--out node-attributes.md]

Input: the `model_attributes` object (top-level in any QC data source, or exported
from the Model Editor / v3 `models` API). It's a map of attribute_name -> definition.

Output: a Markdown catalog for the chosen entity type (default: node), grouped by the
model's own `grouping`, with each attribute's read type, single/multi instance, picklist
values, and a human-readable meaning. Drop this in references/datasets/ and repackage.

Nothing here is Katapult-specific beyond the field names below, so it also works for
connection / section / photo / job by passing --entity.
"""

import argparse
import json
import sys
from collections import defaultdict

# gui_element -> how a K-Logic check should treat the value
TYPE_MAP = {
    "dropdown": "text (picklist)",
    "multi_dropdown": "list (picklist, multi)",
    "checkbox": "boolean",
    "textbox": "text",
    "textbox_commit": "text",
    "textarea": "text",
    "date": "text (date)",
    "file": "file",
    "link": "text (url)",
    "table": "object (table)",
    "group": "object (group)",
    "object": "object",
}

# Picklists this large aren't worth inlining into the catalog; a check rarely compares
# against the full set, and it bloats the reference. We note the count instead.
MAX_VALUES_INLINE = 40


def collect_values(defn):
    """Pull every picklist `value` out of an attribute definition, however it's shaped."""
    values = []

    def add(v):
        if isinstance(v, (str, int, float)) and v != "":
            values.append(str(v))

    # picklists: { <listname>: [ {value: ...} | "literal" , ... ], ... }
    picklists = defn.get("picklists")
    if isinstance(picklists, dict):
        for lst in picklists.values():
            if isinstance(lst, list):
                for item in lst:
                    if isinstance(item, dict):
                        add(item.get("value"))
                    else:
                        add(item)

    # picklist: [ {value: ...} | "literal", ... ]   (e.g. the `over` attribute)
    pl = defn.get("picklist")
    if isinstance(pl, list):
        for item in pl:
            add(item.get("value") if isinstance(item, dict) else item)

    # properties: [ { picklist: [ {value}... ] }, ... ]   (e.g. PLA)
    for prop in defn.get("properties", []) or []:
        if isinstance(prop, dict) and isinstance(prop.get("picklist"), list):
            for item in prop["picklist"]:
                add(item.get("value") if isinstance(item, dict) else item)

    # de-dupe, preserve order
    seen = set()
    out = []
    for v in values:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out


def meaning(defn):
    return (defn.get("label") or defn.get("placeholder") or defn.get("help_text") or "").strip()


def instances(defn):
    if defn.get("gui_element") == "multi_dropdown" or defn.get("allow_duplicates"):
        return "multi"
    return "single"


def read_path(entity, key):
    # Table/group attributes hold sub-attributes rather than a single value; flag that.
    return f"{entity}.attributes.{key}.*"


def build(model, entity):
    rows_by_group = defaultdict(list)
    for key, defn in sorted(model.items()):
        if not isinstance(defn, dict):
            continue
        if entity not in (defn.get("attribute_types") or []):
            continue
        gui = defn.get("gui_element", "")
        typ = TYPE_MAP.get(gui, gui or "unknown")
        vals = collect_values(defn)
        if len(vals) > MAX_VALUES_INLINE:
            vals_str = f"_{len(vals)} options — large picklist, pull from model if needed_"
        elif vals:
            vals_str = ", ".join(f"`{v}`" for v in vals)
        else:
            vals_str = "—"
        group = defn.get("grouping", "Ungrouped")
        rows_by_group[group].append(
            (key, typ, instances(defn), vals_str, meaning(defn) or "—")
        )
    return rows_by_group


def render(rows_by_group, entity):
    lines = [
        f"# {entity.capitalize()} attribute catalog (generated)",
        "",
        f"Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.",
        f"Source of truth for model-specific `{entity}` attributes. Read single-valued attributes with a",
        "trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item",
        "operator. Table/group attributes hold sub-attributes, not a single value.",
        "",
        "If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export.",
        "",
    ]
    for group in sorted(rows_by_group):
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| key | type | instances | values | meaning |")
        lines.append("|---|---|---|---|---|")
        for key, typ, inst, vals, mean in sorted(rows_by_group[group]):
            mean = mean.replace("|", "\\|")
            lines.append(f"| `{key}` | {typ} | {inst} | {vals} | {mean} |")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_attributes", help="Path to model_attributes.json")
    ap.add_argument("--entity", default="node",
                    help="Entity type to catalog: node, connection, section, photo, job")
    ap.add_argument("--out", default=None, help="Output .md path (default: stdout)")
    args = ap.parse_args()

    with open(args.model_attributes) as f:
        model = json.load(f)

    rows = build(model, args.entity)
    total = sum(len(v) for v in rows.values())
    md = render(rows, args.entity)

    if args.out:
        with open(args.out, "w") as f:
            f.write(md)
        print(f"Wrote {total} {args.entity} attributes across {len(rows)} groups to {args.out}",
              file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
