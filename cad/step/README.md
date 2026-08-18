# CAD STEP Models & Interchange Files

This directory is reserved for standard **ISO 10303 STEP (.step / .stp)** exchange files and raw CAD assemblies.

## Directory Layout
- `cad/step/enpire_yam_gripper_assembly.step`: Full CAD assembly for the I2RT YAM ENPIRE gripper.
- `cad/step/piper_adapter_assembly.step`: AgileX Piper gripper adapter assembly.
- `cad/step/robotiq_adapter_assembly.step`: Robotiq 2F-85 / 2F-140 bracket assembly.
- `cad/step/franka_adapter_assembly.step`: Franka Emika Panda / FR3 dovetail assembly.
- `cad/step/universal_iso_flange_assembly.step`: ISO 9409-1 tool flange adapter.

## How to Add / Export Your CAD Files
If you are developing or modifying designs in **SolidWorks**, **Autodesk Fusion 360**, **Onshape**, **FreeCAD**, or **PTC Creo**:
1. Export as **STEP AP214** or **STEP AP203** format for maximum CAD interoperability.
2. Place the resulting `.step` files in this directory.
3. If generating 3D printable meshes, export as high-resolution binary `.stl` (chord tolerance $\le 0.01\text{ mm}$, angular tolerance $\le 5^\circ$) and place them into the respective folder in `stl/`.
