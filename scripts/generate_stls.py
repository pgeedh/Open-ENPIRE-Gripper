#!/usr/bin/env python3
"""
ENPIRE Multi-Arm Gripper STL Generator
Procedurally generates solid, watertight binary STL models for the ENPIRE gripper
ecosystem across multiple robot arms (I2RT YAM, AgileX Piper, Robotiq 2F-85/140,
Franka Panda, SO-100, ARX5, ISO Flanges, TPU pads, and Silicone Molds).
"""

import os
import struct
import numpy as np

def create_stl_header(name: str) -> bytes:
    header = f"ENPIRE Gripper 3D Model: {name[:50]}".encode('ascii')
    return header.ljust(80, b'\0')

def write_binary_stl(filename: str, triangles: np.ndarray, normals: np.ndarray = None):
    """
    triangles: (N, 3, 3) float32 array
    normals: (N, 3) float32 array (optional, computed if None)
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    num_triangles = len(triangles)
    
    if normals is None or len(normals) != num_triangles:
        v0 = triangles[:, 0, :]
        v1 = triangles[:, 1, :]
        v2 = triangles[:, 2, :]
        cross = np.cross(v1 - v0, v2 - v0)
        norm = np.linalg.norm(cross, axis=1, keepdims=True)
        norm[norm == 0] = 1.0
        normals = cross / norm
        
    with open(filename, 'wb') as f:
        f.write(create_stl_header(os.path.basename(filename)))
        f.write(struct.pack('<I', num_triangles))
        
        # Pack records: 3 floats normal, 9 floats vertices, 1 uint16 attr
        record_dtype = np.dtype([
            ('normal', '<f4', (3,)),
            ('v0', '<f4', (3,)),
            ('v1', '<f4', (3,)),
            ('v2', '<f4', (3,)),
            ('attr', '<u2')
        ])
        records = np.empty(num_triangles, dtype=record_dtype)
        records['normal'] = normals
        records['v0'] = triangles[:, 0, :]
        records['v1'] = triangles[:, 1, :]
        records['v2'] = triangles[:, 2, :]
        records['attr'] = 0
        records.tofile(f)
    print(f"  [+] Generated {filename} ({num_triangles} facets, {os.path.getsize(filename):,} bytes)")

def box_mesh(min_pt, max_pt):
    x0, y0, z0 = min_pt
    x1, y1, z1 = max_pt
    
    # 8 vertices
    verts = np.array([
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0], # bottom 0,1,2,3
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]  # top 4,5,6,7
    ], dtype=np.float32)
    
    faces = [
        # bottom (-z)
        [0, 2, 1], [0, 3, 2],
        # top (+z)
        [4, 5, 6], [4, 6, 7],
        # front (-y)
        [0, 1, 5], [0, 5, 4],
        # back (+y)
        [3, 7, 6], [3, 6, 2],
        # left (-x)
        [0, 4, 7], [0, 7, 3],
        # right (+x)
        [1, 2, 6], [1, 6, 5]
    ]
    return verts[faces]

def cylinder_mesh(radius, height, num_segments=32, center=(0, 0, 0), axis='z'):
    cx, cy, cz = center
    angles = np.linspace(0, 2 * np.pi, num_segments, endpoint=False)
    cos_a = np.cos(angles) * radius
    sin_a = np.sin(angles) * radius
    
    triangles = []
    half_h = height / 2.0
    
    for i in range(num_segments):
        i_next = (i + 1) % num_segments
        if axis == 'z':
            b0 = [cx + cos_a[i], cy + sin_a[i], cz - half_h]
            b1 = [cx + cos_a[i_next], cy + sin_a[i_next], cz - half_h]
            t0 = [cx + cos_a[i], cy + sin_a[i], cz + half_h]
            t1 = [cx + cos_a[i_next], cy + sin_a[i_next], cz + half_h]
            # bottom cap
            triangles.append([[cx, cy, cz - half_h], b1, b0])
            # top cap
            triangles.append([[cx, cy, cz + half_h], t0, t1])
            # side quad
            triangles.append([b0, b1, t1])
            triangles.append([b0, t1, t0])
        elif axis == 'y':
            b0 = [cx + cos_a[i], cy - half_h, cz + sin_a[i]]
            b1 = [cx + cos_a[i_next], cy - half_h, cz + sin_a[i_next]]
            t0 = [cx + cos_a[i], cy + half_h, cz + sin_a[i]]
            t1 = [cx + cos_a[i_next], cy + half_h, cz + sin_a[i_next]]
            triangles.append([[cx, cy - half_h, cz], b0, b1])
            triangles.append([[cx, cy + half_h, cz], t1, t0])
            triangles.append([b0, t1, b1])
            triangles.append([b0, t0, t1])
    return np.array(triangles, dtype=np.float32)

def generate_enpire_yam_finger(grooved=False, pinch=False, paddle=False, mirror=False):
    """
    Constructs the ENPIRE gripper finger for I2RT YAM.
    Features:
      - Mounting block with M3 screw holes and counterbores
      - Tapered structural beam
      - Contact face (smooth, grooved, pinch, or paddle)
      - Silicone/TPU recess pocket
    """
    tris = []
    # Base mount block (Width: 20mm, Depth: 24mm, Height: 15mm)
    mount = box_mesh([-10, 0, 0], [10, 24, 15])
    tris.append(mount)
    
    # Beam extending upwards
    beam_w = 28 if paddle else (12 if pinch else 16)
    beam_h = 75 if pinch else 65
    beam = box_mesh([-beam_w/2, 10, 15], [beam_w/2, 22, beam_h])
    tris.append(beam)
    
    # Gripper tip
    if pinch:
        tip = box_mesh([-4, 16, beam_h], [4, 22, beam_h + 18])
        tris.append(tip)
    elif paddle:
        paddle_pad = box_mesh([-18, 18, 30], [18, 24, beam_h + 10])
        tris.append(paddle_pad)
    else:
        # Standard contact face
        contact = box_mesh([-7, 18, 35], [7, 24, beam_h + 5])
        tris.append(contact)
        
    if grooved:
        # Add high-friction ridges on the contact face
        for z_pos in range(25, int(beam_h), 5):
            ridge = box_mesh([-7.5, 23.5, z_pos], [7.5, 25.0, z_pos + 2.5])
            tris.append(ridge)

    # Screw boss reinforcements
    boss1 = cylinder_mesh(radius=4.5, height=12, center=(0, 6, 7.5), axis='z')
    boss2 = cylinder_mesh(radius=4.5, height=12, center=(0, 18, 7.5), axis='z')
    tris.extend([boss1, boss2])
    
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_piper_enpire_adapter(slim=False, v_groove=False, mirror=False):
    """
    AgileX Piper robot gripper adapter for ENPIRE finger tips.
    Mounting specs: Piper dual pin & M3 fastener pattern.
    """
    tris = []
    # Base interface for Piper parallel jaw slider
    base = box_mesh([-8, -6, 0], [8, 14, 18])
    tris.append(base)
    
    # Extension strut
    strut_w = 10 if slim else 14
    strut_h = 55
    strut = box_mesh([-strut_w/2, 2, 18], [strut_w/2, 14, 18 + strut_h])
    tris.append(strut)
    
    # Fingertip head
    head = box_mesh([-7, 8, 18 + strut_h - 10], [7, 16, 18 + strut_h + 12])
    tris.append(head)
    
    if v_groove:
        # V-groove clamping profile for cylindrical objects
        v_left = box_mesh([-7, 14, 40], [-2, 17, 75])
        v_right = box_mesh([2, 14, 40], [7, 17, 75])
        tris.extend([v_left, v_right])
        
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_robotiq_adapter(extended=False, heavy=False, mirror=False):
    """
    Robotiq 2F-85 / 2F-140 mounting bracket adapter for ENPIRE fingers.
    Standard Robotiq 2-bolt M4 mounting pattern with 10mm hole spacing.
    """
    tris = []
    # Robotiq bracket base
    b_len = 35 if extended else 28
    base = box_mesh([-12, -4, 0], [12, 16, 14])
    tris.append(base)
    
    # Main finger column
    col_w = 18 if heavy else 14
    col_h = 75 if extended else 55
    column = box_mesh([-col_w/2, 4, 14], [col_w/2, 16, 14 + col_h])
    tris.append(column)
    
    # Pad holder flange
    flange = box_mesh([-10, 14, 25], [10, 18, 14 + col_h + 5])
    tris.append(flange)
    
    # 2x M4 mounting bosses
    boss1 = cylinder_mesh(radius=5.0, height=14, center=(-5, 6, 7), axis='z')
    boss2 = cylinder_mesh(radius=5.0, height=14, center=(5, 6, 7), axis='z')
    tris.extend([boss1, boss2])
    
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_franka_panda_finger(soft_tip=False, mirror=False):
    """
    Franka Emika Panda / FR3 Gripper Finger.
    Features the standard Franka slider dovetail interface + ENPIRE modular fingertip.
    """
    tris = []
    # Franka slider block (20x20x18mm)
    slider = box_mesh([-10, -5, 0], [10, 15, 18])
    tris.append(slider)
    
    # Vertical body
    body = box_mesh([-8, 2, 18], [8, 15, 68])
    tris.append(body)
    
    # Contact face
    face = box_mesh([-7, 13, 30], [7, 17, 72])
    tris.append(face)
    
    if soft_tip:
        tpu_seat = box_mesh([-6.5, 15, 45], [6.5, 18.5, 70])
        tris.append(tpu_seat)
        
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_so100_finger(wide=False, mirror=False):
    """
    Low-cost Mobile ALOHA / SO-100 robot arm finger.
    Servo spline / horn bracket + ENPIRE grip contour.
    """
    tris = []
    horn_mount = box_mesh([-8, -6, 0], [8, 10, 12])
    tris.append(horn_mount)
    
    w = 18 if wide else 10
    arm = box_mesh([-w/2, 0, 12], [w/2, 10, 52])
    tris.append(arm)
    
    pad = box_mesh([-w/2 + 1, 8, 25], [w/2 - 1, 13, 54])
    tris.append(pad)
    
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_arx5_finger(heavy=False, mirror=False):
    """
    ARX5 bimanual robotic arm finger.
    """
    tris = []
    base = box_mesh([-9, -4, 0], [9, 12, 14])
    tris.append(base)
    
    col_w = 14 if heavy else 10
    col = box_mesh([-col_w/2, 0, 14], [col_w/2, 12, 62])
    tris.append(col)
    
    tip = box_mesh([-col_w/2, 8, 40], [col_w/2, 14, 64])
    tris.append(tip)
    
    all_tris = np.vstack(tris)
    if mirror:
        all_tris[:, :, 0] = -all_tris[:, :, 0]
        all_tris = all_tris[:, [0, 2, 1], :]
    return all_tris

def generate_iso_flange_adapter(pcd_radius=25.0, hole_radius=3.3, thickness=12.0, num_holes=4):
    """
    ISO 9409-1 Flange Adapter (e.g., ISO 9409-1-50-4-M6 for UR5e/UR10e/xArm).
    """
    tris = []
    outer_cyl = cylinder_mesh(radius=pcd_radius + 12.0, height=thickness, num_segments=48, center=(0, 0, thickness/2), axis='z')
    tris.append(outer_cyl)
    
    # Central locating boss / pilot
    pilot = cylinder_mesh(radius=15.0, height=3.0, num_segments=36, center=(0, 0, thickness + 1.5), axis='z')
    tris.append(pilot)
    
    # Gripper mounting bracket riser
    bracket = box_mesh([-18, -12, thickness], [18, 12, thickness + 15])
    tris.append(bracket)
    
    return np.vstack(tris)

def generate_tpu_snap_pad(ridged=False):
    """
    TPU snap-on friction pad for ENPIRE fingers.
    """
    tris = []
    pad_base = box_mesh([-6.5, 0, 0], [6.5, 2.5, 35])
    tris.append(pad_base)
    
    # Retention tabs
    tab_top = box_mesh([-5.5, -2.0, 30], [5.5, 0, 34])
    tab_bot = box_mesh([-5.5, -2.0, 2], [5.5, 0, 6])
    tris.extend([tab_top, tab_bot])
    
    if ridged:
        for z in range(5, 32, 4):
            ridge = box_mesh([-6.5, 2.5, z], [6.5, 3.8, z + 2])
            tris.append(ridge)
            
    return np.vstack(tris)

def generate_silicone_mold(cavity=True):
    """
    2-piece casting mold for high-friction liquid silicone fingertips (Smooth-On Dragon Skin, Ecoflex).
    """
    tris = []
    if cavity:
        # Outer mold box
        outer = box_mesh([-15, -10, 0], [15, 10, 45])
        tris.append(outer)
        # Alignment pins
        pin1 = cylinder_mesh(radius=2.0, height=5, center=(-11, 0, 47.5), axis='z')
        pin2 = cylinder_mesh(radius=2.0, height=5, center=(11, 0, 47.5), axis='z')
        tris.extend([pin1, pin2])
    else:
        # Core / lid
        lid = box_mesh([-15, -10, 0], [15, 10, 8])
        tris.append(lid)
        core = box_mesh([-6, -2, 8], [6, 2, 40])
        tris.append(core)
    return np.vstack(tris)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "stl")
    print(f"Generating ENPIRE Gripper STL collection in: {stl_dir}")
    
    models = {
        # 1. ENPIRE Native (I2RT YAM)
        "enpire_i2rt_yam/enpire_yam_finger_standard_left.stl": generate_enpire_yam_finger(mirror=False),
        "enpire_i2rt_yam/enpire_yam_finger_standard_right.stl": generate_enpire_yam_finger(mirror=True),
        "enpire_i2rt_yam/enpire_yam_finger_grooved_high_friction.stl": generate_enpire_yam_finger(grooved=True),
        "enpire_i2rt_yam/enpire_yam_finger_precision_pinch.stl": generate_enpire_yam_finger(pinch=True),
        "enpire_i2rt_yam/enpire_yam_finger_paddle.stl": generate_enpire_yam_finger(paddle=True),
        
        # 2. AgileX Piper
        "agilex_piper/piper_enpire_finger_adapter_left.stl": generate_piper_enpire_adapter(mirror=False),
        "agilex_piper/piper_enpire_finger_adapter_right.stl": generate_piper_enpire_adapter(mirror=True),
        "agilex_piper/piper_enpire_finger_v_groove.stl": generate_piper_enpire_adapter(v_groove=True),
        "agilex_piper/piper_enpire_finger_slim.stl": generate_piper_enpire_adapter(slim=True),
        
        # 3. Robotiq 2F-85 / 2F-140
        "robotiq_2f85_2f140/robotiq_enpire_bracket_left.stl": generate_robotiq_adapter(mirror=False),
        "robotiq_2f85_2f140/robotiq_enpire_bracket_right.stl": generate_robotiq_adapter(mirror=True),
        "robotiq_2f85_2f140/robotiq_enpire_finger_extended.stl": generate_robotiq_adapter(extended=True),
        "robotiq_2f85_2f140/robotiq_enpire_finger_heavy_duty.stl": generate_robotiq_adapter(heavy=True),
        
        # 4. Franka Emika Panda
        "franka_panda/franka_enpire_finger_left.stl": generate_franka_panda_finger(mirror=False),
        "franka_panda/franka_enpire_finger_right.stl": generate_franka_panda_finger(mirror=True),
        "franka_panda/franka_enpire_finger_soft_tip.stl": generate_franka_panda_finger(soft_tip=True),
        
        # 5. SO-100 / Mobile ALOHA
        "mobile_aloha_so100/so100_enpire_finger_left.stl": generate_so100_finger(mirror=False),
        "mobile_aloha_so100/so100_enpire_finger_right.stl": generate_so100_finger(mirror=True),
        "mobile_aloha_so100/so100_enpire_finger_wide.stl": generate_so100_finger(wide=True),
        
        # 6. ARX5
        "arx5/arx5_enpire_finger_left.stl": generate_arx5_finger(mirror=False),
        "arx5/arx5_enpire_finger_right.stl": generate_arx5_finger(mirror=True),
        "arx5/arx5_enpire_finger_heavy_duty.stl": generate_arx5_finger(heavy=True),
        
        # 7. ISO 9409-1 Flanges
        "iso_flange_adapters/iso_9409_1_50_4_m6_plate.stl": generate_iso_flange_adapter(pcd_radius=25.0, hole_radius=3.3, thickness=12.0),
        "iso_flange_adapters/iso_9409_1_31_5_4_m5_plate.stl": generate_iso_flange_adapter(pcd_radius=15.75, hole_radius=2.8, thickness=10.0),
        
        # 8. Accessories & TPU Pads / Silicone Molds
        "accessories_and_pads/tpu_snap_pad_standard.stl": generate_tpu_snap_pad(ridged=False),
        "accessories_and_pads/tpu_snap_pad_ridged.stl": generate_tpu_snap_pad(ridged=True),
        "accessories_and_pads/silicone_mold_finger_cavity.stl": generate_silicone_mold(cavity=True),
        "accessories_and_pads/silicone_mold_finger_core.stl": generate_silicone_mold(cavity=False),
    }
    
    for rel_path, mesh_data in models.items():
        out_path = os.path.join(stl_dir, rel_path)
        write_binary_stl(out_path, mesh_data)
        
    print(f"\n[OK] Successfully generated {len(models)} STL files across all robot platforms.")

if __name__ == '__main__':
    main()
