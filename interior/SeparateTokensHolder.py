from solid import *
from solid.utils import *

from parametrizedBox.helpers.Chamfer import *
from parametrizedBox.helpers.PrinterConstants import *

from parametrizedBox.stored_objects.Round import *

from parametrizedBox.interior.Interior import *

class SeparateTokensHolder(Interior):
    def get_roof(self, depth) -> OpenSCADObject:
        return  chamfer(self)

    def __init__(self, token: Measured, amount: int, depth: float, separator: float = nozzle_diameter):
        height = (token.get_depth() + separator)
        Interior.__init__(self, "Separate Tokens Holder", token.get_width(), height * amount, depth)

        path = forward(token.get_height() / 2)(cube([token.get_width(), token.get_height() / 2, token.get_depth()]))
        high_token = union()(token.scad(), path)
        tokens = forward(height * amount)(
                    rot_z_to_neg_y(
                        union()(
                            [up(height * i)(high_token) for i in range(amount)])))
        self.body = tokens

if __name__ == '__main__':
    obj = SeparateTokensHolder(Round(23,2,16),3,23)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
