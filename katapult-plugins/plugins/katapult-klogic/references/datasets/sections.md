# Section dataset

The data source a **Section** QC check resolves against. Every DATA path in a Section check is
rooted at one of the top-level keys below (or a procedure variable / loop `item_key`).

A Section represents one point along a Connection (typically a midspan). Its `main_photo` is the
midspan photo, and its wire markers are the cables crossing the span at that point. **For span /
midspan wire checks — clearances, overtop/attachment order, midspan `over` callouts — the Section
entity is usually the right choice over Connection:** it hands you a single `main_photo_id` (no
looping across a connection's sections to find main photos), and the check naturally evaluates each
span point on its own. Reach for Connection only when the check is about the span as a whole
(e.g. `connection_type`) rather than the wires measured at a point.

Structural fields (`section`, `connection`, `job`, and everything under them) follow the official
job schema: https://katapultpro.com/schema/job.json. Attribute *keys* and many `photofirst_data`
fields are **job/model-specific** — see the generated catalogs in this folder. Where a path below is
job-specific rather than schema-backed, it's labeled.

## Top-level keys of the QC data source

Some keys are the schema objects themselves; others are convenience lookups the QC Logic Editor
provides (not part of the job schema). Confirmed from a real Section data source:

| key | shape | source | notes |
|---|---|---|---|
| `section` | object | schema (`job.connections.<connId>.sections.<id>`) | the current section being checked (see below) |
| `section_id` | text | QC | the current section's id |
| `main_photo` | object | QC | the section's main (midspan) photo; same shape as a `job.photos.<id>` entry |
| `main_photo_id` | text | QC | id of the section's main photo; index into `job.photos`. **This is the midspan photo** |
| `connection` | object | schema (`job.connections.<id>`) | the parent connection: `attributes`, `button`, `node_id_1`, `node_id_2`, `sections`, `_created` |
| `connection_id` | text | QC | the parent connection's id |
| `job` | object | schema | the whole job — `job.nodes`, `job.connections`, `job.photos`, `job.traces` |
| `connection_lookup` | object | QC | keyed by node id, giving that node's connections |
| `marker_lookup` | object | QC | keyed lookup of markers |
| `markers` | list | QC | markers on/near this section (5 in the sample) |
| `mr_clearances` | list | QC | make-ready clearance records |
| `model_attributes`, `model_defaults`, `input_models`, `cu_lookup`, `trace_models`, `alternate_designs_config` | object | QC | model/config lookups |

## The current section — `section`

Per schema (and confirmed in the sample), a section object has:

| path | type | notes |
|---|---|---|
| `section.latitude` | number | decimal degrees |
| `section.longitude` | number | decimal degrees |
| `section.main_photo` | object | the midspan photo's data (same shape as a `job.photos.<id>` entry) |
| `section.main_photo_id` | text | id of the midspan photo (mirrors the top-level `main_photo_id`) |
| `section.photos` | object | keyed by photo id, each `{ "association": "main" \| "manual" \| true }` |
| `section.multi_attributes` | object | instance-keyed attribute list (same shape as `node.attributes`; read single-valued ones with a trailing `.*`) |
| `section.markers` | list | markers recorded at this section |
| `section.section_id` | text | this section's id |
| `section._created` | object | `{ method, timestamp, uid }` |

Because `main_photo_id` is exposed at the top level, the section's midspan wires are simply:

```json
{"path":"job.photos.$(main_photo_id).photofirst_data.wire","type":"DATA"}
```

`LIST_VALUES` that to loop the wire markers. (You can equivalently read
`main_photo.photofirst_data.wire`.)

## `section.multi_attributes` — instance-keyed

Same shape as `node.attributes`: each attribute maps an **instance id** to a value, so read a
single-valued attribute with a trailing `.*`. Model-specific section attribute keys and picklist
values are in `section-attributes-full.md` (this folder) — confirm keys and exact value strings
there; do not guess.

## Photos & measurements — `job.photos.$(main_photo_id)`

`main_photo_id` is the usual `photo_id` for a Section check. A photo carries camera/date metadata
plus `photofirst_data.<category>` (`wire`, `insulator`, `arm`, `messenger`, `equipment`,
`pole_top`), each a keyed lookup — turn into a list with `LIST_VALUES` before looping. See
`../photofirst-markers.md` for the marker tree (`_children`), height sourcing
(`_measured_height` → `_manual_height`, `mr_move`, round), and trace reads. Model-specific marker
fields (e.g. `wire_tension` with values `Full` / `Slack`) are in `photo-attributes-full.md`.

## Traces — `job.traces`

`job.traces.trace_data.$(trace_id)` holds `{ _trace_type, cable_type, company, label }` plus
model-specific fields such as `proposed` (boolean; true = proposed, absent/false = existing). Wire
markers reference a trace via their `_trace` field, e.g.
`job.traces.trace_data.$(w._trace).cable_type`. **Where the same concept can live on either the
marker or the trace, confirm which the customer's model uses** — observed in one model:
`wire_tension` on the marker, `proposed` and `cable_type` on the trace.

## Parent connection — `connection`

The parent connection is right there at top level (no `connection_lookup` hop needed). Per schema
it has `node_id_1`, `node_id_2`, `attributes` (incl. `connection_type.*`:
`aerial cable`, `overlash`, `slack span`, `overhead guy`, `pole to pole guy`, `underground cable`,
`reference`, `down guy`, `pushbrace`), `button`, and `sections`. Read connection attributes with
`connection.attributes.<attr>.*` and confirm keys/values in `connection-attributes-full.md`.
