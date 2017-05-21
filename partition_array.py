#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date:


“Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example

If nums = [3,2,2,1] and k=2, a valid answer is 1.

Note

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length”

“Challenge

Can you partition the array in-place and in O(n)?”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""

def solution(s, k):
    p = 0
    t = p + 1
    while(t < len(s)):
        if s[t] < k:
            s[p], s[t] = s[t], s[p]
            p += 1
        t += 1
    if p == 0:
        return len(s)
    return p

def solution1(s, k):
    """ 快排的思想，两根指针从左右同时开始 """
    length = len(s)
    left, right = 0, length - 1
    while(left < right):

        while(left < right and s[left] < k):
            left += 1

        while(left < right and s[right] >= k):
            right -= 1

        if (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return left


if __name__ == '__main__':
    s = [3, 2, 1, 2, 1]
    print(solution(s, 2))
    print(solution1(s, 2))

