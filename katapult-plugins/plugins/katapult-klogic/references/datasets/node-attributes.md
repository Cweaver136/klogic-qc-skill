# Node attributes — index

All **524** model-specific node attributes, grouped as they are in the model. Generated from the
customer's `model_attributes` by `scripts/build_attribute_catalog.py`.

This index exists so the skill can confirm **whether an attribute exists and how to read it** without
loading every picklist. Markers: `[b]` boolean, `[p]` picklist text, `[m]` multi-instance (loop it with
`LIST_VALUES`), `[o]` object/table/group (holds sub-attributes, not one value), otherwise plain text.

**For picklist values and meanings, read `node-attributes-full.md`** — do that whenever a check compares
an attribute against a specific value, so the exact string is right.

Anything not in this list is not in the model: ask the user, don't guess.

## Aggregate Tracking

`PPL_comment`, `customer_action`[p], `customer_comment`, `resolved`[b]

## Application Info

`PPL_complex_MR`[b], `ROW_exclusion`[b], `job_id`, `new_attach_type`, `op_area`, `pole_app_order`
`pole_owner`[p], `region`, `take_off_pole`[b], `take_off_pole_not_applicable`[b], `take_off_pole_note`

## Directives

`design_category`[p]

## Doublewood

`NJUN_true-up`[b], `PPL_NTG_step`[p], `attachers`, `bucket_truck_access`[p], `close_NJUNS_ticket`[b]
`doublewood_address`, `doublewood_exists`[p], `doublewood_priority`, `doublewood_review`[p]
`doublewood_status`[p], `exception`[p], `location_source`, `material`[p], `nearest_existing_ppl_grid`
`njuns_last_updated`, `pole_pulled`[b], `start_date`, `status`, `steps`[o], `survey_date`, `ticket_id`
`ticket_type_name`, `verified_ready_for_removal`[b]

## Feedback

`contractor_feedback`[o], `contractor_feedback_note`, `contractor_feedback_viewed`[b]
`external_contractor_QA-QC`[b]

## Field Collected Data

`doublewood_conditions`[p]

## Inspection

`unauthorized_att`[p]

## Invoicing

`annotated_by`[p], `applicant_invoice`[p], `fielded_by`[p], `invoice_note`, `original_pole_count`
`subcontract_pickups`[o], `subcontractor_billing`[o]

## Laser Heights

`ht_ground`, `ht_lowest_com_cable`, `ht_lowest_power_cable`, `ht_other_one`, `ht_other_two`
`ht_top_com_cable`, `ht_top_of_pole`, `ht_top_of_pole_tag`, `lt_notes`, `set_gate`

## Load Analysis

`proposed`[b], `transformer_loading`[p], `transformer_loading_notes`, `voltage_drop_checked`[b]

## Loading Analysis

`PLA`, `PPL_250C_loading_percentage`, `accepted_failure_direction`, `accepted_loading_percentage`
`baseline_buckling_ratio`, `baseline_failure_direction`, `baseline_guy_loading_ratio`[o]
`baseline_loading_percentage`, `baseline_rod_loading_ratio`[o], `baseline_soil_loading_ratio`[o]
`buckling_ratio`, `buckling_ratio_drift`, `collection_temperature`, `cut_pole`[b]
`effective_groundline_circumference`, `failure_direction`, `failure_direction_diff`
`failure_direction_drift`, `guy_loading_ratio`[o], `guy_loading_ratio_drift`[o], `katapult_loading`[o]
`kpla_drift_present`[b], `load_case`[p], `loading_analysis`[p], `loading_error`[b], `loading_notes`
`loading_percentage`, `loading_percentage_diff`, `loading_percentage_drift`, `loading_result`[p]
`loading_zone`[p], `proposed_uplift`, `rod_loading_ratio`[o], `rod_loading_ratio_drift`[o]
`soil_loading_ratio`[o], `soil_loading_ratio_drift`[o], `uplift_if_this_pole_doesnt_change`
`wind_loading_result`[p]

