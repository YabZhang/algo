#!/usr/bin/env python3
# coding: utf8

"""
@Author: yabin
@Date: 2017.5.20

“Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def wildcard_matching(string, pattern):
    """
    check if string match the pattern
    :param string:
    :param pattern:
    :return:
    """
    if not (string and pattern):
        return False

    return is_match(string, 0, pattern, 0)


def is_match(string, indexA, pattern, indexB):
    """
    ? : match one char;
    * : match any seq of char, including empty seq;
    """
    if (len(string) == indexA or len(pattern) == indexB):
        if (len(string) == indexA and len(pattern) == indexB):
            return True
        else:
            return False

    if pattern[indexB] == '*':

        while(indexB < len(pattern) and pattern[indexB] == '*'):
            indexB += 1

        if indexB == len(pattern):
            return True
        else:

            while(indexB < len(pattern) and not is_match(string, indexA, pattern, indexB)):
                indexB += 1

            if indexB != len(pattern):
                return True
            else:
                return False
    elif pattern[indexB] == '?' or pattern[indexB] == string[indexA]:
        return is_match(string, indexA + 1, pattern, indexB + 1)
    else:
        return False


if __name__ == '__main__':
    assert wildcard_matching("aa", "a") == False
    assert wildcard_matching("aa", "aa") == True
    assert wildcard_matching("aaa", "aa") == False
    assert wildcard_matching("aa", "*") == True
    assert wildcard_matching("aa", "a*") == True
    assert wildcard_matching("ab", "?*") == True
    assert wildcard_matching("aab", "c*a*b") == False