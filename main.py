from solid import *
from solid.utils import *

from VerticalCardHolder import *
from CardHolderWithCover import *

path = "f:\Druk3D\STL\openSCAD\\"

def main():
    width = 63.5
    height = 88
    depth = 68

    holder = CardHolderWithCover(Cube(width, height, depth))

    scad_render_to_file(holder.get(), f"{path}{width}x{height}x{depth}mm.scad")

main()