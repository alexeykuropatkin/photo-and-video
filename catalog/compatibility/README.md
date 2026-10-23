# Model-to-model and interface compatibility

Relations must distinguish mount fit, lens image circle coverage, AF/electrical compatibility, camera firmware, physical gimbal clearance, and battery-to-camera power path. Mount compatibility is necessary but **not** sufficient for verified operational compatibility. In `battery-power.yaml`, `manufacturer_confirmed` means the manufacturer states the native pack is supplied/supported. Do not extrapolate to third-party adapters or regulated V-Mount systems without evidence.

A future normalized `relations.yaml` should model evidence/source, test configuration, result (`supported`, `unsupported`, `unknown`, `tested`) and conditions. This folder is intentionally only seeded with verified Sony NP-FZ100 direct-slot relations.
