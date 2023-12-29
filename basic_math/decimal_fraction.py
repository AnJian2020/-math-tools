#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fractions import Fraction

__author__ = "tom"


def decimal_to_fraction(num: float) -> Fraction:
    """
    将小数转化为分数
    """
    return Fraction(num).limit_denominator()


def fraction_to_decimal(expression: str = None, numerator=None, denominator=None, reserve: int = 2) -> float:
    """
    将分数转化为小数
    """
    if expression:
        assert '/' in expression, Exception("Error: 分数格式错误！")
        numerator, denominator = tuple(map(int, expression.split("/")))
    elif numerator is None or denominator is None:
        raise Exception("分子和分母不能为空！")
    fraction = Fraction(numerator, denominator)
    return round(float(fraction), reserve)
