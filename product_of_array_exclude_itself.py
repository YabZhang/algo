#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21

“Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A=[1, 2, 3], return [6, 3, 2].”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s):
    if not s:
        return []
    left, right = gen_help_table(s)
    result = []
    for i in range(len(s)):
        result.append(left[i] * right[i])
    return result


def gen_help_table(s):
    left = [1] * len(s)
    right = [1] * len(s)
    for i in range(len(s)):
        if i != 0:
            left[i] = left[i - 1] * s[i - 1]
            right[len(s) - i - 1] = right[len(s) - i] * s[len(s) - i]
    return left, right


def solution1(s):
    if not s:
        return []
    result = [1] * len(s)


    # left part
    for i in range(len(s)):
        if i > 0:
            result[i] = s[i - 1] * result[i - 1]

    # right part
    temp = 1
    for i in range(len(s)):
        if i > 0:
            temp *= s[len(s) - i]
            result[len(s) - i - 1] *= temp
    return result


if __name__ == '__main__':
    s = [1, 2, 3]
    print(solution(s))
    print(solution1(s))