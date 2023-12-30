#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fractions import Fraction

__author__ = "tom"


def decimal_to_fraction(num: float) -> Fraction:
    """
    将小数转化为分数
    :param nums: 序列
    :return: 分数
    """
    return Fraction(num).limit_denominator()


def fraction_to_decimal(expression: str = None, numerator=None, denominator=None, reserve: int = 2) -> float:
    """
    将分数转化为小数，分数表达式与分母、分子不能同时为空
    :param expression: 分数表达式
    :param numerator: 分子
    :param denominator: 分母
    :param reserver: 保留小数位数，默认为2
    :return: 小数
    """
    if expression:
        assert '/' in expression, Exception("Error: 分数格式错误！")
        numerator, denominator = tuple(map(int, expression.split("/")))
    elif numerator is None or denominator is None:
        raise Exception("分子和分母不能为空！")
    fraction = Fraction(numerator, denominator)
    return round(float(fraction), reserve)
