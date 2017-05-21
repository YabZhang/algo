#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21

“Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]

Challenge
O(nlogn) time”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""

def solution(s):
    sum_pairs = [(0, 0)]
    sum = 0
    for i in range(len(s)):
        sum += s[i]
        sum_pairs.append((i + 1, sum))

    sum_pairs.sort(key=lambda x: x[1])

    min_d = abs(sum_pairs[1][1] - sum_pairs[0][1])
    result = []
    for j in range(len(sum_pairs)):
        if j + 1 < len(sum_pairs):
            if abs(sum_pairs[j + 1][1] - sum_pairs[j][1]) <= min_d:
                pair = sum_pairs[j + 1][0], sum_pairs[j][0]
                result.append((min(pair), max(pair) - 1))
                # print('pair: ', pair)
                # print('result: ', result)
    return result


if __name__ == '__main__':
    s = [-3, 1, 1, -3, 5]
    print(solution(s))
