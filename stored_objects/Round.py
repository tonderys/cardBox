from solid import *
from solid.utils import *

from parametricBox.helpers.Measured import *

class Round(Measured):
    def __init__(self, diameter: float,  depth: float, segments: int):
        Measured.__init__(self, diameter, depth, diameter)
        self.seg = segments

    def __str__(self):
        return f"Round(d={self.get_width()}, depth={self.get_depth()})"

    def scad(self):
        return translate([self.get_width() / 2, self.get_height(), self.get_depth() / 2])(
                 rot_z_to_neg_y(
                    cylinder(d=self.get_width(), h=self.get_height(), segments = self.seg)))

if __name__ == '__main__':
    obj = Round(23, 2, 8)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
