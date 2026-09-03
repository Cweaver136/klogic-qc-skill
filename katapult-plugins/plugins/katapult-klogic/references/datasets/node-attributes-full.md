# Node attribute catalog (generated)

Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.
Source of truth for model-specific `node` attributes. Read single-valued attributes with a
trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item
operator. Table/group attributes hold sub-attributes, not a single value.

Read this file when a check compares an attribute against a specific value, so the exact picklist string
is right. For a quick existence/type check, `node-attributes.md` (the index) is smaller and enough.

A few attributes have picklists too large to inline (`company`, `pole_spec`, `proposed_pole_spec`,
`PPL_construction_spec`, `PATA`, load cases). The option count is noted; pull exact values from the model
export or ask the user when a check needs to match one.

If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export:
`python scripts/build_attribute_catalog.py model_attributes.json --entity node --out references/datasets/node-attributes-full.md`

## Aggregate Tracking

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PPL_comment` | text | single | — | — |
| `customer_action` | text (picklist) | single | `Incomplete Application`, `Remediation Required`, `Awaiting Customer Payment: MR Engineering`, `Awaiting Customer Payment: MR Construction`, `Awaiting Customer Payment: Pre-Existing Violations`, `Awaiting Customer Construction`, `Customer Hold` | — |
| `customer_comment` | text | single | — | — |
| `resolved` | boolean | single | — | — |

## Application Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PPL_complex_MR` | boolean | single | — | — |
| `ROW_exclusion` | boolean | single | — | — |
| `job_id` | text | single | — | — |
| `new_attach_type` | text | single | `Bolted Cable`, `Cabinet`, `Guy (below com space)`, `Guy (in com space)`, `Guy (stub pole)`, `Service Drop`, `Telephone Cable`, `Mirror`, `Vertical Banner`, `Cross Street Banner`, `Public Sign`, `Wireless Antenna - Middle`, `Wireless Antenna - Bottom`, `Other`, `Wireless Antenna - Top`, `Streetlight`, `Holiday Decoration (lit)`, `Holiday Decoration (unlit)` | New Attachment Type |
| `op_area` | text | single | — | PPL Operating Area |
| `pole_app_order` | text | single | — | — |
| `pole_owner` | text (picklist) | single | `PPL Company` | Owner |
| `region` | text | single | — | PPL Region |
| `take_off_pole` | boolean | single | — | Take Off Pole |
| `take_off_pole_not_applicable` | boolean | single | — | No Take Off Pole |
| `take_off_pole_note` | text | single | — | Take Off Pole Note |

## Directives

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `design_category` | text (picklist) | single | `New`, `Remove`, `Replace`, `Abandon`, `Reuse`, `Modify` | — |

## Doublewood

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `NJUN_true-up` | boolean | single | — | — |
| `PPL_NTG_step` | text (picklist) | single | `NJUNS updated with foreign transfers`, `DISPUTE`, `Sent to Region` | — |
| `attachers` | text | single | — | — |
| `bucket_truck_access` | text (picklist) | single | `no`, `yes` | — |
| `close_NJUNS_ticket` | boolean | single | — | — |
| `doublewood_address` | text | single | — | Address |
| `doublewood_exists` | text (picklist) | single | `Unknown`, `yes`, `no`, `dangler` | — |
| `doublewood_priority` | text | single | — | Priority |
| `doublewood_review` | text (picklist) | single | `Access Issue - Revisit Required`, `Validated No Doublewood Location`, `Unclear` | — |
| `doublewood_status` | text (picklist) | single | `Access Issue`, `No Pole to Pull`, `Ready for Removal`, `Transfers Needed`, `Splicing/Transfers Needed` | — |
| `exception` | text (picklist) | single | `UNEXPECTED UPDATE`, `DUPLICATE`, `DISPUTE`, `OTHER` | — |
| `location_source` | text | single | — | — |
| `material` | text (picklist) | single | `Soil`, `Asphalt`, `Concrete`, `Sidewalk - Lancaster City`, `Other` | — |
| `nearest_existing_ppl_grid` | text | single | — | — |
| `njuns_last_updated` | text | single | — | — |
| `pole_pulled` | boolean | single | — | — |
| `start_date` | text | single | — | — |
| `status` | text | single | — | — |
| `steps` | object (table) | single | — | — |
| `survey_date` | text | single | — | — |
| `ticket_id` | text | single | — | — |
| `ticket_type_name` | text | single | — | — |
| `verified_ready_for_removal` | boolean | single | — | — |

## Feedback

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `contractor_feedback` | object (group) | single | — | — |
| `contractor_feedback_note` | text | single | — | — |
| `contractor_feedback_viewed` | boolean | single | — | — |
| `external_contractor_QA-QC` | boolean | single | — | — |

## Field Collected Data

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `doublewood_conditions` | text (picklist) | single | `None`, `Ready for Removal`, `Transfers Needed`, `Splicing/Transfers Needed`, `Unsure if Transfers are needed` | — |

## Inspection

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `unauthorized_att` | text (picklist) | single | `Unauthorized Strand`, `Unauthorized Fiber`, `Unauthorized Equipment`, `Adjacent but not attached (NESC violation)` | — |

## Invoicing

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `annotated_by` | text (picklist) | single | `Universal: Ready for payment`, `Universal: Paid`, `Universal : Additional Pole`, `Katapult: No payment`, `UNDC: Ready for payment`, `UNDC: Paid`, `UNDC: Additional Pole`, `Grizzly: Ready for payment`, `Grizzly: Paid`, `Grizzly: Additional Pole` | — |
| `applicant_invoice` | text (picklist) | single | `Applicant Invoiced`, `Applicant Paid`, `Additional pole` | — |
| `fielded_by` | text (picklist) | single | `Universal: Ready for payment`, `Universal: Paid`, `Universal: Additional pole`, `Katapult: No payment`, `UNDC: Ready for payment`, `UNDC: Paid`, `UNDC: Additional pole`, `Grizzly: Ready for payment`, `Grizzly: Paid`, `Grizzly: Additional pole` | — |
| `invoice_note` | text | single | — | Invoice Note |
| `original_pole_count` | text | single | — | Original Pole Count |
| `subcontract_pickups` | object (group) | single | — | — |
| `subcontractor_billing` | object (group) | single | — | — |

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

## Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `proposed` | boolean | single | — | — |
| `transformer_loading` | text (picklist) | single | `Pass`, `Fail` | — |
| `transformer_loading_notes` | text | single | — | — |
| `voltage_drop_checked` | boolean | single | — | — |

