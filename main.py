from solid import *
from solid.utils import *

from VerticalCardHolder import *
from HorizontalCardHolder import *
from CoinHolder import *
path = "f:\Druk3D\STL\openSCAD\\"

def main():
    width = 46
    height = 49
    depth = 68

    holder = union()(left(width * 1.2)(VerticalCardHolder(Cube(width, height, depth)).get()),
                     HorizontalCardHolder(Cube(width, height, depth)).get())
    scad_render_to_file(holder, f"{path}test_{width}x{height}x{depth}mm.scad")

    coin_diameter = 26
    coid_column_height = 36
    amount_of_columns = 3
    coin_holder = CoinHolder(coin_diameter, coid_column_height, amount_of_columns)
    coin_holder = EmptyBox(coin_holder)
    scad_render_to_file(coin_holder.scad(), f"{path}coin_holder_{coin_diameter}x{coid_column_height}mm_x{amount_of_columns}.scad")
main()