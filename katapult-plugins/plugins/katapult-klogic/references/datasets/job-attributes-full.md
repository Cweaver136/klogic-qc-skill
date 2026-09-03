# Job attribute catalog (generated)

Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.
Source of truth for model-specific `job` attributes. Read single-valued attributes with a
trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item
operator. Table/group attributes hold sub-attributes, not a single value.

If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export.

## Aggregate Tracking

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `job_link` | text | single | — | — |

## Application Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `advance_attachment_approval_doc` | file | single | — | — |
| `date_OTMR_construction_start` | text (date) | single | — | — |
| `engineering_closeout` | object (group) | single | — | — |
| `op_area` | text | single | — | PPL Operating Area |
| `region` | text | single | — | PPL Region |

## Asset Suite & Designer

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `overlapping_bundle` | object (group) | single | — | — |

## Invoicing

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `MCS_billing_complete` | boolean | single | — | — |
| `MRC_invoice_sent` | boolean | single | — | — |
| `MR_engineering_invoice_amount` | text | single | — | MR Engineering Invoice Amount |
| `capital_dollars` | text | single | — | — |
| `construction_hours` | text | single | — | — |
| `date_payment_received` | text (date) | single | — | Date Payment Received |
| `date_to_accept_MR_estimate` | text (date) | single | — | — |
| `engineering_quote_number` | text | single | — | Engineering Quote Number |
| `expense_dollars` | text | single | — | — |
| `field_billable_hours` | text | single | — | — |
| `final_design_invoice_date` | text (date) | single | — | — |
| `flagging_hours` | text | single | — | — |
| `invoice_data` | object | single | — | — |
| `mr_construction_estimate` | text | single | — | MR Construction Estimate |
| `mr_construction_invoice` | text | single | — | — |
| `mr_construction_invoice_applicant` | text | single | — | MR Construction Invoice (Applicant) |
| `mr_engineering_actual` | text | single | — | MR Engineering Actual |
| `mr_engineering_invoice` | text | single | — | MR Engineering Invoice |
| `mr_pole_count` | text | single | — | MR Pole Count |
| `office_billable_hours` | text | single | — | — |
| `one_touch_PPL_payment_sent` | text (date) | single | — | — |
| `one_touch_poles_engineered` | text | single | — | number of poles |
| `one_touch_poles_paid` | text | single | — | number of poles |
| `original_pole_count` | text | single | — | Original Pole Count |
| `pass_through_fee_date` | text (date) | single | — | — |
| `pre_existing_violation_invoices_foreign` | text | single | — | Pre-Existing Violation Invoices (Foreign) |
| `pre_existing_violation_ppl_costs` | text | single | — | Pre-Existing Violation PPL Absorbed Costs |
| `remediation_billable_hours` | text | single | — | — |
| `senior_designer_billable_hours` | text | single | — | — |
| `survey_invoice_date` | text (date) | single | — | — |

## Job Dashboard

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `QC_general_check` | boolean | single | — | — |
| `QC_job_has_sufficient_cable_tags` | boolean | single | — | — |
| `assigned_to` | user-dropdown | single | — | — |
| `deployment_note` | text | single | — | — |
| `task_status` | text (picklist) | single | _50 options — large picklist, pull from model if needed_ | — |

## KPI Metrics

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `OTMR_revenue` | text | single | — | — |
| `accrual_notes` | text | single | — | How much was already accrued? |
| `annotation_COGS` | text | single | — | — |
| `fielding_COGS` | text | single | — | — |
| `foreign_app_submissions` | text (picklist) | single | `Needed`, `Unnecessary`, `Complete` | — |
| `foreign_pole_work` | text (picklist) | single | `None`, `Make Ready`, `Make Ready and Pole Loading` | — |
| `misc_COGS` | text | single | — | — |
| `otmr_accrual` | text (picklist) | single | `Fully Ready`, `Fully Accrued`, `Partial Ready`, `Partial Accrued` | — |
| `sub_COGS_payment_date` | text (date) | single | — | — |
| `subcontractor_COGS` | object (group) | single | — | — |

