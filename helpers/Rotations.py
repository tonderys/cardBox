from solid import *

from parametricBox.helpers.Measured import *

def move_to_middle(object):
    object.body = translate([-object.width / 2, -object.height / 2, -object.depth / 2])(object.body)

def move_back(object):
    object.body = translate([object.width / 2, object.height / 2, object.depth / 2])(object.body)

def exchange_width_and_height(object):
    object.width, object.height = object.height, object.width

def exchange_depth_and_width(object):
    object.depth, object.width = object.width, object.depth

def exchange_depth_and_height(object):
    object.depth, object.height = object.height, object.depth

angle = 90 #I'll do the math with other angles in step#2

def rot_z(object: Measured):
    move_to_middle(object)
    object.body = rotate(a=angle, v=[0,0,1])(object.body)
    exchange_width_and_height(object)
    move_back(object)
    return object

def rot_y(object: Measured):
    move_to_middle(object)
    object.body = rotate(a=angle, v=[0,1,0])(object.body)
    exchange_depth_and_width(object)
    move_back(object)
    return object

def rot_x(object: Measured):
    move_to_middle(object)
    object.body = rotate(a=angle, v=[1,0,0])(object.body)
    exchange_depth_and_height(object)
    move_back(object)
    return object