## Make Ready

`CUs_completed`[b], `FCC_category`[p], `MRE_estimated_cost`, `MRE_estimation`[p], `MR_bundle`[o]
`PPL_construction_spec`[m], `Visual_Inspection`[p], `bucket_truck_accessible`[b]
`checked_for_adjacent_vsbs`[b], `complex_category`[p], `complex_reason`[m], `cost_causer`
`cost_causer_note`, `customer_directive`, `foreign_utility_make_ready`, `grounding_present`[p]
`maintenance_email`[p], `mr_category`[p], `mr_note`, `mr_state`[p], `one_touch_summary`[o]
`original_mr_category`[p], `overlapping_work`[p], `post_construction_proposed`[p], `power_mr_annotation`
`ppl_make_ready`, `proposed_pole_spec`[p], `pwr_mr_required`[b], `reason_for_replacement`[m]
`remedial_make_ready_required`[b], `remedial_mr_note`, `replacement_notes`, `replacement_process`[p]
`seth_testing_complex_reason`[p], `street_view_com_count`[p], `total_pole_cut_length`, `traffic_control`[p]
`unauthorized_email`[p], `work_location`, `zach_pilot`[o]

## PA 1 Call

`PA_1_call`, `PA_1_call_api_request_sent`[b], `PA_1_call_required`[b], `intersecting_street`
`location_description`, `location_of_work`[m]

## PPL Package

`%cap`, `PPL_package_note`, `foreign_utility_replacements_WO`, `package_completed`[b], `wo_number`

## Permit Info

`ADA_clearance`, `FAA_permit_status`[p], `LOJ`[b], `PATA`[p], `PPL_ROW_status`[p], `PPL_approval`[p]
`PennDOT_app_number`, `PennDOT_district`[p], `PennDOT_expiration_date`, `PennDOT_grade`[p]
`PennDOT_municipal_code`, `PennDOT_north`[p], `PennDOT_permit_status`[p], `PennDOT_response_letter`
`PennDOT_roadside`[p], `PennDOT_setback`, `PennDot_revision_date`, `PennDot_revision_reasons`[m]
`PennDot_revisions`[m], `ROW_record`, `ROW_record_page`, `ROW_width`, `RxR_LiDAR_scan_file`
`RxR_crossing_number`, `RxR_inventory_report`, `RxR_lidar_scan`[p], `RxR_mailing_address`, `RxR_name`[p]
`RxR_pass_through_fees_(PPL)`, `RxR_permit_info`[o], `RxR_permit_status`[p], `RxR_plan_and_profile`
`RxR_road_ROW_status`[p], `RxR_val_map_status`[p], `RxR_valuation_map`, `SE_ft`, `anchor_CL_ft`
`anchor_installation`[b], `attacher_approval`[p], `average_annual_daily_traffic`, `cl_ft`
`clear_zone_distance`, `comcast_PennDOT_status`[p], `confirm_pickup_fielded_(Permits)`, `custom_note`[b]
`custom_utility_sketch_note`, `description_(Permits)`, `drawn_by`, `environmental_permit_status`[p]
`eop_ft`, `extensions_submitted`[p], `fielder_(Permit_pickup)`[m], `gr_ft`, `guiderail_type`[p]
`include_in_multi_pole_sketch`[b], `letter_of_justification`, `location_photo`, `map_app_link`
`meets_clear_zone`[b], `misc_permit_requires_plan_profile`[b], `misc_permit_status`[p]
`municipal_mailing_address`, `municipal_payment_status`[p], `municipal_permit`[p], `municipal_permit_number`
`municipality_type`[p], `no_pavement_cut`[b], `offset`, `pa_1_call_bundle`[o], `permit`[o]
`permit_date_submitted`, `permit_date_updated`, `permit_fees`, `permit_follow-up_date`, `permit_note`
`permit_number`, `permit_payment_date`, `permit_payment_info`[o], `permit_payment_status`[p]
`permit_pickup`[o], `permit_pickup_required`[p], `permit_type`[p], `permits_bundle`[o]
`permits_unnecessary`[o], `plan_and_profile`[m], `plan_and_profile_annotation`
`plan_and_profile_description`, `railroad_permit_bundle`[o], `railroad_submitted_to`[p], `redline_permit`[p]
`segment`, `segment_offset_bundle`[o], `sidewalk_cut_permit`[p], `speed_limit`, `stake_location`[p]
`state_route`, `total_pavement_width_(ft)`, `trans_undercrossing_permit_status`[p]
`transmission_attachment`[p], `turnpike_permit_status`[p], `utility_sketch`, `vehicle_damage`[b]
`vehicle_protection`[p], `working_on_permit`

