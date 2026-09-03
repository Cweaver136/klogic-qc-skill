# Node dataset

The data source a **Node** QC check resolves against. Every DATA path in a Node check is rooted at one of the top-level keys below (or a procedure variable / loop `item_key`).

Structural fields (`node`, `job`, and everything under them) follow the official job schema: https://katapultpro.com/schema/job.json. Attribute *keys* and many `photofirst_data` fields are **job/model-specific** — the schema documents the common ones and states that customizable properties beyond them exist. Where a path below is job-specific rather than schema-backed, it's labeled. When you need an attribute key that isn't listed, ask the user for the exact key as it appears in their job.

## Top-level keys of the QC data source

Some keys are the schema objects themselves; others are convenience lookups the QC Logic Editor provides (not part of the job schema).

| key | shape | source | notes |
|---|---|---|---|
| `node` | object | schema (`job.nodes.<id>`) | the current node being checked (see below) |
| `node_id` | text | QC | the current node's id |
| `job` | object | schema | the whole job — `job.nodes`, `job.connections`, `job.photos`, `job.traces` |
| `main_photo_id` | text | QC | id of the node's main photo; index into `job.photos` |
| `main_photo` | object | QC | the main photo's data (same shape as a `job.photos.<id>` entry) |
| `connection_lookup` | object | QC | keyed by node id, giving that node's connections; read with `GET_FROM(connection_lookup, node_id)` |
| `marker_lookup` | object | QC | keyed lookup of markers |
| `markers` | list | QC | markers on/near the node |
| `mr_clearances` | list | QC | make-ready clearance records |
| `model_attributes`, `model_defaults`, `input_models`, `trace_models`, `cu_lookup`, `alternate_designs_config` | object | QC | model/config lookups |

## The current node — `node`

Per schema, a node object has:

| path | type | notes |
|---|---|---|
| `node.attributes` | object | instance-keyed attribute list (see below) |
| `node.latitude` | number | decimal degrees |
| `node.longitude` | number | decimal degrees |
| `node.button` | text | id of the button that created the node |
| `node.photos` | object | keyed by photo id holds `{ "association": "main" | "manual" | true }` |

## `node.attributes` — instance-keyed

Every attribute is an object mapping an **instance id** to a value, so read a single-valued attribute with a trailing `.*` (grabs the first/only value; see `paths.md`).

Schema-documented attribute:

- `node.attributes.node_type.*` returns one of: `existing anchor`, `new anchor`, `slack loop`, `splice`, `pole`, `building attachment`, `bridge attachment`, `crossover`, `reference`, `pushbrace`, `doublewood pole`, `midspan takeoff`, `break point`, `handhole`, `manhole`, `obstacle`, `map note`.

Job-specific attributes are catalogued in generated files (same folder), built from the customer's real model: **`node-attributes.md`** (compact index of all 524 node attributes) and **`node-attributes-full.md`** (picklist values + meanings). Consult the index to confirm a key, the full file to get an exact value string. Sibling `-full` catalogs exist for connection, section, photo, and job. A few examples (from real checks):

- `node.attributes.mr_category.*` — e.g. `Medium Make Ready`, `Complex Make Ready`
- `node.attributes.customer_directive.*` — e.g. `Deselected by Applicant`
- `node.attributes.proposed_pole_spec` — presence/absence is meaningful (used with `EXISTS` / `NOT_EXISTS`)

An attribute can legitimately hold multiple instances. If you need all values rather than the first, read the attribute object and loop it with `LIST_VALUES` + an item operator instead of `*`.

## Photos & measurements — `job.photos.$(photo_id)`

`main_photo_id` is the usual `photo_id` for a node check; use it in a template: `job.photos.$(main_photo_id)....` A photo has camera/date metadata plus:

### `photofirst_data.<category>`

Measured markers grouped by category, each a **keyed lookup** (turn into a list with `LIST_VALUES` before looping). Categories and their schema fields:

| category | schema fields |
|---|---|
| `wire` | `_trace`, `_measured_height`, `_manual_height`, `wire_spec`, `pixel_selection` |
| `messenger` | `_children`, `_measured_height`, `_manual_height`, `messenger_spec`, `pixel_selection` |
| `insulator` | `_children`, `_measured_height`, `_manual_height`, `insulator_spec`, `pixel_selection`, `bearing` |
| `arm` | `_children`, `_measured_height`, `_manual_height`, `arm_spec`, `pixel_selection`, `bearing` |
| `pole_top` | `_measured_height`, `_manual_height`, `pixel_selection`, `pole_top_extension` (boolean) |
| `equipment` | object of equipment markers |

Job-specific marker fields seen in real checks (not in the base schema; per model): `mr_note` (e.g. `Transfer`), `over` (e.g. `Railroad`), and custom categories like `midspanHeight`.

**Height pattern:** heights are in decimal inches. Use `_measured_height`, falling back to `_manual_height` when it's absent — a `FALLBACK` expression over the two.

## Connections & sections (reached from a node)

`connection_lookup` gives this node's connections. Per schema, `job.connections.$(conn_id)` has `node_id_1`, `node_id_2`, `attributes` (incl. `connection_type.*` enum: `aerial cable`, `overlash`, `slack span`, `overhead guy`, `pole to pole guy`, `underground cable`, `reference`, `down guy`, `pushbrace`), and `sections`. A section (`...sections.$(section_key)`) has `latitude`, `longitude`, `multi_attributes` (same instance-keyed shape as node attributes), and `photos` (keyed by photo id, each `{ association }`). Find a section's main photo by the photo whose `association` equals `"main"`.

## Traces — `job.traces`

`job.traces.trace_data.$(trace_id)` holds `{ _trace_type, cable_type, company, label }`. Photo markers reference a trace via their `_trace` field. `job.traces.trace_items` is the reverse lookup (trace to photos).

## Other entity types

Connections, Sections, Markers, and Job each expose their own QC data source. When the user asks for a check on one, gather that entity's top-level keys the same way and add a sibling file here. The schema above already covers the `job.connections` / `sections` / `traces` structure those checks will read.
