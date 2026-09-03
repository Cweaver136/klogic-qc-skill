---
name: katapult-klogic
description: Write K-Logic JSON blocks for Katapult Pro QC (quality control) checks. Use this skill whenever the user describes, in plain English, a check they want to run over a Katapult Pro entity (a Job, Node, Connection, Section, or Marker) and wants K-Logic JSON in return. Trigger on any mention of K-Logic, "KLOGIC:", the Katapult Logic Editor, QC logic/checks, or requests like "write a check that flags nodes missing X", "make a K-Logic block that returns Y", or "turn this rule into K-Logic". Always use this skill when producing, editing, or explaining K-Logic; never hand-write K-Logic from memory, because the exact block shapes, operator keys, argument indexing, and the "KLOGIC:" clipboard prefix must all be exact or the paste into Katapult Pro will fail.
---

# Katapult K-Logic (QC Checks)

Turn a plain-English description of a quality-control check into a **paste-ready K-Logic JSON block** for Katapult Pro's Logic Editor.

K-Logic is a small computation engine. A block is a tree that resolves to a single value against a data source (the entity being checked). Your job: read the user's description, build the block tree, and hand back the exact string they paste into Katapult.

## Output contract (read this first)

The thing the user pastes is **not** bare JSON. It is the literal prefix `KLOGIC:` followed by the minified JSON of the root block:

```
KLOGIC:{"return":{...},"step_01":{...},"type":"PROCEDURE","var_keys":[...]}
```

Rules for every block you emit:

- Prefix the final output with `KLOGIC:` and minify the JSON (no spaces/newlines).
- Blocks are **bare**. Never add `is_klogic_block`, ids, `description`, or other editor metadata — real clipboard payloads don't have them.
- Arguments are **1-indexed**: `arg_01`, `arg_02`, `arg_03`, … (never `arg_00`). Use contiguous keys for blocks you generate.
- Present the `KLOGIC:` string in a copyable code block, then a short plain-English explanation of what it evaluates and the data paths it depends on.

## Workflow

1. **Confirm the entity type before building anything** (Job, Node, Connection, Section, Marker). It determines the data source and every root path, so a wrong guess is expensive — the block pastes but reads the wrong thing. **The physical noun in the request is not the entity.** "If any *connection* has a wire overtop another…" names a structure that could bind to a Connection *or* a Section check, and a "*pole* is missing X" check is a Node check. When the phrasing maps cleanly to exactly one entity, state which you're using and proceed. When it could map to more than one — especially span/midspan wire checks, which are usually cleaner as **Section** than Connection (see `references/datasets/sections.md`) — name the candidates and ask the user which entity the QC should run off of before writing the tree. See `references/datasets/` — start with `nodes.md` (Node) or `sections.md` (Section). Structural paths follow the official job schema (https://katapultpro.com/schema/job.json); attribute keys and some marker fields are job/model-specific. For any entity attribute, consult the catalogs in `references/datasets/` — **do not invent or guess an attribute key or its values.** They're generated from the customer's real model (981 attributes: 524 node, 355 job, 129 photo, 51 section, 30 connection). Two tiers, so you don't load 50KB to check one key:
   - **`node-attributes.md`** — compact index of every node attribute with type markers. Use it to confirm an attribute exists and how to read it (`.*` vs. `LIST_VALUES`).
   - **`<entity>-attributes-full.md`** — picklist values and meanings. **Read this whenever a check compares an attribute against a specific value**, so the exact string is right. Available for node, connection, section, photo, job.

   If an attribute isn't in the catalog, the model has changed or it doesn't exist: ask the user the questions listed in the index, use the answers immediately, and regenerate with `scripts/build_attribute_catalog.py model_attributes.json --entity <entity> --out references/datasets/<entity>-attributes-full.md`.
2. **Decompose the check** into conditions. "Flag nodes that are complex AND missing a proposed pole spec" → two conditions joined by `AND`.
3. **Decide the return type**, then whether you need a procedure. First fix what the root should resolve to (see "Return value" below) — boolean flag, count, list, message, etc. If the check reuses an intermediate value or reads across lists, use a `PROCEDURE` with `step_NN` variables and a `return` block (the common shape for real QC checks — see `references/examples.md`). Otherwise a single expression tree is fine.
4. **Build the tree** using `references/klogic-syntax.md` for block shapes and `references/operators.md` for the operator catalog (exact `op` keys, argument counts, and list/item behavior). Build paths per `references/paths.md`.
5. **Serialize**: minify, prefix with `KLOGIC:`, and (optional, cosmetic) sort object keys alphabetically to match native output.
6. **Validate** against the checklist below before returning.

