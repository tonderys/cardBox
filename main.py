from solid import *
from solid.utils import *

from parametricBox.helpers.BoxBuilder import *
from parametricBox.helpers.roof import *

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

main()
