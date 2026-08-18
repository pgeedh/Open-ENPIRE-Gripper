# ENPIRE Gripper Design Ecosystem

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![Isaac Sim Ready](https://img.shields.io/badge/NVIDIA-Isaac_Sim_Ready-76B900.svg)](https://developer.nvidia.com/isaac-sim)
[![ROS 2](https://img.shields.io/badge/ROS_2-Humble_%7C_Iron_%7C_Jazzy-22314E.svg)](https://docs.ros.org/)
[![3D Print Ready](https://img.shields.io/badge/3D_Printing-FDM_%7C_SLA_%7C_TPU-orange.svg)](docs/3D_PRINTING_GUIDE.md)
[![Mesh Validation](https://img.shields.io/badge/Mesh_Status-28%2F28_Valid_STLs-success.svg)](scripts/validate_mesh.py)

**Open-source, high-friction, multi-platform 3D printable gripper designs and adapter interfaces for physical AI manipulation research.**

[Getting Started](#-quick-start) • [Robot Arm Adapters](#-supported-robot-arms--adapters) • [3D Model Catalog](#-3d-model-catalog) • [Bill of Materials](#-hardware-bill-of-materials-bom) • [Simulation](#-simulation--urdf) • [Citation](#-citation--attribution)

</div>

---

## 📖 Overview

The **ENPIRE Gripper Ecosystem** originates from NVIDIA GEAR Lab's research framework on **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World** (Wenli Xiao et al., CMU & NVIDIA). 

While the baseline research utilized the **I2RT YAM** robot arm with custom high-friction 3D printed finger tips, this repository expands the design into a **universal multi-arm gripper hardware and simulation platform**. It provides drop-in adapter mounts, modular finger profiles, parametric CAD scripts, and URDF simulation definitions for all leading physical AI and collaborative robotic arms.

```
       ┌─────────────────────────────────────────────────────────┐
       │                   ENPIRE Gripper Hub                    │
       └────────────────────────────┬────────────────────────────┘
                                    │
    ┌────────────────┬──────────────┼──────────────┬────────────────┐
    ▼                ▼              ▼              ▼                ▼
[ I2RT YAM ]  [ AgileX Piper ] [ Robotiq ]  [ Franka Panda ] [ SO-100 / ALOHA ]
 (Baseline)     (Bimanual AI)  (2F-85 / 140)   (7-DoF Cobot)    (Low-Cost Open)
```

---

## 🦾 Supported Robot Arms & Adapters

| Robot Platform | Arm Type | Mounting Standard | Max Continuous Force | Stroke | STL Directory |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **I2RT YAM** | 6-DoF AI Research Arm | Native Dual M3 Clamp | 45 N | 80 mm | [`stl/enpire_i2rt_yam/`](stl/enpire_i2rt_yam/) |
| **AgileX Piper** | 6-DoF Lightweight Bimanual | Dual Pin + M3 Fasteners | 35 N | 70 mm | [`stl/agilex_piper/`](stl/agilex_piper/) |
| **Robotiq 2F-85** | Industrial 2-Finger Gripper | 2× M4 Bracket Mount | 85 N | 85 mm | [`stl/robotiq_2f85_2f140/`](stl/robotiq_2f85_2f140/) |
| **Robotiq 2F-140** | Long-Stroke Industrial Gripper | 2× M4 Bracket Mount | 85 N | 140 mm | [`stl/robotiq_2f85_2f140/`](stl/robotiq_2f85_2f140/) |
| **Franka Emika Panda / FR3** | 7-DoF Research Cobot | Quick-Mount Dovetail / M4 | 70 N | 80 mm | [`stl/franka_panda/`](stl/franka_panda/) |
| **SO-100 / Mobile ALOHA** | Low-Cost 3D Printed Arm | Servo Horn Spline Clamp | 15 N | 60 mm | [`stl/mobile_aloha_so100/`](stl/mobile_aloha_so100/) |
| **ARX5 / ARX Series** | 5/6-DoF Bimanual Arm | Direct Dual Lug M3 | 40 N | 75 mm | [`stl/arx5/`](stl/arx5/) |
| **Universal Robots (UR3e/5e/10e)** | Industrial Cobots | ISO 9409-1-50-4-M6 Flange | 120 N | N/A | [`stl/iso_flange_adapters/`](stl/iso_flange_adapters/) |
| **UFactory xArm 6 / 7** | Collaborative Arm | ISO 9409-1-50-4-M6 Flange | 100 N | N/A | [`stl/iso_flange_adapters/`](stl/iso_flange_adapters/) |

*See [docs/ROBOT_COMPATIBILITY.md](docs/ROBOT_COMPATIBILITY.md) for full mechanical drawings, bolt hole PCD dimensions, and payload ratings.*

---

## 📦 3D Model Catalog

All models are provided as watertight, manifold binary `.stl` files generated in standard millimeter units.

### 1. I2RT YAM Native ENPIRE Fingers (`stl/enpire_i2rt_yam/`)
- `enpire_yam_finger_standard_left.stl` / `..._right.stl`: Standard research finger with M3 fastener counterbores.
- `enpire_yam_finger_grooved_high_friction.stl`: Anti-slip ribbed profile for grasping cylindrical / slippery items.
- `enpire_yam_finger_precision_pinch.stl`: Tapered narrow tip for picking micro-objects and precision assembly.
- `enpire_yam_finger_paddle.stl`: Broad surface area paddle for compliant box/package handling.

### 2. AgileX Piper Gripper Adapters (`stl/agilex_piper/`)
- `piper_enpire_finger_adapter_left.stl` / `..._right.stl`: Direct bolt-on replacement for Piper gripper carriages.
- `piper_enpire_finger_v_groove.stl`: V-notch clamping finger for tubes, cables, and cylindrical labware.
- `piper_enpire_finger_slim.stl`: Narrow profile finger for tight workspace clearances.

### 3. Robotiq 2F-85 / 2F-140 Adapters (`stl/robotiq_2f85_2f140/`)
- `robotiq_enpire_bracket_left.stl` / `..._right.stl`: 2-bolt M4 mounting bracket for Robotiq slider links.
- `robotiq_enpire_finger_extended.stl`: Extended-reach (94mm) finger for deep-bin picking.
- `robotiq_enpire_finger_heavy_duty.stl`: Reinforced beam for maximum payload clamping.

### 4. Franka Emika Panda / FR3 (`stl/franka_panda/`)
- `franka_enpire_finger_left.stl` / `..._right.stl`: Franka hand slider dovetail mount.
- `franka_enpire_finger_soft_tip.stl`: Recessed seat for snap-in TPU compliant pads.

### 5. SO-100 & Mobile ALOHA (`stl/mobile_aloha_so100/`)
- `so100_enpire_finger_left.stl` / `..._right.stl`: Feetech / STS3215 servo horn gripper finger.
- `so100_enpire_finger_wide.stl`: High-surface paddle variant for bimanual imitation learning.

### 6. Universal Tool Flange Plates (`stl/iso_flange_adapters/`)
- `iso_9409_1_50_4_m6_plate.stl`: 50mm PCD 4-bolt M6 adapter (UR3e/5e/10e, xArm, Doosan, Elite).
- `iso_9409_1_31_5_4_m5_plate.stl`: 31.5mm PCD 4-bolt M5 adapter for compact arms.

### 7. High-Friction Pads & Silicone Molds (`stl/accessories_and_pads/`)
- `tpu_snap_pad_standard.stl` / `tpu_snap_pad_ridged.stl`: Flexible snap-in friction pads for TPU 85A/95A.
- `silicone_mold_finger_cavity.stl` / `silicone_mold_finger_core.stl`: 2-piece casting mold for high-grip silicone tips (Smooth-On Dragon Skin / Ecoflex).

---

## 🛠️ Hardware Bill of Materials (BOM)

| Item | Spec | Quantity | Usage |
| :--- | :--- | :---: | :--- |
| **M3 Socket Head Cap Screws** | M3 × 12mm (DIN 912) | 4 | Base finger mount (YAM / Piper) |
| **M4 Socket Head Cap Screws** | M4 × 16mm (DIN 912) | 4 | Robotiq 2F-85/140 bracket |
| **M6 Socket Head Cap Screws** | M6 × 16mm (DIN 912) | 4 | ISO 9409-1 Flange to Robot Wrist |
| **M3 Brass Heat-Set Inserts** | M3 × 4mm (OD 4.6mm) | 4–8 | Finger mounting blocks |
| **Filament: Structural** | PETG-CF / PLA-CF / PA12-CF | ~200g | Main finger bodies & brackets |
| **Filament: High Friction** | TPU 85A or TPU 95A | ~50g | Snap-in contact pads |
| **Liquid Silicone (Optional)** | Smooth-On Dragon Skin 20 | ~50ml | Cast soft fingertip pads |

*See [docs/HARDWARE_BOM.md](docs/HARDWARE_BOM.md) for torque specifications and vendor details.*

---

## 🖨️ 3D Printing & Fabrication Guide

```
Recommended Slicer Profile (Bambu Studio / PrusaSlicer / OrcaSlicer):
├── Layer Height: 0.16mm - 0.20mm
├── Walls / Perimeters: 5 - 6 walls (CRITICAL for shear strength)
├── Infill Density: 40% - 60% (Gyroid or Cubic)
├── Top/Bottom Layers: 5 top, 5 bottom
└── Orientation: Print fingers horizontally on their lateral side
```

*See [docs/3D_PRINTING_GUIDE.md](docs/3D_PRINTING_GUIDE.md) for full slicer profiles, temperatures, and post-processing steps.*

---

## 🤖 Simulation & URDF

Standalone URDF models and modular Xacro macros are located in `urdf/`:

```
urdf/
├── enpire_gripper.urdf.xacro    # Parameterized modular macro for ROS / ROS 2
├── enpire_yam_gripper.urdf       # Standalone URDF for I2RT YAM
├── enpire_piper_gripper.urdf     # Standalone URDF for AgileX Piper
├── enpire_robotiq_gripper.urdf   # Standalone URDF for Robotiq 2F-85
├── enpire_franka_gripper.urdf    # Standalone URDF for Franka Panda
└── enpire_so100_gripper.urdf     # Standalone URDF for SO-100
```

### NVIDIA Isaac Sim Quickstart
1. Open **Isaac Utils** -> **URDF Importer**.
2. Select `urdf/enpire_yam_gripper.urdf`.
3. Check **Convex Decomposition** and **Self Collision**.
4. Click **Import**.

*See [docs/SIMULATION_GUIDE.md](docs/SIMULATION_GUIDE.md) for Isaac Lab Python snippets and MoveIt 2 configs.*

---

## 💻 Parametric CAD & Mesh Tools

Generate, customize, or validate all 3D models programmatically:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Regenerate all 28 binary STL models
python3 scripts/generate_stls.py

# 3. Validate watertightness, volume, and bounding boxes
python3 scripts/validate_mesh.py

# 4. Generate & validate simulation URDFs
python3 scripts/export_urdf.py
```

### Parametric Customization via OpenSCAD
Open `cad/open_scad/enpire_parametric_finger.scad` in [OpenSCAD](https://openscad.org/) to customize:
- `finger_length` (e.g. 50mm to 120mm)
- `screw_type` (`M2.5`, `M3`, `M4`, `M5`)
- `screw_spacing` and `counterbore_depth`
- `grip_texture` (`smooth`, `grooved`, `v_notch`, `tpu_slot`, `silicone_pocket`)

---

## 📚 Citation & Attribution

If you utilize the ENPIRE gripper designs in your robotics research, please cite the foundational ENPIRE paper and this repository:

```bibtex
@article{xiao2024enpire,
  title={ENPIRE: Agentic Robot Policy Self-Improvement in the Real World},
  author={Xiao, Wenli and GEAR Lab and Collaborators},
  journal={arXiv preprint},
  year={2024}
}
```

Original I2RT YAM finger concept by **Wenli Xiao** (CMU / NVIDIA GEAR Lab) via MakerWorld. Multi-arm adapters and parametric ecosystem maintained by the open-source robotics community.

---

## 📄 License

This repository is licensed under the [Apache License, Version 2.0](LICENSE).
