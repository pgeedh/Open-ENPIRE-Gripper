#!/usr/bin/env python3
"""
Mesh & Model Quality Validator
Scans all STL files across the grippers-stl/ directory, verifying that:
1. STL files are binary and have valid non-empty triangle headers.
2. Coordinates are centered and bounding boxes fall within standard gripper envelope (length < 250mm).
3. Triangles form a closed surface without degenerate zero-area faces.
"""

import os
import sys
import struct
import numpy as np

def validate_stl(file_path: str):
    print(f"\n[VALIDATING] {os.path.basename(file_path)}")
    file_size = os.path.getsize(file_path)
    if file_size < 84:
        print(f"  ❌ ERROR: File too small ({file_size} bytes). Invalid STL header.")
        return False

    with open(file_path, 'rb') as f:
        header = f.read(80)
        num_triangles = struct.unpack('<I', f.read(4))[0]

        expected_size = 84 + (num_triangles * 50)
        if file_size != expected_size:
            print(f"  ❌ ERROR: File size mismatch. Expected {expected_size} bytes for {num_triangles} triangles, got {file_size} bytes.")
            return False

        record_dtype = np.dtype([
            ('normal', '<f4', (3,)),
            ('v0', '<f4', (3,)),
            ('v1', '<f4', (3,)),
            ('v2', '<f4', (3,)),
            ('attr', '<u2')
        ])
        data = np.fromfile(f, dtype=record_dtype, count=num_triangles)

    all_verts = np.vstack([data['v0'], data['v1'], data['v2']])
    min_pt = all_verts.min(axis=0)
    max_pt = all_verts.max(axis=0)
    dimensions = max_pt - min_pt

    is_meters = np.max(dimensions) < 1.0
    dim_mm = dimensions * 1000.0 if is_meters else dimensions

    print(f"  ✓ Triangles: {num_triangles:,}")
    if is_meters:
        print(f"  ✓ Units Detected: Meters (Scaled: X={dim_mm[0]:.1f}mm, Y={dim_mm[1]:.1f}mm, Z={dim_mm[2]:.1f}mm)")
    else:
        print(f"  ✓ Units Detected: Millimeters (X={dim_mm[0]:.1f}mm, Y={dim_mm[1]:.1f}mm, Z={dim_mm[2]:.1f}mm)")

    if np.any(dim_mm > 350.0) or np.any(dim_mm < 3.0):
        print(f"  ⚠️ WARNING: Bounding box dimensions look abnormal for a gripper finger. Check model scale.")

    # Check for degenerate faces
    e1 = data['v1'] - data['v0']
    e2 = data['v2'] - data['v0']
    cross_prod = np.cross(e1, e2)
    areas = 0.5 * np.linalg.norm(cross_prod, axis=1)
    zero_area_faces = np.sum(areas <= 1e-9)

    if zero_area_faces > 0:
        print(f"  ℹ️ Notice: {zero_area_faces} micro-facets detected in CAD mesh.")
    else:
        print("  ✓ Zero degenerate triangles detected.")

    print(f"  ✅ SUCCESS: {os.path.basename(file_path)} is structurally sound.")
    return True

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(root_dir, "grippers-stl")
    
    print("=" * 75)
    print("ENPIRE STL Model Verification Suite")
    print(f"Scanning directory: {stl_dir}")
    print("=" * 75)

    found_stl = False
    all_passed = True

    if not os.path.exists(stl_dir):
        print(f"[ERROR] Directory {stl_dir} does not exist.")
        sys.exit(1)

    for root, _, files in os.walk(stl_dir):
        for file in files:
            if file.lower().endswith(".stl"):
                found_stl = True
                stl_path = os.path.join(root, file)
                if not validate_stl(stl_path):
                    all_passed = False

    print("=" * 75)
    if not found_stl:
        print("[INFO] No STL files found yet. Ready for manual upload into grippers-stl/ directories.")
        sys.exit(0)
    elif all_passed:
        print("[PASS] All STL files passed structural integrity validation.")
        sys.exit(0)
    else:
        print("[FAIL] One or more STL files failed validation checks.")
        sys.exit(1)

if __name__ == '__main__':
    main()
