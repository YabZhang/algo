#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.20

“Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def remove_element(alist, val):
    n = len(alist)
    i = 0

    while(i < n - 1):
        if alist[i] == val:
            alist[i] = alist[n - 1]
            n -= 1
            i -= 1
        i += 1

    return n


if __name__ == '__main__':
    s = [0, 4, 4, 0, 0, 2, 4, 4]
    r = remove_element(s, 4)
    print('result: ', r)
