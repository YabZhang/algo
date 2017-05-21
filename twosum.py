#!/usr/bin/env python
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21

“Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example

numbers=[2, 7, 11, 15], target=9

return [1, 2]

Note

You may assume that each input would have exactly one solution

Challenge

Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""

def solution(s, k):
    hash_dict = {}
    for i in range(len(s)):
        if s[i] in hash_dict:
            return hash_dict[s[i]], i + 1
        hash_dict[k - s[i]] = i + 1
    return -1, -1


def solution1(s, k):
    if not s:
        return -1, -1

    pairs = list(enumerate(s))
    pairs.sort(key=lambda x: x[1])
    left, right = 0, len(s) - 1

    while left < right:

        # right
        while(left < right and
              pairs[right][1] > k - pairs[left][1]):
            right -= 1

        # left
        while(left < right and
              pairs[left][1] < k - pairs[right][1]):
            left += 1

        if pairs[left][1] + pairs[right][1] == k:
            return left + 1, right + 1

    return -1, -1


if __name__ == '__main__':
    s = [2, 7, 11, 15]
    print(solution(s, 9))
    print(solution1(s, 9))