## Loading Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PLA` | loading-data | single | `NESC - 250B - Heavy - C - Elsewhere`, `NESC - 250B - Heavy - C - Crossing`, `NESC - 250B - Heavy - B - Elsewhere`, `NESC - 250B - Heavy - B - Crossing`, `NESC - 205B - Medium - C - Elsewhere`, `NESC - 250B - Medium - C - Crossing`, `NESC - 250B - Medium - B - Elsewhere`, `NESC - 250B - Medium - B - Crossing`, `NESC - 250B - Light - C - Elsewhere`, `NESC - 250B - Light - C - Crossing`, `NESC - 250B - Light - B - Elsewhere`, `NESC - 250B - Light - B - Crossing`, `fail`, `pass`, `existing conditions fail`, `passes with make ready` | — |
| `PPL_250C_loading_percentage` | text | single | — | PPL 250C Loading Percentage |
| `accepted_failure_direction` | text | single | — | [deg] |
| `accepted_loading_percentage` | text | single | — | Percent Load |
| `baseline_buckling_ratio` | text | single | — | Baseline Buckling Percentage |
| `baseline_failure_direction` | text | single | — | — |
| `baseline_guy_loading_ratio` | object (table) | single | — | Baseline Guy Loading Percentage |
| `baseline_loading_percentage` | text | single | — | — |
| `baseline_rod_loading_ratio` | object (table) | single | — | Baseline Rod Loading Percentage |
| `baseline_soil_loading_ratio` | object (table) | single | — | Baseline Soil Loading Percentage |
| `buckling_ratio` | text | single | — | Buckling Percentage |
| `buckling_ratio_drift` | text | single | — | Buckling Percentage Drift |
| `collection_temperature` | text | single | — | Temperature at time of collection |
| `cut_pole` | boolean | single | — | — |
| `effective_groundline_circumference` | text | single | — | — |
| `failure_direction` | text | single | — | — |
| `failure_direction_diff` | text | single | — | — |
| `failure_direction_drift` | text | single | — | — |
| `guy_loading_ratio` | object (table) | single | — | Guy Loading Percentage |
| `guy_loading_ratio_drift` | object (table) | single | — | Guy Loading Percentage Drift |
| `katapult_loading` | object (group) | single | — | — |
| `kpla_drift_present` | boolean | single | — | — |
| `load_case` | text (picklist) | single | `NESC - 250B - Heavy - B`, `NESC - 250B - Heavy - B - Com - Exception`, `NESC - 250B - Heavy - C - Crossing`, `NESC - 250B - Heavy - C - Elsewhere`, `NESC - 250C - Heavy - B - 120 - Wind`, `NESC - 250C - Heavy - B - 95 - Wind`, `NESC - 250C - Heavy - C - 110 - Wind`, `NESC - 250C - Heavy - C - 90 - Wind`, `NESC - 250C - Heavy - 100 - Wind`, `NESC - 250D - Heavy - B - 50 - Wind - 075 - Ice`, `NESC - 250D - Heavy - C - 50 - Wind - 075 - Ice`, `NESC - 250D - Heavy - B - 40 - Wind - 100 - Ice`, `NESC - 250D - Heavy - B - 40 - Wind - 075 - Ice`, `NESC - 250D - Heavy - C - 40 - Wind - 100 - Ice`, `NESC - 250D - Heavy - C - 40 - Wind - 075 - Ice` | — |
| `loading_analysis` | text (picklist) | single | `NESC - 250B - Heavy - C - Elsewhere`, `NESC - 250B - Heavy - C - Crossing`, `NESC - 250B - Heavy - B`, `NESC - 250B - Medium - C - Elsewhere`, `NESC - 250B - Medium - C - Crossing`, `NESC - 250B - Medium - B`, `NESC - 250B - Light - C - Elsewhere`, `NESC - 250B - Light - C - Crossing`, `NESC - 250B - Light - B`, `Unity`, `NESC - 250B - Heavy - B - Com - Exception`, `NESC - 250B - Medium - B - Com - Exception`, `NESC - 250B - Light - B - Com - Exception` | — |
| `loading_error` | boolean | single | — | — |
| `loading_notes` | text | single | — | enter your loading notes |
| `loading_percentage` | text | single | — | Percent Load (external) |
| `loading_percentage_diff` | text | single | — | — |
| `loading_percentage_drift` | text | single | — | — |
| `loading_result` | text (picklist) | single | `fail`, `pass`, `existing conditions fail`, `passes with make ready` | — |
| `loading_zone` | text (picklist) | single | `Heavy`, `Medium`, `Light`, `Warm Island` | — |
| `proposed_uplift` | text | single | — | — |
| `rod_loading_ratio` | object (table) | single | — | Rod Loading Percentage |
| `rod_loading_ratio_drift` | object (table) | single | — | Rod Loading Percentage Drift |
| `soil_loading_ratio` | object (table) | single | — | Soil Loading Percentage |
| `soil_loading_ratio_drift` | object (table) | single | — | Soil Loading Percentage Drift |
| `uplift_if_this_pole_doesnt_change` | text | single | — | — |
| `wind_loading_result` | text (picklist) | single | `fail`, `pass`, `existing conditions fail`, `passes with make ready` | — |

