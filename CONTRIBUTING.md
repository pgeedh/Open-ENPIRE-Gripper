# Contributing to Open-ENPIRE-Gripper-NVIDIA

We welcome community contributions! The goal of this project is to build an open standard of 3D printable ENPIRE-style high-friction gripper finger adapters for all generalist robotic arms.

---

## 📋 Rules for Contributing STL Files

To ensure that every 3D model in this repository is reliable, physically functional, and ready to print, all contributions must adhere to the following rules:

### 1. Watertight Mesh & Geometry Integrity
* **Units**: All STL files must be exported in **Millimeters (mm)**.
* **Format**: Export as solid, high-resolution **Binary STL** files.
* **Topology**: Meshes must be **100% watertight and manifold** (no self-intersections, no zero-area facets, no open boundary edges, and correctly oriented outward surface normals).
* **Validation**: Run the automated validator before submitting:
  ```bash
  python3 scripts/validate_mesh.py
  ```
  Your model must output `[PASS]` with valid dimensions and volume.

---

### 2. Standard Coordinate System & Orientation
All finger STL models should follow standard robotics coordinate conventions:
* **$+Z$ Axis**: Points along the length of the finger toward the fingertip.
* **$+Y$ Axis**: Points inward in the clamping/contact direction (the gripping face).
* **$+X$ Axis**: Points laterally across the finger width.
* **Print Orientation**: The model should be export-oriented to lay flat on its lateral side on the 3D printer build plate for maximum inter-layer shear strength under clamping tension.

---

### 3. Fastener & Tolerance Standards
* **Standard Metric Hardware**: Use standard metric fasteners (**M2.5, M3, M4, M5, M6**) conforming to ISO 4762 / DIN 912 socket head cap screws.
* **Counterbore Dimensions**: Include proper counterbore depth and clearance diameter so screw heads sit flush or recessed without interfering with robot arm mechanisms.
* **Heat-Set Insert Tolerances**: For brass heat-set threaded inserts, size pilot holes with standard FDM thermal expansion allowances ($+0.1\text{ mm}$ to $+0.2\text{ mm}$ over nominal insert outer diameter).

---

### 4. File Naming Conventions
Place STL files into the designated folder under `stl/<arm_name>/` using clean, lowercase, snake_case naming:
* Left Finger: `<arm>_enpire_finger_<variant>_left.stl` (e.g., `hand_e_enpire_finger_standard_left.stl`)
* Right Finger: `<arm>_enpire_finger_<variant>_right.stl`
* Symmetrical / Universal: `<arm>_enpire_finger_<variant>.stl` (e.g., `aloha_enpire_finger_grooved.stl`)
* Adapter Plates: `<standard>_adapter_plate.stl` (e.g., `iso_9409_1_50_4_m6_plate.stl`)

---

### 5. Physical Verification & Stroke Clearance
* **Physical Test Print Required**: Before submitting a PR, you **must physically 3D print the part** and mount it on the target robot gripper.
* **Full-Stroke Zero Interference**: Confirm that the fingers close and open across their full stroke range without binding, twisting, or colliding with the gripper chassis.

---

### 6. Pull Request (PR) Requirements
When submitting a Pull Request:
1. **Target Directory**: Place STL files in the appropriate folder under `stl/`.
2. **Include Photos**: Attach at least one clear photo or video of the 3D-printed part mounted on the actual robot arm or gripper.
3. **Specify Print Parameters**:
   - Material used (e.g., PETG-CF, PA12-CF, PLA+, TPU 95A)
   - Slicer settings (layer height, number of perimeters/walls, infill percentage)
   - Fastener sizes used for installation.
4. **Update Documentation**: Add your robot arm details to [docs/ROBOT_COMPATIBILITY.md](file:///docs/ROBOT_COMPATIBILITY.md).

---

## 🛠️ Step-by-Step Contribution Workflow

1. **Fork the Repository** on GitHub.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feat/add-<arm-name>-finger-stl
   ```
3. **Add Your STL Files** to `stl/<arm-name>/`.
4. **Run the Mesh Validator**:
   ```bash
   python3 scripts/validate_mesh.py
   ```
5. **Commit and Push**:
   ```bash
   git add stl/<arm-name>/
   git commit -m "feat: add <arm-name> ENPIRE gripper finger STL models"
   git push origin feat/add-<arm-name>-finger-stl
   ```
6. **Open a Pull Request** with your test print photos and slicer details!
