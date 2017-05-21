#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21

“Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Example”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(s):
    """

    :param s: sorted array
    :return:
    """
    j = 0    # point to no dupl element
    for i in range(len(s)):
        if i == len(s) - 1:
            continue
        if s[i] != s[i + 1]:
            if i != j:
                s[j + 1] = s[i + 1]
            j += 1
    s[j + 1:] = []
    return j + 1


def solution1(s):
    """

    :param s: sorted array
    :return:
    """
    j = 0
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] != s[j]:
            if i != j + 1:
                s[j + 1] = s[i]
            j += 1
    s[j + 1:] = []
    return j + 1


"""
“Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
Example”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution2(s):
    """
    dup at most 2 times
    :param s:
    :return:
    """
    j = 0
    for i in range(len(s)):
        if j > 1 and s[i] == s[j - 2]:
            continue
        if i != j - 1:
            s[j] = s[i]
        j += 1

    s[j:] = []
    return j




if __name__ == '__main__':
    s = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5]
    # print(solution(list(s)))
    # print(solution1(list(s)))
    print(solution2(list(s)))
