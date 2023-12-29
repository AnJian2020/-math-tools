import unittest
from arithmetic_operations import *


class TestArithmeticOperations(unittest.TestCase):
    """
    测试四则运算
    """

    def test_calculate(self):
        test_data = {
            "1+2": 3.0,
            "2.75346+3.1415934": 5.8950534,
            "3*0": 0,
            "4*(-1)": -4,
            "4/0": None,
            "5.236*4": 20.944,
            "1-3.4561": -2.4561,
        }
        for k, v in test_data.items():
            if v is not None:
                self.assertEqual(calculate(k), round(v, 2))
            else:
                self.assertIsNone(calculate(k))
        expression1 = "1a+dfs"
        # self.assertRaises(Exception, calculate, expression1)
        self.assertIsNone(calculate(expression1))
        self.assertEqual(calculate('2.75346+3.1415934', 4), 5.8951)
