from solid import *
from solid.utils import *

from parametricBox.helpers.PrinterConstants import *

from parametricBox.interior.Interior import *

def get_max_width(tokens):
    return max([token.width for token in tokens])

def get_max_depth(tokens):
    return max([token.depth for token in tokens])

def get_sum_height(tokens, separator):
    return sum([token.height for token in tokens]) + (len(tokens) - 1) * separator

class VariousTokensHolder(Interior):
    def __init__(self, tokens, depth: float, separator: float = nozzle_diameter):
        max_width = get_max_width(tokens)
        Interior.__init__(self, "Various Tokens Holder", max_width, get_sum_height(tokens, separator), depth)
        self.body = union()
        actual_depth = 0.0
        for token in tokens:
            token_depth = token.height
            token = translate([(max_width - token.width) / 2, 0 , depth - token.depth])(token.scad())

            self.body = union()(self.body, forward(actual_depth)(token))
            actual_depth += token_depth + separator

if __name__ == '__main__':
    from parametricBox.interior.Bowl import *
    from parametricBox.interior.Pipe import *
    from parametricBox.interior.Cube import *
    from parametricBox.interior.Column import *

    obj = VariousTokensHolder([Cube(22,22,22),
                               Bowl(27, 27, 55),
                               Pipe(27, 27, 23),
                               Column(10,10)],24)
    scad_render_to_file(obj.scad(), f"f:\\Druk3D\\STL\\openSCAD\\test.scad")
