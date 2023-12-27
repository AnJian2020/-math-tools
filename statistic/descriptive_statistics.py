#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "tom"


def sequence_sum(nums: list, reserve: int = 2) -> float:
    """
    计算序列的总和
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 和
    """
    res = 0
    for item in nums:
        res += item
    return round(res, reserve)


def sequence_mean(nums: list, reserve: int = 2) -> float:
    """
    计算序列的平均数
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 平均数
    """
    return round(sequence_sum(nums, reserve) / len(nums), reserve)



