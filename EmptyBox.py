from solid import *
from solid.utils import *

from Cube import *
from PrinterConstants import *

class EmptyBox:
    def __init__(self, inner: Cube):
        self.outer = Cube(inner.width + (2 * min_wall_thickness),
                          inner.height + (2 * min_wall_thickness),
                          inner.depth + (2 * min_wall_thickness))
        self.inner = inner

    def increase_width(self, delta: float):
        self.outer.width += delta

    def increase_height(self, delta: float):
        self.outer.height += delta

    def increase_depth(self, delta: float):
        self.outer.depth += delta

    def get_wall_x(self) -> float:
        return (self.outer.width - self.inner.width) / 2

    def get_wall_y(self) -> float:
        return (self.outer.height - self.inner.height) / 2

    def get_wall_z(self) -> float:
        return (self.outer.depth - self.inner.depth) / 2

    def get_roof(self) -> OpenSCADObject:
        roof = up(self.inner.depth)(cube([self.inner.width,self.inner.height, self.get_wall_z()]))
        return translate([self.get_wall_x(),
                          self.get_wall_y(),
                          self.get_wall_z()])(roof)

    def scad(self) -> OpenSCADObject:
        outer = self.outer.scad()
        inner = translate((self.get_wall_x(),
                           self.get_wall_y(),
                           self.get_wall_z()))(self.inner.scad())

        return difference()(outer, inner)
