from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *
from MeasuredObject import *

class CardHolderWithCover():
    def __init__(self, interior: Cube):
        with_joints = WithJoints(EmptyBox(interior))
        self.box = with_joints.box
        diameter = min(0.8 * with_joints.get_width(), finger_diameter)

        roof = self.box.get_roof()

        flaps = union()([intersection()(self.box.scad(), hole) for hole in self._get_holes(self.box, diameter - printer_gap)])
        flaps = difference()(flaps, down(self.box.inner.depth + self.box.get_wall_z())(roof))

        self.top = union()(roof, flaps)
        self.bottom = difference()(with_joints.scad(), self._get_holes(with_joints, diameter))

    def _get_holes(self, obj: MeasuredObject, diameter: float) -> OpenSCADObject:
        hole = forward(obj.get_height() / 2)(cylinder(d = diameter, h = obj.get_depth(), segments = 36))
        return [hole, right(obj.get_width())(hole)]

    def get(self) -> OpenSCADObject:
        return union()(self.bottom, translate([1.5,1.5,71])(self.top))
