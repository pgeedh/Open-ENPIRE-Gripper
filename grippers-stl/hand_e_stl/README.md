<div align="center">

<img src="../../docs/images/robotiq_logo.png" alt="Robotiq Logo" width="180" />

# Robotiq Hand-E Universal Compliant Gripper (UCG)

### Transforming the Standard Industrial Robotiq Hand-E into a Frontier High-Friction Compliant Gripper for Robot Learning & Physical AI

<br>

<table align="center" border="0">
  <tr>
    <th align="center" width="50%">Standard OEM Robotiq Hand-E</th>
    <th align="center" width="50%">Robotiq Hand-E + ENPIRE UCG Compliant Fingers</th>
  </tr>
  <tr>
    <td align="center" valign="top">
      <img src="../../docs/images/robotiq_hand_e_standard.jpg" alt="Standard OEM Robotiq Hand-E" width="100%" />
    </td>
    <td align="center" valign="top">
      <img src="../../docs/images/robotiq_hand_e_ucg_mounted.jpg" alt="Robotiq Hand-E with ENPIRE UCG Fingers" width="100%" />
    </td>
  </tr>
</table>

</div>

---

## 📦 Production-Ready STL Files

This directory contains the production-ready **3D-printable binary STL files** for mounting the ENPIRE Universal Compliant Gripper (UCG) fingertip geometry directly onto the **Robotiq Hand-E** electric parallel gripper:

* **`hand_e_enpire_finger_left.stl`** (Left finger adapter)
* **`hand_e_enpire_finger_right.stl`** (Right finger adapter)

---

## 📐 Mechanical Specifications

| Parameter | Specification |
| :--- | :--- |
| **Gripper Platform** | **Robotiq Hand-E** (Linear Parallel Stroke) |
| **Finger Design Paradigm** | **Universal Compliant Gripper (UCG)** |
| **Mounting Fasteners** | 2× M4 / M3 socket head cap screws per finger |
| **Fastener Spacing** | Standard Robotiq 10 mm PCD pattern |
| **Overall Length ($+Z$)** | 96.0 mm |
| **Base Width ($+X$)** | 22.0 mm |
| **Linear Stroke** | 50.0 mm parallel travel |
| **Programmable Clamping Force** | 20 N to 130 N |
| **Contact Surface** | Dual-material rigid backbone with ribbed compliant high-friction core ($\mu > 0.8$) |

---

## 🖨️ Tested 3D Printing Profile (Bambu Lab P1S)

* **Materials**:
  * **Outer Rigid Backbone**: **PETG-CF**, **PLA-CF**, or **PA12-CF (Nylon-CF)** (Blue)
  * **Compliant Friction Core**: **TPU 85A** or **TPU 95A** (Orange)
* **Layer Height**: **0.16 mm** (Optimal for screw counterbores)
* **Wall Loops / Perimeters**: **5 to 6 walls** (Critical for bolt clamp strength)
* **Infill Pattern & Density**: **50% – 60% Gyroid** (Rigid frame) / **30% – 40% Gyroid** (TPU core)
* **Support Configuration**: Tree (Auto), 40° threshold, 0.20 mm Top Z distance
