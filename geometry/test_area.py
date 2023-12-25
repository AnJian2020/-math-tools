import unittest

from area import *

class TestArea(unittest.TestCase):

    def test_rectangle_area(self):
        length = 2.13256
        width = 0.239102
        self.assertEqual(rectangle_area(length, width), round(length*width, 2))
        self.assertIsInstance(rectangle_area(length, width), float)
        self.assertEqual(rectangle_area(length, width, 4), round(length*width, 4))




if __name__=="__main__":
    unittest.main()