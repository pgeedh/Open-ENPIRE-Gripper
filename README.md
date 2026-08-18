# Open-ENPIRE-Gripper-NVIDIA

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![NVIDIA GEAR](https://img.shields.io/badge/NVIDIA-GEAR_Lab-76B900.svg?logo=nvidia&logoColor=white)](https://research.nvidia.com/labs/gear/enpire/)
[![NVIDIA Isaac Sim](https://img.shields.io/badge/NVIDIA-Isaac_Sim_%7C_Isaac_Lab-76B900.svg?logo=nvidia&logoColor=white)](https://developer.nvidia.com/isaac-sim)
[![MakerWorld](https://img.shields.io/badge/MakerWorld-Original_Model_%233349177-FF5A00.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)
[![Simulation](https://img.shields.io/badge/Simulation-URDF_%7C_MuJoCo_%7C_ROS_2-purple.svg)](scripts/generate_urdf_from_stl.py)
[![3D Printing](https://img.shields.io/badge/3D_Printing-PA--CF_%7C_PETG--CF_%7C_TPU-orange.svg)](docs/3D_PRINTING_GUIDE.md)
[![Hardware](https://img.shields.io/badge/Hardware-Open_Source-green.svg)](https://github.com/pgeedh/Open-ENPIRE-Gripper-nvidia)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-@NVIDIA-black.svg?logo=x)](https://twitter.com/NVIDIA)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-@DrJimFan-black.svg?logo=x)](https://twitter.com/DrJimFan)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-@YukeZhu-black.svg?logo=x)](https://twitter.com/YukeZhu)

### Democratizing the NVIDIA GEAR ENPIRE Gripper Design for more diverse Robot Arms
*Robotiq Hand-E • ALOHA • Open Arm • AgileX Piper • Seeed Studio reBot • Franka Panda • ARX5*

<br>

<table align="center" border="0">
  <tr>
    <th align="center" width="50%">NVIDIA GEAR ENPIRE Research Video</th>
    <th align="center" width="50%">Robotiq Hand-E Physical Adapter</th>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="https://research.nvidia.com/labs/gear/enpire/">
        <img src="docs/images/enpire_research_demo.gif" alt="NVIDIA GEAR ENPIRE Autonomous Manipulation" width="100%" />
      </a>
    </td>
    <td align="center" valign="top">
      <img src="docs/images/robotiq_hand_e_enpire_gripper.jpg" alt="Robotiq Hand-E ENPIRE Gripper" width="100%" />
    </td>
  </tr>
</table>

</div>

---

## Purpose & Mission

### Why This Project Exists
In physical AI manipulation research, grasping reliability is fundamentally determined by hardware contact mechanics—surface friction, structural compliance, and tactile geometry. When NVIDIA's GEAR lab published **ENPIRE** (*Agentic Robot Policy Self-Improvement in the Real World*), co-led by **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)) and **Dr. Yuke Zhu**, the physical robot achieved remarkable grasping reliability using a custom-engineered 3D-printable finger designed by **Wenli Xiao** (CMU & NVIDIA GEAR) for the **I2RT YAM** robotic arm.

However, the I2RT YAM is a specialized research arm that very few universities, startups, independent makers, or robotics labs own.

In the real world, the robotics community builds and trains policies on **generalist robotic arms** and industry-standard parallel grippers:
* **Robotiq Hand-E** (Precision electric parallel gripper)
* **ALOHA / Mobile ALOHA** (Bimanual imitation learning standard)
* **Open Arm** (Open-source accessible robotics)
* **AgileX (Piper)** (Lightweight bimanual research arms)
* **Seeed Studio reBot** (Accessible AI robotics)
* **Franka Emika Panda / FR3** (7-DoF research standard)
* **Robotiq 2F-85 & 2F-140** (Universal Robots, Kinova, AUBO)
* **ARX5** (Bimanual manipulation arms)

### Mission: Democratizing Frontier Gripper Design
> **Hardware breakthroughs in robotics should not be locked to a single proprietary arm.**
> 
> The mission of **Open-ENPIRE-Gripper-NVIDIA** is to bridge the gap between frontier physical AI research and the global robotics community:
> 1. **Universal Accessibility**: Translate the proven high-friction, compliant contact profile into 3D-printable STL adapters for popular generalist robotic arms.
> 2. **Physical AI for Everyone**: Enable anyone with a standard 3D printer to achieve frontier-grade contact mechanics on their existing robot without purchasing expensive custom end-effectors.
> 3. **Community-Driven Standardization**: Establish this geometry as an open-source standard across all parallel-jaw robotic grippers, starting with our physical adaptation for the **Robotiq Hand-E**.

*Original MakerWorld Project: [Gripper Finger for Robot Arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm) / [Profile #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177) by Wenli Xiao.*

---

## Robotiq Hand-E Adapter Design

Our primary physical adaptation mounts the ENPIRE fingertip geometry directly onto the **Robotiq Hand-E** parallel electric gripper:

<p align="center">
  <img src="docs/images/enpire_finger_model_render.png" alt="ENPIRE Finger Model Render" width="300" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/images/hand_e_enpire_fingers_detail.jpg" alt="Hand-E ENPIRE Finger Detail" width="300" />
  <br>
  <em>Left: Dual-material CAD render (blue rigid skeleton + orange compliant lattice). Right: Assembled physical hardware on Robotiq Hand-E.</em>
</p>

| Parameter | Specification |
| :--- | :--- |
| **Target Directory** | [`stl/hand_e_stl/`](stl/hand_e_stl/) |
| **Mounting Interface** | Standard 2× M4 / M3 counterbore bracket per finger |
| **Stroke & Force** | 50 mm linear parallel stroke | 20 N to 130 N programmable grip force |
| **Contact Surface** | Dual-material structural beam with integrated anti-slip compliant friction inserts |

---

## Robot Compatibility Matrix

| Robot Platform | Arm Type | Status | Precision | Bimanual Support | Grip Force Rating | Ease of Print | Target STL Folder |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Robotiq Hand-E** | Precision Electric Gripper | **Available** | High | Dual & Single | 130 N | High | [`stl/hand_e_stl/`](stl/hand_e_stl/) |
| **ALOHA / Mobile ALOHA** | Bimanual Imitation Rig | *In Progress* | High | Dual | 40 N | High | [`stl/aloha_stl/`](stl/aloha_stl/) |
| **Open Arm** | Open-Source Robotic Arm | *In Progress* | Moderate | Dual | 35 N | High | [`stl/open_arm_stl/`](stl/open_arm_stl/) |
| **AgileX (Piper)** | Lightweight Bimanual Arm | *In Progress* | High | Dual | 35 N | High | [`stl/agilex_stl/`](stl/agilex_stl/) |
| **Seeed Studio reBot** | AI Robotic Arm | *In Progress* | Moderate | Dual | 25 N | High | [`stl/seeed_rebot_stl/`](stl/seeed_rebot_stl/) |
| **Robotiq 2F-85 / 2F-140** | Industrial Cobot Gripper | *In Progress* | High | Single | 235 N | High | [`stl/robotiq_2f85_2f140_stl/`](stl/robotiq_2f85_2f140_stl/) |
| **Franka Panda / FR3** | 7-DoF AI Research Cobot | *In Progress* | High | Single | 70 N | High | [`stl/franka_panda_stl/`](stl/franka_panda_stl/) |
| **ARX5** | Bimanual Research Arm | *In Progress* | High | Dual | 40 N | High | [`stl/arx5_stl/`](stl/arx5_stl/) |
| **I2RT YAM** | AI Research Arm | *Baseline* | High | Dual | 45 N | High | [`stl/enpire_i2rt_yam_stl/`](stl/enpire_i2rt_yam_stl/) |
| **ISO 9409-1 (UR / xArm)** | Universal Tool Flanges | *In Progress* | High | Single | 150 N | High | [`stl/iso_flange_adapters_stl/`](stl/iso_flange_adapters_stl/) |

*Status: Available (Ready for print) | In Progress (Community Contributions Welcome)*

---

## 3D Printing Specifications & Guide

To achieve maximum grasping friction, layer adhesion, and durability:

### 1. Print Orientation (Critical for Structural Integrity)
```
      [RECOMMENDED]: Print flat on lateral side (Layer lines run parallel to tension)
      +----------------------------------------------------------+
      |  Base Mount  =================> Structural Fingertip     |
      +----------------------------------------------------------+
      ============================================================ (Build Plate)

      [AVOID]: Print standing vertically (Shear forces will cause layer delamination)
```

### 2. Dual-Material & Multi-Color Recommendations
* **Blue Outer Frame (Rigid)**: Print in **PETG-CF**, **PLA-CF**, or **PA12-CF (Nylon-CF)** for extreme beam stiffness and sharp mounting tolerances.
* **Orange Grip Core (Compliant)**: Print in **TPU 85A** or **TPU 95A** (flexible filament) for high-friction tactile compliance ($\mu > 0.8$) against smooth or irregular objects.
* *Single-Extruder Printers*: The design can also be printed as a single solid piece in PETG or PLA with 100% mechanical functionality.

### 3. Slicer Parameter Table (Bambu Studio / PrusaSlicer / OrcaSlicer)

| Parameter | Rigid Frame (PETG-CF / PA-CF) | Compliant Grip Ribs (TPU 85A/95A) |
| :--- | :--- | :--- |
| **Layer Height** | **0.16 mm** (Optimal for fine screw counterbores) | **0.16 mm – 0.20 mm** |
| **Wall Loops / Perimeters** | **5 to 6 walls** (Critical for shear load resistance) | **4 walls** |
| **Top / Bottom Solid Layers** | **5 Top, 5 Bottom** | **4 Top, 4 Bottom** |
| **Infill Density & Pattern** | **50% – 60% Gyroid or Cubic** | **30% – 40% Gyroid** |
| **Printing Speed** | Standard (60 – 120 mm/s) | Slow (20 – 35 mm/s) |
| **Supports** | Tree / Organic supports (Overhang angle: 45°) | None needed |

### 4. Fastener Assembly Tips
* **Heat-Set Brass Inserts**: Set soldering iron to **230°C** for PETG/PLA or **275°C** for PA-CF. Press M3/M4 threaded inserts until flush with the plastic face.
* **Threadlocker**: Apply a small drop of medium-strength blue threadlocker (Loctite 243) to prevent fastener loosening under high-frequency robotic vibration.

---

## URDF Simulation Models & STL Automation

We provide an automated script in `scripts/generate_urdf_from_stl.py` that parses any pair of finger STL files, calculates center-of-mass, inertia, scales from millimeters to meters, and outputs a physics-ready **URDF** for **NVIDIA Isaac Sim, MuJoCo, PyBullet, and ROS 2**:

```bash
# Generate a URDF from your STL files:
python3 scripts/generate_urdf_from_stl.py \
  --name hand_e_enpire_gripper \
  --left_stl stl/hand_e_stl/hand_e_enpire_finger_left.stl \
  --right_stl stl/hand_e_stl/hand_e_enpire_finger_right.stl \
  --stroke_mm 50.0 \
  --force_n 130.0 \
  --out hand_e_enpire_gripper.urdf
```

---

## Rules for Contributing

1. **Watertight Mesh**: Export binary STL files in **Millimeters (mm)** with zero non-manifold edges. Verify using:
   ```bash
   python3 scripts/validate_mesh.py
   ```
2. **Standard Orientation**: Coordinate frames must align ($+Z$ finger length, $+Y$ inward contact face). Export oriented flat on its side.
3. **Physical Test Print Required**: You must physically print the part and verify full stroke closure without binding before submitting a PR.
4. **PR Checklist**: Attach clear photos of the 3D-printed part installed on your robot arm and list your slicer settings.

*See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.*

---

## Citation & Attribution

If you use this gripper design or its multi-arm adapters in your research, please cite both the foundational ENPIRE paper and this open-source hardware project:

### 1. Foundational ENPIRE Research Paper
```bibtex
@article{xiao2024enpire,
  title={ENPIRE: Agentic Robot Policy Self-Improvement in the Real World},
  author={Xiao, Wenli and Fan, Linxi and Zhu, Yuke and GEAR Lab and Collaborators},
  journal={arXiv preprint},
  year={2024}
}
```

### 2. Open-ENPIRE-Gripper-NVIDIA Repository & Design Adaptation
```bibtex
@misc{open_enpire_gripper_2026,
  title={Open-ENPIRE-Gripper-NVIDIA: Democratizing the ENPIRE High-Friction Gripper Design for Generalist Robot Arms},
  author={Geedh, Pruthvi Omkar and Open Source Robotics Community},
  howpublished={\url{https://github.com/pgeedh/Open-ENPIRE-Gripper-nvidia}},
  year={2026}
}
```

*Foundational fingertip design by **Wenli Xiao** (CMU / NVIDIA GEAR) via [MakerWorld #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm). Research led by **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)) & **Dr. Yuke Zhu**.*

---

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
