from solid import *
from solid.utils import *

from parametricBox.Builder import *

from parametricBox.interior.Cube import *
path = "f:\Druk3D\STL\openSCAD\\"

def main():
    # build("Battle Chips_Upgrade Tokens holder", Type.HORIZONTAL_COIN_HOLDER, 26, 100, 25)
    # build("Battle Chips_Energy Tokens holder", Type.HORIZONTAL_COIN_HOLDER, 48, 81, 25)
    # build("Battle Chips_Battlechips Card Deck", Type.HORIZONTAL_CARD_HOLDER, 67.5, 91.5, 66)
    # build("Battle Chips_Spudnet Card Deck", Type.VERTICAL_CARD_HOLDER, 91.5, 14.5, 68)
    # build("Battle Chips_Captain Cards", Type.VERTICAL_CARD_HOLDER, 91.5, 8.5, 68)
    # build("Battle Chips_Power Cards", Type.VERTICAL_CARD_HOLDER, 46, 9, 68)

    # build("Smallworld_Coin holder_10", Type.HORIZONTAL_COIN_HOLDER, Round(23, 2, 8), 29, 23)
    # build("Smallworld_Coin holder_5", Type.HORIZONTAL_COIN_HOLDER, 23, 48, 23)
    # build("Smallworld_Coin holder_5", Type.HORIZONTAL_COIN_HOLDER, Round(23, 2.4, 8), 24, 24)
    #  build("Smallworld_Coin holder_3", Type.HORIZONTAL_COIN_HOLDER, Round(23, 2, 8), 20, 24, 0.0)
    # build("Smallworld_Coin holder_2", Type.HORIZONTAL_COIN_HOLDER, 23, 6, 23)
    # build("Smallworld_Coin holder_1", Type.HORIZONTAL_COIN_HOLDER, Round(23, 2, 8), 39, 24, 0.0)

    # build("Smallworld_Modifiers deck", Type.VERTICAL_CARD_HOLDER, 46, 62, 41)
    # build("Smallworld_behemoths tokens", Type.VERTICAL_CARD_HOLDER, 27.5, 24.5, 27.5)
    # build("Smallworld_tunnel tokens", Type.HORIZONTAL_COIN_HOLDER, Round(24.5, 2, 4), 12, 25, 0.0)
    # build("Smallworld_Mountains deck", Type.VERTICAL_CARD_HOLDER, 50, 20, 41)
    # build("Smallworld_Forts deck", Type.VERTICAL_CARD_HOLDER, 38, 12, 38)
    # build("Smallworld_Camps deck", Type.HORIZONTAL_COIN_HOLDER, Round(40,2,10), 5, 37, 0.0)
    build("Smallworld_Various tiles", Type.VARIOUS_TOKENS_HOLDER, [Cube(31, 6.5, 31),
                                                                   Cube(31,6.5, 31),
                                                                   Cube(27, 8, 27),
                                                                   Cube(27, 4.5, 27),
                                                                   Cube(27, 2.5, 27),
                                                                   Cube(27, 2.5, 27),
                                                                   Cube(27, 2.5, 27),
                                                                   Cube(27, 2.5, 27)], 31, 1.0)

main()