## Make Ready

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `NonUtilityEntities` | text (picklist) | single | `Yes`, `No` | — |
| `PrivateFacilitiesNotPA1Call` | text (picklist) | single | `Yes`, `No` | — |
| `bucket_truck_accessible` | boolean | single | — | — |
| `comm_mr_required` | boolean | single | — | Communications MR Required? |
| `exit_MR_eng_status` | text (date) | single | — | — |
| `foreign_utility_pole_replacements` | boolean | single | — | Foreign Utility Pole Replacements? |
| `initial_photofirst_complete` | boolean | single | — | — |
| `no_MR` | boolean | single | — | — |
| `overlapping_hold` | boolean | single | — | — |
| `permits_exist?` | boolean | single | — | — |
| `pwr_mr_required` | boolean | single | — | Power MR Required? |
| `survey_available` | boolean | single | — | — |

## PPL Package

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `FU_replacements_design` | text | single | — | — |
| `PPL_package_note` | text | single | — | Infor/Designer Note |
| `PPL_package_status` | text (picklist) | single | `Not Ready`, `Package Entry Required`, `Revisions Required`, `Package Review Required`, `Finished`, `Not Required`, `Other (see note)` | — |
| `RxR_bifurcation` | text | single | — | These poles were bifurcated from APP_XXXXXX - WO #XXXXXXXX - Engineering was paid for as part of WO #XXXXXXXX please do not bill as part of new WO # |
| `design_change_coordination_status` | text (picklist) | single | `Pending Confirmation`, `Confirmed` | — |
| `design_changed_since_rideout` | text (picklist) | single | `Needs Attention`, `Resolved` | — |
| `design_number` | text | single | — | — |
| `ethan_bundle` | object (group) | single | — | — |
| `foreign_utility_replacements_WO` | text | single | — | Enter Foreign Utility Work Order |
| `impacted_streams_wetlands_waterways` | text (picklist) | single | `Yes`, `No` | — |
| `job_address` | text | single | — | Address |
| `overlapping_polygon` | text | single | — | Polygon # |
| `overlapping_polygon_status` | text (picklist) | single | `None Found`, `Found: not relevant`, `Found: in progress`, `Found: resolved` | — |
| `overlapping_polygons_checked` | boolean | single | — | — |
| `package_reviewed` | boolean | single | — | — |
| `project_number` | text | single | — | Project Number |
| `revision_note` | text | single | — | Revision Notes |
| `revisions_required` | text (picklist) | single | `Revisions in Process`, `Revisions Complete` | — |
| `wo_number` | text | single | — | WO Number |
| `work_holds` | text | single | — | Ex. PLH, FUW, TT, IRQ, and ORCA |

## Permit Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ROW_plans` | text | single | — | — |
| `contact_person` | text | single | — | Contact Person |
| `drawn_by` | text | single | — | — |