## Pole Info

`AT&T_RSRP`, `AT&T_RSRQ`, `SmartGrid`[o], `Verizon_RSRP`, `Verizon_RSRQ`, `banner_pole_loading`[b]
`banner_pole_normal`[b], `banner_pole_over_limit`[b], `current_limiting_fuse_area`[p]
`existing_attachers`[o], `face_of_pole`, `field_tag`, `general_job_size`, `google_elevation`
`ground_material`[p], `imported_number_of_attachments`[p], `imported_pole_class`[p]
`imported_pole_height`[p], `laz_file`, `measured_groundline_circumference`, `measured_pole_height`
`missing_pole`, `other_attachments_on_record`[o], `overlapping_note`, `overlash_at_risk`[b]
`permit_district_number`[p], `pole_class`[p], `pole_condition`[p], `pole_height`[p], `pole_install_date`
`pole_spec`[p], `pole_species`, `pole_status`[p], `pole_tag`, `storm_hardening_required`[b]
`verify_new_anchor_location`[b], `wires_on_record`[o]

## Post Construction Inspection

`COC_feedback`[o], `NJUNS_action`[p], `NJUNS_action_date`, `NJUNs_ticket_action_table`[o], `PCI_date`
`PCI_doublewood_r1`[p], `PCI_doublewood_r2`[p], `PCI_doublewood_r3`[p], `PCI_doublewood_r4`[p]
`PCI_extraction_complete`[b], `PCI_failure_type`[p], `PCI_field_collection_hours`, `PCI_field_note`
`PCI_field_overhead_hours`, `PCI_height_stick_required`[b], `PCI_note`, `PCI_photo_upload`
`PCI_proper_guying_was_installed`[b], `PCI_random_sample`[b], `PCI_review`[b], `PCI_trainee_review`[b]
`SE_unauthorized`[p], `actions_exist`[b], `anchor_was_installed`[p], `anchor_was_tested`[p], `binary`[p]
`cable_was_bonded`[p], `coms_as_designed`[p], `date_approved_for_installation`, `date_installed`
`down_guy_installed`[p], `down_guy_was_upgraded`[p], `new_attacher_constructed`[p]
`new_attachment_as_designed`[p], `original_MR`, `post_construction_inspection`[p]
`post_construction_status`[p], `power_as_designed`[p], `reinspection`[b], `seth's_table_attribute_test`[o]
`upgraded_or_new_anchor`[p]

## Review

`CU_review`[p], `MR_failure_type`[p], `MR_review`[p], `OT_review`[p], `OT_review_impact`[p]
`PE_review_note`, `pe_review`[p], `random_review`[p], `random_review_fail`[o]
`random_review_failure_type`[m], `review_impact`[p]

## Tracking

`internal_note`, `invoice_number`, `otmr_billing_status`[p]

## Ungrouped

