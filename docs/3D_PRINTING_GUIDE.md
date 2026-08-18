# 3D Printing & Fabrication Guide

This guide details the recommended materials, slicing profiles, and hardware assembly steps for manufacturing the **Open-ENPIRE-Gripper** finger adapters.

All components have been printed, fitted, and tested on a **Bambu Lab P1S** using **Bambu Studio / OrcaSlicer**.

---

## 1. Material Recommendations

### A. Rigid Structural Outer Frame
* **Primary Recommendation**: **PETG-CF** or **PLA-CF** (Carbon Fiber reinforced).
* **High-End Industrial Option**: **PA12-CF (Nylon-CF)**.
* **Why CF Filament?**: Carbon fiber infill significantly increases tensile modulus, prevents bending under 130 N clamping forces, and provides clean dimensional accuracy for M3/M4 bolt counterbores.

### B. High-Friction Compliant Grip Core
* **Primary Recommendation**: **TPU 85A** or **TPU 95A** (Thermoplastic Polyurethane).
* **Why TPU?**: Offers exceptional surface friction ($\mu > 0.8$) and elasticity, allowing the fingertips to conform passively around micro-pins, deformable cables, and delicate PCBs without marring surfaces.

---

## 2. Tested Slicer Profiles (Bambu Lab P1S)

| Parameter | Rigid Frame (PETG-CF / PA-CF) | Compliant Grip Core (TPU 85A/95A) |
| :--- | :--- | :--- |
| **Tested Machine** | **Bambu Lab P1S** | **Bambu Lab P1S** |
| **Layer Height** | **0.16 mm** | **0.16 mm – 0.20 mm** |
| **Wall Loops / Perimeters** | **5 – 6 walls** (Critical for strength) | **4 walls** |
| **Top / Bottom Solid Layers** | **5 Top, 5 Bottom** | **4 Top, 4 Bottom** |
| **Infill Pattern** | **Gyroid (50% – 60%)** | **Gyroid (30% – 40%)** |
| **Nozzle Temperature** | 255°C (PETG-CF) / 285°C (PA-CF) | 225°C – 235°C (TPU) |
| **Bed Temperature** | 70°C – 80°C (Textured PEI Plate) | 45°C – 55°C (Engineering Plate) |
| **Printing Speed** | 80 – 160 mm/s | 20 – 35 mm/s |
| **Supports** | Tree Auto (40° threshold, 0.2mm Top-Z) | None needed |

---

## 3. Infill Geometry & Support Details

### Infill Pattern
* **Gyroid**: Strongly recommended over Grid or Triangles. Gyroid distributes compression and shear stresses isotropically in 3D, preventing internal shear fractures when clamping under high motor current.

### Support Settings (Bambu Studio / OrcaSlicer)
* **Support Type**: Tree (Auto) / Tree Slim
* **Threshold Angle**: 35° – 45°
* **Top Z Distance**: **0.20 mm** (enables clean interface release with zero surface scarring)
* **Bottom Z Distance**: 0.20 mm
* **Support Wall Loops**: 1

---

## 4. Hardware Assembly Tips

1. **Heat-Set Threaded Inserts**:
   * Set your soldering iron to **230°C** for PETG/PLA or **275°C** for PA-CF.
   * Press M3 or M4 brass inserts straight and flush with the plastic face.
2. **Fastener Torquing & Threadlocker**:
   * Use Grade 12.9 M3/M4 socket head cap screws.
   * Apply medium blue threadlocker (Loctite 243) to prevent bolts from loosening under high-speed robotic cycles.
