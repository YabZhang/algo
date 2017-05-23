#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21

TODO: 几种基本排序算法；
Basic Sort Algo
"""


def bubble_sort(s):
    """ 冒泡排序 n^2 """
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            if s[j - 1] > s[j]:
                s[j - 1], s[j] = s[j], s[j - 1]
    return s


def select_sort(s):
    """ 选择排序 n^2 """
    for i in range(len(s)):
        min_index = i
        for j in range(i + 1, len(s)):
            if s[j] < s[min_index]:
                min_index = j
        if min_index != i:
            s[min_index], s[i] = s[i], s[min_index]
    return s


def insert_sort(s):
    """ 插入排序 n^2 """
    for i in range(len(s) - 1):
        temp = s[i + 1]
        for j in range(i + 1, -1, -1):
            if temp < s[j - 1]:
                s[j] = s[j - 1]
            else:
                break
        s[j] = temp
    return s


def merge_sort(s):
    """ in-place 归并排序 nlogn"""
    return _merge_helper(s, 0, len(s) - 1)


def _merge_helper(s, l, u):
    if (u - l + 1) <= 1:
        return

    mid = (u + l) // 2
    _merge_helper(s, l, mid)
    _merge_helper(s, mid + 1, u)

    k, v = l, mid + 1
    helper = s[:]
    for i in range(l, u + 1):
        if k > mid:
            s[i] = helper[v]
            v += 1
        elif v > u:
            s[i] = helper[k]
            k += 1
        elif helper[k] < helper[v]:    # v <= u
            s[i] = helper[k]
            k += 1
        else:
            s[i] = helper[v]
            v += 1
    return s


def quick_sort(s):
    """ in-place 快排 nlogn """
    return _quick_helper(s, 0, len(s) - 1)


def _quick_helper(s, l, u):
    if (u - l + 1) <= 1:
        return

    mid = (u + l) // 2

    pt = l
    s[l], s[mid] = s[mid], s[l]
    for i in range(l + 1, u + 1):
        if s[i] < s[l]:
            pt += 1
            s[pt], s[i] = s[i], s[pt]
    s[l], s[pt] = s[pt], s[l]

    _quick_helper(s, l, pt - 1)
    _quick_helper(s, pt + 1, u)
    return s


def heap_sort():
    """ 堆排序 """
    pass


def redix_sort():
    """ 基数排序 """
    pass


def count_sort():
    """ 计数排序 """
    pass


def bucket_sort():
    """ 桶排序 """
    pass


if __name__ == "__main__":
    s = list('2718281828459045')
    # r = bubble_sort(list(s))
    # r = select_sort(list(s))
    # r = insert_sort(list(s))
    # r = merge_sort(list(s))
    r = quick_sort(list(s))
    print('========= Origin ==========')
    print(s)
    print('========= Sorted ==========')
    print(r)
