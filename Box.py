from parametrizedBox.helpers.Chamfer import *
from parametrizedBox.interior.Interior import *
from parametrizedBox.interior.Cube import *
from parametrizedBox.helpers.PrinterConstants import *

class Box():
    def __init__(self, inner: Interior):
        self.floor_thickness = min_floor_thickness
        self.roof_thickness = min_floor_thickness
        self.x_wall_thickness = min_wall_thickness
        self.y_wall_thickness = min_wall_thickness

        self.inner = inner
    def get_width(self):
        return self.inner.width + (2 * self.x_wall_thickness)

    def get_height(self):
        return self.inner.height + (2 * self.y_wall_thickness)

    def get_depth(self):
        return self.inner.depth + self.roof_thickness + self.floor_thickness

    def increase_width(self, delta: float):
        self.x_wall_thickness += delta

    def increase_height(self, delta: float):
        self.y_wall_thickness += delta

    def thicken_floor(self, delta: float):
        self.floor_thickness += delta

    def chamfer_inside(self) -> OpenSCADObject:
        self.roof_thickness = chamfer(self)

    def scad(self) -> OpenSCADObject:
        outer = cube([self.inner.width + (2 * self.x_wall_thickness),
                      self.inner.height + (2 * self.y_wall_thickness),
                      self.inner.depth + self.floor_thickness + self.roof_thickness])

        inner = translate((self.x_wall_thickness,
                           self.y_wall_thickness,
                           self.floor_thickness))(self.inner.scad())
        roof = translate([self.x_wall_thickness,
                          self.y_wall_thickness,
                          self.roof_thickness + self.floor_thickness])(self.inner.get_roof(self.roof_thickness))

        return difference()(outer, inner, roof)

from parametrizedBox.interior.Cube import *
if __name__ == '__main__':
    obj = Box(Cube(26, 105, 31))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")