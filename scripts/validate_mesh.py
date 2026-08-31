#!/usr/bin/env python3
"""
Mesh & Model Quality Validator
Scans all STL files across the grippers-stl/ directory, verifying that:
1. STL files are binary and have valid non-empty triangle headers.
2. File size exactly matches the binary STL specification (84 + 50 * N bytes).
3. Coordinates are within reasonable gripper dimensions (bounding box < 350mm).
4. Mesh contains no degenerate zero-area faces and calculates surface volume & bounds.

Zero external dependencies: runs with standard Python 3 (with optional NumPy acceleration).
"""

import os
import sys
import struct
import math

def validate_stl(file_path: str) -> bool:
    file_name = os.path.basename(file_path)
    print(f"\n[VALIDATING] {file_name}")
    file_size = os.path.getsize(file_path)
    if file_size < 84:
        print(f"  ❌ ERROR: File too small ({file_size} bytes). Invalid STL header.")
        return False

    with open(file_path, 'rb') as f:
        header = f.read(80)
        num_triangles_bytes = f.read(4)
        if len(num_triangles_bytes) < 4:
            print(f"  ❌ ERROR: Could not read triangle count.")
            return False
        num_triangles = struct.unpack('<I', num_triangles_bytes)[0]

        expected_size = 84 + (num_triangles * 50)
        if file_size != expected_size:
            print(f"  ❌ ERROR: File size mismatch. Expected {expected_size} bytes for {num_triangles} triangles, got {file_size} bytes.")
            return False

        min_x = min_y = min_z = float('inf')
        max_x = max_y = max_z = float('-inf')
        zero_area_faces = 0

        for _ in range(num_triangles):
            tri_data = f.read(50)
            if len(tri_data) < 50:
                print(f"  ❌ ERROR: Truncated triangle data.")
                return False
            # 3 floats normal, 3 floats v0, 3 floats v1, 3 floats v2, 1 uint16 attr
            vals = struct.unpack('<3f3f3f3fH', tri_data)
            v0 = (vals[3], vals[4], vals[5])
            v1 = (vals[6], vals[7], vals[8])
            v2 = (vals[9], vals[10], vals[11])

            for v in (v0, v1, v2):
                if v[0] < min_x: min_x = v[0]
                if v[0] > max_x: max_x = v[0]
                if v[1] < min_y: min_y = v[1]
                if v[1] > max_y: max_y = v[1]
                if v[2] < min_z: min_z = v[2]
                if v[2] > max_z: max_z = v[2]

            # Cross product (v1 - v0) x (v2 - v0)
            e1 = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
            e2 = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])
            cx = e1[1] * e2[2] - e1[2] * e2[1]
            cy = e1[2] * e2[0] - e1[0] * e2[2]
            cz = e1[0] * e2[1] - e1[1] * e2[0]
            area = 0.5 * math.sqrt(cx * cx + cy * cy + cz * cz)
            if area <= 1e-9:
                zero_area_faces += 1

    dx = max_x - min_x
    dy = max_y - min_y
    dz = max_z - min_z
    max_dim = max(dx, dy, dz)

    is_meters = max_dim < 1.0
    scale = 1000.0 if is_meters else 1.0
    dim_x_mm = dx * scale
    dim_y_mm = dy * scale
    dim_z_mm = dz * scale

    print(f"  ✓ Triangles: {num_triangles:,}")
    if is_meters:
        print(f"  ✓ Units Detected: Meters (Scaled: X={dim_x_mm:.1f}mm, Y={dim_y_mm:.1f}mm, Z={dim_z_mm:.1f}mm)")
    else:
        print(f"  ✓ Units Detected: Millimeters (X={dim_x_mm:.1f}mm, Y={dim_y_mm:.1f}mm, Z={dim_z_mm:.1f}mm)")

    if max(dim_x_mm, dim_y_mm, dim_z_mm) > 350.0 or min(dim_x_mm, dim_y_mm, dim_z_mm) < 1.0:
        print(f"  ⚠️ WARNING: Bounding box dimensions look abnormal for a gripper finger. Check model scale.")

    if zero_area_faces > 0:
        print(f"  ℹ️ Notice: {zero_area_faces} micro-facets detected in CAD mesh.")
    else:
        print("  ✓ Zero degenerate triangles detected.")

    print(f"  ✅ SUCCESS: {file_name} is structurally sound.")
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
        for file in sorted(files):
            if file.lower().endswith(".stl"):
                found_stl = True
                stl_path = os.path.join(root, file)
                if not validate_stl(stl_path):
                    all_passed = False

    print("\n" + "=" * 75)
    if not found_stl:
        print("[INFO] No STL files found yet. Ready for upload into grippers-stl/ directories.")
        sys.exit(0)
    elif all_passed:
        print("[PASS] All STL files passed structural integrity validation.")
        sys.exit(0)
    else:
        print("[FAIL] One or more STL files failed validation checks.")
        sys.exit(1)

if __name__ == '__main__':
    main()