## Make Ready

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `CUs_completed` | boolean | single | — | — |
| `FCC_category` | text (picklist) | single | `No Make Ready`, `Simple Make Ready`, `Complex Make Ready` | — |
| `MRE_estimated_cost` | text | single | — | — |
| `MRE_estimation` | text (picklist) | single | `No Make Ready`, `Communication Make Ready`, `Power Make Ready`, `Pole Replacement` | — |
| `MR_bundle` | object (group) | single | — | — |
| `PPL_construction_spec` | list (picklist, multi) | multi | _205 options — large picklist, pull from model if needed_ | — |
| `Visual_Inspection` | text (picklist) | single | `Pass`, `Fail, Replace`, `Fail, Notify` | — |
| `bucket_truck_accessible` | boolean | single | — | — |
| `checked_for_adjacent_vsbs` | boolean | single | — | — |
| `complex_category` | text (picklist) | single | `Foreign Utility Work`, `Advanced Power`, `Primary Power`, `Pole Replacement` | — |
| `complex_reason` | list (picklist, multi) | multi | `1 - Not enough space for new attachment`, `2 - Not enough space for existing attachments`, `3 - Midspan clearance issues`, `4 - PLA Failure (PPL only fails)`, `5 - PLA Failure (PPL passes, existing coms fail)`, `6 - PLA Failure (existing passes, new attachment fails)`, `7 - Uplift`, `8 - Visual Failure`, `9 - Adjacent Pole`, `10 - Storm Hardening Failure`, `11 - Doublewood Transfers`, `12 - Transmission Pole` | — |
| `cost_causer` | cost-causer | single | — | — |
| `cost_causer_note` | text | single | — | — |
| `customer_directive` | text | single | — | Enter customer directive |
| `foreign_utility_make_ready` | text | single | — | Enter foreign utility make ready |
| `grounding_present` | text (picklist) | single | `Grounded`, `Not Grounded`, `Broken`, `Com Only`, `Adjacent Poles`, `Proposed` | — |
| `maintenance_email` | text (picklist) | single | `Notified Katapult PM`, `Sent to PPL` | — |
| `mr_category` | text (picklist) | single | `No Make Ready`, `Simple Make Ready`, `Medium Make Ready`, `Complex Make Ready` | MR Category |
| `mr_note` | text | single | — | enter make ready note |
| `mr_state` | text (picklist) | single | `No MR`, `MR Resolved`, `MR Unresolved` | MR State |
| `one_touch_summary` | object (table) | single | — | — |
| `original_mr_category` | text (picklist) | single | `No Make Ready`, `Simple Make Ready`, `Medium Make Ready`, `Complex Make Ready`, `Power Make Ready Required`, `Power Make Ready N/A` | — |
| `overlapping_work` | text (picklist) | single | `No Impact`, `Overlapping Conflict`, `Overlapping Resolved` | — |
| `post_construction_proposed` | text (picklist) | single | — | — |
| `power_mr_annotation` | text | single | — | Annotation |
| `ppl_make_ready` | text | single | — | PPL Make Ready |
| `proposed_pole_spec` | text (picklist) | single | _226 options — large picklist, pull from model if needed_ | — |
| `pwr_mr_required` | boolean | single | — | Power MR Required? |
| `reason_for_replacement` | list (picklist, multi) | multi | `1 - Not enough space for new attachment`, `2 - Not enough space for existing attachments`, `3 - Midpan clearance issues`, `4 - PLA Failure (PPL only fails)`, `5 - PLA Failure (PPL passes, existing coms fail)`, `6 - PLA Failure (exisiting passes, new attachment fails)`, `7 - Uplift`, `8 - Visual Failure` | Replacement Reason |
| `remedial_make_ready_required` | boolean | single | — | — |
| `remedial_mr_note` | text | single | — | — |
| `replacement_notes` | text | single | — | notes on the replacement so we can improve the process |
| `replacement_process` | text (picklist) | single | `Cut and Dry`, `External Reference Required`, `Soft Data was Required`, `Walked it back` | — |
| `seth_testing_complex_reason` | text (picklist) | single | `1 - Not enough space for new attachment`, `2 - Not enough space for existing attachments`, `3 - Midspan clearance issues`, `4 - PLA Failure (PPL only fails)`, `5 - PLA Failure (PPL passes, existing coms fail)`, `6 - PLA Failure (existing passes, new attachment fails)`, `7 - Uplift`, `8 - Visual Failure`, `9 - Adjacent Pole`, `10 - Storm Hardening Failure`, `11 - Doublewood Transfers` | — |
| `street_view_com_count` | text (picklist) | single | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` | — |
| `total_pole_cut_length` | text | single | — | Total length of the pole after it is cut. (NOT AGL!) |
| `traffic_control` | text (picklist) | single | `average`, `double`, `none` | — |
| `unauthorized_email` | text (picklist) | single | `Notified Katapult PM`, `Sent to PPL` | — |
| `work_location` | text | single | — | ppl work location |
| `zach_pilot` | object (group) | single | — | — |

## PA 1 Call

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `PA_1_call` | text | single | — | — |
| `PA_1_call_api_request_sent` | boolean | single | — | — |
| `PA_1_call_required` | boolean | single | — | — |
| `intersecting_street` | text | single | — | — |
| `location_description` | text | single | — | Describe the location |
| `location_of_work` | list (picklist, multi) | multi | `Street`, `Sidewalk`, `Public Property`, `Private Property (Front)`, `Private Property (Rear)`, `Private Property (Left)`, `Private Property (Right)` | — |

## PPL Package

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `%cap` | text | single | — | percent of the dollars that are captial on this pole |
| `PPL_package_note` | text | single | — | Infor/Designer Note |
| `foreign_utility_replacements_WO` | text | single | — | Enter Foreign Utility Work Order |
| `package_completed` | boolean | single | — | — |
| `wo_number` | text | single | — | WO Number |

## Permit Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ADA_clearance` | text | single | — | ft |
| `FAA_permit_status` | text (picklist) | single | `Investigating`, `PP&L Contacted`, `Revisions Required`, `Submitted`, `Resubmitted`, `Approved`, `Cancelled`, `Unnecessary`, `Deselected`, `Investigated; deemed unnecessary` | — |
| `LOJ` | boolean | single | — | — |
| `PATA` | text (picklist) | single | _71 options — large picklist, pull from model if needed_ | — |
| `PPL_ROW_status` | text (picklist) | single | `Investigating`, `Investigated; deemed unnecessary`, `Ready to submit`, `Revision required`, `ROW Width Requested`, `Staking Requested`, `Submitted`, `Approved`, `Rejected`, `Canceled`, `Unnecessary`, `Deselected`, `Resolved` | — |
| `PPL_approval` | text (picklist) | single | `Requested`, `Approved`, `Rejected`, `Unnecessary` | — |
| `PennDOT_app_number` | text | single | — | — |
| `PennDOT_district` | text (picklist) | single | `District 2`, `District 3`, `District 4`, `District 5`, `District 6`, `District 8` | — |
| `PennDOT_expiration_date` | text (date) | single | — | — |
| `PennDOT_grade` | text (picklist) | single | `Positive`, `Level`, `Negative` | — |
| `PennDOT_municipal_code` | text | single | — | — |
| `PennDOT_north` | text (picklist) | single | `0° N`, `30° N`, `60° N`, `90° N`, `120° N`, `150° N`, `180° N`, `210° N`, `240° N`, `270° N`, `300° N`, `330° N` | — |
| `PennDOT_permit_status` | text (picklist) | single | `Investigating`, `ROW Request Submitted`, `ROW Received`, `Ready to Submit`, `Investigated; deemed unnecessary`, `Determine Setback`, `Pickup Requested`, `On Standby`, `Submitted`, `Revision Required`, `Revision Standby`, `Resubmitted`, `Approved`, `Unnecessary`, `Change in Work Supplement Required`, `Change in Work Supplement Submitted`, `Change in Work Supplement Approved`, `Deselected`, `Canceled`, `Closed`, `Doublewood` | — |
| `PennDOT_response_letter` | file | single | — | — |
| `PennDOT_roadside` | text (picklist) | single | `Left`, `Right` | — |
| `PennDOT_setback` | text | single | — | — |
| `PennDot_revision_date` | text (date) | single | — | — |
| `PennDot_revision_reasons` | list (picklist, multi) | multi | `EOP/SE/CL/GR`, `Seg/Offset`, `Missing Documents`, `Incorrect PATA`, `Doublewood`, `Staking Requested`, `Rejected LOJ`, `Unpermittable Location`, `Wrong Utility Sketch Form Used`, `Misc. Utility Sketch Errors`, `EPS Information` | — |
| `PennDot_revisions` | object (table) | multi | — | — |
| `ROW_record` | file | single | — | — |
| `ROW_record_page` | text | single | — | Page Number |
| `ROW_width` | text | single | — | From CL |
| `RxR_LiDAR_scan_file` | file | single | — | — |
| `RxR_crossing_number` | text | single | — | — |
| `RxR_inventory_report` | file | single | — | — |
| `RxR_lidar_scan` | text (picklist) | single | `Needed`, `Request Submitted`, `Received`, `Processing`, `Not Needed` | — |
| `RxR_mailing_address` | text | single | — | — |
| `RxR_name` | text (picklist) | single | `North Shore`, `Norfolk Southern`, `Reading Blue Mountain and Northern`, `Pennsylvania Northeast Regional `, `Delaware Lackawanna`, `Shamokin Valley Railroad`, ` Union County Industrial Railroad`, `Luzerne and Susquehanna Railway` | — |
| `RxR_pass_through_fees_(PPL)` | text | single | — | — |
| `RxR_permit_info` | object (table) | single | — | — |
| `RxR_permit_status` | text (picklist) | single | `Investigating`, `Awaiting Attacher Approval`, `Included in Submission`, `Plan/Profile Creation`, `Submitted`, `Approved`, `Closed`, `Canceled`, `Unnecessary`, `Investigated; deemed unnecessary`, `Billable Hours`, `Deselected` | — |
| `RxR_plan_and_profile` | file | single | — | — |
| `RxR_road_ROW_status` | text (picklist) | single | `PD ROW Needed`, `Muni ROW Needed`, `Received`, `Submitted`, `Not Needed`, `Private ROW Needed`, `Requested` | — |
| `RxR_val_map_status` | text (picklist) | single | `Needed`, `Received`, `Interpreted`, `Requested`, `Not Needed` | — |
| `RxR_valuation_map` | file | single | — | — |
| `SE_ft` | text | single | — | — |
| `anchor_CL_ft` | text | single | — | Enter anchor's distance from CL |
| `anchor_installation` | boolean | single | — | — |
| `attacher_approval` | text (picklist) | single | `Requested`, `Approved`, `Rejected`, `Unnecessary` | — |
| `average_annual_daily_traffic` | text | single | — | — |
| `cl_ft` | text | single | — | enter centerline measurement |
| `clear_zone_distance` | text | single | — | from EOP; ft |
| `comcast_PennDOT_status` | text (picklist) | single | `Investigating`, `ROW Request Submitted`, `ROW Received`, `Ready to Submit`, `Submitted`, `Approval Letter`, `Approval Letter Submitted`, `Investigated; Deemed unnecessary`, `Pickup Requested`, `Revision Required`, `Resubmitted`, `Approved`, `Canceled`, `Closed`, `Deselected`, `Overhead Wire` | PennDOT Status |
| `confirm_pickup_fielded_(Permits)` | text | single | — | Date & Initials |
| `custom_note` | boolean | single | — | — |
| `custom_utility_sketch_note` | text | single | — | Enter a Custom Utility Sketch Note |
| `description_(Permits)` | text | single | — | what photos ya want?? |
| `drawn_by` | text | single | — | — |
| `environmental_permit_status` | text (picklist) | single | `Investigating`, `Contacted PPL`, `Submitted`, `Unnecessary`, `Approved`, `Cancelled` | — |
| `eop_ft` | text | single | — | enter eop measurement |
| `extensions_submitted` | text (picklist) | single | `1`, `2`, `Too Many` | — |
| `fielder_(Permit_pickup)` | list (picklist, multi) | multi | `stevenmiller`, `smorris`, `jcavallaro`, `hrhoads`, `stiday`, `cpartridge`, `isalim`, `ljessen`, `zschreiber`, `echapman`, `bwarner`, `ssieber` | — |
| `gr_ft` | text | single | — | enter guiderail measurement |
| `guiderail_type` | text (picklist) | single | `31-SCC (nested)`, `31-SCC`, `31-SC`, `31-S`, `2-WCC`, `2-WC`, `2-W` | — |
| `include_in_multi_pole_sketch` | boolean | single | — | — |
| `letter_of_justification` | file | single | — | — |
| `location_photo` | file | single | — | — |
| `map_app_link` | text | single | — | — |
| `meets_clear_zone` | boolean | single | — | — |
| `misc_permit_requires_plan_profile` | boolean | single | — | — |
| `misc_permit_status` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `municipal_mailing_address` | text | single | — | — |
| `municipal_payment_status` | text (picklist) | single | `Investigating`, `Needed`, `Not Needed`, `Pickup Requested`, `Revision Required`, `Ready to be Paid`, `Payment Submitted`, `Paid` | — |
| `municipal_permit` | text (picklist) | single | `Investigating`, `Ready to Submit`, `ROW Width Requested`, `Revision Required`, `Payment Needed`, `Payment Submitted`, `Canceled`, `Submitted`, `Approved`, `Unnecessary`, `Prepped`, `Investigated; deemed unnecessary`, `Waiting on Pickups`, `On Hold`, `Deselected` | — |
| `municipal_permit_number` | text | single | — | — |
| `municipality_type` | text (picklist) | single | `BOROUGH`, `TOWNSHIP`, `CITY`, `TOWN` | — |
| `no_pavement_cut` | boolean | single | — | — |
| `offset` | text | single | — | State Road Offset |
| `pa_1_call_bundle` | object (group) | single | — | — |
| `permit` | object (group) | single | — | — |
| `permit_date_submitted` | text (date) | single | — | — |
| `permit_date_updated` | text (date) | single | — | — |
| `permit_fees` | text | single | — | — |
| `permit_follow-up_date` | text (date) | single | — | — |
| `permit_note` | text | single | — | — |
| `permit_number` | text | single | — | — |
| `permit_payment_date` | text (date) | single | — | — |
| `permit_payment_info` | object (table) | single | — | — |
| `permit_payment_status` | text (picklist) | single | `Needs to be paid`, `Paid` | — |
| `permit_pickup` | object (group) | single | — | — |
| `permit_pickup_required` | text (picklist) | single | `field visit required`, `fielding complete`, `pickup fully resolved` | — |
| `permit_type` | text (picklist) | single | `PDOT`, `SW`, `ROW`, `RR`, `MISC`, `TRANS` | — |
| `permits_bundle` | object (group) | single | — | — |
| `permits_unnecessary` | object (group) | single | — | — |
| `plan_and_profile` | list (picklist, multi) | multi | `Max Sag`, `Railroad` | — |
| `plan_and_profile_annotation` | text | single | — | P&P Annotation |
| `plan_and_profile_description` | text | single | — | — |
| `railroad_permit_bundle` | object (group) | single | — | — |
| `railroad_submitted_to` | text (picklist) | single | `Bill Alvarez`, `Nate Andregg`, `Annette Cevis`, `Chelsea Pine`, `Dan Gerber`, `Dan Marston`, `John Shattah`, `Dan Walker`, `Adam Hoover` | — |
| `redline_permit` | text (picklist) | single | `Permit required`, `Resolved` | — |
| `segment` | text | single | — | State Road Segment |
| `segment_offset_bundle` | object (group) | single | — | — |
| `sidewalk_cut_permit` | text (picklist) | single | `Unnecessary`, `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved` | — |
| `speed_limit` | text | single | — | — |
| `stake_location` | text (picklist) | single | `Staked`, `Staking Required` | — |
| `state_route` | text | single | — | State Road Number |
| `total_pavement_width_(ft)` | text | single | — | — |
| `trans_undercrossing_permit_status` | text (picklist) | single | `Investigating`, `Required`, `Submitted`, `Attacher Obtained`, `Approved`, `Rejected`, `Unnecessary`, `Investigated; deemed unnecessary`, `Deselected` | — |
| `transmission_attachment` | text (picklist) | single | `Investigating`, `Submitted`, `Approved`, `Rejected` | — |
| `turnpike_permit_status` | text (picklist) | single | `Investigating`, `Unnecessary`, `Contacted PPL`, `Submitted`, `Approved`, `Canceled`, `Revisions Required`, `Deselected`, `Investigated; deemed unnecessary`, `Resubmitted` | — |
| `utility_sketch` | file | single | — | — |
| `vehicle_damage` | boolean | single | — | — |
| `vehicle_protection` | text (picklist) | single | `Guiderail`, `Curb`, `None` | — |
| `working_on_permit` | text | single | — | — |

