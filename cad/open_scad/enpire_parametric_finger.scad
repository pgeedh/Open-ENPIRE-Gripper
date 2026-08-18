// ==============================================================================
// ENPIRE Parametric Gripper Finger
// OpenSCAD Source File for NVIDIA GEAR ENPIRE-compatible Gripper Designs
// ==============================================================================
// Description: Fully customizable parametric gripper finger supporting
//              I2RT YAM, AgileX Piper, Robotiq 2F-85/140, Franka Panda, SO-100.
// ==============================================================================

/* [General Dimensions (mm)] */
finger_length       = 70.0;    // Total height of the finger beam
base_width          = 20.0;    // Width at the mounting base
base_depth          = 24.0;    // Depth at the mounting base
base_height         = 15.0;    // Height of the base mounting block
beam_thickness      = 12.0;    // Structural beam thickness
tip_width           = 14.0;    // Width at the contact tip
tip_length          = 35.0;    // Height of the contact pad zone

/* [Mounting Screws & Inserts] */
screw_type          = "M3";    // [M2.5, M3, M4, M5]
screw_diameter      = 3.3;     // Clearance hole diameter (3.3mm for M3, 4.3mm for M4)
screw_spacing       = 12.0;    // Distance between mounting hole centers
counterbore_diam    = 6.5;     // Counterbore diameter for socket head cap screw
counterbore_depth   = 4.0;     // Counterbore depth
heatset_insert      = false;   // Set true to generate heat-set brass insert pockets (e.g. M3x4x5)
insert_diameter     = 4.2;     // Heat-set insert outer diameter

/* [Friction Surface & Textures] */
grip_texture        = "grooved"; // [smooth, grooved, v_notch, tpu_slot, silicone_pocket]
groove_pitch        = 5.0;     // Spacing between friction ribs
groove_depth        = 1.5;     // Rib height / depth
tpu_recess_depth    = 2.0;     // Depth for snap-in TPU pad

/* [Symmetry & Mirroring] */
is_mirrored         = false;   // Generate left (false) or right (true) finger

// ------------------------------------------------------------------------------
// Modules
// ------------------------------------------------------------------------------

module bolt_hole() {
    union() {
        cylinder(h=base_height + 2, r=screw_diameter/2, center=true, $fn=32);
        translate([0, 0, base_height/2 - counterbore_depth])
            cylinder(h=counterbore_depth + 1, r=counterbore_diam/2, $fn=32);
        if (heatset_insert) {
            translate([0, 0, -base_height/2 - 0.1])
                cylinder(h=5.5, r=insert_diameter/2, $fn=32);
        }
    }
}

module finger_body() {
    difference() {
        union() {
            // Mounting Base
            translate([-base_width/2, 0, 0])
                cube([base_width, base_depth, base_height]);
            
            // Structural Beam
            hull() {
                translate([-base_width/2 + 2, 8, base_height - 2])
                    cube([base_width - 4, base_depth - 8, 4]);
                translate([-tip_width/2, base_depth - beam_thickness, finger_length - 5])
                    cube([tip_width, beam_thickness, 5]);
            }
            
            // Tip Head
            translate([-tip_width/2, base_depth - beam_thickness, finger_length - 5])
                cube([tip_width, beam_thickness, 5]);
                
            // Grip texturing
            if (grip_texture == "grooved") {
                for (z = [base_height + 10 : groove_pitch : finger_length - 5]) {
                    translate([-tip_width/2, base_depth, z])
                        cube([tip_width, groove_depth, groove_pitch/2]);
                }
            }
        }
        
        // Mounting Holes
        translate([0, base_depth/2 - screw_spacing/2, base_height/2])
            bolt_hole();
        translate([0, base_depth/2 + screw_spacing/2, base_height/2])
            bolt_hole();
            
        // TPU / Silicone insert recess
        if (grip_texture == "tpu_slot" || grip_texture == "silicone_pocket") {
            translate([-tip_width/2 + 1.5, base_depth - tpu_recess_depth, finger_length - tip_length])
                cube([tip_width - 3, tpu_recess_depth + 1, tip_length - 2]);
        }
        
        // V-notch clamp for cylinders
        if (grip_texture == "v_notch") {
            translate([0, base_depth, finger_length - tip_length/2])
                rotate([0, 45, 0])
                    cube([10, 10, 10], center=true);
        }
    }
}

// ------------------------------------------------------------------------------
// Top-Level Assembly Render
// ------------------------------------------------------------------------------
mirror([is_mirrored ? 1 : 0, 0, 0]) {
    finger_body();
}
