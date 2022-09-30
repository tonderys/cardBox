import solid
from Cube import Cube


class EmptyBox:

    def __init__(self, width, height, depth):
        min_walls_thickness = 1
        self.outer = Cube(width + (2 * min_walls_thickness),
                          height + (2 * min_walls_thickness),
                          depth + (2 * min_walls_thickness))
        self.inner = Cube(width, height, depth + min_walls_thickness)

    def increase_width(self, delta):
        self.outer.width += delta

    def increase_height(self, delta):
        self.outer.height += delta

    def increase_depth(self, delta):
        self.outer.depth += delta
        self.inner.depth += delta / 2

    def scad(self):
        wall_x = (self.outer.width - self.inner.width) / 2
        wall_y = (self.outer.height - self.inner.height) / 2
        wall_z = (self.outer.depth - self.inner.depth)

        outer = self.outer.scad()
        inner = solid.translate((wall_x, wall_y, wall_z))(self.inner.scad())

        return solid.difference()(outer, inner)
