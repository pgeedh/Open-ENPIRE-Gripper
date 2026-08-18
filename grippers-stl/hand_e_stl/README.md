# Robotiq Hand-E ENPIRE Gripper Finger Models

This directory contains the production-ready **3D-printable binary STL files** for mounting the ENPIRE high-friction compliant finger geometry directly onto the **Robotiq Hand-E** electric parallel gripper.

---

## 📦 Files in this Directory

* **`hand_e_enpire_finger_left.stl`** (Left finger adapter)
* **`hand_e_enpire_finger_right.stl`** (Right finger adapter)

---

## 📐 Mechanical Specifications

| Parameter | Value |
| :--- | :--- |
| **Gripper Compatibility** | Robotiq Hand-E (Linear Parallel Stroke) |
| **Mounting Fasteners** | 2× M4 / M3 socket head cap screws per finger |
| **Fastener Spacing** | Standard Robotiq 10 mm PCD pattern |
| **Overall Length ($+Z$)** | 96.0 mm |
| **Base Width ($+X$)** | 22.0 mm |
| **Linear Stroke** | 50.0 mm parallel travel |
| **Target Clamping Force** | Up to 130 N programmable force |
| **Friction Grip Face** | Ribbed compliant contact zone with dual-material core |

---

## 🖨️ Recommended 3D Printing Settings (Bambu Lab P1S)

* **Material**: **PETG-CF** or **PA12-CF** for the rigid body, **TPU 85A/95A** for the grip ribs.
* **Layer Height**: **0.16 mm**
* **Wall Loops**: **5 – 6 walls** (Crucial for screw counterbore strength)
* **Infill**: **50% – 60% Gyroid**
* **Supports**: Tree (Auto), 40° threshold, 0.20 mm Top Z distance
