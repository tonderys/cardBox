from enum import Enum
from solid import *

from VerticalCardHolder import *
from HorizontalCardHolder import *
from HorizontalCoinHolder import *
from Bowl import *

path = "f:\\Druk3D\\STL\\openSCAD\\"

class Type(Enum):
    BOWL = 1
    HORIZONTAL_CARD_HOLDER = 2
    VERTICAL_CARD_HOLDER = 3
    HORIZONTAL_COIN_HOLDER = 4

def get_filename(type: Type, *args):
    arguments = "x".join(str(arg) for arg in args)
    typename = str(type).split('.')[1].lower()
    return f"{path}{typename}_{arguments}mm.scad"

def get_object(type: Type, *args):
    print(f"{type}, {args}:", end = " ")
    match type:
        case Type.BOWL:
            return WithJoints(EmptyBox(Bowl(*args)))
        case Type.HORIZONTAL_CARD_HOLDER:
            return HorizontalCardHolder(Cube(*args))
        case Type.VERTICAL_CARD_HOLDER:
            return VerticalCardHolder(Cube(*args))
        case Type.HORIZONTAL_COIN_HOLDER:
            return WithJoints(EmptyBox(HorizontalCoinHolder(*args)))

def build(type: Type, *args):
    scad_render_to_file(get_object(type, *args).scad(), get_filename(type, *args))

if __name__ == '__main__':
    print (build(Type.BOWL, 1,1,2,3,5,8))
