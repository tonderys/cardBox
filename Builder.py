from enum import Enum

from parametrizedBox.helpers.Fillet import *

from parametrizedBox.interior.Bowl import *
from parametrizedBox.interior.Cube import *
from parametrizedBox.interior.Pipe import *
from parametrizedBox.interior.SeparateTokensHolder import *

from parametrizedBox.PlainBox import *
from parametrizedBox.WithHorizontalHole import *
from parametrizedBox.WithJoints import *
from parametrizedBox.WithRoundedCorners import *
from parametrizedBox.WithVerticalHoles import *

path = "f:\\Druk3D\\STL\\openSCAD\\"

class Type(Enum):
    BOWL = 1
    HORIZONTAL_CARD_HOLDER = 2
    VERTICAL_CARD_HOLDER = 3
    HORIZONTAL_COIN_HOLDER = 4

def get_filename(name: str, type: Type, *args):
    arguments = "x".join(str(arg) for arg in args)
    typename = str(type).split('.')[1].lower()
    return f"{path}{name}_{typename}_{arguments}mm.scad"

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
    return WithRoundedCorners(obj)

def build(name: str, type: Type, *args):
    obj = get_object(type, *args)
    print(f"{name}\n{type}{args}:\n{obj.log()}\n")
    scad_render_to_file(obj.scad(), get_filename(name, type, *args))

if __name__ == '__main__':
    build("test", Type.HORIZONTAL_CARD_HOLDER, 23, 29, 23)
