#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "tom"


def factorial(num: int) -> int:
    """
    计算阶乘
    :param num: 参数
    :return: 计算结果
    """
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result


def perm(n: int, m: int) -> int:
    """
    排列
    :param n: 元素的总个数
    :param m: 参与选择的元素个数
    :return: 排列数
    """
    return factorial(n) / factorial(n - m)


def comb(n: int, m: int) -> int:
    """
    组合
    :param n: 元素的总个数
    :param m: 参与选择的元素个数
    :return: 组合数
    """
    return factorial(n) / (factorial(m) * factorial(n - m))
