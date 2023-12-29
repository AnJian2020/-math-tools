import unittest

from area import *


class TestArea(unittest.TestCase):
    def test_rectangle_area(self):
        # 测试矩形面积的计算
        length = 2.13256
        width = 0.239102
        self.assertEqual(rectangle_area(length, width), round(length * width, 2))
        self.assertIsInstance(rectangle_area(length, width), float)
        self.assertEqual(rectangle_area(length, width, 4), round(length * width, 4))

    def test_triangle_area(self):
        # 测试三角形面积的计算
        base1, base2 = 2.2, 3
        height1, height2 = 5.4, 6
        self.assertEqual(triangle_area(base1, height1), round(0.5 * base1 * height1, 2))
        self.assertEqual(
            triangle_area(base1, height1, reserve=0), round(0.5 * base1 * height1, 0)
        )
        self.assertIsInstance(triangle_area(base2, height2), float)
        self.assertEqual(
            triangle_area(base2, height1, reserve=0), round(0.5 * base2 * height1, 0)
        )

    def test_circle_area(self):
        # 测试圆的面积的计算
        radius1, radius2, radius3 = 2, 3.4, 7.2314
        self.assertEqual(circle_area(radius=radius1), round(pi * radius1**2, 2))
        self.assertEqual(circle_area(radius2, 3), round(pi * radius2**2, 3))
        self.assertEqual(circle_area(radius3, 0), round(pi * radius3**2, 0))

    def test_parallelogram_area(self):
        # 测试计算平行四边形的面积
        base1, base2 = 1.2389, 6
        height1, height2 = 2.478, 9
        self.assertEqual(parallelogram_area(base1, height1), 3.07)
        self.assertEqual(parallelogram_area(base1, height1, 1), 3.1)
        self.assertEqual(parallelogram_area(base2, height2), 54.0)

    def test_trapezium_area(self):
        # 测试计算梯形的面积
        base1_1, base1_2, base2_1, base2_2 = 1.234, 2.9845, 4, 7.0
        height1, height2 = 3.2003462, 5
        self.assertEqual(trapezium_area(base1_1, base1_2, height1), 6.75)
        self.assertEqual(trapezium_area(base2_1, base2_2, height2), 27.5)
        self.assertEqual(trapezium_area(base1_1, base1_2, height1, 5), 6.75033)
        self.assertEqual(trapezium_area(base2_1, base2_2, height2, 3), 27.5)

    def test_cuboid_area(self):
        # 测试计算长方体和正方体的面积
        length1, length2 = 5, 7.5734862101
        width1, width2 = 3, 2.1459127
        height1, height2 = 3.2003462, 5
        self.assertEqual(cuboid_area(length1, width1, height1), 81.21)
        self.assertEqual(cuboid_area(length2, width2, height2), 129.70)
        self.assertEqual(cuboid_area(length1, width2, height1), 67.20)
        self.assertEqual(cuboid_area(length2, width2, height1, 3), 94.715)
        self.assertEqual(cuboid_area(length2, width2, height1, 5), 94.71496)

    def test_ball_area(self):
        # 测试计算球体的面积
        radius1, radius2, radius3 = 5, 4.873, 8.12314
        self.assertEqual(ball_area(radius1), round(4 * pi * radius1**2, 2))
        self.assertEqual(ball_area(radius2), round(4 * pi * radius2**2, 2))
        self.assertEqual(ball_area(radius3), round(4 * pi * radius3**2, 2))
        self.assertEqual(ball_area(radius2, 3), round(4 * pi * radius2**2, 3))
        self.assertEqual(ball_area(radius3, 4), round(4 * pi * radius3**2, 4))

    def test_polygon_area(self):
        # 测试计算多边形的面积
        points1 = [(0, 0), (2, 2), (0, 2), (2, 0)]
        self.assertEqual(polygon_area(points1), 4.0)
        points2 = [(0, 0), (2.53, 2.53), (2.53, 0), (0, 2.53)]
        self.assertEqual(polygon_area(points2), round(2.53 * 2.53, 2))
        self.assertEqual(polygon_area(points2, 4), round(2.53 * 2.53, 4))
