from solid import *
from solid.utils import *

from parametricBox.Box import *

from parametricBox.helpers.PrinterConstants import *

class WithHorizontalHole(Box):
    def __init__(self, box: Box, hole_height: float = 0.0):
        self.box = box
        self.hole_height = hole_height if hole_height else self._get_diameter()
        Box.__init__(self, self.box.width, self.box.height, self.box.depth)

    def _get_diameter(self) -> float:
        card_width = self.box.width - (self.box.get_wall_x() * 2)
        return min(0.8 * card_width, finger_diameter)

    def log(self) -> str:
        return f"{self.box.log()}  {type(self).__name__}"

    def scad(self) -> OpenSCADObject:
        diameter = self._get_diameter()
        hole = rot_z_to_y(cylinder(d=diameter, h=self.box.height))
        hole = union()(hole,
                       left(diameter / 2)(
                           cube([diameter,
                                 self.box.height,
                                 self.box.depth])))
        hole = translate([self.box.width / 2,
                          0.0,
                          self.box.depth + (diameter / 2) - self.hole_height])(hole)

        self.bottom = difference()(self.box.scad(), hole)
        return self.bottom

if __name__ == '__main__':
    from parametricBox.PlainBox import *
    from parametricBox.WithJoints import *

    obj = WithHorizontalHole(WithJoints(PlainBox(Cube(100, 20, 30))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
