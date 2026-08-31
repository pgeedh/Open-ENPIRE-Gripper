# Robot Arm Compatibility Matrix

The **Open-ENPIRE-Gripper-NVIDIA** project aims to establish an open standard across generalist robotic arms, bimanual learning platforms, collaborative cobots, and open-source hardware.

All 3D-printable gripper STL models for supported robot arms are stored in [`grippers-stl/`](../grippers-stl/).

---

## Supported Robot Platforms & Adapter Directories

| Robot Platform | Arm Type / Gripper Interface | Status | Target STL Folder |
| :--- | :--- | :---: | :--- |
| [**Robotiq Hand-E**](https://robotiq.com/products/hand-e-adaptive-robot-gripper) | Precision Electric Parallel Gripper | **Available** | [`grippers-stl/hand_e_stl/`](../grippers-stl/hand_e_stl/) |
| [**Robotiq 2F-85 / 2F-140**](https://robotiq.com/products/2f85-140-adaptive-robot-gripper) | 2× M4 Bracket Mount (10 mm spacing) | **Available** | [`grippers-stl/robotiq_2f85_2f140_stl/`](../grippers-stl/robotiq_2f85_2f140_stl/) |
| **Open Arm** | Modular Open-Source Parallel Mount | **Available** | [`grippers-stl/open_arm_stl/`](../grippers-stl/open_arm_stl/) |
| **I2RT YAM** | Native Dual M3 Clamp (Wenli Xiao Baseline) | **Available** | [`grippers-stl/enpire_i2rt_yam_stl/`](../grippers-stl/enpire_i2rt_yam_stl/) |
| **ALOHA / Mobile ALOHA** | ViperX Parallel Jaw Carriage | *In Progress* | [`grippers-stl/aloha_stl/`](../grippers-stl/aloha_stl/) |
| **AgileX (Piper)** | Dual Pin + M3 Fastener Slider | *In Progress* | [`grippers-stl/agilex_stl/`](../grippers-stl/agilex_stl/) |
| **Seeed Studio reBot** | AI Arm Parallel Gripper Slider | *In Progress* | [`grippers-stl/seeed_rebot_stl/`](../grippers-stl/seeed_rebot_stl/) |
| **Franka Panda / FR3** | Quick-Mount Dovetail / M4 Slider | *In Progress* | [`grippers-stl/franka_panda_stl/`](../grippers-stl/franka_panda_stl/) |
| **ARX5** | Direct Dual Lug M3 Pattern | *In Progress* | [`grippers-stl/arx5_stl/`](../grippers-stl/arx5_stl/) |
| **ISO 9409-1 (UR / xArm)** | Universal Tool Flange Adapter Plates | *In Progress* | [`grippers-stl/iso_flange_adapters_stl/`](../grippers-stl/iso_flange_adapters_stl/) |

*Status: Available (Production-ready STL models available) | In Progress (Community Contributions Welcome)*

---

## Contributing New Arm Adapters

To add an adapter for an unlisted robot arm or gripper:
1. Export high-resolution binary **STL** files into `grippers-stl/<arm_folder>_stl/`.
2. Follow the rules in [CONTRIBUTING.md](../CONTRIBUTING.md).
3. Open a Pull Request referencing the robot arm platform!
