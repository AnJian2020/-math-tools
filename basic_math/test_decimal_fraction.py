import unittest
from decimal_fraction import *


class TestDecimalFraction(unittest.TestCase):
    """
    测试小数与分数之间的转换
    """

    def test_decimal_to_fraction(self):
        # 测试小数转分数
        num1, num2 = 0.25, 3.75
        self.assertEqual(decimal_to_fraction(num1).__str__(), "1/4")
        self.assertIsInstance(decimal_to_fraction(num1), Fraction)
        self.assertEqual(decimal_to_fraction(num2).__str__(), "15/4")

    def test_fraction_to_decimal(self):
        expression1, expression2, expression3, expression4 = "1/4", "6/5", "1/3", "1a2"
        self.assertEqual(fraction_to_decimal(expression=expression1), 0.25)
        self.assertEqual(fraction_to_decimal(expression=expression2, reserve=1), 1.2)
        self.assertEqual(fraction_to_decimal(expression=expression3, reserve=3), 0.333)
        # self.assertRegex(Exception, fraction_to_decimal, "Error: 分数格式错误！")
        with self.assertRaisesRegex(Exception, "Error: 分数格式错误！"):
            fraction_to_decimal(expression=expression4)
        numerator1, numerator2 = 1, 4
        denominator1, denominator2 = 3, 7
        self.assertEqual(fraction_to_decimal(numerator=numerator1, denominator=denominator1), 0.33)
        self.assertEqual(fraction_to_decimal(numerator=numerator2, denominator=denominator2, reserve=3), 0.571)
        with self.assertRaisesRegex(Exception, "分子和分母不能为空！"):
            fraction_to_decimal(numerator=numerator1)


if __name__=="__main__":
    unittest.main()