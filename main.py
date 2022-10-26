from solid import *
from solid.utils import *

from parametricBox.Builder import *

from parametricBox.interior.Cube import *
path = "f:\Druk3D\STL\openSCAD\\"

def main():
    build("Smallworld_upgrades", Type.VARIOUS_TOKENS_HOLDER, [Pipe(23, 20, 23)], 23)

main()