`1st_day_of_work`, `ABD_completed`[b], `CJW_test`, `Circuit`, `ILEC_status`[p], `PCI_pole_count`
`QC_has_proper_field_photos`[b], `QC_markers_are_properly_formed`[b], `QC_wires_are_fully_traced`[b]
`ROW`[o], `Reported`[b], `SE_rebuild_good`, `SE_rebuild_poles`, `Stake_Location`[p]
`VZ_pole_replacement`[p], `added_for_MR`[b], `added_for_loading`[b], `address`, `agreement_number`
`anc_elevation`, `anchor_eyes`[p], `anchor_guy`, `anchor_spec`[p], `app_number`, `app_status`[p]
`app_type`[p], `attachment_order`, `attachment_type`[p], `azmyth_pickup`[b], `bad_table`[o]
`basti_table`[o], `billable_to_PPL`[b], `birthmark`[o], `blank_attribute_for_map_prints`
`bond_street_light`[b], `calculated_groundline_circumference`, `cluster`, `code`, `color`, `commit_test`[o]
`company`[p], `confirm_pickup_fielded`, `county`, `customer_count`, `date_submitted`
`deployment_completed`[b], `description`, `deselected_by_applicant`[p], `design_coordination_note`
`direction`[p], `does_it_add`[o], `done`[b], `drift`, `due_date`, `elevation`, `end_pole`, `estimated`[b]
`existing_attach_type`[p], `existing_aux_eye`[p], `exists_in_EFD`[b], `eyes`[p], `feeder`
`field_completed`[b], `fielder`[m], `fielder_feedback_required?`[p], `flag_for_loading`[p]
`flag_for_review`[b], `foreign_owned`[b], `found_doublewood`[o], `framing_unit`[p], `grounded`[b], `guy_id`
`height_class_bundle`[o], `job_name`, `job_type`, `jump_to_job`, `kyle_test_table`[o]
`lasered_cable_height`, `lasered_distance_to_rail`, `lasered_ground_height`, `lasered_span_distance`
`lasered_vertical_distance_to_rail`[o], `lean_amount`, `lean_direction`, `lidar_pickup`[b], `link`
`loading_ratio`, `manhours`, `marked_complex`[b], `measured_elevation`, `mr_remove`[b], `mr_violation`
`multi_attr_test_KMG`[m], `municipality`, `nason's_test`[o], `node_sub_type`[p], `node_type`[p], `note`
`obstacle_resolved`[b], `one_calls`, `one_touch_category`[p], `overlapping_import`[p], `overlash_state`[p]
`photo_name`, `pickup`[o], `pickup_description`, `pickup_required`[p], `pole_butt_removed`, `pole_count`
`pole_environment`[p], `pole_material`, `pole_photo`, `pole_replacement`[b], `pole_tag_text`, `ppl_app_no`
`predesign_completed`[b], `proposed_rod_size`[p], `pushbrace`[p], `recommendation`, `remarks`
`remedial_bundle`[o], `remove_attach_type`[p], `replace_anchor`[o], `replacement_checklist`[b]
`rod_size`[p], `scheduled_for_data_collection`[b], `scid`, `scope`, `sdw_multi_test`[m], `sequence`
`signal_strength_ATT`, `signal_strength_VZ`, `size`[p], `sizes_of_attached_dn_guys`, `soil_type`[p]
`start_pole`, `state`, `street_address`, `street_name`, `street_number`, `submission_required`[p]
`submission_status`[p], `submission_type`[p], `submissions`[o], `surface_material`[p], `syle_override`[p]
`t_-_d`, `tag_ppl`, `time_bucket`, `tokyo_drift`, `township`, `transmission_undercrossing`[b], `type`
`update_by`, `vantage_point`, `verify_location_in_field`[b], `vertical_distance_to_other_pole`
`vertical_distance_to_pole`, `warning`, `weather`[p], `weeks_until_due`, `zip_code`

## Voltage Load Analysis

`LA_equipment`[p], `add_for_voltage_analysis`[b], `load_KVA`, `power_consumption`, `power_supplied`
`transformer_energized`[b], `transformer_spec`[p], `transformer_tag`, `vertical_transition`
`voltage_drop_percentage`, `voltage_drop_streetlight_bundle`[o]
