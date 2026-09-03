# Photo attribute catalog (generated)

Auto-generated from a Katapult `model_attributes` export by `scripts/build_attribute_catalog.py`.
Source of truth for model-specific `photo` attributes. Read single-valued attributes with a
trailing `.*`; read `multi` attributes by looping the attribute object with `LIST_VALUES` + an item
operator. Table/group attributes hold sub-attributes, not a single value.

If a check needs an attribute not listed here, the model changed — re-run the generator on a fresh export.

## Doublewood

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `material` | text (picklist) | single | `Soil`, `Asphalt`, `Concrete`, `Sidewalk - Lancaster City`, `Other` | — |

## Inspection

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `unauthorized_att` | text (picklist) | single | `Unauthorized Strand`, `Unauthorized Fiber`, `Unauthorized Equipment`, `Adjacent but not attached (NESC violation)` | — |

## Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `proposed` | boolean | single | — | — |

## Loading Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `proposed_uplift` | text | single | — | — |
| `uplift_if_this_pole_doesnt_change` | text | single | — | — |

## Make Ready

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `grounding_present` | text (picklist) | single | `Grounded`, `Not Grounded`, `Broken`, `Com Only`, `Adjacent Poles`, `Proposed` | — |
| `mr_note` | text | single | — | enter make ready note |
| `post_construction_proposed` | text (picklist) | single | — | — |
| `power_mr_annotation` | text | single | — | Annotation |
| `remedial_make_ready_required` | boolean | single | — | — |
| `remedial_mr_note` | text | single | — | — |

## Pole Info

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `ground_material` | text (picklist) | single | `Asphalt`, `Concrete`, `Yard`, `Other` | — |
| `pole_condition` | text (picklist) | single | `A Tag`, `B Tag`, `C Tag`, `White X` | — |

