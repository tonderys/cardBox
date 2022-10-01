import solid
from Cube import Cube
from PrinterConstants import *

class EmptyBox:

    def __init__(self, width, height, depth):
        self.outer = Cube(width + (2 * min_wall_thickness),
                          height + (2 * min_wall_thickness),
                          depth + (2 * min_wall_thickness))
        self.inner = Cube(width, height, depth + min_wall_thickness)

    def increase_width(self, delta):
        self.outer.width += delta

    def increase_height(self, delta):
        self.outer.height += delta

    def increase_depth(self, delta):
        self.outer.depth += delta
        self.inner.depth += delta / 2

    def get_wall_x(self):
        return (self.outer.width - self.inner.width) / 2

    def get_wall_y(self):
        return (self.outer.height - self.inner.height) / 2

    def get_wall_z(self):
        return (self.outer.depth - self.inner.depth)

    def scad(self):
        outer = self.outer.scad()
        inner = solid.translate((self.get_wall_x(),
                                 self.get_wall_y(),
                                 self.get_wall_z()))(self.inner.scad())

        return solid.difference()(outer, inner)
