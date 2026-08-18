# Robot Arm Compatibility Matrix

The **Open-ENPIRE-Gripper-NVIDIA** project aims to establish an open standard across generalist robotic arms, bimanual learning platforms, collaborative cobots, and open-source hardware.

---

## Supported Robot Platforms & Adapter Directories

| Robot Platform | Arm Type / Gripper Interface | Status | Target STL Folder |
| :--- | :--- | :---: | :--- |
| **Robotiq Hand-E** | Precision Electric Parallel Gripper | **Available** | [`stl/hand_e_stl/`](../stl/hand_e_stl/) |
| **ALOHA / Mobile ALOHA** | ViperX Parallel Jaw Carriage | *In Progress* | [`stl/aloha_stl/`](../stl/aloha_stl/) |
| **Open Arm** | Modular Open-Source Parallel Mount | *In Progress* | [`stl/open_arm_stl/`](../stl/open_arm_stl/) |
| **AgileX (Piper)** | Dual Pin + M3 Fastener Slider | *In Progress* | [`stl/agilex_stl/`](../stl/agilex_stl/) |
| **Seeed Studio reBot** | AI Arm Parallel Gripper Slider | *In Progress* | [`stl/seeed_rebot_stl/`](../stl/seeed_rebot_stl/) |
| **Robotiq 2F-85 / 2F-140** | 2× M4 Bracket Mount (10 mm spacing) | *In Progress* | [`stl/robotiq_2f85_2f140_stl/`](../stl/robotiq_2f85_2f140_stl/) |
| **Franka Panda / FR3** | Quick-Mount Dovetail / M4 Slider | *In Progress* | [`stl/franka_panda_stl/`](../stl/franka_panda_stl/) |
| **ARX5** | Direct Dual Lug M3 Pattern | *In Progress* | [`stl/arx5_stl/`](../stl/arx5_stl/) |
| **I2RT YAM** | Native Dual M3 Clamp (Wenli Xiao Baseline) | *Baseline* | [`stl/enpire_i2rt_yam_stl/`](../stl/enpire_i2rt_yam_stl/) |
| **ISO 9409-1 (UR / xArm)** | Universal Tool Flange Adapter Plates | *In Progress* | [`stl/iso_flange_adapters_stl/`](../stl/iso_flange_adapters_stl/) |

*Status: Available (Ready to print) | In Progress (Community Contributions Welcome)*

---

## Contributing New Arm Adapters

To add an adapter for an unlisted robot arm or gripper:
1. Export high-resolution binary **STL** files into `stl/<arm_folder>_stl/`.
2. Follow the rules in [CONTRIBUTING.md](../CONTRIBUTING.md).
3. Open a Pull Request referencing the robot arm platform!
