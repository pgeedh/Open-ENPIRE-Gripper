# Rules for Contributing STL Models

Thank you for helping expand **Open-ENPIRE-Gripper-NVIDIA** across more robotic arms and gripper platforms!

To maintain strict mechanical tolerances, simulation compatibility, and print reliability, all contributed **STL models** must adhere to the rules outlined below.

---

## 1. 3D Model & STL Specifications

All submissions must provide clean 3D-printable **STL** files:

| Requirement | Specification | Verification Method |
| :--- | :--- | :--- |
| **File Format** | Binary `.stl` (High resolution) | Export as binary STL from CAD |
| **Units** | **Millimeters (mm)** (1 unit = 1 mm) | Mesh bounds check |
| **Manifoldness** | **Watertight / 2-Manifold** (0 non-manifold edges) | `python3 scripts/validate_mesh.py` |
| **Orientation** | Flat on lateral side (Layer lines parallel to tension) | Visual slicer inspection |
| **Tolerance** | Mounting hole clearance: nominal $+0.2\,\text{mm}$ | Caliper verification |

---

## 2. Coordinate System & File Naming Conventions

* **$+Z$ Axis**: Points along the length of the finger (from base mount to fingertip).
* **$+Y$ Axis**: Points inward toward the opposing finger (the contact grasp face).
* **$+X$ Axis**: Lateral width.

### Naming Pattern
Place STL files into the designated folder under `grippers-stl/<arm_name>_stl/` using clean, lowercase, snake_case naming:
```
grippers-stl/<arm_folder>_stl/
├── <arm_name>_enpire_finger_left.stl
├── <arm_name>_enpire_finger_right.stl
└── README.md
```

---

## 3. Physical 3D Test Print Required

Before submitting a Pull Request, you **must physically 3D-print and test the adapter** on your robot arm or gripper:

1. **Verify Full Stroke**: The fingers must open to full stroke and close completely without colliding, binding, or flexing unexpectedly.
2. **Verify Fastener Alignment**: Standard metric bolts (M3/M4) must seat cleanly into the counterbore holes without requiring manual drilling or reaming.
3. **Verify Grasp Stability**: Perform at least one physical grasp on a rigid object and a deformable object.

---

## 4. Pull Request Checklist

When opening a Pull Request, ensure:
1. **Target Directory**: Place STL files in the appropriate folder under `grippers-stl/`.
2. **Watertight Check**: Mesh validation passes:
   ```bash
   python3 scripts/validate_mesh.py
   ```
3. **Hardware Photos**: Attach at least **one clear photo** of the 3D-printed adapter installed on your robot arm.
4. **Slicer Settings**: Document your tested filament, layer height, wall loops, and infill pattern in your PR description.

Thank you for helping democratize physical AI hardware for the entire robotics community!
