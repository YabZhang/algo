#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21

“Given an nonnegative integer array, find a subarray where the sum of numbers is k.
 Your code should return the index of the first number and the index of the last number.

Example

Given [1, 4, 20, 3, 10, 5], sum k = 33, return [2, 4].”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s, k):
    """ f(m) - f(n) = k """
    sum_dict = {0: 0}
    sum = 0
    result = []
    for i in range(len(s)):
        sum += s[i]
        if sum - k in sum_dict:
            result.append((sum_dict[sum - k], i))
        sum_dict[sum] = i + 1   # 前i项之和
    # print(sum_dict)
    return result


if __name__ == '__main__':
    s = [1, 4, 20, 3, 10, 5]
    k = 33
    print(solution(s, k))
    s = [-3, 1, 2, -3, 4]
    k = 0
    print(solution(s, k))
