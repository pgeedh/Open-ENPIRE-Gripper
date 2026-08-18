# Robot Arm Compatibility Matrix & Specifications

The **Open-ENPIRE-Gripper-NVIDIA** project aims to establish an open standard across generalist robotic arms, bimanual learning platforms, collaborative cobots, and open-source hardware.

---

## 1. Supported Robot Platforms & Adapter Directories

| Platform | Arm Type | Gripper Interface | Target Folder | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Robotiq Hand-E** | Precision Electric Parallel Gripper | 2× M4/M3 standard bracket | [`stl/hand_e_gripper/`](file:///stl/hand_e_gripper/) | **Primary Upload** |
| **ALOHA / Mobile ALOHA** | Bimanual Imitation Learning Rig | ViperX / Parallel jaw slider | [`stl/aloha/`](file:///stl/aloha/) | Ready for STLs |
| **Open Arm** | Open-Source Robotic Arm | Modular parallel gripper mount | [`stl/open_arm/`](file:///stl/open_arm/) | Ready for STLs |
| **AgileX Piper** | 6-DoF Lightweight Bimanual Arm | Dual Pin + M3 Fasteners | [`stl/agilex_piper/`](file:///stl/agilex_piper/) | Ready for STLs |
| **Seeed Studio reBot** | AI Robotic Arm Platform | Parallel gripper interface | [`stl/seeed_rebot/`](file:///stl/seeed_rebot/) | Ready for STLs |
| **Robotiq 2F-85 / 2F-140** | Industrial 2-Finger Gripper | 2× M4 Bracket Mount | [`stl/robotiq_2f85_2f140/`](file:///stl/robotiq_2f85_2f140/) | Ready for STLs |
| **Franka Emika Panda / FR3** | 7-DoF AI Research Cobot | Quick-Mount Dovetail / M4 | [`stl/franka_panda/`](file:///stl/franka_panda/) | Ready for STLs |
| **ARX5 / ARX Series** | 5/6-DoF Bimanual Arm | Direct Dual Lug M3 | [`stl/arx5/`](file:///stl/arx5/) | Ready for STLs |
| **I2RT YAM** | AI Research Arm | Native Dual M3 Clamp | [`stl/enpire_i2rt_yam/`](file:///stl/enpire_i2rt_yam/) | Wenli Xiao Baseline |
| **Universal Robots (UR3e/5e/10e)** | Industrial Cobots | ISO 9409-1-50-4-M6 Flange | [`stl/iso_flange_adapters/`](file:///stl/iso_flange_adapters/) | Flange Adapter |
| **UFactory xArm 6 / 7** | Collaborative Arm | ISO 9409-1-50-4-M6 Flange | [`stl/iso_flange_adapters/`](file:///stl/iso_flange_adapters/) | Flange Adapter |

---

## 2. Contributing New Arm Adapters

To add an adapter for an unlisted robot arm or gripper:
1. Export your CAD models as **STEP** in `cad/step/` and binary **STL** in `stl/<arm_folder>/`.
2. Open a Pull Request referencing the robot arm platform!
