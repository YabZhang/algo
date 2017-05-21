#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.21

“Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s, k):
    s.sort()
    closet = 0
    for i in range(len(s)):
        r = two_sum_coloset(s[i + 1:], k)
        temp = r + s[i]
        # print('temp ', r, s[i])
        if abs(temp - k) < abs(closet - k):
            closet = temp
    return closet


def two_sum_coloset(s, k):
    if len(s) < 2:
        return 0

    left, right = 0, len(s) - 1
    closet = s[left] + s[right]

    while(left < right):
        if closet - k > 0:
            right -= 1
        elif closet == k:
            return closet
        else:
            left += 1
        if left < right and \
                abs(s[left] + s[right] - k) < abs(closet - k):
            # print(s[left], s[right])
            closet = s[left] + s[right]
    return closet


if __name__ == '__main__':
    s = [-1, 2, 1, -4]
    r = solution(s, 2)
    # r = two_sum_coloset(s, 3)
    print('result', r)