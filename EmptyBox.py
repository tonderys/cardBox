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

    def _get_chamfer(self) -> OpenSCADObject:
        return polyhedron(points=[[self.get_wall_x(), self.get_wall_y(), self.outer.depth * 0.8],
                                  [self.get_wall_x(), self.outer.height - self.get_wall_y(), self.outer.depth * 0.8],
                                  [self.outer.width - self.get_wall_x(), self.outer.height - self.get_wall_y(), self.outer.depth * 0.8],
                                  [self.outer.width - self.get_wall_x(), self.get_wall_y(), self.outer.depth * 0.8],
                                  [self.get_wall_x() / 2, self.get_wall_y() / 2, self.outer.depth],
                                  [self.get_wall_x() / 2, self.outer.height - (self.get_wall_y() / 2), self.outer.depth],
                                  [self.outer.width - (self.get_wall_x() / 2), self.outer.height - (self.get_wall_y() / 2), self.outer.depth],
                                  [self.outer.width - (self.get_wall_x() / 2), self.get_wall_y() / 2, self.outer.depth]],
                          faces=[[0, 1, 2, 3],
                                 [4, 5, 1, 0],
                                 [5, 6, 2, 1],
                                 [6, 7, 3, 2],
                                 [7, 4, 0, 3],
                                 [7, 6, 5, 4]])

    def _get_chamfered_outer(self) -> OpenSCADObject:
        return difference()(self.outer.scad(), self._get_chamfer())

    def get_roof(self) -> OpenSCADObject:
        roof = up(self.outer.depth - self.get_wall_z())(cube([self.outer.width, self.outer.height, self.get_wall_z()]))
        return difference()(roof, self._get_chamfered_outer())

    def scad(self) -> OpenSCADObject:
        outer = self._get_chamfered_outer()

        inner = translate((self.get_wall_x(),
                           self.get_wall_y(),
                           self.get_wall_z()))(self.inner.scad())

        return difference()(outer, inner)
