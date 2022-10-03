from solid import *
from solid.utils import *

from Cube import *
from PrinterConstants import *
from MeasuredObject import *
from Chamfer import *

class EmptyBox(MeasuredObject):
    def __init__(self, inner: Cube):
        self.chamfered = False
        self._outer = Cube(inner.width + (2 * min_wall_thickness),
                           inner.height + (2 * min_wall_thickness),
                           inner.depth + (2 * min_wall_thickness))
        self.inner = inner
        self.roof =translate([self.get_wall_x(), self.get_wall_y(), inner.depth + self.get_wall_z()])(
                    cube([inner.width, inner.height, self.get_wall_z()]))

    def get_width(self):
        return self._outer.width

    def get_height(self):
        return self._outer.height

    def get_depth(self):
        return self._outer.depth

    def increase_width(self, delta: float):
        self._outer.width += delta

    def increase_height(self, delta: float):
        self._outer.height += delta

    def increase_depth(self, delta: float):
        self._outer.deptht += delta

    def get_wall_x(self) -> float:
        return (self.get_width() - self.inner.width) / 2

    def get_wall_y(self) -> float:
        return (self.get_height() - self.inner.height) / 2

    def get_wall_z(self) -> float:
        return (self.get_depth() - self.inner.depth) / 2

    def chamfer_inside(self) -> OpenSCADObject:
        self.roof = chamfer(self)

    def scad(self) -> OpenSCADObject:
        outer = difference()(self._outer.scad(), self.roof)

        inner = translate((self.get_wall_x(),
                           self.get_wall_y(),
                           self.get_wall_z()))(self.inner.scad())

        return difference()(outer, inner)
