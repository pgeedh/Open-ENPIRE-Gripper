# Open-ENPIRE-Gripper-NVIDIA

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MakerWorld Original](https://img.shields.io/badge/MakerWorld-Original_Model-FF5A00.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
[![MakerWorld Profile](https://img.shields.io/badge/MakerWorld-Profile_%233349177-green.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)
[![NVIDIA GEAR](https://img.shields.io/badge/NVIDIA-GEAR_Lab-76B900.svg)](https://research.nvidia.com/)
[![Physical AI](https://img.shields.io/badge/Robotics-Generalist_Arm_Standard-purple.svg)](docs/ROBOT_COMPATIBILITY.md)
[![3D Print Ready](https://img.shields.io/badge/3D_Printing-FDM_%7C_SLA_%7C_TPU-orange.svg)](docs/3D_PRINTING_GUIDE.md)

**Democratizing the high-performance NVIDIA GEAR ENPIRE gripper design — making frontier physical AI contact mechanics accessible to generalist robotic arms and makers worldwide.**

[The Story & Mission](#-the-story-from-niche-research-to-universal-access) • [Original Design](#-original-design--credits) • [NVIDIA Research & Jim Fan](#-nvidia-gear-enpire-research--dr-jim-fan) • [Robotiq Hand-E](#-robotiq-hand-e-adapter) • [Multi-Arm Folders](#-multi-arm-ecosystem-folders) • [Printing Guide](#-3d-printing-guide) • [Citation](#-citation--credits)

</div>

---

## 📖 The Story: From Niche Research to Universal Access

### 1. The Breakthrough
When NVIDIA's GEAR lab published **ENPIRE** (*Agentic Robot Policy Self-Improvement in the Real World*), the robotics community witnessed a milestone: autonomous AI coding agents training physical robots to master ultra-demanding contact tasks—such as **threading zip-ties, inserting PCIe cards/GPUs, and precision sorting**—with up to 99% success rates.

Behind this software intelligence was an unsung hardware hero: a custom, high-friction, compliant 3D-printable gripper finger designed by **Wenli Xiao** (CMU & NVIDIA GEAR) for the **I2RT YAM** robotic arm.

### 2. The Missing Link: Generalist Arms vs. Specialized Hardware
The original research proved how crucial fingertip geometry and contact friction are for Physical AI. However, the original CAD was built exclusively for the **I2RT YAM** arm. 

In the real world, the vast majority of universities, startups, hobbyists, and independent roboticists don't own an I2RT YAM arm. Instead, the robotics community builds on **generalist robotic arms** and industry-standard grippers:
* **Robotiq Hand-E** & **2F-85 / 2F-140** (Universal Robots, Kinova, AUBO)
* **AgileX Piper** (Lightweight bimanual research)
* **Franka Emika Panda / FR3** (7-DoF AI research standard)
* **SO-100 / Mobile ALOHA / Lerobot** (Open-source low-cost robotics)
* **ARX5** (Bimanual manipulation)

### 3. The Mission: Democratizing the Design for Everyone
> **Why should an extraordinary hardware innovation remain locked to one specific robot arm?**
>
> Great robotics design should be accessible to everyone. The goal of this repository is to bridge frontier physical AI research with the broader open-source community: taking the proven ENPIRE contact geometry and adapting it for **generalist robotic arms**.
> 
> Starting with our custom adapter for the **Robotiq Hand-E**, this repository is an open collaborative home to standardize this gripper across all popular robotic platforms—enabling anyone with a 3D printer to supercharge their robot's dexterous grasping capabilities.

---

## 🌟 Original Design & Credits

This project stands on the shoulders of the original open-source design created by **Wenli Xiao** (Carnegie Mellon University & NVIDIA GEAR Lab):

* 🔗 **MakerWorld Model Page**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
* 🔗 **MakerWorld Profile**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)

> ### 🙏 A Note of Gratitude
> *"Wenli Xiao's design is a masterclass in functional 3D-printable robotics hardware. We give full credit and deep appreciation to Wenli and the NVIDIA GEAR lab for open-sourcing the initial model. Our work here is simply to amplify that value, building adapters so every roboticist can benefit from this geometry regardless of which robot arm they operate."*

---

## 🔬 NVIDIA GEAR ENPIRE Research & Dr. Jim Fan

The ENPIRE framework represents the cutting edge of autonomous robot learning, developed by the **NVIDIA GEAR** (Generalist Embodied Agent Research) lab led by **Dr. Jim Fan** and **Dr. Yuke Zhu**, in collaboration with CMU and UC Berkeley.

```
       ┌─────────────────────────────────────────────────────────────┐
       │             NVIDIA GEAR Lab: Project ENPIRE                 │
       │     Agentic Robot Policy Self-Improvement in the Real World │
       └──────────────────────────────┬──────────────────────────────┘
                                      │
    ┌─────────────────────────────────┼─────────────────────────────────┐
    ▼                                 ▼                                 ▼
[ Autonomous Coding Agents ]   [ Closed-Loop Feedback ]   [ High-Precision Dexterity ]
  Literature Search & Coding     Physical Self-Correction    Zip-Ties, GPUs, Precision Assembly
```

### 📺 Research Demos & Video Highlights
* **Agentic Self-Improvement**: Teams of LLM coding agents autonomously write code, launch physical robot rollouts, analyze video logs, and iteratively evolve manipulation policies without human intervention.
* **Extreme Contact Precision**: Utilizing high-friction fingertips, the robots achieved unprecedented dexterity—threading flexible zip-ties and seating fragile hardware into motherboard expansion slots.
* **Continuous 24/7 Learning**: Automated self-resetting environments enable robots to recover from failed attempts and continuously train around the clock.

> *"The bottleneck in robot learning has always been human babysitting. ENPIRE demonstrates that AI agents can run end-to-end robotics research in the physical world—writing code, debugging runs, and self-improving physical manipulation."*  
> — **Dr. Jim Fan**, Director of AI / Embodied AI at NVIDIA

---

## 🦾 Robotiq Hand-E Adapter

Our primary contribution begins with adapting the ENPIRE high-friction finger profile to the **Robotiq Hand-E** precision parallel electric gripper:

| Specification | Robotiq Hand-E Parameters |
| :--- | :--- |
| **Gripper Type** | High-Precision Electric Parallel Gripper |
| **Stroke Range** | 50 mm linear stroke |
| **Grip Force** | 20 N to 130 N (programmable) |
| **Repeatability** | 0.02 mm |
| **Mounting Pattern** | 2× M4/M3 fastener bracket |
| **Target Directory** | [`stl/hand_e_gripper/`](stl/hand_e_gripper/) |

---

## 📁 Multi-Arm Ecosystem Folders

To establish an open standard across all platforms, clean folder structures are organized for manual uploads and community CAD contributions:

```
Open-ENPIRE-Gripper-NVIDIA/
├── stl/
│   ├── hand_e_gripper/         # 🌟 Robotiq Hand-E ENPIRE adapter STL files (Main upload)
│   ├── enpire_i2rt_yam/        # I2RT YAM baseline finger STLs (Wenli Xiao original)
│   ├── agilex_piper/           # AgileX Piper bimanual robot arm adapters
│   ├── robotiq_2f85_2f140/     # Robotiq 2F-85 and 2F-140 bracket adapters
│   ├── franka_panda/           # Franka Emika Panda / FR3 dovetail slider fingers
│   ├── mobile_aloha_so100/     # Low-cost SO-100 / Mobile ALOHA servo horn fingers
│   ├── arx5/                   # ARX5 bimanual robotic arm fingers
│   ├── iso_flange_adapters/    # Universal ISO 9409-1 (UR3e/5e/10e, xArm) flange plates
│   └── accessories_and_pads/   # TPU friction snap-pads & silicone casting molds
├── cad/
│   └── step/                   # Raw STEP / CAD assemblies for community exchange
├── docs/
│   ├── HARDWARE_BOM.md         # Fasteners, inserts, torque specifications
│   ├── 3D_PRINTING_GUIDE.md    # Slicer profiles, layer heights, materials
│   └── ROBOT_COMPATIBILITY.md  # Dimensional specs and mounting standards
├── scripts/
│   └── validate_mesh.py        # Automated STL watertightness & bounding box validator
└── README.md
```

---

## 🖨️ 3D Printing Guide

For optimal mechanical shear strength and grasping friction:

| Parameter | Structural Finger Body | Contact Grip Pad |
| :--- | :--- | :--- |
| **Recommended Material** | PETG-CF, PLA-CF, or PA12-CF | TPU 85A or TPU 95A |
| **Layer Height** | 0.16 mm – 0.20 mm | 0.16 mm – 0.20 mm |
| **Perimeters / Walls** | **5 to 6 walls** (Essential for shear resistance) | 4 walls |
| **Infill Density** | 40% – 60% (Gyroid or Cubic) | 30% – 50% |
| **Print Orientation** | Lay flat on lateral side | Flat on bed |

*For complete slicer details, hardware lists, and assembly tips, see [docs/3D_PRINTING_GUIDE.md](docs/3D_PRINTING_GUIDE.md) and [docs/HARDWARE_BOM.md](docs/HARDWARE_BOM.md).*

---

## 🤝 Contributing & Expanding Generalist Arms

We encourage roboticists, makers, and labs to contribute adapter designs for other robot arms:
1. Export your adapter CAD model as **STEP** (`cad/step/`) and high-resolution binary **STL** (`stl/<arm_folder>/`).
2. Run `python3 scripts/validate_mesh.py` to verify mesh integrity.
3. Open a Pull Request so the entire robotics community can access your design!

---

## 📚 Citation & Credits

### Foundational Hardware Design
* **Original Creator**: Wenli Xiao (Carnegie Mellon University & NVIDIA GEAR Lab)
* **MakerWorld Project**: [Gripper Finger for Robot Arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm) / [Profile #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)

### Foundational Research Paper
```bibtex
@article{xiao2024enpire,
  title={ENPIRE: Agentic Robot Policy Self-Improvement in the Real World},
  author={Xiao, Wenli and Fan, Linxi and Zhu, Yuke and GEAR Lab and Collaborators},
  journal={arXiv preprint},
  year={2024}
}
```

---

## 📄 License

This repository is licensed under the [Apache License, Version 2.0](LICENSE). All foundational design credits and research acknowledgments belong to Wenli Xiao and the NVIDIA GEAR research team.
