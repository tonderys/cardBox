from solid import *
from solid.utils import *

from parametrizedBox.Box import *

from parametrizedBox.helpers.Fillet import *
from parametrizedBox.helpers.PrinterConstants import *

class WithHorizontalHole(Box):
    def __init__(self, box: Box):
        self.box = box

    def _get_diameter(self):
        card_width = self.box.get_width() - (self.box.get_wall_x() * 2)
        return min(0.8 * card_width, finger_diameter)

    def scad(self) -> OpenSCADObject:
        diameter = self._get_diameter()
        hole = rot_z_to_y(cylinder(d=diameter, h=self.box.get_height()))
        hole = union()(hole,
                       left(diameter / 2)(
                           cube([diameter,
                                 self.box.get_height(),
                                 self.box.get_depth() / 2])))
        hole = translate([self.box.get_width() / 2,
                          0,
                          self.box.get_depth() / 2])(hole)

        self.bottom = difference()(self.box.scad(), hole)
        return self.bottom

if __name__ == '__main__':
    from parametrizedBox.PlainBox import *
    from parametrizedBox.WithJoints import *

    obj = WithHorizontalHole(WithJoints(PlainBox(Cube(100, 20, 30))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
