# K-Logic operator catalog

Every operator usable as an EXPRESSION `op`, from `KLogicOperators.js`. Columns: **op key** (what goes in `"op"`), **name** (Logic Editor label), **args** (in order; the count of `arg_NN` you supply), **returns**, and notes. "chainable" = accepts unlimited args. "item" = loops a list and exposes the current element via `item_key` (see `klogic-syntax.md`).

Argument slots are 1-indexed: the first listed arg is `arg_01`, second `arg_02`, etc.

## Existence & truthiness

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `EXISTS` | Exists | value | boolean | true unless null/undefined/`""` |
| `NOT_EXISTS` | Does Not Exist | value | boolean | true if null/undefined/`""` |
| `IS_TRUE` | Is True | value | boolean | `Boolean(v) === true` |
| `IS_FALSE` | Is False | value | boolean | `Boolean(v) === false` |

## Logic

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `AND` | Logical And | conditions… | boolean | chainable; all truthy |
| `OR` | Logical Or | conditions… | boolean | chainable; any truthy |

## Comparison

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `EQUAL` | Equal | a, b | boolean | loose `==` |
| `NOT_EQUAL` | Not Equal | a, b | boolean | loose `!=` |
| `GREATER_THAN` | Greater Than | a, b | boolean | numeric coercion |
| `LESS_THAN` | Less Than | a, b | boolean | numeric coercion |
| `GREATER_OR_EQUAL` | Greater Than or Equal | a, b | boolean | numeric coercion |
| `LESS_OR_EQUAL` | Less Than or Equal | a, b | boolean | numeric coercion |
| `INCLUDES` | Includes | listOrText, value | boolean | `arg_01.includes(arg_02)` |
| `EXCLUDES` | Excludes | listOrText, value | boolean | negation of Includes |
| `MATCHES_REGEX` | Matches Regex | text, pattern, flags | boolean | escape specials with `\\` |

## Control flow

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `IF_ELSE` | If-Else | condition, then, else | any | ternary |
| `FALLBACK` | Fallback | a, b | any | `a ?? b` (b if a null/undefined) |
| `GET_FROM` | Get From | source, path | any | `Path.get(source, path)`; treat arg_01 as data, arg_02 as a path string |

## Math

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `SUM` | Sum | numbers… | number | chainable |
| `SUBTRACT` | Subtract | a, b | number | a − b |
| `MULTIPLY` | Multiply | numbers… | number | chainable |
| `DIVIDE` | Divide | a, b | number | a ÷ b |
| `ROUND` | Round | value, places | number | places default 0 |
| `FLOOR` | Floor | value | number | |
| `CEIL` | Ceiling | value | number | |
| `MAX` | Maximum | numbers… | number | chainable |
| `MIN` | Minimum | numbers… | number | chainable |
| `SUM_LIST` | Sum List | list | number | sums a list's items |
| `MAX_LIST` | Maximum List Item | list | number | null on empty |
| `MIN_LIST` | Minimum List Item | list | number | null on empty |
| `CONVERT_UNITS` | Convert Units | value, fromUnit, toUnit, precision | number | |

## Lists

| op key | name | args | returns | item? | notes |
|---|---|---|---|---|---|
| `LENGTH` | Count | listOrText | number | | length / char count |
| `SOME` | Some List Item Is | list, condition | boolean | item | any item passes |
| `EVERY` | Every List Item Is | list, condition | boolean | item | all items pass |
| `COUNT` | Count If | list, condition | number | item | count of passing items |
| `FILTER` | Filter List | list, condition | list | item | passing subset |
| `FIND` | Find In List | list, condition | any | item | first passing item |
| `MAP` | Map List | list, expression | list | item | transform each item |
| `REDUCE` | Reduce List | list, expression, initial | any | item | uses `<item_key>_accumulator` |
| `UNIQUE` | Filter Unique | list | list | | dedupe |
| `FLATTEN_LIST` | Flatten List | list, depth | list | | depth default 0 |
| `MAKE_LIST` | Make List From Args | items… | list | | chainable |
| `CONCATENATE_LISTS` | Concatenate Lists | lists… | list | | chainable; flattens one level |
| `LIST_KEYS` | List Object Keys | object | list | | `Object.keys` |
| `LIST_VALUES` | List Object Values | object | list | | `Object.values` — the usual way to turn a keyed lookup (e.g. `photofirst_data.wire`) into a list before looping |

## Lookups (objects)

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `MAKE_LOOKUP` | Make Lookup From Args | pairs… | object | each arg a `[key,value]` list; chainable |
| `CONCATENATE_LOOKUPS` | Concatenate Lookups | objects… | object | merge; chainable |

## Text

| op key | name | args | returns | notes |
|---|---|---|---|---|
| `CONCATENATE` | Concatenate | parts… | text | chainable |
| `JOIN` | Join List | list, delimiter | text | delimiter optional |
| `SPLIT` | Split Text | text, delimiter | list | delimiter optional (char split) |
| `REPLACE` | Find and Replace | text, find, replaceWith | text | replaces all |
| `TO_UPPER_CASE` | To Upper Case | text | text | |
| `TO_LOWER_CASE` | To Lower Case | text | text | |
| `PAD_START` | Pad Start | text, length, padStr | text | padStr default space |
| `PAD_END` | Pad End | text, length, padStr | text | padStr default space |
| `FORMAT_TIMESTAMP` | Format Timestamp | epochMs, formatTokens | text | Luxon tokens |

## Deprecated (do not emit)

`CONVERT` ("Convert (Deprecated)") — use `CONVERT_UNITS` instead. Deprecated ops are hidden in the editor.
