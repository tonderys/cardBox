from solid import *
from solid.utils import *

from Builder import *

path = "f:\Druk3D\STL\openSCAD\\"

def main():
    build("Battle Chips_Upgrade Tokens holder", Type.HORIZONTAL_COIN_HOLDER, 26, 105, 25)
    build("Battle Chips_Energy Tokens holder", Type.BOWL, 50, 126, 25)
    build("Battle Chips_Battlechips Card Deck", Type.HORIZONTAL_CARD_HOLDER, 67.5, 91.5, 66)
    build("Battle Chips_Spudnet Card Deck", Type.VERTICAL_CARD_HOLDER, 91, 14.5, 68)
    build("Battle Chips_Captain Cards", Type.VERTICAL_CARD_HOLDER, 91, 14.5, 68)
    build("Battle Chips_Power Cards", Type.VERTICAL_CARD_HOLDER, 46, 9, 68)

main()
