# Changelog

## 0.1.0

Initial packaging of the katapult-klogic skill as a Claude Code plugin, plus reference updates:

- **New** `references/datasets/sections.md` — Section QC data source (top-level keys incl. `main_photo_id`, `section`, `connection`; how to reach midspan wires).
- **SKILL.md** — workflow step 1 now requires confirming the entity type before building, since the physical noun in a request doesn't determine the QC entity.
- **references/paths.md** — added Section path shapes and a note that `main_photo_id` / `main_photo` are top-level on Section sources, not node-only.
- **references/photofirst-markers.md** — added "wire tension absence = full" rule (`NOT_EQUAL(...,"Slack")`, never `EQUAL(...,"Full")`); generalized to missing optional fields.
- **references/datasets/photo-attributes-full.md** — annotated the `wire_tension` row with the absence-means-full semantics and marker-not-trace location.
- **references/examples.md** — added Example 4: proposed slack comm cable overtop an existing full-tension comm cable, as a Section check (entity choice + marker-vs-trace split + absence-means-full).
