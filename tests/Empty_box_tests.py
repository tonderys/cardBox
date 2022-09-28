import unittest
import sys

sys.path.append("..")

from Empty_box import Empty_box

class Empty_box_tests(unittest.TestCase):
    def test_simple(self):
        sut = Empty_box(1,2,3)
        self.assertEqual(sut.outer.width, 3)
        self.assertEqual(sut.outer.height, 4)
        self.assertEqual(sut.outer.depth, 5)

if __name__ == '__main__':
    unittest.main()