## Post Construction Inspection

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ABD_span_count` | text | single | — | — |
| `ADB_pole_count` | text | single | — | — |
| `PCI_1_date` | text | single | — | Date of First Inspection |
| `PCI_2_date` | text | single | — | Date of Second Inspection |
| `PCI_3_date` | text | single | — | Date of Third Inspection |
| `PCI_4_date` | text | single | — | Date of Fourth Inspection |
| `PCI_MCS_billing_complete` | boolean | single | — | — |
| `PCI_build_matches_submission_plan` | boolean | single | — | — |
| `PCI_count` | text | single | — | — |
| `PCI_defect_WO_number` | text | single | — | WO Number |
| `PCI_ensured_MR_completion_by_existing_attachers` | boolean | single | — | — |
| `PCI_extraction_complete` | boolean | single | — | — |
| `PCI_field_billable_hours` | text | single | — | — |
| `PCI_invoice` | pci-invoice | single | — | — |
| `PCI_notification_bundle` | object (group) | single | — | — |
| `PCI_passed_NESC_safety_check` | boolean | single | — | — |
| `PCI_proper_guying_was_installed` | boolean | single | — | — |
| `PCI_results` | object (table) | single | — | — |
| `PCI_status` | text (picklist) | single | `Not Prepped`, `ABD`, `PCI Routine`, `Remediation Required`, `Closeout`, `Delivered`, `Complete`, `Not Yet Constructed`, `Not Invoiceable (Complete)`, `Needs Remediation Application`, `PPL Issues List`, `Awaiting PPL Work Completion`, `Remediation Review`, `Noncompliant Attachment` | — |
| `actions_exist` | boolean | single | — | — |
| `date_approved_for_installation` | text (date) | single | — | Date Approved for Installation |
| `date_installed` | text (date) | single | — | Date Installed |
| `date_marked_noncompliant` | text (date) | single | — | — |
| `date_removed` | text (date) | single | — | — |
| `include_midspans_for_PCI` | boolean | single | — | — |
| `invoice_status` | text (picklist) | single | `Ready for Invoicing`, `Not Invoicing`, `Sent` | — |
| `poles_built_correctly_in_app` | text | single | — | — |
| `reinspection` | boolean | single | — | — |
| `seth's_table_attribute_test` | object (table) | single | — | — |

## Revisions

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `mr_revision_file` | file | single | — | — |
| `mr_revision_notes` | text | single | — | Add revisions notes |
| `mr_revisions_required` | boolean | single | — | — |
| `package_revisions_required?` | boolean | single | — | — |
| `permit_revisions_required?` | boolean | single | — | — |
| `post_rideout_revisions` | boolean | single | — | — |
| `revision_bundle` | object (group) | single | — | — |
| `revision_status` | text (picklist) | single | `Make Ready needed`, `CU's needed`, `Permits needed`, `Package revisions needed`, `Ready to Deliver`, `Revisions Complete` | — |

## Tracking

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `60_day_payment_timeout` | boolean | single | — | — |
| `FCC_-_RCA` | object (group) | single | — | — |
| `FCC_-_RCA_picklist` | list (picklist, multi) | multi | `1 - Design Coordination - Utility Coordination Required`, `2 - PennDOT Permit`, `3 - Private ROW Permit`, `4 - Municipal Permit`, `5 - RxR Permit`, `6 - Pickups`, `7 - Design Coordination - Applicant Approval Required`, `8 - Application Marked "Paid" Late`, `9 - Overlapping Hold`, `10 - Transmission Attachment Approval`, `11 - Other (See Note)` | — |
| `OTMR_done_(Day)` | text (picklist) | single | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31` | — |
| `OTMR_done_(Month)` | text (picklist) | single | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` | — |
| `OTMR_done_(Year)` | text (picklist) | single | `2023` | — |
| `OTMR_done_bundle` | object (group) | single | — | — |
| `active_construction_issues` | text (picklist) | single | `Redline`, `Permit`, `In Review`, `Resolved`, `Respond Via email`, `Awaiting Attacher Decision` | — |
| `application_submission_completed` | boolean | single | — | — |
| `closeout_tracking_attributes` | object (group) | single | — | — |
| `data_collection_company` | text (picklist) | single | `Katapult Engineering`, `Universal`, `UNDC`, `Intern team`, `Grizzly`, `Other` | — |
| `date_MR_construction_complete` | text (date) | single | — | Date MR Construction Complete |
| `date_OTMR_submitted` | text (date) | single | — | Date OTMR Submitted |
| `date_of_virtual_rideout` | text (date) | single | — | Date of Virtual Rideout |
| `do_closeout` | boolean | single | — | — |
| `do_field` | boolean | single | — | — |
| `do_office` | boolean | single | — | — |
| `emailed_MR_notification` | boolean | single | — | — |
| `impediment_note` | text | single | — | — |
| `internal_note` | text | single | — | general note |
| `one_touch_status` | text (picklist) | single | `Draft`, `Katapult Awaiting Payment`, `Data Collection`, `Engineering`, `Compiling Make Ready`, `Submitting Applications`, `PPL Awaiting Payment`, `Waiting on Permits`, `Resolving Permits`, `Creating PPL Package (3.0)`, `Complex Construction`, `One Touch Construction`, `PCI Data Collection`, `PCI Office`, `Installation Defect Detected`, `Complete`, `On Hold`, `Canceled`, `Predesign`, `Ready For Rideout`, `Ready for Submission`, `Construction`, `Post Rideout Revisions`, `Awaiting Post Construction Inspection` | — |
| `one_touch_tracking_bundle` | object (group) | single | — | — |
| `one_touch_work_complete` | boolean | single | — | — |
| `original_engineering_job` | job_chooser | single | — | Job Id of Original Engineering Job |
| `queued_for_cancellation_timer_expired` | boolean | single | — | — |
| `read_access_shared` | boolean | single | — | — |
| `ready_for_rideout` | boolean | single | — | — |
| `reason_late_-_S&D_(FCC)` | text | single | — | — |
| `reason_late_-_e` | text | single | — | — |
| `redline_notes` | text | single | — | — |
| `redline_status` | text (picklist) | single | `Required`, `In Design`, `Waiting on Pickups`, `External Response Required`, `Waiting on Permits`, `Redlining Package`, `Redline Ready for Delivery`, `Delivered`, `Not Required` | — |
| `revisions_requested` | object (group) | single | — | — |
| `subcontractor_access` | object (group) | single | — | — |
| `submitted_with_integrated_pole_loading` | boolean | single | — | — |
| `tracking_model` | text (picklist) | single | `ppl_standard`, `pci`, `5G`, `one_touch`, `No Project Associated`, `distribution_design` | — |
| `transferred_to_subcontractor` | boolean | single | — | — |
| `virtual_rideout_notes` | text | single | — | Virtual Rideout Notes |
| `working_on_it` | text | single | — | Name |

