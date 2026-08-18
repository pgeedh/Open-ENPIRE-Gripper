# Contributing to the ENPIRE Gripper Project

We welcome community contributions, including new robot arm adapter brackets, improved finger geometries, tactile sensor integration, and simulation bindings!

## How to Contribute

### 1. Adding a New Robot Arm Adapter
1. Check existing models in `stl/` and `urdf/`.
2. Add parametric OpenSCAD or CAD definitions in `cad/` or python generators in `scripts/generate_stls.py`.
3. Export the watertight binary `.stl` into a new folder under `stl/<arm_name>/`.
4. Run `python3 scripts/validate_mesh.py` to ensure zero manifold defects.
5. Add the mechanical specifications to [ROBOT_COMPATIBILITY.md](file:///docs/ROBOT_COMPATIBILITY.md).
6. Submit a Pull Request referencing the hardware platform.

### 2. Code & CAD Standards
- **STL Units**: Millimeters (mm).
- **STL Format**: Binary STL (with standard 80-byte header and triangle normal vectors).
- **Coordinate Conventions**:
  - $+Z$: Pointing along finger extension towards fingertip.
  - $+Y$: Gripping contact normal (inward clamping direction).
  - $+X$: Lateral width across the finger face.
- **Fasteners**: Standard metric fasteners (M2.5, M3, M4, M5, M6) with ISO/DIN counterbores.
