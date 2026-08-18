# Simulation Guide (NVIDIA Isaac Sim, MuJoCo, ROS 2)

This guide covers importing and controlling the **ENPIRE Gripper** in robotics simulation environments.

---

## 1. NVIDIA Isaac Sim & Isaac Lab (Omniverse)

The ENPIRE gripper URDFs are directly compatible with NVIDIA Isaac Sim / Isaac Lab:

### Loading the URDF in Isaac Sim
1. In Isaac Sim, navigate to `Isaac Utils` -> `Workflows` -> `URDF Importer`.
2. Select `urdf/enpire_yam_gripper.urdf` (or your arm of choice).
3. Set the following import options:
   - **Fix Base Link**: Checked (or attach to robot arm tool link).
   - **Self Collision**: Enabled.
   - **Convex Decomposition**: Enabled (V-HACD algorithm).
   - **Drive Type**: `Position` or `Force` (Gain: $k_p=1000$, $k_d=50$).
4. Click **Import**.

### Isaac Lab Simulation Python Snippet
```python
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg

ENPIRE_GRIPPER_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/Robot/enpire_gripper",
    spawn=None,
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.0),
        joint_pos={"left_finger_joint": 0.04, "right_finger_joint": 0.04},
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*_finger_joint"],
            effort_limit=50.0,
            velocity_limit=0.2,
            stiffness=1000.0,
            damping=50.0,
        ),
    },
)
```

---

## 2. MuJoCo Simulation

To import into MuJoCo, convert the URDF using the built-in compiler:
```bash
# Convert URDF to MJCF XML
python3 -c "import mujoco; m = mujoco.MjModel.from_xml_path('urdf/enpire_yam_gripper.urdf'); print('Loaded successfully in MuJoCo! NV:', m.nv)"
```

---

## 3. ROS 2 & MoveIt 2 Integration

Include the parameterized Xacro macro inside your robot's main URDF/Xacro description:

```xml
<xacro:include filename="$(find enpire_gripper)/urdf/enpire_gripper.urdf.xacro" />

<!-- Attach ENPIRE gripper to robot wrist / tool flange -->
<xacro:enpire_gripper prefix="gripper_" parent="wrist_3_link" stroke="0.08">
  <origin xyz="0 0 0" rpy="0 0 0" />
</xacro:enpire_gripper>
```
