import unittest

from parametricBox.Builder import *

class Builder_tests(unittest.TestCase):
    def test_get_filename_with_no_args(self):
        self.assertEqual(get_filename("a", Type.BOWL),
                         "f:\\Druk3D\\STL\\openSCAD\\a_bowl_mm.scad")
        self.assertEqual(get_filename("a", Type.HORIZONTAL_CARD_HOLDER),
                         "f:\\Druk3D\\STL\\openSCAD\\a_horizontal_card_holder_mm.scad")
        self.assertEqual(get_filename("a", Type.VERTICAL_CARD_HOLDER),
                         "f:\\Druk3D\\STL\\openSCAD\\a_vertical_card_holder_mm.scad")
        self.assertEqual(get_filename("a", Type.HORIZONTAL_COIN_HOLDER),
                         "f:\\Druk3D\\STL\\openSCAD\\a_horizontal_coin_holder_mm.scad")

    def test_get_filename_with_int_args(self):
        self.assertEqual(get_filename("object: a",Type.BOWL, 1),
                         "f:\\Druk3D\\STL\\openSCAD\\object: a_bowl_1mm.scad")
        self.assertEqual(get_filename("object: a",Type.BOWL, 1, 2),
                         "f:\\Druk3D\\STL\\openSCAD\\object: a_bowl_1x2mm.scad")
        self.assertEqual(get_filename("object: a",Type.BOWL, 21, 34, 55, 89, 144),
                         "f:\\Druk3D\\STL\\openSCAD\\object: a_bowl_21x34x55x89x144mm.scad")

    def test_get_filename_with_various_args(self):
        self.assertEqual(get_filename("some bowl", Type.BOWL, 1.0),
                         "f:\\Druk3D\\STL\\openSCAD\\some bowl_bowl_1.0mm.scad")
        self.assertEqual(get_filename("some bowl", Type.BOWL, '1,5', 2, 3.4),
                         "f:\\Druk3D\\STL\\openSCAD\\some bowl_bowl_1,5x2x3.4mm.scad")

    def test_get_object_raises_TypeError_for_bowl_with_wrong_args(self):
        self.assertRaises(TypeError, get_object, Type.BOWL)
        self.assertRaises(TypeError, get_object, Type.BOWL, 1)
        self.assertRaises(TypeError, get_object, Type.BOWL, 1, 2)
        self.assertRaises(TypeError, get_object, Type.BOWL, "a", 'b', 'c')

    def test_get_object_raises_TypeError_for_horizontal_card_holder_with_wrong_args(self):
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_CARD_HOLDER)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_CARD_HOLDER, 1.1)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_CARD_HOLDER, 2.3, 5.8)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_CARD_HOLDER, "13.21", "34.55", "89.144")

    def test_get_object_raises_TypeError_for_vartival_card_holder_with_wrong_args(self):
        self.assertRaises(TypeError, get_object, Type.VERTICAL_CARD_HOLDER)
        self.assertRaises(TypeError, get_object, Type.VERTICAL_CARD_HOLDER, 5)
        self.assertRaises(TypeError, get_object, Type.VERTICAL_CARD_HOLDER, 4, 9)
        self.assertRaises(TypeError, get_object, Type.VERTICAL_CARD_HOLDER, Cube(1,2,3), Cube(4,5,6), Cube(7,8,9))

    def test_get_object_raises_TypeError_for_vartival_card_holder_with_wrong_args(self):
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_COIN_HOLDER)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_COIN_HOLDER, 63.5)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_COIN_HOLDER, 63.8, 88)
        self.assertRaises(TypeError, get_object, Type.HORIZONTAL_COIN_HOLDER, max, min, max)

    def test_get_object_with_proper_arguments_returns_bowl(self):
        obj = get_object(Type.BOWL, 63.5, 88, 25)

        self.assertIsInstance(obj, WithRoundedCorners)
        self.assertIsInstance(obj.box, WithJoints)
        self.assertIsInstance(obj.box.box, PlainBox)
        self.assertIsInstance(obj.box.box.inner, Bowl)

    def test_get_object_with_proper_arguments_returns_horizontal_card_holder(self):
        obj = get_object(Type.HORIZONTAL_CARD_HOLDER, 63.5, 88, 25)

        self.assertIsInstance(obj, WithRoundedCorners)
        self.assertIsInstance(obj.box, WithVerticalHoles)
        self.assertIsInstance(obj.box.box, WithJoints)
        self.assertIsInstance(obj.box.box.box, PlainBox)
        self.assertIsInstance(obj.box.box.box.inner, Cube)

    def test_get_object_with_proper_arguments_returns_certical_card_holder(self):
        obj = get_object(Type.VERTICAL_CARD_HOLDER, 63.5, 88, 25)

        self.assertIsInstance(obj, WithRoundedCorners)
        self.assertIsInstance(obj.box, WithHorizontalHole)
        self.assertIsInstance(obj.box.box, WithJoints)
        self.assertIsInstance(obj.box.box.box, PlainBox)
        self.assertIsInstance(obj.box.box.box.inner, Cube)

    def test_get_object_with_proper_arguments_returns_horizontal_coin_holder(self):
        obj = get_object(Type.HORIZONTAL_COIN_HOLDER, 63.5, 88, 25)

        self.assertIsInstance(obj, WithRoundedCorners)
        self.assertIsInstance(obj.box, WithHorizontalHole)
        self.assertIsInstance(obj.box.box, WithJoints)
        self.assertIsInstance(obj.box.box.box, PlainBox)
        self.assertIsInstance(obj.box.box.box.inner, Pipe)

