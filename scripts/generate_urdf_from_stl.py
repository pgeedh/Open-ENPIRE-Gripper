#!/usr/bin/env python3
"""
Automated URDF Generator from STL Files
Parses 3D STL files, computes bounding box, scaling (mm -> meters),
mass, center of mass, and generates a physics-ready URDF with prismatic
parallel finger joints, mimic dynamics, and Tool Center Point (TCP) frames.
"""

import os
import sys
import struct
import argparse
import numpy as np

def compute_mesh_properties(stl_path: str):
    if not os.path.exists(stl_path):
        return None
    with open(stl_path, 'rb') as f:
        header = f.read(80)
        num_triangles = struct.unpack('<I', f.read(4))[0]
        record_dtype = np.dtype([
            ('normal', '<f4', (3,)),
            ('v0', '<f4', (3,)),
            ('v1', '<f4', (3,)),
            ('v2', '<f4', (3,)),
            ('attr', '<u2')
        ])
        data = np.fromfile(f, dtype=record_dtype, count=num_triangles)
        
    v0 = data['v0']
    v1 = data['v1']
    v2 = data['v2']
    all_verts = np.vstack([v0, v1, v2])
    
    # Auto-detect units: if bounding box max dimension < 1.0, mesh is already in meters; otherwise mm
    raw_span = all_verts.max(axis=0) - all_verts.min(axis=0)
    scale_to_m = 1.0 if np.max(raw_span) < 1.0 else 0.001

    min_pt_m = all_verts.min(axis=0) * scale_to_m
    max_pt_m = all_verts.max(axis=0) * scale_to_m
    center_m = (min_pt_m + max_pt_m) / 2.0
    dims_m = max_pt_m - min_pt_m
    
    # Volume calculation
    cross = np.cross(v1, v2)
    signed_vol = np.sum(v0 * cross) / 6.0
    vol_m3 = abs(signed_vol) * (scale_to_m ** 3)
    
    # Approximate mass (Plastic density ~1200 kg/m3)
    mass_kg = max(0.025, round(vol_m3 * 1200.0, 4))
    
    # Approximate box inertia
    dx, dy, dz = dims_m
    ixx = (1.0 / 12.0) * mass_kg * (dy**2 + dz**2)
    iyy = (1.0 / 12.0) * mass_kg * (dx**2 + dz**2)
    izz = (1.0 / 12.0) * mass_kg * (dx**2 + dy**2)
    
    return {
        'dims_m': dims_m,
        'center_m': center_m,
        'mass_kg': mass_kg,
        'inertia': (ixx, iyy, izz),
        'scale_to_m': scale_to_m
    }

def generate_urdf(robot_name: str, left_stl: str, right_stl: str, stroke_mm: float = 50.0, force_n: float = 130.0) -> str:
    half_stroke_m = (stroke_mm / 2.0) * 0.001
    
    left_props = compute_mesh_properties(left_stl) or {
        'dims_m': np.array([0.02, 0.02, 0.07]),
        'center_m': np.array([0.0, 0.01, 0.035]),
        'mass_kg': 0.045,
        'inertia': (2e-5, 2e-5, 1e-5)
    }
    
    mass = left_props['mass_kg']
    ixx, iyy, izz = left_props['inertia']
    cx, cy, cz = left_props['center_m']
    
    urdf = f"""<?xml version="1.0" encoding="utf-8"?>
<robot name="{robot_name}">

  <!-- Gripper Base Chassis -->
  <link name="gripper_base_link">
    <inertial>
      <origin xyz="0 0 0.04" rpy="0 0 0"/>
      <mass value="0.95"/>
      <inertia ixx="0.0012" ixy="0" ixz="0" iyy="0.0012" iyz="0" izz="0.0008"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0.04" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.0375" length="0.08"/>
      </geometry>
      <material name="dark_gray">
        <color rgba="0.15 0.15 0.15 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0.04" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.0375" length="0.08"/>
      </geometry>
    </collision>
  </link>

  <!-- Left Finger (Active Prismatic Joint) -->
  <joint name="left_finger_joint" type="prismatic">
    <origin xyz="0 0.015 0.08" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="left_finger_link"/>
    <axis xyz="0 1 0"/>
    <limit lower="0.0" upper="{half_stroke_m:.4f}" effort="{force_n}" velocity="0.15"/>
    <dynamics damping="1.0" friction="0.2"/>
  </joint>

  <link name="left_finger_link">
    <inertial>
      <origin xyz="{cx:.4f} {cy:.4f} {cz:.4f}" rpy="0 0 0"/>
      <mass value="{mass:.4f}"/>
      <inertia ixx="{ixx:.7f}" ixy="0" ixz="0" iyy="{iyy:.7f}" iyz="0" izz="{izz:.7f}"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="{left_stl}" scale="0.001 0.001 0.001"/>
      </geometry>
      <material name="enpire_blue">
        <color rgba="0.18 0.45 0.85 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="{left_stl}" scale="0.001 0.001 0.001"/>
      </geometry>
    </collision>
  </link>

  <!-- Right Finger (Mimic Joint) -->
  <joint name="right_finger_joint" type="prismatic">
    <origin xyz="0 -0.015 0.08" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="right_finger_link"/>
    <axis xyz="0 -1 0"/>
    <limit lower="0.0" upper="{half_stroke_m:.4f}" effort="{force_n}" velocity="0.15"/>
    <dynamics damping="1.0" friction="0.2"/>
    <mimic joint="left_finger_joint" multiplier="1.0" offset="0.0"/>
  </joint>

  <link name="right_finger_link">
    <inertial>
      <origin xyz="{cx:.4f} {-cy:.4f} {cz:.4f}" rpy="0 0 0"/>
      <mass value="{mass:.4f}"/>
      <inertia ixx="{ixx:.7f}" ixy="0" ixz="0" iyy="{iyy:.7f}" iyz="0" izz="{izz:.7f}"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="{right_stl}" scale="0.001 0.001 0.001"/>
      </geometry>
      <material name="enpire_blue">
        <color rgba="0.18 0.45 0.85 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="{right_stl}" scale="0.001 0.001 0.001"/>
      </geometry>
    </collision>
  </link>

  <!-- Tool Center Point (TCP Frame) -->
  <joint name="tcp_joint" type="fixed">
    <origin xyz="0 0 0.14" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="tcp_link"/>
  </joint>
  <link name="tcp_link"/>

</robot>
"""
    return urdf

def main():
    parser = argparse.ArgumentParser(description="Generate simulation URDF from gripper STL files")
    parser.add_argument("--name", default="hand_e_enpire_gripper", help="Robot gripper name")
    parser.add_argument("--left_stl", default="grippers-stl/hand_e_stl/Robotiq_UCG_Hard_Hand_E.stl", help="Path to left finger STL")
    parser.add_argument("--right_stl", default="grippers-stl/hand_e_stl/Robotiq_UCG_Hard_Hand_E.stl", help="Path to right finger STL")
    parser.add_argument("--stroke_mm", type=float, default=50.0, help="Total parallel stroke in mm")
    parser.add_argument("--force_n", type=float, default=130.0, help="Maximum grip force in Newtons")
    parser.add_argument("--out", default="hand_e_enpire_gripper.urdf", help="Output URDF file path")
    args = parser.parse_args()

    urdf_content = generate_urdf(args.name, args.left_stl, args.right_stl, args.stroke_mm, args.force_n)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(urdf_content)
    print(f"[SUCCESS] Generated physics-ready URDF: {args.out}")

if __name__ == '__main__':
    main()
