// ==============================================================================
// ENPIRE Universal Robot Flange & Gripper Adapter
// OpenSCAD Source File for ISO 9409-1 Flange & Custom Robot Arm Interfaces
// ==============================================================================

/* [Flange Configuration] */
flange_standard     = "ISO_50_4_M6"; // [ISO_50_4_M6, ISO_31_5_4_M5, Custom]
flange_thickness    = 12.0;          // Base plate thickness (mm)
pilot_diameter      = 31.5;          // Central locating boss / pilot diameter (mm)
pilot_height        = 3.0;           // Locating boss protrusion (mm)
pcd_diameter        = 50.0;          // Pitch Circle Diameter (PCD) for mounting bolts
bolt_hole_diam      = 6.5;           // Bolt hole diameter (6.5mm for M6, 5.5mm for M5)
num_bolts           = 4;             // Number of mounting holes (standard 4 or 6)

/* [Gripper Interface Bracket] */
bracket_height      = 18.0;          // Height of the gripper mounting uprights
bracket_spacing     = 24.0;          // Distance between upright brackets
bracket_screw_diam  = 3.3;           // M3 mounting holes for ENPIRE fingers

// ------------------------------------------------------------------------------
// Geometry
// ------------------------------------------------------------------------------

module flange_base() {
    difference() {
        union() {
            cylinder(h=flange_thickness, r=(pcd_diameter/2) + 12, $fn=64);
            translate([0, 0, flange_thickness])
                cylinder(h=pilot_height, r=pilot_diameter/2, $fn=64);
                
            // Upright mounting brackets for gripper fingers
            translate([-bracket_spacing/2 - 4, -12, flange_thickness])
                cube([8, 24, bracket_height]);
            translate([bracket_spacing/2 - 4, -12, flange_thickness])
                cube([8, 24, bracket_height]);
        }
        
        // Center cable / pneumatic passthrough
        cylinder(h=flange_thickness + pilot_height + 2, r=8.0, center=true, $fn=32);
        
        // Circular bolt hole pattern
        for (i = [0 : num_bolts - 1]) {
            angle = i * (360 / num_bolts);
            rotate([0, 0, angle])
                translate([pcd_diameter/2, 0, -1])
                    cylinder(h=flange_thickness + 2, r=bolt_hole_diam/2, $fn=32);
        }
        
        // Upright mounting screw holes
        translate([-bracket_spacing/2, 0, flange_thickness + bracket_height/2])
            rotate([0, 90, 0])
                cylinder(h=12, r=bracket_screw_diam/2, center=true, $fn=32);
        translate([bracket_spacing/2, 0, flange_thickness + bracket_height/2])
            rotate([0, 90, 0])
                cylinder(h=12, r=bracket_screw_diam/2, center=true, $fn=32);
    }
}

flange_base();
