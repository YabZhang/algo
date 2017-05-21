#!/usr/bin/env python3
# coding: utf8

"""
@Author: Yabin
@Date: 2017.5.20

Write a method to replace all spaces in a string with %20.
The string is given in a characters array, you can assume it has enough space
for replacement and you are given the true length of the string.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python，please use characters array instead of string.

Challenge
Do it in-place.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def replace_blank(st, length):
    """
    @param: st [] char list
    @param: length int length of the string
    """

    n = 0
    for i in range(length):
        if st[i] == ' ':
            n += 1

    r_len = length + 2 * n
    for i in list(range(length))[::-1]:
        if st[i] != ' ':
            st[r_len - 1] = st[i]
            r_len -= 1
        else:
            st[r_len - 1] = '0'
            st[r_len - 2] = '2'
            st[r_len - 3] = '%'
            r_len -= 3


if __name__ == '__main__':
    st = list('3x, i am fine!') + list('*' * 10)
    length = len('3x, i am fine!')
    replace_blank(st, length)
    print('result: %s' % ''.join(st))
