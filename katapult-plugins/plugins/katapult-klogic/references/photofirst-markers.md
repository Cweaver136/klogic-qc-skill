# Photos, markers, and traces (`photofirst_data`)

How measured markers are stored on a photo and read in a check. This is model/behavior knowledge that the base schema doesn't spell out — get it wrong and a check pastes fine but reads the wrong thing.

## Marker categories

Under `job.photos.$(photo_id).photofirst_data`, markers are grouped by category, each a **keyed lookup** `{ markerId: marker }`: `wire`, `insulator`, `arm`, `messenger`, `equipment`, `pole_top`. Turn a category into a list with `LIST_VALUES(...)` before looping. `main_photo_id` is the usual photo for a node check: `job.photos.$(main_photo_id).photofirst_data.wire`.

## Nesting — `_children` is category-keyed, not a flat list

Markers form a tree. A marker's `_children` is structured **exactly like `photofirst_data`** — keyed by category:

- `insulator._children.wire.<id>`
- `arm._children.insulator.<id>`, `arm._children.wire.<id>`
- messengers can hold wires: `messenger._children.wire.<id>`

So wires nested in an insulator are `LIST_VALUES(insulator._children.wire)`. **Never** `LIST_VALUES(marker._children)` — that returns the category objects (`wire`, `insulator`, …), not the markers.

Observed stacks: a wire can be top-level, nested in an insulator, nested in an arm's insulator (`arm._children.insulator.*._children.wire`), or directly on an arm.

## Height lives on the TOP-LEVEL marker

Only the top-level `photofirst_data` marker carries a height. Nested children have `_exists` and `_trace` but **no `_measured_height` of their own** — the whole stack shares the top-level marker's height, because it's one physical attachment point. (Confirmed: a top-level insulator carries its own height; an insulator nested in an arm does not — the arm carries it.)

Consequence: to get a nested marker's height, use its **top-level ancestor's** height. In practice, iterate the top-level markers, decide relevance by inspecting their nested wires (via `SOME` over `_children.wire`), and read the height off the top-level marker.

### Height formula

```
ROUND( SUM( FALLBACK(marker._measured_height, marker._manual_height),
            FALLBACK(marker.mr_move, 0) ),
       0 )
```

- `_measured_height` preferred; `_manual_height` is the fallback.
- add `mr_move` (inches the marker is moved; default 0 when absent).
- **round** — heights are stored with many decimals; specs and annotations use whole inches.

## Traces — company & cable type

A marker references a trace by `_trace`. Resolve it at `job.traces.trace_data.$(marker._trace)`:

- `.company` — the owner. **Company is always on the trace.** Compare against the literal value stored there (e.g. `PPL Company`).
- `.cable_type` — e.g. `Primary`, `Neutral`, `Secondary`, `Open Secondary`, `Service`, `Power Guy`, …

Equipment markers carry `equipment_type` **on the marker** (e.g. `riser` — lowercase, per the photo attribute catalog); their company is still on the trace.

## Wire tension — absence means full

`wire_tension` lives **on the wire marker** (`<wire>.wire_tension`), not the trace, with picklist `Full` / `Slack`. Only `Slack` is reliably set: a full-tension wire may carry `Full`, an empty value, or **no `wire_tension` attribute at all**. So test tension by its complement, never by matching `"Full"`:

- slacked → `EQUAL(<wire>.wire_tension, "Slack")`
- full tension → `NOT_EQUAL(<wire>.wire_tension, "Slack")` (an absent/blank attribute passes, as it should)

Matching `EQUAL(..., "Full")` silently drops every unmarked full-tension wire — a common and hard-to-spot bug. The same "absence = the default state" caution applies to other optional marker/trace booleans (e.g. treat a missing `proposed` as existing via `IS_FALSE`, not `EQUAL(...,false)`).

## Reusable patterns

**Wire owned by company X and of a power type** (item `w`):
```
AND( EQUAL( $(w._trace).company, "X" ),
     OR( EQUAL($(w._trace).cable_type,"Secondary"), EQUAL(...,"Neutral"), EQUAL(...,"Service") ) )
```

**All low-power hosts on a photo** — iterate each top-level category, keep the ones whose stack contains a qualifying wire (or that are a qualifying equipment marker), then map to the **host's** rounded height. Don't map height off the nested wire.

**Marker height → feet-inches string** (`28'-6"`), inches already rounded:
```
feet = FLOOR( DIVIDE(inches, 12) )
rem  = SUBTRACT( inches, MULTIPLY(feet, 12) )
str  = CONCATENATE( feet, "'-", rem, "\"" )
```

**Does a free-text annotation reference the right height?** Format the marker height as above and test **`EXCLUDES(annotation, str)`** (a contains-check) rather than `EQUAL` — robust to surrounding prose ("ENSURE LOW POWER FACILITIES AT OR ABOVE 28'-6\""). Guard the whole thing with `IF_ELSE( EXISTS(value), …, $FALSE )` so an empty result (no relevant markers) doesn't false-flag. Note the format must match byte-for-byte: straight `"`, `'-` separator, nearest inch, and confirm how round feet are written (`28'-0"` vs `28'`).

See Example 3 in `references/examples.md` for a full check built from these pieces.
