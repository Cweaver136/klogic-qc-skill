# Section attribute catalog (generated)

Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.
Source of truth for model-specific `section` attributes. Read single-valued attributes with a
trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item
operator. Table/group attributes hold sub-attributes, not a single value.

If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export.

## Laser Heights

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ht_ground` | laser_data | single | — | — |
| `ht_lowest_com_cable` | laser_data | single | — | — |
| `ht_lowest_power_cable` | laser_data | single | — | — |
| `ht_other_one` | laser_data | single | — | — |
| `ht_other_two` | laser_data | single | — | — |
| `ht_top_com_cable` | laser_data | single | — | — |
| `ht_top_of_pole` | laser_data | single | — | — |
| `ht_top_of_pole_tag` | laser_data | single | — | — |
| `lt_notes` | text | single | — | Insert laser notes here |
| `set_gate` | laser_data | single | — | — |

## Loading Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `collection_temperature` | text | single | — | Temperature at time of collection |

## Make Ready

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `mr_state` | text (picklist) | single | `No MR`, `MR Resolved`, `MR Unresolved` | MR State |
| `pinch_point` | text (picklist) | single | `pass`, `fail`, `error` | — |
| `remedial_mr_note` | text | single | — | — |

## Permit Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PennDOT_permit_status` | text (picklist) | single | `Investigating`, `ROW Request Submitted`, `ROW Received`, `Ready to Submit`, `Investigated; deemed unnecessary`, `Determine Setback`, `Pickup Requested`, `On Standby`, `Submitted`, `Revision Required`, `Revision Standby`, `Resubmitted`, `Approved`, `Unnecessary`, `Change in Work Supplement Required`, `Change in Work Supplement Submitted`, `Change in Work Supplement Approved`, `Deselected`, `Canceled`, `Closed`, `Doublewood` | — |
| `RxR_name` | text (picklist) | single | `North Shore`, `Norfolk Southern`, `Reading Blue Mountain and Northern`, `Pennsylvania Northeast Regional `, `Delaware Lackawanna`, `Shamokin Valley Railroad`, ` Union County Industrial Railroad`, `Luzerne and Susquehanna Railway` | — |
| `RxR_permit_status` | text (picklist) | single | `Investigating`, `Awaiting Attacher Approval`, `Included in Submission`, `Plan/Profile Creation`, `Submitted`, `Approved`, `Closed`, `Canceled`, `Unnecessary`, `Investigated; deemed unnecessary`, `Billable Hours`, `Deselected` | — |
| `confirm_pickup_fielded_(Permits)` | text | single | — | Date & Initials |
| `description_(Permits)` | text | single | — | what photos ya want?? |
| `extensions_submitted` | text (picklist) | single | `1`, `2`, `Too Many` | — |
| `fielder_(Permit_pickup)` | list (picklist, multi) | multi | `stevenmiller`, `smorris`, `jcavallaro`, `hrhoads`, `stiday`, `cpartridge`, `isalim`, `ljessen`, `zschreiber`, `echapman`, `bwarner`, `ssieber` | — |
| `misc_permit_status` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `municipal_permit` | text (picklist) | single | `Investigating`, `Ready to Submit`, `ROW Width Requested`, `Revision Required`, `Payment Needed`, `Payment Submitted`, `Canceled`, `Submitted`, `Approved`, `Unnecessary`, `Prepped`, `Investigated; deemed unnecessary`, `Waiting on Pickups`, `On Hold`, `Deselected` | — |
| `permit_fees` | text | single | — | — |
| `permit_pickup` | object (group) | single | — | — |
| `permit_pickup_required` | text (picklist) | single | `field visit required`, `fielding complete`, `pickup fully resolved` | — |
| `sidewalk_cut_permit` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `trans_undercrossing_permit_status` | text (picklist) | single | `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved`, `Rejected`, `Unnecessary`, `Investigated; deemed unnecessary`, `Deselected` | — |

## Post Construction Inspection

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PCI_failure_type` | text (picklist) | single | `Com MR not executed`, `Power MR not executed`, `Com to power MR conversion`, `Issues with original MR`, `Other (see PCI note)` | — |
| `PCI_midspan_status` | text (picklist) | single | `Pass`, `Fails`, `Already passed in previous round`, `Fails(resolved)`, `Delayed`, `Not Invoiceable` | — |
| `post_construction_inspection` | text (picklist) | single | `Pass`, `Passes; not built as designed`, `Fails`, `Already passed in previous round`, `Not yet constructed`, `Delayed`, `Not Invoiceable`, `Not in Random Sample` | — |

## Tracking

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `internal_note` | text | single | — | general note |

## Ungrouped

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ABD_completed` | boolean | single | — | — |
| `confirm_pickup_fielded` | text | single | — | Date & Initials |
| `crosses_over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `crossing_obstacle` | text (picklist) | single | `Crossing cable`, `Bolted cable`, `Tree limb`, `Traffic arm`, `Transmission line`, `Other` | — |
| `driveway_type` | text (picklist) | single | `Residential`, `Commercial` | — |
| `field_completed` | boolean | single | — | — |
| `lasered_cable_height` | text | single | — | All cable heights, ordered bottom to top |
| `lasered_ground_height` | text | single | — | Rail height for railroad, ground height otherwise |
| `mr_violation` | text | single | — | Make Ready Violation |
| `note` | text | single | — | Note |
| `obstacle` | text (picklist) | single | `Transmission Line`, `Traffic Arm`, `Wire (attached)`, `Wire (unattached)`, `Structure`, `Other` | — |
| `over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `pickup` | object (group) | single | — | — |
| `pickup_description` | text | single | — | Enter Pickup description |
| `pickup_required` | text (picklist) | single | `field visit required`, `fielding complete`, `pickup fully resolved` | — |
| `roadway_type` | text (picklist) | single | `PA Turnpike`, `PA State Road`, `Non-State Road` | — |
| `time_bucket` | timer | single | — | — |
| `vantage_point` | coordinate_capture | single | — | — |
| `warning` | text | single | — | Warning Message |
