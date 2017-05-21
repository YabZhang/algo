#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21


Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5,
2nd largest element is 4, 3rd largest element is 3 and etc.

Note
You can swap elements in the array

Challenge
O(n) time, O(1) extra memory.

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s, k):
    if len(s) < k:
        return -1
    return helper(s, 0, len(s) - 1, k)


def helper(s, l, u, k):
    m = l
    for i in range(l + 1, u + 1):
        if s[i] > s[l]:
            m += 1
            s[i], s[m] = s[m], s[i]

    s[l], s[m] = s[m], s[l]

    if k == m - l + 1:
        return s[m]

    elif k < m - l + 1:
        return helper(s, l, m - 1, k)

    else:
        return helper(s, m + 1, u, k - (m - l + 1))


if __name__ == '__main__':
    s = [9, 3, 2, 4, 8]
    print(solution(s, 3))
    s = [1, 2, 3, 4, 5]
    print(solution(s, 1))
    print(solution(s, 2))
    print(solution(s, 3))
