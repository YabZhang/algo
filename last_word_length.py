#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.20


“Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Have you met this question in a real interview? Yes
Example
Given s = "Hello World", return 5.

Note
A word is defined as a character sequence consists of non-space characters only.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def last_word_length(s):
    if not s:
        return 0

    n = len(s) - 1
    count = 0
    while(n > 0):
        if s[n] != ' ':
            count += 1
            n -= 1
        else:
            if not count:
                n -= 1
                continue
            break
    return count


if __name__ == "__main__":
    s = 'Hello World'
    ss = 'Hello World '
    assert last_word_length(s) == 5
    assert last_word_length(ss) == 5