## Ungrouped

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ABD_pole_count` | text | single | — | — |
| `EGR_payment_not_received` | boolean | single | — | — |
| `GPS_files` | file | single | — | — |
| `MRE_invoice_sent` | boolean | single | — | — |
| `MR_engineering_required?` | boolean | single | — | — |
| `NJUN_ticket_count` | text | single | — | — |
| `OTMR_invoice_status` | text (picklist) | single | `Ready for Invoicing`, `Sent` | — |
| `PCI_amount_invoiced` | text | single | — | — |
| `PCI_cost` | text | single | — | — |
| `PCI_days_left` | text (date) | single | — | — |
| `PCI_inspection_count` | text | single | — | — |
| `PCI_surveys` | text | single | — | — |
| `PPE_present` | text (picklist) | single | `Yes`, `No` | — |
| `PPL_package_complete` | text (date) | single | — | — |
| `active_for_applicant` | boolean | single | — | — |
| `active_for_engineering` | boolean | single | — | — |
| `additional_pole_height` | text | single | — | Additional Pole Height Required (ft) |
| `agree_to_payment_timelines` | boolean | single | — | — |
| `alex_test1` | boolean | single | — | — |
| `app_attach_type` | unknown | single | — | App Attach Type |
| `app_name` | text | single | — | App Name |
| `app_note` | text | single | — | Note |
| `app_number` | text | single | — | App Number |
| `app_queued_for_cancellation` | boolean | single | — | — |
| `app_required_revisions` | text | single | — | Required Revisions |
| `app_review_complete` | boolean | single | — | — |
| `app_revisions` | text | single | — | Applicant Revisions |
| `app_status` | text (picklist) | single | _66 options — large picklist, pull from model if needed_ | Status |
| `app_type` | text (picklist) | single | `attachment_application`, `one_touch_make_ready_application`, `overlash_notification`, `rebuild_notification`, `remediation_application`, `removal_notification`, `small_cell_service_request_application`, `unauthorized_attachment_application`, `violation_notification` | App Type |
| `applicant_cable_type` | text (picklist) | single | `Telco Comm`, `Fiber Optic Comm`, `CATV Comm`, `Comm Drop`, `Traffic Cable`, `Alarm Cable`, `Strand`, `Conductor` | — |
| `attacher_agent` | text | single | — | — |
| `attachment_owner` | text (picklist) | single | — | Attachment Owner |
| `banner_dimensions` | text | single | — | Banner Dimensions |
| `banner_vents` | text | single | — | Number of Banner Vents |
| `billing_address` | text | single | — | — |
| `bundle_size` | text | single | — | Bundle Size |
| `cable_diameter` | text | single | — | Diameter |
| `cable_weight` | text | single | — | Cable Weight |
| `caleb_bundle` | object (group) | single | — | — |
| `complex_mr_eng_end` | text (date) | single | — | — |
| `complex_mr_eng_start` | text (date) | single | — | — |
| `confirm_overlapping_for_delivery` | text | single | — | — |
| `construction_contractor` | text (picklist) | single | `Celerity Integrated Services, Inc.`, `IB Abel, Inc.`, `Infrasource`, `Primoris Electric, Inc.`, `Qualified Contractor (List in Notes)` | Construction Contractor |
| `construction_invoice_amount` | text | single | — | — |
| `construction_prints` | file | single | — | Construction Prints |
| `construction_quote_date` | text (date) | single | — | — |
| `construction_quote_number` | text | single | — | — |
| `contact_email` | text | single | — | — |
| `contact_name` | text | single | — | — |
| `contact_number` | text | single | — | — |
| `create_survey_phase` | boolean | single | — | — |
| `creator` | unknown | single | — | App Creator |
| `data_collection_complete` | text (date) | single | — | — |
| `data_collection_complete_checkbox` | boolean | single | — | — |
| `data_collection_required?` | boolean | single | — | — |
| `date` | text | single | — | Date |
| `date_PCI_done` | text (date) | single | — | — |
| `date_admin_review` | text (date) | single | — | Date Submitted for Admin Review |
| `date_advance_attachment_approved` | text (date) | single | — | — |
| `date_application_complete` | text (date) | single | — | Date Application Complete |
| `date_application_declined` | text (date) | single | — | — |
| `date_application_submitted_for_review` | text (date) | single | — | Date Application Submitted for Review |
| `date_approved_for_removal` | text (date) | single | — | Date Approved for Removal |
| `date_attacher_accepted` | text (date) | single | — | — |
| `date_awaiting_comm_space_mr` | text (date) | single | — | Date Awaiting Comm Space MR |
| `date_awaiting_pci` | text (date) | single | — | — |
| `date_awaiting_power_mr` | text (date) | single | — | Date Awaiting Power Space MR |
| `date_canceled` | text (date) | single | — | Date Canceled |
| `date_cancellation_requested` | text (date) | single | — | — |
| `date_comm_mr_complete` | text (date) | single | — | Date Comm MR Complete |
| `date_compiling_mr` | text (date) | single | — | — |
| `date_completed` | text (date) | single | — | Date Completed |
| `date_creating_package` | text (date) | single | — | — |
| `date_data_collection` | text (date) | single | — | — |
| `date_data_collection_and_mr_eng` | text (date) | single | — | Date Data Collection and MR Eng |
| `date_design_complete` | text (date) | single | — | — |
| `date_draft_submitted` | text (date) | single | — | — |
| `date_estimate_start` | text (date) | single | — | — |
| `date_expiration_extended` | text (date) | single | — | Date Expiration Extended |
| `date_expired` | text (date) | single | — | Date Expired |
| `date_fcc_start` | text (date) | single | — | FCC Start Date |
| `date_foreign_make_ready_start` | text (date) | single | — | — |
| `date_generating_wo` | text (date) | single | — | — |
| `date_installation_defect_detected` | text (date) | single | — | Date Installation Defect Detected |
| `date_invoice_paid` | text (date) | single | — | Please Input Date the Invoice was Paid |
| `date_marked_incomplete` | text (date) | single | — | — |
| `date_mr_cost_statement_accepted` | text (date) | single | — | Date Make Ready Cost Statement Accepted |
| `date_mr_cost_statement_provided` | text (date) | single | — | Date Make Ready Cost Statement Provided |
| `date_mr_eng` | text (date) | single | — | Date Make Ready Engineering |
| `date_mr_engineering_complete` | text (date) | single | — | Date Make Ready Engineering Complete |
| `date_mr_estimate_accepted` | text (date) | single | — | Date Make Ready Estimate Accepted |
| `date_mr_estimate_provided` | text (date) | single | — | Date Make Ready Estimate Provided |
| `date_of_last_invoice` | text | single | — | Please Input Date Invoice was Sent |
| `date_of_unauthorized_attachment_notification` | text (date) | single | — | Unauthorized Attachment Notification Date |
| `date_otmr_construction` | text (date) | single | — | Date of One Touch Construction |
| `date_power_mr_approved` | text (date) | single | — | Date Approved for Power MR |
| `date_power_mr_complete` | text (date) | single | — | Date Power MR Complete |
| `date_power_mr_construction_start` | text (date) | single | — | Date Power MR Construction Start |
| `date_ppl_mr_start` | text (date) | single | — | — |
| `date_quote_submitted` | text (date) | single | — | Date Quote Submitted |
| `date_ready_for_virtual_rideout` | text (date) | single | — | — |
| `date_rejected` | text (date) | single | — | Date Rejected |
| `date_resolving_permits` | text (date) | single | — | — |
| `date_resubmit_per_revisions` | text (date) | single | — | Date Resubmit Per Revisions |
| `date_resubmitted` | text (date) | single | — | Date Resubmitted |
| `date_reviewing_for_completeness_revisions` | text (date) | single | — | — |
| `date_revised` | text (date) | single | — | Date Revised |
| `date_scheduling_otmr_construction` | text (date) | single | — | — |
| `date_start` | text (date) | single | — | Start Date |
| `date_submitted` | text (date) | single | — | Date Submitted |
| `date_verify_comm_mr` | text (date) | single | — | — |
| `date_virtual_rideout_scheduled` | text (date) | single | — | — |
| `date_waiting_on_permits` | text (date) | single | — | Date Waiting on Permits |
| `days_left_in_stage` | unknown | single | — | Days Left in Stage |
| `decoration_dimensions` | text | single | — | Decoration Height and Width |
| `decoration_weight` | text | single | — | Decoration Weight |
| `delivery_-_NO_MR` | object (group) | single | — | — |
| `delivery_-_cost_causer` | object (group) | single | — | — |
| `delivery_-_no_cost_causer` | object (group) | single | — | — |
| `due_date` | text (date) | single | — | — |
| `duplicated_job` | boolean | single | — | — |
| `engineering_active` | boolean | single | — | — |
| `engineering_closeout_complete` | boolean | single | — | — |
| `engineering_contractor` | text (picklist) | single | `davey_resource_group`, `katapult`, `westwood_professional_services` | Engineering Contractor |
| `engineering_status` | text (picklist) | single | `Ready for PMR`, `PMR Complete` | — |
| `existing_cable_owner` | text (picklist) | single | `test`, `pick 2` | — |
| `expiration_date` | text (date) | single | — | Expiration Date |
| `fauna_hazard` | text (picklist) | single | `Yes`, `No` | — |
| `fcc_attacher_acceptance_end` | text (date) | single | — | — |
| `fcc_attacher_acceptance_start` | text (date) | single | — | — |
| `fcc_estimate_end` | text (date) | single | — | — |
| `fcc_estimate_start` | text (date) | single | — | — |
| `fcc_mr_construction_end` | text (date) | single | — | — |
| `fcc_review_app_for_completeness_end` | text (date) | single | — | — |
| `fcc_review_app_for_completeness_start` | text (date) | single | — | — |
| `fcc_survey_and_design_end` | text (date) | single | — | — |
| `fcc_survey_and_design_start` | text (date) | single | — | — |
| `feeder` | text | single | — | — |
| `flora_hazard` | text (picklist) | single | `Yes`, `No` | — |
| `foreign_app_number` | text | single | — | Foreign Application Number |
| `guying_plan_file` | file | single | — | Guying Plan |
| `holiday_decoration_photo_file` | file | single | — | Holiday Decoration Image |
| `intentional_update` | text | single | — | — |
| `invoice_generated` | boolean | single | — | — |
| `invoice_year` | text | single | — | invoice year for bulk admin reporting |
| `is_remediation_engineering_invoiceable?` | boolean | single | — | — |
| `job_package_file` | file | single | — | — |
| `job_package_url` | text (url) | single | — | Job Package URL |
| `last_update_boundary_date` | text | single | — | — |
| `location_hazard` | text (picklist) | single | `Yes`, `No` | — |
| `make_ready_complete_checkbox` | boolean | single | — | — |
| `max_power_consumption` | text | single | — | Max Power Consumption |
| `mr_engineering_post_construction_inspection_cost` | text | single | — | Post Construction Inspection Cost |
| `note` | text | single | — | Note |
| `notified_AR_about_invoicing` | boolean | single | — | — |
| `old_storm_hardening_standard` | boolean | single | — | — |
| `one_touch_target_delivery` | text (date) | single | — | — |
| `other_files` | file | single | — | Other Files |
| `overlapping_applications` | boolean | single | — | — |
| `overlapping_applications_checked_-_ready_to_deliver` | boolean | single | — | — |
| `overlapping_hold_end_date` | text (date) | single | — | — |
| `overlapping_hold_start_date` | text (date) | single | — | — |
| `permit_contact` | text | single | — | Contact info for third-party permits |
| `pole_count` | text | single | — | Pole Count |
| `pole_tag_summary` | text | single | — | Pole Tag Summary |
| `pole_type` | text (picklist) | single | `Secondary Pole`, `Stub Pole`, `Municipal Owned Pole`, `Customer Owned Pole` | Pole Type |
| `ppl_invoice_bundle` | object (group) | single | — | — |
| `projected_field_date` | text | single | — | — |
| `quality_control_type` | text (picklist) | single | `Standard`, `One Touch 3.0` | — |
| `review_contractor` | text (picklist) | single | `davey_resource_group`, `katapult`, `leidos`, `osmose` | — |
| `revisions_checklist_complete` | boolean | single | — | — |
| `revisions_declined` | boolean | single | — | — |
| `row_submission_date` | text | single | — | date for row submission on map prints |
| `safety_and_environmental_assessment` | boolean | single | — | — |
| `scheduled_for_data_collection` | boolean | single | — | — |
| `service_request_WO` | text | single | — | Service Request WO |
| `service_request_amperage` | text (picklist) | single | `100A`, `200A`, `400A`, `600A` | Service Request Amperage |
| `service_request_survey` | text (url) | single | — | Service Request Survey |
| `service_request_voltage` | text (picklist) | single | `120V`, `120/240V` | Service Request Voltage |
| `stamped_eme_study` | file | single | — | Stamped EME Study |
| `strand_size` | text (picklist) | single | `1/4" (6.6M)`, `5/16" (6M)`, `3/8" (10M)`, `1/2" (25M)`, `Other (See Job Notes)` | Strand Size |
| `submitted_by` | text | single | — | — |
| `survey_and_design_complete` | text (date) | single | — | — |
| `timeline_progress` | unknown | single | — | App Timeline |
| `unobstructed_pole` | boolean | single | — | Pole Unobstructed by power equipment or risers |
| `utility_active` | boolean | single | — | — |
| `vertical_banner_photo_file` | file | single | — | Vertical Banner Image |
| `virtual_rideout_complete` | boolean | single | — | — |
| `virtual_rideout_date` | text | single | — | Virtual Rideout Date |
| `virtual_rideout_scheduled` | boolean | single | — | — |
| `wo_created` | text (date) | single | — | — |
| `wr_number` | text | single | — | WR Number |

## Voltage Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `transformer_reports` | file | single | — | Please, upload pole transformer reports! |
