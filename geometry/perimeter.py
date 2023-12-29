#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "tom"

pi = 3.141592653589793


def rectangle_perimeter(length: float, width: float, reserve: int = 2) -> float:
    """
    计算矩形的周长
    :param length: 矩形的长
    :param width: 矩形的宽
    :param reserve: 保留小数位数，默认为2
    :return: 矩形周长
    """
    return round(length * 2 + width * 2, reserve)


def circle_perimeter(radius: float, reserve: int = 2) -> float:
    """
    计算圆的周长
    :param radius: 圆的半径
    :param reserve: 保留小数位数，默认为2
    :return: 圆的周长
    """
    return round(pi * radius * 2, reserve)


def cuboid_perimeter(
    length: float, width: float, height: float, reserve: int = 2
) -> float:
    """
    计算长方体和正方体的周长
    :param length: 长方体和正方体的长
    :param width: 长方体和正方体的宽
    :param height: 长方体和正方体的高
    :param reserve: 保留小数位数，默认为2
    :return: 长方体和正方体周长
    """
    return round((length + width + height) * 2, reserve)
