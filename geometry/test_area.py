import unittest

from area import *


class TestArea(unittest.TestCase):
    def test_rectangle_area(self):
        length = 2.13256
        width = 0.239102
        self.assertEqual(rectangle_area(length, width), round(length * width, 2))
        self.assertIsInstance(rectangle_area(length, width), float)
        self.assertEqual(rectangle_area(length, width, 4), round(length * width, 4))

    def test_triangle_area(self):
        base1, base2 = 2.2, 3
        height1, height2 = 5.4, 6
        self.assertEqual(triangle_area(base1, height1), round(0.5 * base1 * height1, 2))
        self.assertEqual(triangle_area(base1, height1, reserve=0), round(0.5 * base1 * height1, 0))
        self.assertIsInstance(triangle_area(base2, height2), float)
        self.assertEqual(triangle_area(base2, height1, reserve=0), round(0.5 * base2 * height1, 0))
        


if __name__ == "__main__":
    unittest.main()
