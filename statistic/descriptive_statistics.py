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


def sequence_median(nums: list) -> object:
    """
    计算序列的中位数
    :param nums: 序列
    :return: 序列中位数
    """
    sort_nums = sorted(nums)
    mid = len(sort_nums) // 2
    if len(sort_nums) % 2 == 0:
        return (sort_nums[mid - 1] + sort_nums[mid]) / 2
    else:
        return sort_nums[mid]


def sequence_range(nums: list, reserve: int = 2) -> float:
    """
    获取序列的极差
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 序列的极差
    """
    return round(max(nums) - min(nums), reserve)


def sequence_variable_coefficient(nums: list, reserve: int = 2) -> float:
    """
    计算序列的变异系数
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 序列的变异系数
    """
    return round(sequence_std(nums, reserve=reserve + 1) / sequence_mean(nums, reserve=reserve + 1), reserve)


def sequence_central_tendency(nums: list, reserve: int = 2) -> str:
    """
    获取序列的集中趋势（平均数、众数、中位数）
    :param nums: 序列
    :param reserve: 保留小数位数，默认为2
    :return: 序列的集中趋势（平均数、众数、中位数）
    """
    return (f"集中趋势：\n"
            f"平均数:\t{sequence_mean(nums, reserve)}\n"
            f"众数:\t{sequence_mode(nums)}\n"
            f"中位数:\t{sequence_median(nums)}")


def sequence_dispersion_degree(nums: list, reserve: int = 2) -> str:
    """
    获取序列的离散程度（极差、方差、标准差、变异系数）
    :param nums:
    :param reserve:
    :return:
    """
    return (f"离散程度：\n"
            f"极差:\t{sequence_range(nums, reserve)}\n"
            f"方差:\t{sequence_variance(nums, reserve)}\n"
            f"标准差:\t{sequence_std(nums, reserve)}\n"
            f"变异系数:\t{sequence_variable_coefficient(nums, reserve)}")
