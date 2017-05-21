#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.20

“The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Example
Given n = 5, return "111221".

Note
The sequence of integers will be represented as a string.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def count_and_say(n):
    """
    count and say; times + origin
    """
    if n == 0:
        return ''

    res = '1'
    while n > 1:
        n -= 1
        res = gen_result(res)
    return res


def gen_result(res):
    n = len(res)
    r = ''
    i = 0
    while(i < n) :
        count = 1
        while (i + 1 < n and res[i] == res[i + 1]):
            i += 1
            count += 1
        r += str(count) + str(res[i])
        i += 1
    return r

if __name__ == '__main__':
    # for t in ['1', '11', '111', '21', '1121']:
    #     print(t, gen_result(t))
    print(count_and_say(9))




