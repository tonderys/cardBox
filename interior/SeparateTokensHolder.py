from solid import *
from solid.utils import *

from parametricBox.helpers.Chamfer import *
from parametricBox.helpers.PrinterConstants import *

from parametricBox.interior.Pipe import *

from parametricBox.interior.VariousTokensHolder import *

class SeparateTokensHolder(VariousTokensHolder):
    def __init__(self, token: Measured, amount: int, depth: float, separator: float = nozzle_diameter):
        VariousTokensHolder.__init__(self, [token for _ in range(amount)], depth, separator)

if __name__ == '__main__':
    obj = SeparateTokensHolder(Pipe(23,2,16),3,23)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