## Pole Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `AT&T_RSRP` | text | single | — | Signal Strength |
| `AT&T_RSRQ` | text | single | — | Signal Strength |
| `SmartGrid` | object (group) | single | — | — |
| `Verizon_RSRP` | text | single | — | Signal Strength |
| `Verizon_RSRQ` | text | single | — | Signal Strength |
| `banner_pole_loading` | boolean | single | — | — |
| `banner_pole_normal` | boolean | single | — | — |
| `banner_pole_over_limit` | boolean | single | — | — |
| `current_limiting_fuse_area` | text (picklist) | single | `Yes`, `No` | — |
| `existing_attachers` | object (table) | single | — | — |
| `face_of_pole` | text | single | — | — |
| `field_tag` | text | single | — | If field tag does not match |
| `general_job_size` | text | single | — | — |
| `google_elevation` | text | single | — | Elevation data from Google's geographic data |
| `ground_material` | text (picklist) | single | `Asphalt`, `Concrete`, `Yard`, `Other` | — |
| `imported_number_of_attachments` | text (picklist) | single | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20` | — |
| `imported_pole_class` | text (picklist) | single | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `9`, `10`, `H1`, `H2`, `H3`, `H4`, `H5`, `H6` | — |
| `imported_pole_height` | text (picklist) | single | `0`, `5`, `10`, `15`, `20`, `25`, `30`, `35`, `40`, `45`, `50`, `55`, `60`, `65`, `70` | — |
| `laz_file` | file | single | — | — |
| `measured_groundline_circumference` | text | single | — | — |
| `measured_pole_height` | text | single | — | Field measured pole height |
| `missing_pole` | text | single | — | — |
| `other_attachments_on_record` | object (table) | single | — | — |
| `overlapping_note` | text | single | — | — |
| `overlash_at_risk` | boolean | single | — | — |
| `permit_district_number` | text (picklist) | single | `District 1`, `District 2`, `District 3`, `District 4`, `District 5`, `District 6`, `District 7`, `District 8` | — |
| `pole_class` | text (picklist) | single | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `Unknown`, `H1`, `H2`, `H3`, `H4`, `H5`, `H6`, `H7`, `H8` | — |
| `pole_condition` | text (picklist) | single | `A Tag`, `B Tag`, `C Tag`, `White X` | — |
| `pole_height` | text (picklist) | single | `20`, `25`, `30`, `35`, `40`, `45`, `50`, `55`, `60`, `65`, `70`, `75`, `80`, `85`, `90`, `95`, `100`, `105`, `110`, `115`, `120`, `125`, `Unknown` | — |
| `pole_install_date` | text | single | — | installation date of pole |
| `pole_spec` | text (picklist) | single | _247 options — large picklist, pull from model if needed_ | — |
| `pole_species` | text | single | — | Pole Species |
| `pole_status` | text (picklist) | single | `Admin Removed` | — |
| `pole_tag` | pole_tag | single | — | Pole Tag |
| `storm_hardening_required` | boolean | single | — | A indicator that this pole is a part of PPL's underperforming feeders, and needs to be wind loaded. |
| `verify_new_anchor_location` | boolean | single | — | — |
| `wires_on_record` | object (table) | single | — | — |

## Post Construction Inspection

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `COC_feedback` | object (group) | single | — | — |
| `NJUNS_action` | text (picklist) | single | `Trued-up`, `Created new ticket`, `Unchanged`, `Closed out`, `Cloned cancelled ticket`, `Doublewood identified` | — |
| `NJUNS_action_date` | text | single | — | — |
| `NJUNs_ticket_action_table` | object (table) | single | — | — |
| `PCI_date` | text (date) | single | — | — |
| `PCI_doublewood_r1` | text (picklist) | single | `Created new ticket`, `Ticket was trued-up`, `Ticket was closed out`, `Ticket was unchanged`, `Cloned cancelled ticket` | — |
| `PCI_doublewood_r2` | text (picklist) | single | `Created new ticket`, `Ticket was trued-up`, `Ticket was closed out`, `Ticket was unchanged`, `Cloned cancelled ticket` | — |
| `PCI_doublewood_r3` | text (picklist) | single | `Created new ticket`, `Ticket was trued-up`, `Ticket was closed out`, `Ticket was unchanged`, `Cloned cancelled ticket` | — |
| `PCI_doublewood_r4` | text (picklist) | single | `Created new ticket`, `Ticket was trued-up`, `Ticket was closed out`, `Ticket was unchanged`, `Cloned cancelled ticket` | — |
| `PCI_extraction_complete` | boolean | single | — | — |
| `PCI_failure_type` | text (picklist) | single | `Com MR not executed`, `Power MR not executed`, `Com to power MR conversion`, `Issues with original MR`, `Other (see PCI note)` | — |
| `PCI_field_collection_hours` | text | single | — | — |
| `PCI_field_note` | text | single | — | — |
| `PCI_field_overhead_hours` | text | single | — | — |
| `PCI_height_stick_required` | boolean | single | — | — |
| `PCI_note` | text | single | — | — |
| `PCI_photo_upload` | file | single | — | — |
| `PCI_proper_guying_was_installed` | boolean | single | — | — |
| `PCI_random_sample` | boolean | single | — | — |
| `PCI_review` | boolean | single | — | — |
| `PCI_trainee_review` | boolean | single | — | — |
| `SE_unauthorized` | text (picklist) | single | `TRUE`, `FALSE` | — |
| `actions_exist` | boolean | single | — | — |
| `anchor_was_installed` | text (picklist) | single | `No`, `Yes` | — |
| `anchor_was_tested` | text (picklist) | single | `No`, `Yes` | — |
| `binary` | text (picklist) | single | `Yes`, `No` | — |
| `cable_was_bonded` | text (picklist) | single | `No`, `Yes` | — |
| `coms_as_designed` | text (picklist) | single | `Yes`, `No`, `Unsure` | — |
| `date_approved_for_installation` | text (date) | single | — | Date Approved for Installation |
| `date_installed` | text (date) | single | — | Date Installed |
| `down_guy_installed` | text (picklist) | single | `No`, `Yes` | — |
| `down_guy_was_upgraded` | text (picklist) | single | `Yes`, `No` | — |
| `new_attacher_constructed` | text (picklist) | single | `Yes`, `No`, `Unsure` | — |
| `new_attachment_as_designed` | text (picklist) | single | `Yes`, `No`, `Unsure` | — |
| `original_MR` | text | single | — | — |
| `post_construction_inspection` | text (picklist) | single | `Pass`, `Passes; not built as designed`, `Fails`, `Already passed in previous round`, `Not yet constructed`, `Delayed`, `Not Invoiceable`, `Not in Random Sample` | — |
| `post_construction_status` | text (picklist) | single | `ready to field`, `field inspection complete`, `ready for office processing`, `unknown`, `not yet constructed`, `active construction`, `re-inspection required` | — |
| `power_as_designed` | text (picklist) | single | `Yes`, `No`, `Unsure` | — |
| `reinspection` | boolean | single | — | — |
| `seth's_table_attribute_test` | object (table) | single | — | — |
| `upgraded_or_new_anchor` | text (picklist) | single | `New Anchor (Orange)`, `Upgraded Anchor (Blue)`, `Upgraded Down Guy (only)` | Was this an anchor upgrade, a new anchor, or only an upgraded down guy? |

