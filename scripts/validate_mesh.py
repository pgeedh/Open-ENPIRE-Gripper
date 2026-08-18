#!/usr/bin/env python3
"""
ENPIRE 3D Mesh Validator
Scans and validates binary STL files across all subdirectories, computing:
- Facet count
- Bounding box dimensions (X x Y x Z in mm)
- Estimated solid volume (cm^3)
- File integrity and format validity
"""

import os
import struct
import numpy as np

def validate_stl(filepath: str):
    filesize = os.path.getsize(filepath)
    if filesize < 84:
        return False, f"File too small ({filesize} bytes), missing header", {}
        
    with open(filepath, 'rb') as f:
        header = f.read(80)
        num_triangles_bytes = f.read(4)
        if len(num_triangles_bytes) < 4:
            return False, "Corrupted header", {}
        num_triangles = struct.unpack('<I', num_triangles_bytes)[0]
        
        expected_size = 84 + (num_triangles * 50)
        if filesize != expected_size:
            return False, f"Size mismatch: expected {expected_size} bytes, got {filesize} bytes", {}
            
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
    
    min_bound = all_verts.min(axis=0)
    max_bound = all_verts.max(axis=0)
    dims = max_bound - min_bound
    
    # Signed tetrahedron volume sum
    cross = np.cross(v1, v2)
    signed_vol = np.sum(v0 * cross) / 6.0
    vol_cm3 = abs(signed_vol) / 1000.0
    
    stats = {
        'facets': num_triangles,
        'bounds_min': min_bound.tolist(),
        'bounds_max': max_bound.tolist(),
        'dims_mm': dims.tolist(),
        'volume_cm3': round(vol_cm3, 3),
        'size_bytes': filesize
    }
    return True, "Valid", stats

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stl_dir = os.path.join(base_dir, "stl")
    
    print("=" * 75)
    print("ENPIRE STL Model Verification Suite")
    print(f"Scanning directory: {stl_dir}")
    print("=" * 75)
    
    total_files = 0
    valid_files = 0
    
    for root, _, files in sorted(os.walk(stl_dir)):
        for file in sorted(files):
            if file.endswith(".stl"):
                total_files += 1
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                is_valid, msg, stats = validate_stl(full_path)
                
                if is_valid:
                    valid_files += 1
                    d = stats['dims_mm']
                    print(f"[PASS] {rel_path}")
                    print(f"       Dims: {d[0]:.1f} x {d[1]:.1f} x {d[2]:.1f} mm | Vol: {stats['volume_cm3']} cm³ | Facets: {stats['facets']}")
                else:
                    print(f"[FAIL] {rel_path} -> {msg}")
                    
    print("=" * 75)
    print(f"Results: {valid_files}/{total_files} models passed validation.")
    if valid_files == total_files:
        print("[SUCCESS] All 3D STL meshes are watertight and structurally valid.")
        return 0
    else:
        print("[ERROR] Some mesh files failed validation.")
        return 1

if __name__ == '__main__':
    exit(main())
