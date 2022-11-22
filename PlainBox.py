from solid import *
from solid.utils import *

from parametricBox.Box import *

from parametricBox.helpers.Roof import *
from parametricBox.helpers.PrinterConstants import *

from parametricBox.interior.Interior import *

class PlainBox(Box):
    def __init__(self, inner: Interior, get_roof = regular):
        self.floor_thickness = min_floor_thickness
        self.roof_thickness = min_floor_thickness
        self.x_wall_thickness = min_wall_thickness
        self.y_wall_thickness = min_wall_thickness
        self.box = inner
        self.get_roof = get_roof
        Box.__init__(self, self._get_width(), self._get_height(), self._get_depth())

    def _get_width(self) -> float:
        return self.box.width + (2 * self.x_wall_thickness)

    def _get_height(self) -> float:
        return self.box.height + (2 * self.y_wall_thickness)

    def _get_depth(self) -> float:
        return self.box.depth + self.roof_thickness + self.floor_thickness

    def get_wall_x(self) -> float:
        return self.x_wall_thickness

    def get_wall_y(self) -> float:
        return self.y_wall_thickness

    def get_floor(self) -> float:
        return self.floor_thickness

    def scad(self) -> OpenSCADObject:
        outer = cube([self.width,
                      self.height,
                      self.depth])

        inner = translate((self.x_wall_thickness,
                           self.y_wall_thickness,
                           self.floor_thickness))(self.box.scad())
        roof = translate([self.x_wall_thickness,
                          self.y_wall_thickness,
                          self.roof_thickness + self.floor_thickness])(self.get_roof(self.box, min_wall_thickness))

        return difference()(outer, inner, roof)

from parametricBox.interior.Cube import *
if __name__ == '__main__':
    from parametricBox.interior.Cube import *
    obj = PlainBox(Cube(26, 105, 31), regular)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")