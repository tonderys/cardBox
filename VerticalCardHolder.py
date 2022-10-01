from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *

class VerticalCardHolder():
    def __init__(self, interior: Cube):
        self.box = EmptyBox(interior)
        box_with_joints = WithJoints(self.box)

        diameter = min(0.8 * self.box.outer.width, 20)

        hole = union()(sphere(d=diameter, segments=25), cylinder(d=diameter, h=self.box.outer.depth / 2, segments=25))
        hole = translate([self.box.outer.width / 2, 0, self.box.outer.depth / 2])(hole)
        holes = [hole, forward(self.box.outer.height)(hole)]

        self.bottom = difference()(box_with_joints.scad(), holes, self.box.get_roof())

    def get(self) -> OpenSCADObject:
        return self.bottom
