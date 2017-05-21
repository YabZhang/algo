#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""

def solution(s):
    if len(s) < 3:
        return []

    s.sort()
    result = []
    visited = {}

    for i in range(len(s)):
        if s[i] in visited:
            continue
        visited[s[i]] = True

        r = two_sum(s[i + 1:], -1 * s[i])
        for item in r:
            result.append([s[i]] + list(item))

    return result


def two_sum(s, k):
    if not s:
        return []

    pairs = list(enumerate(s))
    # pairs.sort(key=lambda x: x[1])
    left, right = 0, len(s) - 1
    result = []
    while left < right:

        # right
        while(left < right and
              pairs[right][1] > k - pairs[left][1]):
            right -= 1

        # left
        while(left < right and
              pairs[left][1] < k - pairs[right][1]):
            left += 1

        if left < right and pairs[left][1] + pairs[right][1] == k:
            result.append((pairs[left][1], pairs[right][1]))
            left += 1
            right -= 1

    return result


if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4]
    print(solution(s))
