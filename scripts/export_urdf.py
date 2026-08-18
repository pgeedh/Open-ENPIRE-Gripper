#!/usr/bin/env python3
"""
ENPIRE URDF Exporter & Validator
Generates and checks standalone URDF models for NVIDIA Isaac Sim, Isaac Lab,
ROS 2, MuJoCo, and PyBullet.
"""

import os
import xml.etree.ElementTree as ET

STANDALONE_MODELS = {
    "enpire_yam_gripper.urdf": {
        "robot_name": "enpire_yam_gripper",
        "mesh_left": "stl/enpire_i2rt_yam/enpire_yam_finger_standard_left.stl",
        "mesh_right": "stl/enpire_i2rt_yam/enpire_yam_finger_standard_right.stl",
        "stroke": 0.08,
        "mass": 0.045
    },
    "enpire_piper_gripper.urdf": {
        "robot_name": "enpire_piper_gripper",
        "mesh_left": "stl/agilex_piper/piper_enpire_finger_adapter_left.stl",
        "mesh_right": "stl/agilex_piper/piper_enpire_finger_adapter_right.stl",
        "stroke": 0.07,
        "mass": 0.040
    },
    "enpire_robotiq_gripper.urdf": {
        "robot_name": "enpire_robotiq_gripper",
        "mesh_left": "stl/robotiq_2f85_2f140/robotiq_enpire_bracket_left.stl",
        "mesh_right": "stl/robotiq_2f85_2f140/robotiq_enpire_bracket_right.stl",
        "stroke": 0.085,
        "mass": 0.050
    },
    "enpire_franka_gripper.urdf": {
        "robot_name": "enpire_franka_gripper",
        "mesh_left": "stl/franka_panda/franka_enpire_finger_left.stl",
        "mesh_right": "stl/franka_panda/franka_enpire_finger_right.stl",
        "stroke": 0.08,
        "mass": 0.042
    },
    "enpire_so100_gripper.urdf": {
        "robot_name": "enpire_so100_gripper",
        "mesh_left": "stl/mobile_aloha_so100/so100_enpire_finger_left.stl",
        "mesh_right": "stl/mobile_aloha_so100/so100_enpire_finger_right.stl",
        "stroke": 0.06,
        "mass": 0.025
    }
}

def generate_urdf(config: dict) -> str:
    r_name = config["robot_name"]
    m_left = config["mesh_left"]
    m_right = config["mesh_right"]
    stroke = config["stroke"]
    half_stroke = stroke / 2.0
    mass = config["mass"]

    return f"""<?xml version="1.0" encoding="utf-8"?>
<robot name="{r_name}">
  <!-- Gripper Base -->
  <link name="gripper_base_link">
    <inertial>
      <origin xyz="0 0 0.02" rpy="0 0 0"/>
      <mass value="0.25"/>
      <inertia ixx="0.0002" ixy="0" ixz="0" iyy="0.0002" iyz="0" izz="0.0001"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0.02" rpy="0 0 0"/>
      <geometry>
        <box size="0.04 0.08 0.04"/>
      </geometry>
      <material name="dark_gray">
        <color rgba="0.2 0.2 0.2 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0.02" rpy="0 0 0"/>
      <geometry>
        <box size="0.04 0.08 0.04"/>
      </geometry>
    </collision>
  </link>

  <!-- Left Finger Joint -->
  <joint name="left_finger_joint" type="prismatic">
    <origin xyz="0 0.02 0.04" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="left_finger_link"/>
    <axis xyz="0 1 0"/>
    <limit lower="0.0" upper="{half_stroke:.4f}" effort="50" velocity="0.2"/>
    <dynamics damping="1.0" friction="0.1"/>
  </joint>

  <!-- Left Finger Link -->
  <link name="left_finger_link">
    <inertial>
      <origin xyz="0 0.01 0.035" rpy="0 0 0"/>
      <mass value="{mass}"/>
      <inertia ixx="0.00003" ixy="0" ixz="0" iyy="0.00003" iyz="0" izz="0.00001"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="../{m_left}" scale="0.001 0.001 0.001"/>
      </geometry>
      <material name="nvidia_green">
        <color rgba="0.45 0.75 0.15 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="../{m_left}" scale="0.001 0.001 0.001"/>
      </geometry>
    </collision>
  </link>

  <!-- Right Finger Joint -->
  <joint name="right_finger_joint" type="prismatic">
    <origin xyz="0 -0.02 0.04" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="right_finger_link"/>
    <axis xyz="0 -1 0"/>
    <limit lower="0.0" upper="{half_stroke:.4f}" effort="50" velocity="0.2"/>
    <dynamics damping="1.0" friction="0.1"/>
    <mimic joint="left_finger_joint" multiplier="1.0" offset="0.0"/>
  </joint>

  <!-- Right Finger Link -->
  <link name="right_finger_link">
    <inertial>
      <origin xyz="0 -0.01 0.035" rpy="0 0 0"/>
      <mass value="{mass}"/>
      <inertia ixx="0.00003" ixy="0" ixz="0" iyy="0.00003" iyz="0" izz="0.00001"/>
    </inertial>
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="../{m_right}" scale="0.001 0.001 0.001"/>
      </geometry>
      <material name="nvidia_green">
        <color rgba="0.45 0.75 0.15 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <mesh filename="../{m_right}" scale="0.001 0.001 0.001"/>
      </geometry>
    </collision>
  </link>

  <!-- Tool Center Point (TCP) Frame -->
  <joint name="tcp_joint" type="fixed">
    <origin xyz="0 0 0.075" rpy="0 0 0"/>
    <parent link="gripper_base_link"/>
    <child link="tcp_link"/>
  </joint>
  <link name="tcp_link"/>
</robot>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    urdf_dir = os.path.join(base_dir, "urdf")
    os.makedirs(urdf_dir, exist_ok=True)
    
    print("Generating Standalone URDF Simulation Models...")
    for filename, cfg in STANDALONE_MODELS.items():
        content = generate_urdf(cfg)
        target_path = os.path.join(urdf_dir, filename)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
        # Validate XML
        try:
            ET.fromstring(content)
            print(f"  [+] Generated and validated: {target_path}")
        except ET.ParseError as e:
            print(f"  [-] XML Parse Error in {filename}: {e}")
            return 1

    print("\n[OK] All URDF models generated and validated successfully.")
    return 0

if __name__ == '__main__':
    exit(main())
