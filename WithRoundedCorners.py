from solid import *
from solid.utils import *

from parametricBox.Box import *
from parametricBox.helpers.Fillet import *

class WithRoundedCorners(Box):
    def __init__(self, box: Box):
        Box.__init__(self, box.width, box.height, box.depth)
        self.box = box

    def log(self) -> str:
        return f"{self.box.log()}  {type(self).__name__}"

    def scad(self) -> OpenSCADObject:
        return difference()(self.box.scad(), Fillet(self.box).scad())

if __name__ == '__main__':
    from parametricBox.PlainBox import *
    from parametricBox.WithJoints import *
    from parametricBox.WithHorizontalHole import *

    obj = WithRoundedCorners(WithHorizontalHole(WithJoints(PlainBox(Cube(20, 100, 30), chamfer))))
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
