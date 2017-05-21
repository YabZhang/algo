#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21

“Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example
Given [4, 5, 1, 2, 3], return 3

Given [7, 9, 4, 5], return 5

Challenge
O(n) time.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s):
    if not s:
        return -1
    return helper(s, 0, len(s) - 1, (len(s) + 1) // 2)


def helper(s, l, u, n):
    m = l
    for i in range(l + 1, u + 1):
        if s[i] < s[l]:
            m += 1
            s[i], s[m] = s[m], s[i]

    # swap
    s[l], s[m] = s[m], s[l]

    if n == m - l + 1:    # d = m - l + 1
        return s[m]

    elif n > m - l + 1:
        return helper(s, m + 1, u, n - (m - l + 1))

    else:
        return helper(s, l, m - 1, n)


if __name__ == '__main__':
    s = [4, 5, 1, 2, 3]
    print('q1: ', solution(s))
    s = [7, 9, 4, 5]
    print('q2: ', solution(s))