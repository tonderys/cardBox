from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *
from MeasuredObject import *

class HorizontalCardHolder():
    def __init__(self, interior: Cube):
        with_joints = WithJoints(EmptyBox(interior))
        self.box = with_joints.box
        diameter = min(0.8 * with_joints.get_width(), finger_diameter)

        self.bottom = difference()(with_joints.scad(), self._get_holes(with_joints, diameter))

    def _get_holes(self, obj: MeasuredObject, diameter: float) -> OpenSCADObject:
        hole = union()(cylinder(d = diameter, h = obj.get_wall_z(), segments = 36),
                                back(diameter/2)(cube([obj.get_wall_x(), diameter, obj.get_depth()])))
        holes = [right(obj.get_width() - obj.get_wall_x())(hole),
                 right(obj.get_wall_x())(rotate([0,0,180])(hole))]
        return [forward(obj.get_height()/2)(hole) for hole in holes]

    def get(self) -> OpenSCADObject:
        return self.bottom