## Review

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `CU_review` | text (picklist) | single | `Pending`, `Re-review Required`, `Fail`, `Pass`, `Not in Random Sample`, `Resolved` | — |
| `MR_failure_type` | text (picklist) | single | `Communications`, `Low Power`, `Open Secondary`, `Guying`, `Streetlight`, `Pole Replacement`, `PPL Annotation`, `Cost Causer` | — |
| `MR_review` | text (picklist) | single | `Pass`, `Node Info Fail`, `Extraction Fail`, `Make Ready Fail`, `Loading Fail`, `Not Reasonable`, `Resolved`, `Re-review Required`, `Pending`, `Not in Random Sample` | MR Review |
| `OT_review` | text (picklist) | single | `Pass`, `Node Info Fail`, `Extraction Fail`, `Make Ready Fail`, `Loading Fail`, `Overlapping Fail`, `Not Reasonable`, `Resolved`, `Re-review Required`, `Pending`, `Not in Random Sample` | — |
| `OT_review_impact` | text (picklist) | single | `Good`, `Mediocre`, `Edgy`, `Poor` | — |
| `PE_review_note` | text | single | — | Note for the PE |
| `pe_review` | text (picklist) | single | `Pending`, `Re-review Required`, `To Spec, Actionable, Reasonable`, `Not to Spec`, `Not Actionable`, `Not Reasonable`, `Not in Random Sample` | PE Review |
| `random_review` | text (picklist) | single | `Pass`, `Fail`, `Resolved` | — |
| `random_review_fail` | object (group) | single | — | — |
| `random_review_failure_type` | list (picklist, multi) | multi | `Photo Quality`, `Extraction`, `Make Ready`, `Pole Loading `, `CUs`, `Data Inconsistency` | — |
| `review_impact` | text (picklist) | single | `Good`, `Mediocre`, `Edgy`, `Poor` | — |

