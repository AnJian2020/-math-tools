#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "tom"

pi = 3.141592653589793


def rectangle_area(length: float, width: float, reserve: int = 2) -> float:
    """
    计算矩形面积
    :param length: 矩形的长
    :param width: 矩形的宽
    :param reserve: 保留小数位数，默认为2
    :return: 矩形面积
    """
    return round(length * width, reserve)


def triangle_area(base: float, height: float, reserve: int = 2) -> float:
    """
    计算三角形面积
    :param base: 三角形的底
    :param height: 三角形的高
    :param reserve: 保留小数位数，默认为2
    :return: 三角形面积
    """
    return round(base * height * 0.5, reserve)


def circle_area(radius: float, reserve: int = 2) -> float:
    """
    计算圆的面积
    :param radius: 圆的半径
    :param reserve: 保留小数位数，默认为2
    :return: 圆的面积
    """
    return round(pi * radius**2, reserve)


def parallelogram_area(base: float, height: float, reserve: int = 2) -> float:
    """
    计算平行四边形的面积
    :param base: 平行四边形的底
    :param height 平行四边形的高
    :param reserve: 保留小数位数，默认为2
    :return: 平行四边形面积
    """
    return round(base * height, reserve)


def trapezium_area(
    base1: float, base2: float, height: float, reserve: int = 2
) -> float:
    """
    计算梯形的面积
    :param base1: 梯形的上底
    :param base2: 梯形的下底
    :param height: 梯形的高
    :param reserve: 保留小数位数，默认为2
    :return: 梯形面积
    """
    return round((base1 + base2) * height / 2, reserve)


def cuboid_area(length: float, width: float, height: float, reserve: int = 2) -> float:
    """
    计算长方体和正方体的面积
    :param length: 长方体和正方体的长
    :param width: 长方体和正方体的宽
    :param height: 长方体和正方体的高
    :param reserve: 保留小数位数，默认为2
    :return: 长方体和正方体面积
    """
    area = (length * width + length * height + width * height) * 2
    return round(area, reserve)
