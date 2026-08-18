# Open-ENPIRE-Gripper-NVIDIA

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MakerWorld Original](https://img.shields.io/badge/MakerWorld-Original_Model-FF5A00.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
[![MakerWorld Profile](https://img.shields.io/badge/MakerWorld-Profile_%233349177-green.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)
[![NVIDIA GEAR](https://img.shields.io/badge/NVIDIA-GEAR_Lab-76B900.svg)](https://research.nvidia.com/)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-@DrJimFan-black.svg)](https://twitter.com/DrJimFan)
[![Physical AI](https://img.shields.io/badge/Robotics-Generalist_Arm_Standard-purple.svg)](docs/ROBOT_COMPATIBILITY.md)
[![3D Print Ready](https://img.shields.io/badge/3D_Printing-FDM_%7C_SLA_%7C_TPU-orange.svg)](docs/3D_PRINTING_GUIDE.md)

**An open-source, multi-arm 3D printable adaptation of the high-performance NVIDIA GEAR ENPIRE gripper design, engineered to make frontier physical AI contact mechanics accessible to generalist robotic arms.**

[Quick Links](#-quick-links) • [Why This Project Exists](#-why-this-project-exists) • [Original Design & Credits](#-original-design--credits) • [NVIDIA Research & Jim Fan](#-nvidia-gear-enpire-research--dr-jim-fan) • [Robotiq Hand-E](#-robotiq-hand-e-adapter) • [Multi-Arm STL Folders](#-multi-arm-stl-ecosystem) • [Rules for Contributing](#-rules-for-contributing) • [Printing Guide](#-3d-printing-guide)

</div>

---

## 🚀 Quick Links
* 📂 **[Robotiq Hand-E STLs](stl/hand_e_gripper/)**
* 📂 **[Multi-Arm STL Directories](stl/)**
* 🛠️ **[Hardware Bill of Materials](docs/HARDWARE_BOM.md)**
* 🖨️ **[3D Printing & Slicing Guide](docs/3D_PRINTING_GUIDE.md)**
* 🦾 **[Robot Compatibility Matrix](docs/ROBOT_COMPATIBILITY.md)**
* 🌟 **[Original MakerWorld Model](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)**

---

## 💡 Why This Project Exists

### The Problem: Great Hardware Locked to a Single Robot
When NVIDIA's GEAR lab published **ENPIRE** (*Agentic Robot Policy Self-Improvement in the Real World*), they demonstrated that autonomous coding agents could teach physical robots to solve complex dexterous tasks—like **threading zip-ties, seating PCIe/GPU cards into motherboards, and precision micro-sorting**—with up to 99% success rates.

A silent hero of that breakthrough was the custom-designed, high-friction 3D-printed gripper finger created by **Wenli Xiao** (CMU & NVIDIA GEAR) for the **I2RT YAM** robotic arm.

However, the vast majority of robotics labs, startups, universities, and independent makers do not have an I2RT YAM arm. Instead, the robotics ecosystem builds and tests policies on **generalist robotic arms** and industry-standard parallel grippers:
* **Robotiq Hand-E** (High-precision parallel electric gripper)
* **ALOHA / Mobile ALOHA** (Bimanual physical AI imitation learning standard)
* **Open Arm** (Open-source robotic arm platforms)
* **AgileX (Piper)** (Lightweight bimanual research arms)
* **Seeed Studio reBot** (Accessible AI robotic arms)
* **Franka Emika Panda / FR3** (7-DoF research standard)
* **Robotiq 2F-85 & 2F-140** (Universal Robots, Kinova, AUBO)
* **ARX5** (Bimanual manipulation arms)

Without modular adapters, this exceptional fingertip geometry remains inaccessible to 99% of researchers and builders in the field.

### The Solution: Democratizing ENPIRE for Generalist Arms
**Open-ENPIRE-Gripper-NVIDIA** removes this hardware barrier. 

We take the proven contact mechanics, high-friction ridged surface, and compliant fingertip geometry from Wenli Xiao's original design and adapt it into a modular, 3D-printable standard for generalist robot arms.

We start by providing custom adapter STL models for the **Robotiq Hand-E**, while organizing dedicated open-source slots for the entire robotics community to contribute matching STL files for every popular parallel-jaw gripper.

---

## 🌟 Original Design & Credits

This project is built directly on the foundation of the open-source 3D model designed by **Wenli Xiao** (Carnegie Mellon University & NVIDIA GEAR Lab):

* 🔗 **MakerWorld Model Page**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
* 🔗 **MakerWorld Profile**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)

> ### 🙏 Note of Appreciation
> *"Wenli Xiao's original gripper finger is a masterclass in functional robotics hardware design—delivering outstanding contact friction and tactile compliance for autonomous physical AI research.*
>
> *All foundational design credit belongs to Wenli Xiao and the NVIDIA GEAR lab. Our goal is simply to make this design universally accessible across every generalist arm in the robotics community."*

---

## 🔬 NVIDIA GEAR ENPIRE Research & Dr. Jim Fan

The ENPIRE research framework was developed by the **NVIDIA GEAR** (Generalist Embodied Agent Research) lab, co-led by **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)) and **Dr. Yuke Zhu**, in collaboration with researchers from Carnegie Mellon University and UC Berkeley.

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

### Key Highlights from the Research
* **Agentic Closed-Loop Improvement**: Autonomous LLM coding agents write control policies, execute real-world physical trials, inspect video logs, and iteratively evolve skills without constant human babysitting.
* **Extreme Contact Precision**: Enabled by high-friction compliant finger tips, the robot achieved high success rates on tasks traditionally thought impossible for simple parallel grippers—such as **tightening cable zip-ties, inserting delicate GPU boards into slots, and sorting micro-pins**.
* **Self-Resetting Workspaces**: Autonomous recovery loops enable continuous 24/7 self-directed robot learning.

> *"The bottleneck in robot learning has always been human babysitting. ENPIRE demonstrates that AI agents can run end-to-end robotics research in the physical world—writing code, debugging runs, and self-improving physical manipulation."*  
> — **Dr. Jim Fan** ([@DrJimFan](https://twitter.com/DrJimFan)), Director of AI / Embodied AI at NVIDIA

---

## 🦾 Robotiq Hand-E Adapter

Our primary focus begins with adapting the ENPIRE high-friction finger profile to the **Robotiq Hand-E** precision parallel electric gripper:

| Parameter | Specification |
| :--- | :--- |
| **Gripper Type** | Precision Electric Parallel Gripper |
| **Stroke Range** | 50 mm linear parallel stroke |
| **Grip Force** | 20 N to 130 N (programmable) |
| **Repeatability** | 0.02 mm |
| **Mounting Interface** | 2× M4/M3 fastener bracket |
| **Target Directory** | [`stl/hand_e_gripper/`](stl/hand_e_gripper/) |

---

## 📁 Multi-Arm STL Ecosystem

To establish an open standard across all platforms, clean folder structures are organized for manual STL uploads and community contributions:

```
Open-ENPIRE-Gripper-NVIDIA/
├── stl/
│   ├── hand_e_gripper/         # 🌟 Robotiq Hand-E ENPIRE adapter STL files (Main target)
│   ├── aloha/                  # ALOHA & Mobile ALOHA bimanual gripper STL files
│   ├── open_arm/               # Open Arm robotics platform STL files
│   ├── agilex_piper/           # AgileX (Piper) bimanual robot arm STL files
│   ├── seeed_rebot/            # Seeed Studio reBot AI robotic arm STL files
│   ├── robotiq_2f85_2f140/     # Robotiq 2F-85 and 2F-140 bracket STL files
│   ├── franka_panda/           # Franka Emika Panda / FR3 dovetail slider STL files
│   ├── arx5/                   # ARX5 bimanual robotic arm STL files
│   ├── enpire_i2rt_yam/        # I2RT YAM baseline finger STL files (Wenli Xiao original)
│   ├── iso_flange_adapters/    # Universal ISO 9409-1 (UR3e/5e/10e, xArm) flange plates
│   └── accessories_and_pads/   # TPU friction snap-pads & silicone casting molds
├── docs/
│   ├── HARDWARE_BOM.md         # Fasteners, inserts, torque specifications
│   ├── 3D_PRINTING_GUIDE.md    # Slicer profiles, layer heights, materials
│   └── ROBOT_COMPATIBILITY.md  # Dimensional specs and mounting standards
├── scripts/
│   └── validate_mesh.py        # Automated STL watertightness & bounding box validator
├── CONTRIBUTING.md             # Rules for contributing STL files
└── README.md
```

---

## 📋 Rules for Contributing

To ensure that every 3D model in this repository is reliable, physically functional, and ready to print, all contributions must follow these rules:

1. **Watertight Mesh**: STL files must be exported in **Millimeters (mm)** as solid, binary STLs with **zero non-manifold edges** and correct outward normals. Run `python3 scripts/validate_mesh.py` to confirm.
2. **Standard Orientation**: Coordinate axes must follow standard robotics conventions ($+Z$ along finger extension, $+Y$ inward contact normal). Fingers should be export-oriented to print flat on their lateral side for maximum layer shear strength.
3. **Hardware Standards**: Fasteners must follow metric ISO/DIN specifications (M2.5, M3, M4, M5) with proper counterbore depth and heat-set insert tolerances ($+0.1\text{ mm}$ to $+0.2\text{ mm}$ print expansion).
4. **Physical Test Print Required**: You must physically print the part and verify smooth mounting, full stroke closure, and zero mechanical binding before opening a Pull Request.
5. **PR Checklist**: Include clear photos of the 3D-printed part installed on the robot arm and list your slicer settings (material, walls, infill).

*See [CONTRIBUTING.md](CONTRIBUTING.md) for full contribution guidelines and naming conventions.*

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

## 📚 Citation & References

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

This project is licensed under the [Apache License, Version 2.0](LICENSE). All foundational design credits and research acknowledgments belong to Wenli Xiao and the NVIDIA GEAR research team ([@DrJimFan](https://twitter.com/DrJimFan)).
