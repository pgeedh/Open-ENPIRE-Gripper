# 3D Printing & Fabrication Guide

This guide provides optimal slicing parameters, print orientations, material selections, and post-processing instructions for manufacturing **ENPIRE Gripper** components on modern FDM and SLA/Resin 3D printers.

---

## 1. Print Orientation & Layer Adhesion

To ensure maximum shear and tensile strength under high gripping forces:
- **Structural Fingers**: Print oriented **flat on their side** (lateral surface) rather than vertically standing. Printing horizontally aligns the layer lines along the direction of bending tension, preventing delamination along layer boundaries under clamping loads.
- **TPU Grip Pads**: Print flat on the build plate with the textured/ridged contact face pointing **upward**.
- **Silicone Molds**: Print vertically with a layer height of $0.12\text{ mm}$ or $0.16\text{ mm}$ to ensure smooth inner cavity walls with minimal stepping.

```
      Horizontal Orientation (RECOMMENDED)
      ┌──────────────────────────────────────────────┐
      │  Mounting Base  ======> Structural Beam Tip  │  <-- Layer lines run parallel to tension
      └──────────────────────────────────────────────┘
      ════════════════════════════════════════════════ (Build Plate)

      Vertical Orientation (AVOID for high-force fingers)
             ▲  Tip
             │
             │  (Shear stress splits layer lines)
             │
             ▼  Mount
      ═════════════════ (Build Plate)
```

---

## 2. Recommended Slicer Profiles (FDM / FFF)

| Parameter | Structural Parts (PLA-CF / PETG-CF / PA-CF) | Flexible Pads (TPU 85A/95A) | Silicone Molds (PLA / PETG) |
| :--- | :--- | :--- | :--- |
| **Layer Height** | 0.16mm – 0.20mm | 0.16mm – 0.20mm | 0.12mm – 0.16mm |
| **First Layer Height** | 0.20mm | 0.20mm | 0.20mm |
| **Wall Loops (Perimeters)** | **5 to 6 walls** (Critical for strength) | 4 walls | 4 walls |
| **Top / Bottom Solid Layers** | 5 top, 5 bottom | 4 top, 4 bottom | 5 top, 5 bottom |
| **Infill Density** | 40% – 60% (or 100% solid) | 30% – 50% | 25% |
| **Infill Pattern** | Gyroid or Cubic | Gyroid | Grid / Gyroid |
| **Print Speed** | 60 – 150 mm/s (per filament spec) | 20 – 40 mm/s | 60 – 100 mm/s |
| **Nozzle Temperature** | PETG: 245°C–255°C / PA-CF: 275°C–290°C | 225°C – 235°C | 210°C – 220°C |
| **Bed Temperature** | PETG: 75°C–80°C / PA-CF: 100°C | 50°C – 60°C (PEI textured) | 55°C – 65°C |
| **Supports** | Tree / Organic supports (Overhang angle: 45°) | None needed | None needed |

---

## 3. Bambu Lab, PrusaSlicer & OrcaSlicer 3MF Notes

- When using **Bambu Studio** or **OrcaSlicer**, select the `0.16mm Optimal @BBL X1C` or `0.20mm Standard` profile.
- Enable `Fuzzy Skin` on outer contact surfaces (Contour thickness: 0.1mm, Point distance: 0.2mm) if you want a high-grip tactile texture directly off the print bed without TPU inserts.

---

## 4. Post-Processing & Heat-Set Insert Installation

1. **Clean Support Material**: Remove tree supports using needle-nose pliers and deburr mounting faces with a hobby knife.
2. **Install Heat-Set Brass Inserts**:
   - Set soldering iron temperature to **230°C** for PETG / PLA-CF, or **275°C** for PA-CF.
   - Place the brass insert into the pilot hole.
   - Lightly press the soldering iron tip into the insert bore until the brass softens the surrounding plastic and sinks flush with the surface.
   - Allow cooling for 60 seconds before applying screw torque.
3. **Inspect Thread Clearances**: Thread an M3 screw by hand to verify smooth travel without plastic obstruction.
