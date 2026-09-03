# K-Logic syntax reference

The exact wire format K-Logic blocks must follow, derived from the engine (`KLogic.js`). Get any of this wrong and the block either fails to paste or resolves incorrectly.

## Serialization

- Output = the literal string `KLOGIC:` immediately followed by the minified JSON of the root block. Example: `KLOGIC:{"path":"node_id","type":"DATA"}`.
- Blocks are plain JSON objects. No metadata keys (`is_klogic_block`, ids, `description`) — real clipboard payloads are bare.
- Object key order does not affect parsing. Native output happens to be alphabetically sorted (`arg_01` < `arg_02` < `item_key` < `op` < `type`); matching that is cosmetic, not required.

## Every block has a `type`

`type` is one of: `EXPRESSION`, `DATA`, `LITERAL`, `PROCEDURE`, `BLANK`. The type determines which other keys are read; the engine ignores unrelated keys.

## DATA blocks

```json
{"path":"node.attributes.mr_category.*","type":"DATA"}
```

- `path` — a dot-delimited path into the data source. See `paths.md` for `*` wildcard and `$(...)` templating.
- Also how you read **procedure variables** (`{"path":"isComplex","type":"DATA"}`) and **loop items** (`{"path":"wire.mr_note","type":"DATA"}` when the enclosing loop's `item_key` is `wire`).

## LITERAL blocks

```json
{"type":"LITERAL","val":"Transfer","val_type":"TEXT"}
```

`val_type` controls how `val` is parsed:

| `val_type` | `val` becomes | Notes |
|---|---|---|
| `TEXT` | `String(val)` | |
| `NUMBER` | `Number(val)` | |
| `LIST` | the array as-is | `val` is a JSON array |
| `LOOKUP` | the object as-is | `val` is a JSON object (dictionary) |
| `BOOLEAN` | see sentinels | use `$TRUE` / `$FALSE` |
| `SPECIAL` | see sentinels | special values |

Sentinel `val` values (used with `BOOLEAN` or `SPECIAL`):
`$TRUE`→true, `$FALSE`→false, `$NULL`→null, `$UNDEFINED`→undefined, `$EMPTY`→"" (empty string), `$NEWLINE`→"\n", `$TAB`→"\t", `$NOW`→current epoch ms.

## EXPRESSION blocks

```json
{"op":"EQUAL","arg_01":{...},"arg_02":{...},"type":"EXPRESSION"}
```

- `op` — an operator key from `operators.md` (e.g. `AND`, `EQUAL`, `NOT_EXISTS`, `FIND`). Must exist or the engine throws.
- `arg_01`, `arg_02`, … — the operator's arguments, each itself a block. **1-indexed.** The engine collects all keys matching `arg_##`, **sorts them**, and maps them positionally to the operator's expected argument list. So order is by key name, not object order.
- **Chainable** operators (`AND`, `OR`, `SUM`, `MULTIPLY`, `MAX`, `MIN`, `CONCATENATE`, `MAKE_LIST`, `CONCATENATE_LISTS`, `CONCATENATE_LOOKUPS`, `MAKE_LOOKUP`) accept any number of args — add `arg_03`, `arg_04`, …
- **Optional trailing args may be omitted** — the engine pads missing args with `undefined`. E.g. `JOIN` with no delimiter, `ROUND` with no precision.
- Generate **contiguous** keys (`arg_01`, `arg_02`, `arg_03`). Native output sometimes has gaps (`arg_01`, `arg_03`) left by editing; harmless for chainable ops, but don't introduce gaps yourself.
- `item_key` — see below.

### `item_key` and list-looping

Operators that iterate a list (those marked "item" in `operators.md`: `SOME`, `EVERY`, `FILTER`, `COUNT`, `FIND`, `MAP`, `REDUCE`) put the **list in `arg_01`** and a **per-item expression in `arg_02`** (for `REDUCE`, the initial accumulator is `arg_03`). While iterating, the engine injects these keys into the data source, prefixed by `item_key` (default `"item"`):

- `<item_key>` — current element
- `<item_key>_index` — current index
- `<item_key>_list` — the whole list
- `<item_key>_accumulator` — running value (**`REDUCE` only**)

So with `"item_key":"wire"`, inside `arg_02` you read the current item's `mr_note` via `{"path":"wire.mr_note","type":"DATA"}`. Nested loops use distinct `item_key`s; inner expressions can read any enclosing loop's item by its key name.

## PROCEDURE blocks

```json
{
  "type":"PROCEDURE",
  "var_keys":["isComplex","transferWireNote"],
  "step_01":{...},
  "step_02":{...},
  "return":{...}
}
```

- `step_01`, `step_02`, … — steps, run in **sorted key order**. Each step's resolved value is bound to a variable named by the corresponding entry in `var_keys` (step order ↔ `var_keys` order).
- `var_keys` — array of variable names; its length must equal the number of `step_NN` keys.
- Later steps and `return` read earlier variables as bare DATA paths (`{"path":"isComplex","type":"DATA"}`).
- `return` — the block whose value the procedure resolves to. Variables are scoped to the procedure only.

## BLANK blocks

`{"type":"BLANK"}` resolves to `null` and logs a warning. It's an unfilled placeholder — never emit one in finished output.

## Minimal end-to-end example

"Flag a node whose `mr_category` is `Complex Make Ready`":

```
KLOGIC:{"arg_01":{"path":"node.attributes.mr_category.*","type":"DATA"},"arg_02":{"type":"LITERAL","val":"Complex Make Ready","val_type":"TEXT"},"op":"EQUAL","type":"EXPRESSION"}
```
