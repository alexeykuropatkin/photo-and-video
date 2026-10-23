# Weight, dimensions, and assembled camera rigs

## Why measurement conditions matter

A single `weight_g` value is insufficient for cameras and gimbals. Marketing specifications often mean different combinations:

- `bare_body` — body with no removable batteries/cards/accessories (must explicitly state what is excluded).
- `with_battery_and_card` — camera ready to capture without lens, cage or mounting plate.
- `gimbal_head_only` — gimbal without battery grip/QR plate/tripod.
- `assembled_without_tripod` — gimbal with required battery grip and QR plates, excluding fold-out mini tripod.
- `measured_custom` — fully specified physical configuration.

Each measurement carries a stable ID, grams, included/excluded component types, source, and optional tolerance / conditions. Preserve multiple valid measurements; do not choose one universal mass.

## Example scenario and anti-double-counting

The user compares Sony a6700 + pancake 16–50 and Sony A7S III + SEL2470GM on DJI RS 4 Mini / RS 3 Pro **without gimbal mini tripods**. With manufacturer-specified masses using the same conditions:

- Sony A7S III `with_battery_and_card`: approximately 699 g.
- Sony SEL2470GM first-gen lens: 886 g.
- DJI RS 3 Pro `assembled_without_tripod`: approximately 1515 g.
- Total: **3100 g** (699 + 886 + 1515), absent other hardware.

This is a calculated example from known specifications, not confirmation of physical gimbal clearance. Additional ND, cage, cable, counterweight or monitor adds to carried weight, but a separate RED battery on the operator's belt need not add to gimbal motor payload. **Never add the weight of a battery already included in the operational camera specification.**

Do not compute rig compatibility from mass alone: account for center of gravity, motor-arm ranges, cable routing, lens expansion, camera cage clearance and manufacturer/field tests. Return `not_tested` rather than asserting `compatible` from “under payload limit”.

## Batteries

Record nominal vs minimum/maximum voltage, rated energy in Wh, capacity in mAh, manufacturer model, physical weight/dimensions, chemistry, power-output limits, native contact/connector, charging requirements and model variants (standard / high-voltage). The ability to power a camera over an external DC input is different from a mechanically compatible battery slot. Voltage/current regulation and correct pinout are safety-critical.

## Validation checkpoints

Weight values nonnegative, dimension unit explicit, each referenced battery exists, inclusion flags do not conflict within one measurement, selected rig measurement IDs exist, only one mutually exclusive assembled gimbal state is selected, computed motor payload separated from carried weight, and unknown accessory weights disclosed rather than silently treated as zero.
