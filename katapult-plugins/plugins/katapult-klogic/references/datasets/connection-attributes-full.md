# Connection attribute catalog (generated)

Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.
Source of truth for model-specific `connection` attributes. Read single-valued attributes with a
trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item
operator. Table/group attributes hold sub-attributes, not a single value.

If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export.

## Directives

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `design_category` | text (picklist) | single | `New`, `Remove`, `Replace`, `Abandon`, `Reuse`, `Modify` | — |

## Make Ready

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `maintenance_email` | text (picklist) | single | `Notified Katapult PM`, `Sent to PPL` | — |
| `mr_note` | text | single | — | enter make ready note |

## Permit Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PennDOT_permit_status` | text (picklist) | single | `Investigating`, `ROW Request Submitted`, `ROW Received`, `Ready to Submit`, `Investigated; deemed unnecessary`, `Determine Setback`, `Pickup Requested`, `On Standby`, `Submitted`, `Revision Required`, `Revision Standby`, `Resubmitted`, `Approved`, `Unnecessary`, `Change in Work Supplement Required`, `Change in Work Supplement Submitted`, `Change in Work Supplement Approved`, `Deselected`, `Canceled`, `Closed`, `Doublewood` | — |
| `RxR_permit_status` | text (picklist) | single | `Investigating`, `Awaiting Attacher Approval`, `Included in Submission`, `Plan/Profile Creation`, `Submitted`, `Approved`, `Closed`, `Canceled`, `Unnecessary`, `Investigated; deemed unnecessary`, `Billable Hours`, `Deselected` | — |
| `extensions_submitted` | text (picklist) | single | `1`, `2`, `Too Many` | — |
| `misc_permit_status` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `municipal_permit` | text (picklist) | single | `Investigating`, `Ready to Submit`, `ROW Width Requested`, `Revision Required`, `Payment Needed`, `Payment Submitted`, `Canceled`, `Submitted`, `Approved`, `Unnecessary`, `Prepped`, `Investigated; deemed unnecessary`, `Waiting on Pickups`, `On Hold`, `Deselected` | — |
| `permit_fees` | text | single | — | — |
| `sidewalk_cut_permit` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `trans_undercrossing_permit_status` | text (picklist) | single | `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved`, `Rejected`, `Unnecessary`, `Investigated; deemed unnecessary`, `Deselected` | — |

## Pole Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `laz_file` | file | single | — | — |

## Ungrouped

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `connection_sub_type` | text (picklist) | single | `distribution fiber`, `access fiber`, `strand`, `drop fiber`, `pp/slsp`, `railroad ROW`, `state road ROW`, `municipal ROW`, `railroad`, `municipal`, `state road` | — |
| `connection_type` | text (picklist) | single | `aerial cable`, `overlash`, `slack span`, `overhead guy`, `pole to pole guy`, `underground cable`, `reference`, `down guy`, `pushbrace`, `existing cable`, `centerline`, `right of way line`, `state road right of way line`, `Proposed Setback`, `Original Location`, `municipal row line`, `Comcast`, `Water` | — |
| `crosses_over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `neutral_count` | text (picklist) | single | `0`, `1` | — |
| `neutral_spec` | text (picklist) | single | _54 options — large picklist, pull from model if needed_ | — |
| `note` | text | single | — | Note |
| `over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `pickup_required` | text (picklist) | single | `field visit required`, `fielding complete`, `pickup fully resolved` | — |
| `primary_count` | text (picklist) | single | `0`, `1`, `2`, `3`, `4`, `5`, `6` | — |
| `primary_spec` | text (picklist) | single | _56 options — large picklist, pull from model if needed_ | — |
| `reference_type` | text (picklist) | single | `power reference`, `com reference`, `guy reference`, `Proposed Location`, `Original Location` | — |
| `roadway_type` | text (picklist) | single | `PA Turnpike`, `PA State Road`, `Non-State Road` | — |
| `secondary_count` | text (picklist) | single | `0`, `1`, `2`, `3`, `4`, `5`, `6` | — |
| `secondary_spec` | text (picklist) | single | _54 options — large picklist, pull from model if needed_ | — |
| `time_bucket` | timer | single | — | — |
| `tracing_complete` | boolean | single | — | — |
| `warning` | text | single | — | Warning Message |

## Voltage Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `load_wire_spec` | text (picklist) | single | `500 XLP`, `4/0 TX x2`, `4/0 TX UG`, `4/0 TX`, `1/0 TX UG`, `1/0 TX`, `4 TX UG`, `4 TX`, `4 DX UG`, `4 DX` | — |
