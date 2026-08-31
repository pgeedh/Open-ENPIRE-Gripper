# Open Arm Universal Compliant Gripper (UCG) STL Models

### 3D-Printable High-Friction Compliant Gripper Adapters for Open Arm Platforms

<br>

## Overview

This directory contains the production-ready 3D-printable binary STL files for mounting the **Universal Compliant Gripper (UCG)** geometry directly onto **Open Arm** robotic manipulators. 

By translating the high-friction, compliant contact profile into the Open Arm platform, researchers and builders can achieve frontier-grade physical AI grasping reliability on accessible open-source robotics hardware.

---

## 📦 Production-Ready STL Models

* **`OpenArm_UCG_left_hard.stl`** — Primary rigid structural jaw adapter for Open Arm parallel sliders (print in PETG-CF / PA-CF / PLA-CF).

---

## 📐 Mechanical Specifications

| Parameter | Specification |
| :--- | :--- |
| **Robot Platform** | **Open Arm** Robotic Manipulator |
| **Gripper Architecture** | **Universal Compliant Gripper (UCG)** Parallel Jaw |
| **Mounting Interface** | Modular parallel jaw slider mount |
| **Overall Length ($+X$)** | 121.7 mm |
| **Height ($+Y$)** | 61.0 mm |
| **Width ($+Z$)** | 32.6 mm |
| **Estimated Stroke** | 60.0 mm – 70.0 mm |
| **Primary Material** | **PETG-CF** / **PA12-CF** (Rigid Backbone) |
| **Best Applications** | Open-source robotics education, accessible physical AI manipulation, imitation learning |

---

## 🖨️ Tested 3D Printing Profile (Bambu Lab P1S)

All models are verified for dimensional accuracy and structural rigidity:

* **Filament**: **PETG-CF**, **PA12-CF (Nylon-CF)**, or **PLA-CF**
* **Layer Height**: **0.16 mm** (Optimal for mounting tolerances and screw counterbores)
* **Wall Loops / Perimeters**: **5 to 6 walls** (Critical for beam stiffness under clamping load)
* **Infill Pattern & Density**: **50% – 60% Gyroid** (Isotropic shear load resistance)
* **Support Configuration**: Tree (Auto), 40° threshold angle, **0.20 mm Top Z distance**

---

## 🤝 Community Contributions

> 💡 **Have an additional variation?** If you have designed a complementary right jaw, soft TPU friction insert, or alternate slider bracket for Open Arm, we would love your contribution!
>
> Please submit a **[Pull Request](https://github.com/pgeedh/Open-ENPIRE-Gripper-nvidia/pulls)** following our [Rules for Contributing](../../CONTRIBUTING.md).
