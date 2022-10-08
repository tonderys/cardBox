from solid import *
from solid.utils import *

from Builder import *

path = "f:\Druk3D\STL\openSCAD\\"

def main():
    build(Type.HORIZONTAL_COIN_HOLDER, 26, 105, 25)
    build(Type.BOWL, 67.5, 91.5, 66)
    build(Type.HORIZONTAL_CARD_HOLDER, 67.5, 91.5, 66)
main()
