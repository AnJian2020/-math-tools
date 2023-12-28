import unittest
from perimeter import *

class TestPerimeter(unittest.TestCase):
    """
    测试几何图形周长计算
    """
    def test_rectangle_perimeter(self):
        # 测试计算矩形的周长
        length1, length2 = 23, 3.1415926
        width1, width2 = 11, 8.98134213
        self.assertEqual(rectangle_perimeter(length1, width1), 68)
        self.assertEqual(rectangle_perimeter(length2, width1), 28.28)
        self.assertEqual(rectangle_perimeter(length2, width1, 3), 28.283)
        self.assertEqual(rectangle_perimeter(length2, width2, 6), 24.245869)