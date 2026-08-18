# Robot Arm Compatibility Matrix & Specifications

The **ENPIRE Gripper Ecosystem** is designed to provide high-performance physical AI grasping across humanoid arms, bimanual learning rigs, collaborative robots, and low-cost hobbyist platforms.

---

## 1. Supported Robot Platforms

| Platform | Arm Type | Gripper Interface | Pitch / Spacing | Target STL Folder | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **I2RT YAM** | 6-DoF AI Research Arm | Native Dual M3 Clamp | 12.0 mm PCD | `stl/enpire_i2rt_yam/` | **Verified** (NVIDIA Baseline) |
| **AgileX Piper** | 6-DoF Lightweight Bimanual | Dual Pin + M3 Fastener | 14.0 mm width | `stl/agilex_piper/` | **Verified** |
| **Robotiq 2F-85** | Industrial 2-Finger Gripper | 2× M4 Bracket Mount | 10.0 mm spacing | `stl/robotiq_2f85_2f140/` | **Verified** |
| **Robotiq 2F-140** | Industrial Long-Stroke Gripper | 2× M4 Bracket Mount | 10.0 mm spacing | `stl/robotiq_2f85_2f140/` | **Verified** |
| **Franka Emika Panda / FR3** | 7-DoF Research Cobot | Quick-mount Dovetail / M4 | Franka Slider spec | `stl/franka_panda/` | **Verified** |
| **Universal Robots (UR3e / UR5e / UR10e)** | 6-DoF Industrial Cobot | ISO 9409-1-50-4-M6 | 50.0 mm PCD (4× M6) | `stl/iso_flange_adapters/` | **Verified** |
| **UFactory xArm 6 / 7** | 6/7-DoF Collaborative Arm | ISO 9409-1-50-4-M6 | 50.0 mm PCD (4× M6) | `stl/iso_flange_adapters/` | **Verified** |
| **SO-100 / Mobile ALOHA** | Low-Cost 3D Printed Arm | Servo Horn / Spline Clamp | Standard STS3215 | `stl/mobile_aloha_so100/` | **Verified** |
| **ARX5 / ARX Series** | 5/6-DoF Bimanual Arm | Direct M3 Dual Lug | 12.0 mm spacing | `stl/arx5/` | **Verified** |

---

## 2. Mechanical & Gripping Specifications

```
                     ◄──────── Total Stroke (60 - 140 mm) ────────►
               ┌──────────┐                               ┌──────────┐
               │  Left    │◄─── Gripping Contact Force ──►│  Right   │
               │  Finger  │                               │  Finger  │
               └────┬─────┘                               └─────┬────┘
                    │                                           │
             ┌──────┴───────────────────────────────────────────┴──────┐
             │                  Gripper Base Actuator                  │
             └─────────────────────────┬───────────────────────────────┘
                                       │
                              [ Robot Wrist Flange ]
```

| Parameter | I2RT YAM Native | AgileX Piper | Robotiq 2F-85 Mount | Franka Panda | SO-100 / ALOHA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Max Continuous Grip Force** | 45 N | 35 N | 85 N | 70 N | 15 N |
| **Max Stroke Range** | 80 mm | 70 mm | 85 mm | 80 mm | 60 mm |
| **Finger Weight (Pair)** | 90 g | 80 g | 100 g | 84 g | 50 g |
| **Fastener Specification** | 4× M3 × 12mm | 4× M3 × 10mm | 4× M4 × 16mm | 4× M4 × 12mm | 4× M2.5 / Servo |
| **Grip Face Options** | Grooved / Smooth / TPU | V-Groove / Slim | Extended / Heavy | Soft-Tip / TPU | Standard / Wide |

---

## 3. Adapting to Custom Robot Arms

To fit an unlisted robot arm flange:
1. Measure the **Pitch Circle Diameter (PCD)** and bolt hole size on your robot's tool flange.
2. Open `cad/open_scad/enpire_universal_adapter.scad` in [OpenSCAD](https://openscad.org).
3. Adjust `pcd_diameter` and `bolt_hole_diam` to match your arm.
4. Render (`F6`) and export as `.stl`.
