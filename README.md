# Open-ENPIRE-Gripper-NVIDIA

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MakerWorld Original](https://img.shields.io/badge/MakerWorld-Original_Model-FF5A00.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
[![MakerWorld Profile](https://img.shields.io/badge/MakerWorld-Profile_%233349177-green.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)
[![NVIDIA GEAR](https://img.shields.io/badge/NVIDIA-GEAR_Lab-76B900.svg)](https://research.nvidia.com/labs/gear/enpire/)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-@DrJimFan-black.svg)](https://twitter.com/DrJimFan)
[![3D Print Ready](https://img.shields.io/badge/3D_Printing-FDM_%7C_SLA_%7C_TPU-orange.svg)](docs/3D_PRINTING_GUIDE.md)

**Democratizing the NVIDIA GEAR ENPIRE gripper design for generalist robotic arms.**

<br>

<table align="center" border="0">
  <tr>
    <th align="center" width="50%">🎬 NVIDIA GEAR ENPIRE Research</th>
    <th align="center" width="50%">🦾 Robotiq Hand-E Physical Adapter</th>
  </tr>
  <tr>
    <td align="center" valign="top">
      <a href="https://research.nvidia.com/labs/gear/enpire/">
        <img src="docs/images/enpire_research_demo.gif" alt="NVIDIA GEAR ENPIRE Autonomous Manipulation" width="100%" />
      </a>
      <br>
      <a href="https://research.nvidia.com/labs/gear/enpire/">▶️ <b>Watch NVIDIA ENPIRE Research Video</b></a>
    </td>
    <td align="center" valign="top">
      <img src="docs/images/robotiq_hand_e_enpire_gripper.jpg" alt="Robotiq Hand-E ENPIRE Gripper" width="100%" />
      <br>
      <em>ENPIRE compliant fingers mounted on Robotiq Hand-E</em>
    </td>
  </tr>
</table>

</div>

---

## 🎯 Purpose & Mission

### Why This Project Exists
In physical AI manipulation research, grasping success often comes down to hardware contact mechanics—surface friction, structural compliance, and tactile geometry. When NVIDIA's GEAR lab published **ENPIRE** (*Agentic Robot Policy Self-Improvement in the Real World*), co-led by **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)) and **Dr. Yuke Zhu**, the physical robot achieved remarkable grasping reliability using a custom-engineered 3D-printable finger designed by **Wenli Xiao** (CMU & NVIDIA GEAR) for the **I2RT YAM** robotic arm.

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

### Our Mission
> **Hardware breakthroughs in robotics should not be locked to a single proprietary arm.**
> 
> The mission of **Open-ENPIRE-Gripper-NVIDIA** is to bridge the gap between frontier physical AI research and the global robotics community:
> 1. **Universal Accessibility**: Translate the proven high-friction, compliant contact profile into 3D-printable STL adapters for popular generalist robotic arms.
> 2. **Physical AI for Everyone**: Enable anyone with a standard 3D printer to achieve frontier-grade contact mechanics on their existing robot without purchasing expensive custom end-effectors.
> 3. **Community-Driven Standardization**: Establish this geometry as an open-source standard across all parallel-jaw robotic grippers, starting with our physical adaptation for the **Robotiq Hand-E**.

*Original MakerWorld Project: [Gripper Finger for Robot Arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm) / [Profile #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177) by Wenli Xiao.*

---

## 🦾 Robotiq Hand-E Adapter

Our primary physical adaptation mounts the ENPIRE fingertip geometry directly onto the **Robotiq Hand-E** parallel electric gripper:

<p align="center">
  <img src="docs/images/hand_e_enpire_fingers_detail.jpg" alt="Hand-E ENPIRE Finger Detail" width="320" />
</p>

| Parameter | Specification |
| :--- | :--- |
| **Target Directory** | [`stl/hand_e_stl/`](stl/hand_e_stl/) |
| **Mounting Interface** | Standard 2× M4 / M3 counterbore bracket per finger |
| **Stroke & Force** | 50 mm linear parallel stroke | 20 N to 130 N programmable grip force |
| **Contact Surface** | Dual-material structural beam with integrated anti-slip compliant friction inserts |

---

## 🔥 Robot Compatibility Heatmap

| Robot Platform | Arm Type | Status | Precision | Bimanual Support | High-Force Grip | Ease of 3D Print | Target STL Folder |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Robotiq Hand-E** | Precision Electric Gripper | 🟢 **Active** | 🟢 High | 🟢 Full | 🟢 130 N | 🟢 Easy | [`stl/hand_e_stl/`](stl/hand_e_stl/) |
| **ALOHA / Mobile ALOHA** | Bimanual Imitation Rig | 🟡 *In Progress* | 🟢 High | 🟢 Dual | 🟡 40 N | 🟢 Easy | [`stl/aloha_stl/`](stl/aloha_stl/) |
| **Open Arm** | Open-Source Robotic Arm | 🟡 *In Progress* | 🟡 Med | 🟡 Dual | 🟡 35 N | 🟢 Easy | [`stl/open_arm_stl/`](stl/open_arm_stl/) |
| **AgileX (Piper)** | Lightweight Bimanual Arm | 🟡 *In Progress* | 🟢 High | 🟢 Dual | 🟡 35 N | 🟢 Easy | [`stl/agilex_stl/`](stl/agilex_stl/) |
| **Seeed Studio reBot** | AI Robotic Arm | 🟡 *In Progress* | 🟡 Med | 🟡 Dual | 🟡 25 N | 🟢 Easy | [`stl/seeed_rebot_stl/`](stl/seeed_rebot_stl/) |
| **Robotiq 2F-85 / 2F-140** | Industrial Cobot Gripper | 🟡 *In Progress* | 🟢 High | 🟡 Single | 🟢 235 N | 🟢 Easy | [`stl/robotiq_2f85_2f140_stl/`](stl/robotiq_2f85_2f140_stl/) |
| **Franka Panda / FR3** | 7-DoF AI Research Cobot | 🟡 *In Progress* | 🟢 High | 🟡 Single | 🟢 70 N | 🟢 Easy | [`stl/franka_panda_stl/`](stl/franka_panda_stl/) |
| **ARX5** | Bimanual Research Arm | 🟡 *In Progress* | 🟢 High | 🟢 Dual | 🟡 40 N | 🟢 Easy | [`stl/arx5_stl/`](stl/arx5_stl/) |
| **I2RT YAM** | AI Research Arm | 🟢 *Original* | 🟢 High | 🟢 Dual | 🟡 45 N | 🟢 Easy | [`stl/enpire_i2rt_yam_stl/`](stl/enpire_i2rt_yam_stl/) |
| **ISO 9409-1 (UR / xArm)** | Universal Tool Flanges | 🟡 *In Progress* | 🟢 High | 🟡 Single | 🟢 150 N | 🟢 Easy | [`stl/iso_flange_adapters_stl/`](stl/iso_flange_adapters_stl/) |

*Legend: 🟢 Available &nbsp;|&nbsp; 🟡 Community Contribution Open*

---

## 📁 Repository Structure

```
Open-ENPIRE-Gripper-NVIDIA/
├── stl/
│   ├── hand_e_stl/                 # 🌟 Robotiq Hand-E ENPIRE adapter STLs (Main target)
│   ├── agilex_stl/                 # AgileX (Piper) bimanual robot arm STLs
│   ├── aloha_stl/                  # ALOHA & Mobile ALOHA bimanual gripper STLs
│   ├── open_arm_stl/               # Open Arm robotics platform STLs
│   ├── seeed_rebot_stl/            # Seeed Studio reBot AI robotic arm STLs
│   ├── robotiq_2f85_2f140_stl/     # Robotiq 2F-85 and 2F-140 bracket STLs
│   ├── franka_panda_stl/           # Franka Emika Panda / FR3 dovetail slider STLs
│   ├── arx5_stl/                   # ARX5 bimanual robotic arm STLs
│   ├── enpire_i2rt_yam_stl/        # I2RT YAM baseline finger STLs (Wenli Xiao original)
│   ├── iso_flange_adapters_stl/    # Universal ISO 9409-1 (UR3e/5e/10e, xArm) flange plates
│   └── accessories_and_pads_stl/   # TPU friction snap-pads & silicone casting molds
├── docs/
│   ├── images/                     # Hardware photos & animated demos
│   ├── 3D_PRINTING_GUIDE.md        # Detailed slicer profiles & materials
│   └── ROBOT_COMPATIBILITY.md      # Dimensional specs and mounting standards
├── scripts/
│   └── validate_mesh.py            # Automated STL watertightness & bounding box validator
├── CONTRIBUTING.md                 # Rules for contributing STL files
└── README.md
```

---

## 🖨️ Printing Instructions for Best Results

* **Print Orientation**: Always print fingers **flat on their lateral side** to align layer lines parallel with clamping forces and prevent shear failure.
* **Filament**: **PETG-CF / PLA-CF / PA12-CF** for finger bodies + **TPU 85A/95A** for friction pads.
* **Slicer Settings**: **5 to 6 wall perimeters** | **50% Gyroid infill** | **0.16 mm layer height**.
* **Fasteners**: Standard M3/M4 socket head cap screws with medium blue threadlocker (Loctite 243).

---

## 📋 Rules for Contributing

1. **Watertight Mesh**: Export binary STL files in **Millimeters (mm)** with zero non-manifold edges. Verify using `python3 scripts/validate_mesh.py`.
2. **Standard Orientation**: Coordinate frames must align ($+Z$ finger length, $+Y$ inward contact face). Export oriented flat on its side.
3. **Physical Test Print Required**: You must physically print the part and verify full stroke closure without binding before submitting a PR.
4. **PR Checklist**: Attach clear photos of the 3D-printed part installed on your robot arm and list your slicer settings.

*See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.*

---

## 📚 Citation & Attribution

```bibtex
@article{xiao2024enpire,
  title={ENPIRE: Agentic Robot Policy Self-Improvement in the Real World},
  author={Xiao, Wenli and Fan, Linxi and Zhu, Yuke and GEAR Lab and Collaborators},
  journal={arXiv preprint},
  year={2024}
}
```

*Foundational design by **Wenli Xiao** (CMU / NVIDIA GEAR) via [MakerWorld #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm). Research led by **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)) & **Dr. Yuke Zhu**.*

---

## 📄 License

Licensed under the [Apache License, Version 2.0](LICENSE).
