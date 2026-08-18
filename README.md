# Open-ENPIRE-Gripper-NVIDIA

<div align="center">

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MakerWorld Original](https://img.shields.io/badge/MakerWorld-Original_Model-FF5A00.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
[![MakerWorld Profile](https://img.shields.io/badge/MakerWorld-Profile_%233349177-green.svg)](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)
[![NVIDIA GEAR](https://img.shields.io/badge/NVIDIA-GEAR_Lab-76B900.svg)](https://research.nvidia.com/)
[![Physical AI](https://img.shields.io/badge/Robotics-Physical_AI_Standard-purple.svg)](docs/ROBOT_COMPATIBILITY.md)

**A community-driven initiative to adapt the high-performance NVIDIA GEAR ENPIRE gripper design into a standard universal gripper across all robotic arms.**

[Original Design & Inspiration](#-original-design--inspiration) • [NVIDIA Research & Jim Fan](#-nvidia-gear-enpire-research--dr-jim-fan) • [Robotiq Hand-E](#-robotiq-hand-e-adapter) • [Multi-Arm Folders](#-multi-arm-ecosystem) • [Printing Guide](#-3d-printing-guide) • [Citation](#-citation--credits)

</div>

---

## 🌟 Original Design & Inspiration

This project is directly inspired by the brilliant 3D printable **Gripper Finger for Robot Arm** originally created by **Wenli Xiao** (Carnegie Mellon University & NVIDIA GEAR Lab):

* 🔗 **MakerWorld Model Page**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm)
* 🔗 **MakerWorld Profile**: [https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)

> ### 💡 Vision & Purpose
> *"The original ENPIRE gripper finger is a masterclass in functional robotics hardware design—delivering outstanding grasping friction, tactile reliability, and compliance for autonomous physical AI research on the I2RT YAM arm.*
> 
> *I was deeply inspired by this design and created this repository to bring this proven fingertip geometry to **other robotic arms**—starting with the **Robotiq Hand-E**, and expanding to **AgileX Piper, Robotiq 2F-85/140, Franka Emika Panda, SO-100 / Mobile ALOHA, ARX5, and ISO Flanges**.*
> 
> *All credit goes to the original creator, Wenli Xiao, and the NVIDIA GEAR lab. The mission here is to help establish this geometry as an **open-source standard gripper** for the entire robotics research community."*

---

## 🔬 NVIDIA GEAR ENPIRE Research & Dr. Jim Fan

The ENPIRE hardware design plays a vital role in **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World**, developed by the **NVIDIA GEAR** (Generalist Embodied Agent Research) lab led by **Dr. Jim Fan** and **Dr. Yuke Zhu**, in collaboration with CMU and UC Berkeley.

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
* **Agentic Closed-Loop Improvement**: Teams of AI coding agents autonomously propose experiments, write robot control policies, analyze physical rollouts, and iteratively refine manipulation skills without constant human supervision.
* **Extreme Dexterous Precision**: Using high-friction fingertip geometries, the robots successfully mastered demanding real-world contact tasks, including **threading and pulling cable zip-ties, inserting PCIe cards / GPUs into motherboard slots, and micro-sorting pin boxes** with up to 99% success rates.
* **Autonomous Reset Mechanisms**: Built-in physical feedback mechanisms allow the robot to reset its own workspace after failures for uninterrupted 24/7 self-directed training.

> *"The bottleneck in robot learning has always been human babysitting. ENPIRE demonstrates that AI agents can run end-to-end robotics research in the physical world—writing code, debugging runs, and self-improving physical manipulation."*  
> — **Dr. Jim Fan**, Director of AI / Embodied AI at NVIDIA

---

## 🦾 Robotiq Hand-E Adapter

The primary focus of this repository is adapting the ENPIRE high-friction finger profile to the **Robotiq Hand-E** parallel gripper:

| Specification | Robotiq Hand-E Parameters |
| :--- | :--- |
| **Gripper Type** | High-Precision Electric Parallel Gripper |
| **Stroke Range** | 50 mm linear stroke |
| **Grip Force** | 20 N to 130 N (programmable) |
| **Repeatability** | 0.02 mm |
| **Mounting Pattern** | 2× M4/M3 fastener bracket |
| **Target Directory** | [`stl/hand_e_gripper/`](stl/hand_e_gripper/) |

---

## 📁 Multi-Arm Ecosystem Folder Structure

To help standardize this gripper across all robotics platforms, dedicated folders are organized for manual uploads and community CAD contributions:

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

For the best mechanical strength and grip performance:

| Parameter | Structural Finger Body | Contact Grip Pad |
| :--- | :--- | :--- |
| **Recommended Material** | PETG-CF, PLA-CF, or PA12-CF | TPU 85A or TPU 95A |
| **Layer Height** | 0.16 mm – 0.20 mm | 0.16 mm – 0.20 mm |
| **Perimeters / Walls** | **5 to 6 walls** (Essential for shear strength) | 4 walls |
| **Infill Density** | 40% – 60% (Gyroid or Cubic) | 30% – 50% |
| **Print Orientation** | Lay flat on lateral side | Flat on bed |

*For complete slicer details and hardware assembly, see [docs/3D_PRINTING_GUIDE.md](docs/3D_PRINTING_GUIDE.md) and [docs/HARDWARE_BOM.md](docs/HARDWARE_BOM.md).*

---

## 🤝 Contributing & Community Adaptations

If you design or test adapters for additional robotic arms:
1. Export your CAD model as **STEP** (`cad/step/`) and high-resolution binary **STL** (`stl/<arm_folder>/`).
2. Run `python3 scripts/validate_mesh.py` to verify mesh integrity.
3. Open a Pull Request so other roboticists can utilize your adapter!

---

## 📚 Citation & Credits

### Original Hardware Design
* **Creator**: Wenli Xiao (Carnegie Mellon University & NVIDIA GEAR Lab)
* **MakerWorld Original**: [Gripper Finger for Robot Arm](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm) / [Profile #3349177](https://makerworld.com/en/models/2984746-gripper-finger-for-robot-arm#profileId-3349177)

### NVIDIA Research Project
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

This project is licensed under the [Apache License, Version 2.0](LICENSE). All credits and acknowledgments for the foundational design belong to Wenli Xiao and the NVIDIA GEAR research team.
