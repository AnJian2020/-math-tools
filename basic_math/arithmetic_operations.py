#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = "tom"


def is_valid_calculation_expression(expression: str)->bool:
    """
    判断计算的表达式是否只含有数字、小数点、括号和加减乘除符号
    :param expression: 表达式
    :return: 判断结果
    """
    pattern = r"^[0-9().+\-*/]+$"
    match = re.match(pattern, expression)
    return match is not None


def calculate(expression: str, reserve: int = 2) -> float:
    """
    计算表达式
    :param expression: 表达式
    :param reserver: 保留小数位数，默认为2
    :return: 判断结果
    """
    assert is_valid_calculation_expression(expression), Exception(
        "Error: 表达式只能含有数字、小数点、括号和加减乘除符号。"
    )
    return round(eval(expression), reserve)
