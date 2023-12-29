import unittest
from odd_even import *

class TestOddEven(unittest.TestCase):
    """
    测试奇偶数的判断
    """
    def test_is_odd(self):
        # 测试奇数
        num1, num2 = 3, 8
        self.assertTrue(is_odd(num1))
        self.assertFalse(is_odd(num2))

    def test_is_even(self):
        # 测试偶数
        num1, num2 = 3, 8
        self.assertFalse(is_even(num1))
        self.assertTrue(is_even(num2))