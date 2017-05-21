#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21


“Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.

Clarification
What is rotated array:

    - For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s):
    """
    三步翻转法： 确定分割点，分别逆序翻转前后两部分，然后整体翻转
    :param s:
    :return:
    """
    mid_point = len(s) // 2 - 1
    reverse_helper(s, 0, mid_point)
    reverse_helper(s, mid_point + 1, len(s) - 1)
    reverse_helper(s, 0, len(s) - 1)
    return s


def reverse_helper(s, a, b):
    """ in-place reverse seq s[a:b] """
    assert a <= b
    t1, t2 = a, b
    while(t1 < t2):
        s[t1], s[t2] = s[t2], s[t1]
        t1 += 1
        t2 -= 1


if __name__ == '__main__':
    s = [4, 5, 1, 2, 3]
    print(solution(s))
