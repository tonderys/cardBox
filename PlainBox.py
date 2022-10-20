from parametricBox.Box import *

from parametricBox.helpers.Chamfer import *
from parametricBox.helpers.PrinterConstants import *

from parametricBox.interior.Interior import *
from parametricBox.interior.Cube import *

class PlainBox(Box):
    def __init__(self, inner: Interior):
        self.floor_thickness = min_floor_thickness
        self.roof_thickness = min_floor_thickness
        self.x_wall_thickness = min_wall_thickness
        self.y_wall_thickness = min_wall_thickness
        self.box = inner

    def get_width(self) -> float:
        return self.box.get_width() + (2 * self.x_wall_thickness)

    def get_height(self) -> float:
        return self.box.get_height() + (2 * self.y_wall_thickness)

    def get_depth(self) -> float:
        return self.box.get_depth() + self.roof_thickness + self.floor_thickness

    def get_wall_x(self) -> float:
        return self.x_wall_thickness

    def get_wall_y(self) -> float:
        return self.y_wall_thickness

    def get_floor(self) -> float:
        return self.floor_thickness

    def scad(self) -> OpenSCADObject:
        outer = cube([self.get_width(),
                      self.get_height(),
                      self.get_depth()])

        inner = translate((self.x_wall_thickness,
                           self.y_wall_thickness,
                           self.floor_thickness))(self.box.scad())
        roof = translate([self.x_wall_thickness,
                          self.y_wall_thickness,
                          self.roof_thickness + self.floor_thickness])(self.box.get_roof(self.roof_thickness))

        return difference()(outer, inner, roof)

if __name__ == '__main__':
    from parametricBox.interior.Cube import *
    obj = PlainBox(Cube(26, 105, 31))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")