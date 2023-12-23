#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = "tom"


class ArithmeticOperations:
    def calculate(self, expression: str, reserve:int =2)->float:
        try:
            assert self.is_valid_calculation_expression(expression), Exception("Error: 表达式只能含有数字、小数点、括号和加减乘除符号。")
            return round(eval(expression), reserve)
        except Exception as error:
            print(error.__str__())


    def is_valid_calculation_expression(self, expression: str):
        pattern = r"^[0-9().+\-*/]+$"
        match = re.match(pattern, expression)
        return match is not None


if __name__ == "__main__":
    print(ArithmeticOperations().calculate("1+2"))