## The four block types (quick reference)

Full detail in `references/klogic-syntax.md`. In brief:

- **DATA** — `{"path":"node.attributes.done.*","type":"DATA"}`. Reads a value from the data source by dot-path. `*` = first non-null child; `$(x)` = resolve `x` then continue.
- **LITERAL** — `{"type":"LITERAL","val":"Transfer","val_type":"TEXT"}`. A constant. `val_type` ∈ TEXT, NUMBER, BOOLEAN, LIST, LOOKUP, SPECIAL.
- **EXPRESSION** — `{"op":"EQUAL","arg_01":{...},"arg_02":{...},"type":"EXPRESSION"}`. Applies an operator to ordered args. Add `"item_key":"..."` for list-looping operators.
- **PROCEDURE** — `{"type":"PROCEDURE","var_keys":["a","b"],"step_01":{...},"step_02":{...},"return":{...}}`. Runs steps top-to-bottom, binding each result to the matching name in `var_keys`; later steps and `return` read those names as bare DATA paths. Output is whatever `return` resolves to.

## Item-looping operators (the common gotcha)

Operators like `FIND`, `FILTER`, `COUNT` (Count If), `SOME`, `EVERY`, `MAP`, `REDUCE` take a **list in `arg_01`** and a **per-item expression in `arg_02`**. Inside that expression, read the current item with a DATA block whose path is the block's `item_key` (default `item`):

- `item` — the current element (rename via `"item_key":"wire"` → then read `wire`, `wire.mr_note`, …)
- `item_index`, `item_list` — index and full list (prefixed by your `item_key`)
- `item_accumulator` — running value, **`REDUCE` only**

Nested loops each get their own `item_key`; inner blocks can still read outer items by name. See the annotated real examples in `references/examples.md`.

## Photos, markers, and traces

Checks that read measured data off photos (wire heights, cable types, equipment) hit a stored marker tree with its own rules — `_children` is category-keyed, height lives on the top-level marker, ownership/type come from traces, and heights need `mr_move` + rounding. These aren't in the base schema; read `references/photofirst-markers.md` before writing any check that touches `photofirst_data`, and see Example 3 in `references/examples.md` for the full pattern.

## Return value

A K-Logic block resolves to **whatever its root block returns** — it does not have to be a boolean. The return type is just the `returnType` of the root operator (see `references/operators.md`): a comparison or existence check yields a boolean, `COUNT`/`LENGTH` a number, `FILTER`/`MAP` a list, `CONCATENATE` text, `MAKE_LOOKUP` an object, a bare `DATA` block whatever lives at that path, and so on.

So work backward from what the user wants the check to *produce*:

- A **pass/flag** result → root is a boolean expression (`AND`/`OR`/comparison/`EXISTS`…). If it's this boolean form, confirm polarity with the user — does `true` mean "flag this" or "passes"? — and say which you used. Invert with `IS_FALSE` or by negating the comparisons if needed.
- A **count** of problems → root is `COUNT` / `LENGTH`.
- The **offending items** → root is `FILTER` (or `MAP` to reshape them).
- A **message or value** → root is `CONCATENATE`, `IF_ELSE`, a `DATA` read, etc.

Match the root block's `returnType` to the type the user is asking for; don't force a boolean when they want data.

## Validation checklist

Before returning any block, verify:

- Output starts with `KLOGIC:` and the JSON is minified.
- Every block has a `type`; every EXPRESSION has an `op` that exists in `references/operators.md`.
- Argument keys are `arg_01`+ and contiguous; count matches the operator (trailing optional args may be omitted).
- Every list-looping operator has an `item_key`, and item reads inside it use that key.
- Every attribute used appears in the generated catalogs (`references/datasets/`), with its value matching an exact picklist string from the `-full` file. No invented keys or guessed values.
- Every DATA `path` is a real path for the entity type (or is a procedure variable / `item_key`). Flag any path you're not certain of.
- Procedure `var_keys` length equals the number of `step_NN` keys, in order.
- The root resolves to the type the check is supposed to return — boolean, number, list, text, lookup, etc. (match the root operator's `returnType`), not a boolean by default.

Run the block mentally against the data source, or if in doubt, offer to test it in the Logic Editor and iterate.
