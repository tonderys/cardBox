from solid import *
from solid.utils import *

from EmptyBox import *
from WithJoints import *

class CardHolderWithCover():
    def __init__(self, interior: Cube):
        self.box = WithJoints(EmptyBox(interior)).box
        diameter = min(0.8 * self.box.outer.width, 20)

        roof = self.box.get_roof()

        flaps = union()([intersection()(self.box.scad(), hole) for hole in self._get_holes(diameter - printer_gap)])
        flaps = difference()(flaps, down(self.box.inner.depth + self.box.get_wall_z())(roof))

        self.top = union()(roof, flaps)
        self.bottom = difference()(WithJoints(self.box).scad(), roof, self._get_holes(diameter))

    def _get_holes(self, diameter: float) -> OpenSCADObject:
        hole = forward(self.box.outer.height / 2)(cylinder(h=self.box.outer.height, d=diameter))
        return [hole, right(self.box.outer.width)(hole)]

    def get(self):
        return union()(self.bottom, up(self.box.outer.depth)(rot_z_to_down()(self.top)))
