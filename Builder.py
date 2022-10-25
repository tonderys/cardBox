from enum import Enum

from parametricBox.helpers.Fillet import *

from parametricBox.interior.Bowl import *
from parametricBox.interior.Cube import *
from parametricBox.interior.Pipe import *
from parametricBox.interior.SeparateTokensHolder import *
from parametricBox.interior.VariousTokensHolder import *

from parametricBox.PlainBox import *
from parametricBox.WithHorizontalHole import *
from parametricBox.WithJoints import *
from parametricBox.WithRoundedCorners import *
from parametricBox.WithVerticalHoles import *

path = "f:\\Druk3D\\STL\\openSCAD\\"

class Type(Enum):
    BOWL = 1
    HORIZONTAL_CARD_HOLDER = 2
    VERTICAL_CARD_HOLDER = 3
    HORIZONTAL_COIN_HOLDER = 4
    VARIOUS_TOKENS_HOLDER = 5

def get_filename(name: str, type: Type, *args):
    typename = str(type).split('.')[1].lower()
    return f"{path}{name}_{typename}.scad"

def get_object(type: Type, *args):
    match type:
        case Type.BOWL:
            obj = WithJoints(PlainBox(Bowl(*args)))
        case Type.HORIZONTAL_CARD_HOLDER:
            obj = WithVerticalHoles(WithJoints(PlainBox(Cube(*args))))
        case Type.VERTICAL_CARD_HOLDER:
            obj = WithHorizontalHole(WithJoints(PlainBox(Cube(*args))))
        case Type.HORIZONTAL_COIN_HOLDER:
            if isinstance(args[0], Measured):
                obj = WithHorizontalHole(WithJoints(PlainBox(SeparateTokensHolder(*args))))
            else:
                obj = WithHorizontalHole(WithJoints(PlainBox(Pipe(*args))))
        case Type.VARIOUS_TOKENS_HOLDER:
            obj = WithHorizontalHole(WithJoints(PlainBox(VariousTokensHolder(*args))))

    return WithRoundedCorners(obj)

def build(name: str, type: Type, *args):
    obj = get_object(type, *args)
    print(f"{name}\n{type}{args}:\n{obj.log()}\n")
    scad_render_to_file(obj.scad(), get_filename(name, type, *args))

if __name__ == '__main__':
    build("test", Type.HORIZONTAL_CARD_HOLDER, 23, 29, 23)
