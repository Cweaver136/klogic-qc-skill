# DATA paths, wildcards, and templates

How a DATA block's `path` resolves against the data source, from `Path.js` (`Path.get`) and the engine's template handling.

## Dot-delimited paths

A path is entity keys joined by periods: `node.attributes.proposed_pole_spec` walks `data.node.attributes.proposed_pole_spec`. Leading/trailing/duplicate dots are cleaned. If any segment is null/undefined along the way, the whole path returns `undefined`.

## `*` wildcard — first non-null child

`*` does **not** mean "all children". `Path.get` replaces `*` with the **first key at that level whose value is not null**, then continues.

This exists for **instance-keyed attributes**. In Katapult, an attribute stores its value under an unpredictable instance id, e.g. `node.attributes.mr_category = { "-Oabc123": "Complex Make Ready" }`. You usually don't know the instance id, so:

```json
{"path":"node.attributes.mr_category.*","type":"DATA"}
```

returns `"Complex Make Ready"` — the first (typically only) value under `mr_category`. Use `.*` as the last segment whenever you're reading a single-valued attribute whose instance key you don't know.

If an attribute can legitimately hold multiple instances and you need all of them, don't use `*` — read the attribute object itself and loop its values with `LIST_VALUES` + an item operator.

## `$(...)` templates — resolve, then continue

Before lookup, the engine expands any `$(...)` in the path by running `Path.get(data, inner)` and substituting the result. This lets you build a path from data you don't know at authoring time:

```json
{"path":"job.photos.$(main_photo_id).photofirst_data.wire","type":"DATA"}
```

Here `main_photo_id` (a top-level value like `"c2416a53-..."`) is resolved first, giving `job.photos.c2416a53-....photofirst_data.wire`. Templates can reference procedure variables and loop items too, e.g. `job.connections.$(connection.connId).sections.$(sectionKey).photos` inside loops whose `item_key`s are `connection` and `sectionKey`.

Templates and `*` combine freely in one path.

## Common Node path shapes (observed)

- `node_id` — the current node's id (top-level).
- `main_photo_id` — id of the node's main photo (top-level).
- `node.attributes.<attr>.*` — a single-valued node attribute.
- `connection_lookup` — object keyed by node id; `GET_FROM(connection_lookup, node_id)` yields this node's connections.
- `job.photos.$(main_photo_id).photofirst_data.<category>` — a keyed lookup of measured items (`wire`, `arm`, `insulator`, `midspanHeight`, …); each item carries fields like `mr_note`, `over`. Turn it into a list with `LIST_VALUES` before looping.
- `job.connections.$(connId).sections.$(sectionKey).photos.$(photoKey).association` — e.g. `"main"`.

> **`main_photo_id` / `main_photo` are not node-only.** A **Section** data source also exposes both at the top level (there `main_photo` is the section's *midspan* photo), so `job.photos.$(main_photo_id).photofirst_data.wire` reads the section's midspan wires directly — no looping over the connection's sections to find a main photo. Don't assume a convenience key belongs to one entity; check that entity's dataset file.

## Common Section path shapes (observed)

For a **Section** data source (see `datasets/sections.md` for the full top-level key list):

- `main_photo_id` — id of the section's midspan photo (top-level, same as on a node source).
- `main_photo` — the midspan photo's data (top-level; same shape as `job.photos.<id>`).
- `job.photos.$(main_photo_id).photofirst_data.<category>` — this section's midspan markers (`wire`, `arm`, …).
- `section.multi_attributes.<attr>.*` — a single-valued section attribute (instance-keyed like `node.attributes`).
- `connection` / `connection_id` — the parent connection object and its id, both top-level (no `connection_lookup` hop needed).
- `section.photos.$(photoKey).association` — e.g. `"main"`.

Treat these lists as starting points, not exhaustive — confirm unfamiliar paths against the live dataset for the entity type. See `datasets/nodes.md` (Node) and `datasets/sections.md` (Section).
