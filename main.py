from solid import *
from solid.utils import *

from parametricBox.helpers.BoxBuilder import *
from parametricBox.helpers.Roof import *
from parametricBox.helpers.Rotations import *

from parametricBox.interior.Bowl import *
from parametricBox.interior.Column import *
from parametricBox.interior.Cube import *
from parametricBox.interior.Pipe import *
from parametricBox.interior.SeparateTokensHolder import *
from parametricBox.interior.VariousTokensHolder import *

from parametricBox.PlainBox import *
from parametricBox.WithHorizontalHole import *
from parametricBox.WithJoints import *
from parametricBox.WithRoundedCorners import *
from parametricBox.WithVerticalHoles import *

path = "f:\Druk3D\STL\openSCAD\\"

def get_filename(name: str):
    return f"{path}{name}.scad"

def main():
    filename, inner = get_filename("Keep the heroes out resources"), SeparateTokensHolder(Bowl(30,22,25),5,25, 2.0)
    BoxBuilder(inner, filename).withJoints().build()

    filename, inner = get_filename("Keep the heroes out chests"), Cube(30, 36, 25)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Keep the heroes out round tokens"), VariousTokensHolder([Pipe(26,22,25), Pipe(26,12,25)], 25, 3)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Keep the heroes out wound"), Bowl(48, 39, 25)
    BoxBuilder(inner, filename).withJoints().build()

    filename, inner = get_filename("Battle Chips deck"), Cube(66.5,91, 69)
    BoxBuilder(inner, filename).withJoints().withVerticalHoles().build()

    filename, inner = get_filename("bits"), SeparateTokensHolder(rot_z(SeparateTokensHolder(Column(8.2, 14, 6), 10, 14)), 3, 14, 2.0)
    BoxBuilder(inner, filename).build()

    filename, inner = get_filename("SD card holder"), VariousTokensHolder([rot_z(SeparateTokensHolder(Cube(25, 2.5, 25),35, 25)),
                                                                           Cube(76, 11, 15),
                                                                           Cube(99, 18, 25)], 25, 2.0)
    BoxBuilder(inner, filename).withJoints().build()

    filename, inner = get_filename("pen holder"), SeparateTokensHolder(Column(15, 45), 5, 45, 2.0)
    BoxBuilder(inner, filename).withJoints().build()

    elder_sign_box_height = 45
    small_card_height = 66.5

    filename, inner = get_filename("Elders sign clubs"), Cube(small_card_height, 6, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign skills"), Cube(small_card_height, 8, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign allies"), Cube(small_card_height, 8.5, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign common items"), Cube(small_card_height, 10.5, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign unique items"), Cube(small_card_height, 10.5, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign spells"), Cube(small_card_height, 11, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign events"), Cube(small_card_height, 14.5, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign midnights"), Cube(small_card_height, 17.5, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withHorizontalHole().build()


    filename, inner = get_filename("Elders sign adventures"), Cube(73, 124, elder_sign_box_height)
    BoxBuilder(inner, filename).withRoof(chamfer).withJoints().withVerticalHoles().build()

    filename, inner = get_filename("Elders sign dies"), VariousTokensHolder([Cube(16, 16, 48), Cube(16, 16, 48), Cube(16, 16, 32)], elder_sign_box_height, 2)
    BoxBuilder(inner, filename).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign monsters"), SeparateTokensHolder(Cube(56, 19, elder_sign_box_height), 2, elder_sign_box_height, 2)
    BoxBuilder(inner, filename).withJoints().withHorizontalHole().build()

    filename, inner = get_filename("Elders sign clock monsters"), Bowl(116,116, elder_sign_box_height)
    BoxBuilder(inner, filename).withJoints().withHorizontalHole(5.0).build()

main()
