from solid import *
from solid.utils import *

from EmptyBox import EmptyBox
from WithJoints import WithJoints

class Card_holder():
    def __init__(self, width, height, depth):
        self.box = EmptyBox(width, height, depth)
        # hole = forward(height / 2)(cylinder(h=self.box.outer.height, r=radius))
        # self.holes = union()([hole, right(self.box.outer.width)(hole)])

        # roof = (translate((self.box.walls_thickness.x,
        #                    self.box.walls_thickness.y,
        #                    self.box.walls_thickness.z))
        #         (up(depth)(cube([width,height, wall_thickness]))))
        # flaps = union()([intersection()(self.box, hole) for hole in self.holes])
        # flaps = difference()(flaps, down(depth + wall_thickness)(roof))

        box_with_joints = WithJoints(self.box)

        # self.top = union()(roof, flaps)
        # self.bottom = difference()(box_with_joints.scad())#, self.holes)
        self.bottom = box_with_joints.scad()

    # def get_top(self):
    #     return self.top

    def get_bottom(self):
        return self.bottom

def main():
    width = 46
    height = 60
    depth = 46

    holder = Card_holder(width, height, depth).get_bottom()

    # scad_render_to_file(object.get_top(), f"top_{width}x{height}mm.scad")
    scad_render_to_file(holder, f"bottom_{width}x{height}mm.scad")

main()