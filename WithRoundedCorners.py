from solid import *
from solid.utils import *

from parametrizedBox.Box import *
from parametrizedBox.helpers.Fillet import *

class WithRoundedCorners(Box):
    def __init__(self, box: Box):
        self.box = box

    def scad(self) -> OpenSCADObject:
        return difference()(self.box.scad(), Fillet(self.box).scad())

if __name__ == '__main__':
    from parametrizedBox.PlainBox import *
    from parametrizedBox.WithJoints import *

    obj = WithRoundedCorners(WithJoints(PlainBox(Cube(100, 20, 30))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
