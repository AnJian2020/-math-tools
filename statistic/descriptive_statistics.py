#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

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
    return round(sequence_sum(nums, reserve=15) / len(nums), reserve)


def sequence_variance(nums: list, reserve: int = 2) -> float:
    """
    计算序列的方差
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 方差
    """
    mean = sequence_mean(nums, reserve=15)
    res = 0
    for item in nums:
        res += (item - mean) ** 2
    return round(res / len(nums), reserve)


def sequence_std(nums: list, reserve: int = 2) -> float:
    """
    计算序列的标准差
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 标准差
    """
    return round(sequence_variance(nums, reserve=15) ** 0.5, reserve)


def sequence_mode(nums: list) -> list:
    """
    计算序列的众数
    :param nums: 序列
    :return: 众数list
    """
    res = []
    nums_counter = Counter(nums)
    max_count = None
    for k, v in nums_counter.items():
        if max_count is None or v > max_count:
            res = [k]
            max_count = v
        elif v == max_count:
            res.append(k)
    return res


