from enum import Enum

from parametricBox.helpers.Fillet import *
from parametricBox.helpers.BoxBuilder import *

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
    VARIOUS_TOKENS_HOLDER = 4

def get_filename(name: str, type: Type, *args):
    typename = str(type).split('.')[1].lower()
    return f"{path}{name}_{typename}.scad"

def get_object(type: Type, name, *args):
    filename = get_filename(name, type, args)
    match type:
        case Type.BOWL:
            obj = BoxBuilder(PlainBox(Bowl(*args)), filename).withJoints()
        case Type.HORIZONTAL_CARD_HOLDER:
            obj = BoxBuilder(PlainBox(Cube(*args)), filename).withJoints().withVerticalHoles()
        case Type.VERTICAL_CARD_HOLDER:
            obj = BoxBuilder(PlainBox(Cube(*args)), filename).withJoints().withHorizontalHole()
        case Type.VARIOUS_TOKENS_HOLDER:
            obj = BoxBuilder(PlainBox(VariousTokensHolder(*args)), filename).withJoints().withHorizontalHole()
    return obj

def build(name: str, type: Type, *args):
    get_object(type, name, *args).build()

if __name__ == '__main__':
    build("test", Type.VARIOUS_TOKENS_HOLDER, [Pipe(23,23,23), Cube(23,23,23)], 23)
