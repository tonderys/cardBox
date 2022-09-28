from solid import *
from solid.utils import *

from Empty_box import Empty_box

def move_to_center_top(delta):
    return translate((delta,
                      delta,
                      delta))

class Card_holder(OpenSCADObject):
    def __init__(self, width, height, depth):
        radius = 10

        self.box = Empty_box(width, height, depth).get()
        hole = forward(height / 2)(cylinder(h=depth + (2 * self.box.walls_thickness.y), r=radius))
        self.holes = [hole, right(width + (2*wall_thickness))(hole)]

        roof = (translate((self.box.walls_thickness.x,
                           self.box.walls_thickness.y,
                           self.box.walls_thickness.z))
                (up(depth)(cube([width,height, wall_thickness]))))
        flaps = union()([intersection()(self.box, hole) for hole in self.holes])
        flaps = difference()(flaps, down(depth + wall_thickness)(roof))

        joint = Joint(depth + (2 * wall_thickness)).get()
        joints = []
        for i in range(1, width + (2 * wall_thickness), 6):
            joints.append(translate([i, height + (2 * wall_thickness), 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, height + (2 * wall_thickness), 6):
            joints.append(translate([width + (2 * wall_thickness), height + (2 * wall_thickness) - i, 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, width + (2 * wall_thickness), 6):
            joints.append(translate([width + (2 * wall_thickness) - i, 0, 0])(joint))
        joint = rotate([0,0,-90])(joint)
        for i in range(1, height + (2 * wall_thickness), 6):
            joints.append(translate([0, i, 0])(joint))

        self.top = union()(roof, flaps)
        self.bottom = union()(self.box, joints)
        self.bottom = difference()(self.bottom, self.holes)

    def get_top(self):
        return self.top

    def get_bottom(self):
        return self.bottom

class Joint:
    def __init__(self, h):
        gap = 0.2
        bottom_width = 2
        delta = 1
        trapeze_height = 1
        self.body = polyhedron(points=[[0,0,0],
                                       [bottom_width - (gap / 2),0,0],
                                       [bottom_width + delta - (gap / 2),trapeze_height,0],
                                       [-delta,trapeze_height,0],
                                       [0,0,h],
                                       [bottom_width - (gap / 2),0,h],
                                       [bottom_width + delta - (gap / 2),trapeze_height,h],
                                       [-delta,trapeze_height,h]],
                               faces =[[0,1,2,3],[4,5,1,0],[5,6,2,1],[6,7,3,2],[7,4,0,3],[7,6,5,4]])
    def get(self):
        return self.body

def main():
    width = 63
    height = 88
    depth = 20

    object = Card_holder(width, height, depth)

    scad_render_to_file(object.get_top(), f"top_{width}x{height}mm.scad")
    scad_render_to_file(object.get_bottom(), f"bottom_{width}x{height}mm.scad")

main()