## Ungrouped

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `anchor_id` | text | single | — | — |
| `antenna_spec` | text (picklist) | single | `standard` | — |
| `arm_length` | text (picklist) | single | `8 FT`, `10 FT`, `Unknown` | — |
| `arm_spec` | text (picklist) | single | `56" Single Cross Arm`, `56" Double Cross Arm`, `8' Single Cross Arm`, `8' Double Cross Arm`, `8' Fiberglass Deadend Cross Arm`, `8' Fiberglass Tangent Cross Arm`, `8' Double Fiberglass Tangent Cross Arm`, `10' Single Cross Arm`, `10' Double Cross Arm`, `10' Fiberglass Tangent Cross Arm`, `10' Fiberglass Deadend Cross Arm`, `10' Double Fiberglass Tangent Cross Arm`, `12' Single Cross Arm`, `12' Double Cross Arm`, `8' Single Alley Arm`, `8' Fiberglass Alley Arm`, `8' Double Alley Arm`, `8' Double Fiberglass Alley Arm`, `10' Single Alley Arm`, `10' Fiberglass Alley Arm`, `10' Double Alley Arm`, `10' Double Fiberglass Alley Arm`, `56" Single Alley Arm`, `56" Double Alley Arm`, `4' Metal Alley Arm`, `Tri Mount Bracket`, `Brace`, `66" Single Cross Arm` | — |
| `assign_MR_to` | node-dropdown | single | — | — |
| `attaches_to_back` | boolean | single | — | — |
| `banner_spec` | text (picklist) | single | `4' x 2'`, `5' x 2'`, `6' x 2'`, `Cross-Street Banner` | — |
| `bearing` | text | single | — | — |
| `box_spec` | text (picklist) | single | `standard` | — |
| `cabinet_spec` | text (picklist) | single | `AT&T (16x30x31)`, `Commscope (20x44x21)` | — |
| `cable_type` | text (picklist) | single | `Telco Com`, `Fiber Optic Com`, `CATV Com`, `Guy`, `Com Drop`, `Traffic Cable`, `Alarm Cable`, `Strand`, `Conductor`, `Eruv`, `Cathodic Protection Cable`, `Primary`, `Neutral`, `Secondary`, `Open Secondary`, `Power Guy`, `ADSS`, `Bundled Primary`, `Street Light Feed`, `Service`, `Static Wire`, `Power Drop` | — |
| `capacitor_spec` | text (picklist) | single | `300 KVAR`, `600 KVAR`, `900 KVAR`, `1200 KVAR` | — |
| `catenary_parameter` | text | single | — | [ft] |
| `catenary_xc` | text | single | — | [ft] |
| `catenary_yc` | text | single | — | [ft] |
| `company` | text (picklist) | single | _1966 options — large picklist, pull from model if needed_ | — |
| `construction_spec` | text (picklist) | single | `-OMN1zY-BhSj_WJiZFrq`, `-OMRvzlLfw5iOk2xcWss`, `-OMIG68lBI63mx56HiQY`, `-OMgV-H-JMJBhSj_WJi_`, `-OMNT4yzSmYpUQ5src6J` | — |
| `cross-sectional_depth` | text | single | — | [in] |
| `cross-sectional_height` | text | single | — | [in] |
| `cross-sectional_width` | text | single | — | [in] |
| `crosses_over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `crossing_cable_type` | text (picklist) | single | `Communications Cable`, `Open Secondary`, `Neutral/ Secondary` | — |
| `current_limiting_fuse` | boolean | single | — | — |
| `custom_equipment` | object (group) | single | — | — |
| `custom_tension` | text | single | — | [lbf] |
| `cutout_arrestor_spec` | text (picklist) | single | `1-LA`, `2-LA`, `3-LA`, `3-CO, 3-LA SWITCH ARM`, `3-CO, 3-LA TRI-MOUNT BKT` | — |
| `cutout_spec` | text (picklist) | single | `standard` | — |
| `cutout_type` | text (picklist) | single | `TFC`, `LBC`, `LBDC`, `Tripsaver`, `Terminal` | — |
| `decorative_lighting_spec` | text (picklist) | single | `Control`, `Bracket` | — |
| `diameter` | calibrated-width | single | — | — |
| `drip_loop_spec` | text (picklist) | single | `Communications`, `Primary`, `Secondary`, `Signal`, `Streetlight`, `Transformer` | — |
| `driveway_type` | text (picklist) | single | `Residential`, `Commercial` | — |
| `equipment_type` | text (picklist) | single | `cabinet`, `capacitor`, `cutout_arrestor`, `drip_loop`, `recloser`, `regulator`, `riser`, `street_light`, `switch`, `transformer`, `transformer_bank`, `router`, `wireless_antenna`, `vertical_banner`, `cross_street_banner`, `3Ø REG BYPASS SWITCHES`, `Camera`, `sidewalk_light`, `ADSS Storage Case`, `Traffic Sign`, `Fuse Holder`, `Decorative Lighting`, `Flag`, `Custom Equipment`, `CATV Amplifier`, `Safety Mirror`, `Primary terminator`, `Early Fault Detection Sensor - 3 Phase`, `Early Fault Detection Sensor - Single Phase`, `Photocontrol Relay`, `Bottom of Spool Bracket` | — |
| `equipment_weight` | text | single | — | [lbs] |
| `existing_total_pole_length` | text | single | — | ft |
| `feeder` | text | single | — | — |
| `fuse_holder_spec` | text (picklist) | single | `Box 12"x19"x8"`, `Can 20"x8"` | — |
| `ground_rod` | boolean | single | — | — |
| `ground_type` | text (picklist) | single | `Asphalt`, `Concrete`, `Grass`, `Soil`, `Water`, `Other`, `Unknown` | — |
| `ground_wire_cut` | boolean | single | — | — |
| `grounded` | boolean | single | — | — |
| `guying_type` | text (picklist) | single | `down guy`, `sidewalk brace`, `pushbrace`, `broken down guy` | — |
| `height` | text | single | — | Calibration Height |
| `horizontal_offset` | text | single | — | [in] |
| `insulated` | boolean | single | — | — |
| `insulator_bob` | boolean | single | — | — |
| `insulator_count` | text (picklist) | single | `single`, `double` | — |
| `insulator_extension` | text (picklist) | single | `14 Inches`, `3 Feet`, `6 Feet` | — |
| `insulator_spec` | text (picklist) | single | `Pin (Crossarm)`, `Pin (Pole Top)`, `Post (Pole Top)`, `Post (Crossarm)`, `Double Pin (Crossarm)`, `Double Pin (Pole Top)`, `Deadend`, `Suspension`, `Vertical Mounting Bracket`, `Vertical Standoff Bracket`, `Plastic Offset Bracket`, `Neutral Deadend`, `Neutral Tangent`, `Neutral Side Tension`, `Secondary Deadend`, `Secondary Tangent`, `Secondary Side Tension`, `3" Spool`, `MDE`, `Three Bolt`, `Extension Ridge Pin`, `Bottom of Spool Bracket`, `Com Deadend` | — |
| `label` | text | single | — | insert text here |
| `load` | boolean | single | — | — |
| `lookup_collection_temperature` | text | single | — | °F |
| `manual_height` | text | single | — | — |
| `measured_height` | text | single | — | — |
| `measurement_of` | text (picklist) | single | `top_bolt`, `bottom_bolt`, `top_of_equipment`, `bottom_of_equipment`, `top_of_bracket`, `bottom_of_bracket`, `antenna` | — |
| `messenger_spec` | text (picklist) | single | `6.6M`, `6M`, `10M`, `16M`, `25M` | — |
| `mr_existing_bolt_hole` | boolean | single | — | — |
| `mr_ignore` | boolean | single | — | — |
| `mr_items` | text (picklist) | single | `metal alley arm support bracket` | — |
| `mr_move` | text | single | — | enter number of inches to move |
| `mr_remove` | boolean | single | — | — |
| `mr_resolved` | boolean | single | — | — |
| `mr_violation` | text | single | — | Make Ready Violation |
| `note` | text | single | — | Note |
| `obstacle` | text (picklist) | single | `Transmission Line`, `Traffic Arm`, `Wire (attached)`, `Wire (unattached)`, `Structure`, `Other` | — |
| `one_touch_complex` | boolean | single | — | — |
| `one_touch_simple` | boolean | single | — | — |
| `operating_voltage` | text | single | — | Operating Voltage |
| `over` | text (picklist) | single | `Yard`, `Brush`, `Sidewalk`, `Tractor Access`, `Driveway`, `Roadway`, `Driveway/Roadway`, `Unknown`, `Railroad`, `Waterway` | — |
| `photo_quality` | text (picklist) | single | `Poor lighting`, `Poor framing`, `Blurry`, `Stick is not straight` | — |
| `photo_type` | text (picklist) | single | `back`, `birthmark`, `cable tag`, `collection details`, `equipment detail`, `grounding`, `groundline circumfirence`, `hallway`, `midspan height`, `miscellaneous`, `osmose`, `pole height`, `rubbish`, `side`, `tag`, `upshot`, `warning` | — |
| `pla_ignore` | boolean | single | — | — |
| `point_load_end` | boolean | single | — | — |
| `pole_environment` | text (picklist) | single | `Street Side`, `Rear Easement` | — |
| `pole_top_extension` | boolean | single | — | — |
| `proposed_anchor_id` | text | single | — | — |
| `proposed_ground` | boolean | single | — | — |
| `proposed_ground_rod` | boolean | single | — | — |
| `proposed_horizontal_offset` | text | single | — | [in] |
| `proposed_in_previous_design` | text (picklist) | single | — | — |
| `proposed_total_pole_length` | text | single | — | ft |
| `proposed_wire_spec` | text (picklist) | single | — | — |
| `pushbrace_spec` | text (picklist) | single | `standard` | — |
| `quantity` | text (picklist) | single | `1`, `2`, `3` | — |
| `recloser_spec` | text (picklist) | single | `1Ø OCR TYPE H`, `1Ø OCR TYPE 4H`, `1Ø OCR TYPE L`, `1Ø OCR TYPE V4L`, `1Ø OCR TYPE D`, `1Ø OCR TYPE E`, `1Ø OCR TYPE 4E`, `1Ø OCR TYPE V4E`, `3Ø OCR TYPE WVE ER`, `3-1Ø OCR TYPE H`, `3-1Ø OCR TYPE 4H`, `3-1Ø OCR TYPE L`, `3-1Ø OCR TYPE V4L`, `3-1Ø OCR TYPE D`, `3-1Ø OCR TYPE E`, `3-1Ø OCR TYPE 4E`, `3-1Ø OCR TYPE V4E`, `S&C INTELLIRUPTER PC` | — |
| `recloser_type` | text (picklist) | single | `Single Phase`, `Three Phase` | — |
| `regulator_spec` | text (picklist) | single | `50A`, `100A`, `150A`, `219A`, `328A`, `548A` | — |
| `reinforcement_type` | text (picklist) | single | `None`, `C-Truss`, `Fiber Wrap`, `Other`, `Unknown` | — |
| `riser_spec` | text (picklist) | single | `1" PVC`, `2" PVC`, `3" PVC`, `4" PVC`, `5" PVC`, `6" PVC`, `1" Metal`, `2" Metal`, `3" Metal`, `4" Metal`, `5" Metal`, `6" Metal` | — |
| `riser_type` | text (picklist) | single | `Primary`, `Secondary`, `Service`, `Communications`, `Control` | — |
| `roadway_type` | text (picklist) | single | `PA Turnpike`, `PA State Road`, `Non-State Road` | — |
| `router_spec` | text (picklist) | single | `AMI` | — |
| `sag_adjustment` | text | single | — | Enter sag adjustment in inches |
| `sailboat_accessible` | text (picklist) | single | `Yes`, `No` | — |
| `sailboat_launch` | text (picklist) | single | `Yes`, `No` | — |
| `shape_factor` | text (picklist) | single | `1.0 cylindrical`, `1.6 flat structure (non-lattice)`, `3.2 sum of faces flat lattice structure`, `2.0 sum of faces round lattice structure` | — |
| `show_on_photo_thumbnail` | boolean | single | — | — |
| `sidewalk_brace_id` | text | single | — | — |
| `sidewalk_brace_spec` | text (picklist) | single | `standard`, `4'`, `5'`, `6'`, `7'`, `8'`, `9'`, `10'`, `11'`, `12'`, `13'`, `14'`, `15'` | — |
| `street_light_bracket_spec` | text (picklist) | single | `2 ft`, `4 ft`, `6 ft`, `8 ft`, `10 ft`, `12 ft`, `14 ft`, `16 ft`, `18 ft`, `20 ft`, `Area Light`, `Flood Light`, `Unknown` | — |
| `street_light_spec` | text (picklist) | single | `1000W Flood`, `1000W Cobra`, `100W Open Bottom`, `Area Light` | — |
| `switch_spec` | text (picklist) | single | `Horizontal Gang Switch`, `Vertical Gang Switch` | — |
| `team_members` | team-members | single | — | — |
| `terminator_phase_operation` | text (picklist) | single | `Joint, Fused`, `Independent, Fused`, `Unfused` | — |
| `terminator_spec` | text (picklist) | single | `standard` | — |
| `total_pole_length` | text | single | — | ft |
| `transformer_bank_spec` | text (picklist) | single | `3-10 KVA (3PH CL MT)`, `3-25 KVA (3PH CL MT)`, `3-50 KVA (3PH CL MT)`, `3-100 KVA (3PH CL MT)`, `3-167 KVA (3PH CL MT)`, `Unknown` | — |
| `use_catenary_tensions` | boolean | single | — | — |
| `user` | user-dropdown | single | — | — |
| `vehicle_access` | text (picklist) | single | `Pedestrian Only`, `Unlikely`, `Prevented`, `Behind Curb` | — |
| `waterway_size` | text (picklist) | single | `<20`, `21-200`, `201-2,000`, `>2,000` | — |
| `wire_bearing` | text | single | — | — |
| `wire_spec` | text (picklist) | single | _81 options — large picklist, pull from model if needed_ | — |
| `wire_tension` | text (picklist) | single | `Full`, `Slack` | **Absence = full tension.** Only `Slack` is reliably set; a wire may be full-tension with the attribute `Full`, empty, or missing. Test slack with `EQUAL(...,"Slack")` and full with `NOT_EQUAL(...,"Slack")`, never `EQUAL(...,"Full")`. Read off the marker (`<wire>.wire_tension`), not the trace. |
| `wireless_antenna_spec` | text (picklist) | single | `Mobilitie Antenna`, `AT&T AEWD/AEWE`, `AT&T Shroud`, `Nokia AEUB`, `Samsung 5G` | — |

## Voltage Load Analysis

| key | type | instances | values | meaning |
|---|---|---|---|---|
| `transformer_spec` | text (picklist) | single | `10 KVA`, `15 KVA`, `25 KVA`, `50 KVA`, `75 KVA`, `100 KVA`, `167 KVA`, `250 KVA`, `Unknown` | — |
