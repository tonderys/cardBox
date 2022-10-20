from solid import *
from solid.utils import *

from parametricBox.helpers.Chamfer import *
from parametricBox.helpers.PrinterConstants import *

from parametricBox.stored_objects.Round import *
from parametricBox.stored_objects.Rectangle import *

from parametricBox.interior.Interior import *

def get_max_width(tokens):
    return max([token.get_width() for token in tokens])

def get_height(tokens, separator):
    return sum([token.get_depth() for token in tokens]) + (len(tokens) - 1) * separator

class VariousTokensHolder(Interior):
    def get_roof(self, depth) -> OpenSCADObject:
        return  chamfer(self)

    def __init__(self, tokens, depth: float, separator: float = nozzle_diameter):
        max_width = get_max_width(tokens)
        Interior.__init__(self, "Various Tokens Holder", max_width, get_height(tokens, separator), depth)
        self.body = union()
        actual_depth = 0.0
        for token in tokens:
            path = forward(token.get_height() / 2)(cube([token.get_width(), token.get_height() / 2, token.get_depth()]))
            high_token = up(depth - token.get_height())(
                            right((max_width - token.get_width()) / 2)(
                                (token.scad(), path)))

            token_depth = token.get_depth()
            self.body = union()(self.body, forward(actual_depth + token_depth)(rot_z_to_neg_y(high_token)))
            actual_depth += token_depth + separator

if __name__ == '__main__':
    obj = VariousTokensHolder([Round(23,2,16), Rectangle(23,23,2), Round(50,2,8), Round(23,2,16), Round(50,2,8)],23)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
