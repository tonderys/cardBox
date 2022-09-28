import solid
from Cube import Cube

class Empty_box():
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
        outer = self.outer.scad()
        wall_x = (outer.width - inner.width) / 2
        wall_y = (outer.width - inner.width) / 2
        wall_z = (outer.width - inner.width)

        inner = solid.translate((wall_x, wall_y, wall_z))(self.inner.scad())

        return solid.difference()(outer, inner)
