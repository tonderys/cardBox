from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *

class VerticalCardHolder():
    def __init__(self, interior: Cube):
        self.box = EmptyBox(interior)
        box_with_joints = WithJoints(self.box)
        self.box.chamfer_inside()

        diameter = min(0.8 * self.box.get_width(), finger_diameter)

        hole = rot_z_to_y(cylinder(d=diameter, h=box_with_joints.get_height()))
        hole = union()(hole, left(diameter / 2)(cube([diameter, box_with_joints.get_height(), box_with_joints.get_depth() / 2])))
        hole = translate([box_with_joints.get_width() / 2,
                          0,
                          box_with_joints.get_depth() / 2])(hole)

        self.bottom = difference()(box_with_joints.scad(), hole)

    def get(self) -> OpenSCADObject:
        return self.bottom