## Tracking

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `internal_note` | text | single | — | general note |
| `invoice_number` | text | single | — | OTMR invoice number |
| `otmr_billing_status` | text (picklist) | single | `Unbilled (action required)`, `Invoice Sent`, `Prepayment Received`, `Fully Accrued`, `PCI Passed - ready for credit`, `Credit Given (done)`, `Pole added in field - Unbilled (action required)`, `Pole does not exist - refund required`, `Deselected - refund required`, `Deselected - no refund required (done)`, `Refunded (done)`, `PCI Failed - no credit to give (done)`, `No MR, Simple - ready for accrual`, `Medium, Complex -  ready for accrual and COGS` | — |

## Ungrouped

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `1st_day_of_work` | text | single | — | 1st Day of Work |
| `ABD_completed` | boolean | single | — | — |
| `CJW_test` | file | single | — | — |
| `Circuit` | text | single | — | enter circuit |
| `ILEC_status` | text (picklist) | single | `Submitting Application`, `Sending Payment`, `In Construction`, `Released` | — |
| `PCI_pole_count` | text | single | — | PCI Pole Count |
| `QC_has_proper_field_photos` | boolean | single | — | — |
| `QC_markers_are_properly_formed` | boolean | single | — | — |
| `QC_wires_are_fully_traced` | boolean | single | — | — |
| `ROW` | object (group) | single | — | — |
| `Reported` | boolean | single | — | — |
| `SE_rebuild_good` | unknown | single | — | — |
| `SE_rebuild_poles` | unknown | single | — | — |
| `Stake_Location` | text (picklist) | single | `Staked`, `Staking Required` | — |
| `VZ_pole_replacement` | text (picklist) | single | `not replaced`, `replaced, not transferred`, `replaced, transferred` | — |
| `added_for_MR` | boolean | single | — | — |
| `added_for_loading` | boolean | single | — | — |
| `address` | text | single | — | — |
| `agreement_number` | text | single | — | — |
| `anc_elevation` | text | single | — | Enter the anchor elevation |
| `anchor_eyes` | text (picklist) | single | `0`, `1`, `2`, `3`, `BUR` | — |
| `anchor_guy` | text | single | — | Anchor & Guy |
| `anchor_spec` | text (picklist) | single | `5/8" Rod`, `3/4" Rod`, `1" Rod`, `1-1/4" Rod`, `AJB TEST SPEC (will be gone soon)` | — |
| `app_number` | text | single | — | App Number |
| `app_status` | text (picklist) | single | _66 options — large picklist, pull from model if needed_ | Status |
| `app_type` | text (picklist) | single | `attachment_application`, `one_touch_make_ready_application`, `overlash_notification`, `rebuild_notification`, `remediation_application`, `removal_notification`, `small_cell_service_request_application`, `unauthorized_attachment_application`, `violation_notification` | App Type |
| `attachment_order` | text | single | — | — |
| `attachment_type` | text (picklist) | single | `Bolted Cable`, `Cabinet`, `Cross-Street Banner`, `Guy (Below Com Space)`, `Guy (In Com Space)`, `Guy (Stub Pole)`, `Holiday Decoration (Lit)`, `Holiday Decoration (Unlit)`, `Mirror`, `Other`, `Overlash Cable`, `Public Sign`, `Service Drop`, `Streetlight`, `Telephone Cable`, `Vertical Banner`, `Violation`, `Wireless Antenna (Bottom)`, `Wireless Antenna (Middle)`, `Wireless Antenna (Top)`, `Cable`, `Miscellaneous`, `Public Alarm Cable`, `Surveillance System Cable`, `Traffic Control Interconnect Cable`, `XSB Guy` | Attachment Type |
| `azmyth_pickup` | boolean | single | — | — |
| `bad_table` | object (table) | single | — | — |
| `basti_table` | object (table) | single | — | — |
| `billable_to_PPL` | boolean | single | — | — |
| `birthmark` | object (group) | single | — | — |
| `blank_attribute_for_map_prints` | text | single | — | — |
| `bond_street_light` | boolean | single | — | — |
| `calculated_groundline_circumference` | text | single | — | enter calculated glc |
| `cluster` | text | single | — | Cluster # |
| `code` | text | single | — | — |
| `color` | text | single | — | — |
| `commit_test` | object (table) | single | — | — |
| `company` | text (picklist) | single | _1966 options — large picklist, pull from model if needed_ | — |
| `confirm_pickup_fielded` | text | single | — | Date & Initials |
| `county` | text | single | — | County |
| `customer_count` | text | single | — | number customers that could be affect |
| `date_submitted` | text (date) | single | — | Date Submitted |
| `deployment_completed` | boolean | single | — | — |
| `description` | text | single | — | description text here |
| `deselected_by_applicant` | text (picklist) | single | `Before MR Estimate`, `After MR Estimate` | — |
| `design_coordination_note` | text | single | — | — |
| `direction` | text (picklist) | single | `North`, `South`, `East`, `West` | — |
| `does_it_add` | object (table) | single | — | — |
| `done` | boolean | single | — | — |
| `drift` | text | single | — | — |
| `due_date` | text (date) | single | — | — |
| `elevation` | text | single | — | elevation of item |
| `end_pole` | text | single | — | — |
| `estimated` | boolean | single | — | — |
| `existing_attach_type` | text (picklist) | single | `Bolted Cable`, `Cabinet`, `Guy (below com space)`, `Guy (in com space)`, `Guy (stub pole)`, `Service Drop`, `Telephone Cable`, `Mirror`, `Vertical Banner`, `Cross Street Banner`, `Camera`, `Public Sign`, `Wireless Antenna (Middle)`, `Wireless Antenna (Bottom)`, `Other`, `Wireless Antenna (Top)`, `Streetlight`, `Holiday Decoration (lit)`, `Holiday Decoration (unlit)` | Type |
| `existing_aux_eye` | text (picklist) | single | `0`, `1`, `2`, `3` | number aux eyes |
| `exists_in_EFD` | boolean | single | — | — |
| `eyes` | text (picklist) | single | `0`, `1`, `2`, `3`, `BUR` | — |
| `feeder` | text | single | — | — |
| `field_completed` | boolean | single | — | — |
| `fielder` | list (picklist, multi) | multi | `smorris`, `jcavallaro`, `hrhoads`, `zschreiber`, `echapman`, `tbabcock`, `mmosemann`, `jmotter`, `abennett`, `bclepper` | — |
| `fielder_feedback_required?` | text (picklist) | single | `Yes`, `No` | — |
| `flag_for_loading` | text (picklist) | single | `worst pole`, `dead-end`, `not loading` | — |
| `flag_for_review` | boolean | single | — | — |
| `foreign_owned` | boolean | single | — | — |
| `found_doublewood` | object (group) | single | — | — |
| `framing_unit` | text (picklist) | single | `1PTLRP 1Ø TANG RIDGE PIN`, `1PTLDRP 1Ø TANG DBL RIDGE PIN`, `1PST-C 1Ø SUSPENSION`, `1PDE-C 1Ø DEADEND`, `3PTLSA 3Ø TANG 8FT SINGLE CROSSARM`, `3PTLSA 3Ø TANG 8FT DOUBLE CROSSARM`, `3PDADE 3Ø DEADEND 8FT DOUBLE CROSSARM`, `3PTLSAA 3Ø TANG 8FT SINGLE ALLEY ARM`, `3PTLDAA 3Ø TANG 8FT DOUBLE ALLEY ARM`, `3PTLSAA 3Ø TANG 10FT SINGLE ALLEY ARM`, `3PTLDAA 3Ø TANG 10FT DOUBLE ALLEY ARM`, `3PST-E 3Ø VERT SUSPENSION`, `3PHFST-E 3Ø VERT DEADEND`, `3PTLVMB 3Ø TANG VERTICAL MOUNTING BRACKET`, `3PCTLVSBM1 3Ø DELTA TANG VERTICAL STANDOFF BRACKET AND RIDGE PIN`, `3PCTLVSBM2 3Ø VERT TANG STANDOFF BRACKETS` | — |
| `grounded` | boolean | single | — | — |
| `guy_id` | text | single | — | — |
| `height_class_bundle` | object (group) | single | — | — |
| `job_name` | text | single | — | job name |
| `job_type` | text | single | — | — |
| `jump_to_job` | job-link | single | — | jump to job |
| `kyle_test_table` | object (table) | single | — | — |
| `lasered_cable_height` | text | single | — | All cable heights, ordered bottom to top |
| `lasered_distance_to_rail` | text | single | — | — |
| `lasered_ground_height` | text | single | — | Rail height for railroad, ground height otherwise |
| `lasered_span_distance` | text | single | — | — |
| `lasered_vertical_distance_to_rail` | object (table) | single | — | — |
| `lean_amount` | text | single | — | Degrees a pole leans over |
| `lean_direction` | text | single | — | Direction that a pole leans towards |
| `lidar_pickup` | boolean | single | — | — |
| `link` | text (url) | single | — | — |
| `loading_ratio` | text | single | — | Loading Percentage |
| `manhours` | text | single | — | manhours |
| `marked_complex` | boolean | single | — | — |
| `measured_elevation` | text | single | — | Elevation data from a GPS device |
| `mr_remove` | boolean | single | — | — |
| `mr_violation` | text | single | — | Make Ready Violation |
| `multi_attr_test_KMG` | list (picklist, multi) | multi | `1`, `2`, `3` | — |
| `municipality` | text | single | — | Municipality |
| `nason's_test` | object (table) | single | — | — |
| `node_sub_type` | text (picklist) | single | `obstacle`, `tel only pole`, `aggregate action item`, `transmission pole`, `Transmission Line`, `Traffic Arm`, `Wire (attached)`, `Wire (unattached)`, `Structure`, `Other` | — |
| `node_type` | text (picklist) | single | `existing anchor`, `new anchor`, `replaced anchor`, `Comcast`, `slack loop`, `splice`, `map note`, `spatial note`, `pole`, `building attachment`, `bridge attachment`, `crossover`, `reference`, `pushbrace`, `doublewood pole`, `midspan takeoff`, `Proposed Setback`, `Original Pole Location`, `Crossing Obstacle`, `RxR signal`, `centerline`, `right of way line`, `break point`, `handhole`, `manhole`, `pad transformer`, `transformer`, `fire hydrant`, `utility pole`, `marker`, `other` | — |
| `note` | text | single | — | Note |
| `obstacle_resolved` | boolean | single | — | Mark this resolved when the data is converted into a photo chip on the section |
| `one_calls` | text | single | — | PA1-Calls |
| `one_touch_category` | text (picklist) | single | `Complex`, `Simple`, `None` | — |
| `overlapping_import` | text (picklist) | single | `Not Applicable`, `Reuse`, `Validation Required`, `Validation Complete` | — |
| `overlash_state` | text (picklist) | single | `No Violations`, `Violations by others`, `NESC change Violation (others)`, `NESC change Violation`, `Violation` | — |
| `photo_name` | text | single | — | photo name |
| `pickup` | object (group) | single | — | — |
| `pickup_description` | text | single | — | Enter Pickup description |
| `pickup_required` | text (picklist) | single | `field visit required`, `fielding complete`, `pickup fully resolved` | — |
| `pole_butt_removed` | text | single | — | Pole Butt Removed |
| `pole_count` | text | single | — | Pole Count |
| `pole_environment` | text (picklist) | single | `Street Side`, `Rear Easement` | — |
| `pole_material` | text | single | — | — |
| `pole_photo` | file | single | — | Pole Photo |
| `pole_replacement` | boolean | single | — | Pole Replacement |
| `pole_tag_text` | text | single | — | Pole Tag Text |
| `ppl_app_no` | text | single | — | — |
| `predesign_completed` | boolean | single | — | — |
| `proposed_rod_size` | text (picklist) | single | — | — |
| `pushbrace` | text (picklist) | single | — | — |
| `recommendation` | text | single | — | recommendation |
| `remarks` | text | single | — | — |
| `remedial_bundle` | object (group) | single | — | — |
| `remove_attach_type` | text (picklist) | single | `Bolted Cable`, `Cabinet`, `Guy (below com space)`, `Guy (in com space)`, `Guy (stub pole)`, `Service Drop`, `Telephone Cable`, `Mirror`, `Vertical Banner`, `Cross Street Banner`, `Camera`, `Public Sign`, `Wireless Antenna - Middle`, `Wireless Antenna - Bottom`, `Other`, `Wireless Antenna - Top`, `Streetlight` | Type |
| `replace_anchor` | object (group) | single | — | — |
| `replacement_checklist` | boolean | single | — | — |
| `rod_size` | text (picklist) | single | `1/2`, `5/8`, `3/4`, `1`, `1-1/4`, `BUR`, `N/A` | — |
| `scheduled_for_data_collection` | boolean | single | — | — |
| `scid` | text | single | — | SCID |
| `scope` | text | single | — | job scope |
| `sdw_multi_test` | list (picklist, multi) | multi | `Option 1`, `Option 2`, `Option 3` | — |
| `sequence` | text | single | — | — |
| `signal_strength_ATT` | text | single | — | signal strength ATT |
| `signal_strength_VZ` | text | single | — | signal strength Verizon |
| `size` | text (picklist) | single | `1/2`, `5/8`, `3/4`, `1`, `1-1/4`, `BUR`, `N/A` | — |
| `sizes_of_attached_dn_guys` | text | single | — | Enter the dn guy size from top to bottom, separated by commas |
| `soil_type` | text (picklist) | single | `Soil Class 1`, `Soil Class 2`, `Soil Class 3`, `Soil Class 4`, `Soil Class 5`, `Soil Class 6` | — |
| `start_pole` | text | single | — | — |
| `state` | text | single | — | state |
| `street_address` | text | single | — | Street Address |
| `street_name` | text | single | — | Street Name |
| `street_number` | text | single | — | Street Number |
| `submission_required` | text (picklist) | single | — | — |
| `submission_status` | text (picklist) | single | `Required`, `Draft`, `Submitted`, `Awaiting Payment`, `Approved`, `Canceled`, `On Hold` | — |
| `submission_type` | text (picklist) | single | `One Touch`, `Complex` | — |
| `submissions` | object (table) | single | — | — |
| `surface_material` | text (picklist) | single | `Concrete`, `Asphalt` | — |
| `syle_override` | text (picklist) | single | `Yellow`, `Red`, `Green` | — |
| `t_-_d` | text | single | — | — |
| `tag_ppl` | text | single | — | ppl grid number |
| `time_bucket` | timer | single | — | — |
| `tokyo_drift` | text | single | — | — |
| `township` | text | single | — | Township |
| `transmission_undercrossing` | boolean | single | — | — |
| `type` | text | single | — | — |
| `update_by` | text | single | — | Update By |
| `vantage_point` | coordinate_capture | single | — | — |
| `verify_location_in_field` | boolean | single | — | — |
| `vertical_distance_to_other_pole` | text | single | — | — |
| `vertical_distance_to_pole` | text | single | — | — |
| `warning` | text | single | — | Warning Message |
| `weather` | text (picklist) | single | `Yes`, `No` | — |
| `weeks_until_due` | text | single | — | — |
| `zip_code` | text | single | — | — |

## Voltage Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `LA_equipment` | text (picklist) | single | `Residential Building`, `Building`, `Antenna`, `Street Light`, `Traffic Light`, `Transformer`, `Transformer Bank` | — |
| `add_for_voltage_analysis` | boolean | single | — | — |
| `load_KVA` | text | single | — | — |
| `power_consumption` | power_consumption | single | — | — |
| `power_supplied` | power_consumption | single | — | — |
| `transformer_energized` | boolean | single | — | — |
| `transformer_spec` | text (picklist) | single | `10 KVA`, `15 KVA`, `25 KVA`, `50 KVA`, `75 KVA`, `100 KVA`, `167 KVA`, `250 KVA`, `Unknown` | — |
| `transformer_tag` | text | single | — | — |
| `vertical_transition` | text | single | — | — |
| `voltage_drop_percentage` | text | single | — | — |
| `voltage_drop_streetlight_bundle` | object (group) | single | — | — |
