#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = "tom"


class ArithmeticOperations:
    def basic_calculate(self, expression: str):
        try:
            assert self.is_valid_calculation_expression(expression), Exception("Error: 表达式只能含有数字、小数点、括号和加减乘除符号。")
            return eval(expression)
        except Exception as error:
            print(error.__str__())

    
    def complex_calculate(self, expression: str):
        pass


    def is_valid_calculation_expression(self, expression: str):
        pattern = r"^[0-9().+\-*/]+$"
        match = re.match(pattern, expression)
        return match is not None


if __name__ == "__main__":
    print(ArithmeticOperations().basic_calculate("1+2"))
