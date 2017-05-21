#!/usr/bin/env python3
# coding: utf8


"""
@Author: yabin
@Date: 2017.5.21

“Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

Note
You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""


def solution(a, m, b, n):
    p = m + n - 1
    m -= 1
    n -= 1
    while (m >= 0 and n >= 0):
        if a[m] >= b[n]:
            a[p] = a[m]
            m -= 1
        else:
            a[p] = b[n]
            n -= 1
        p -= 1

    if n >= 0:
        while p > 0 and n >= 0:
            a[p] = b[n]
            n -= 1
            p -= 1
    print(a)
    return a


"""
“Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm
if one array is very large and the other is very small?”

摘录来自: yuanbin. “Data Structure and Algorithm notes”。 iBooks.
"""

def solution2(A, m, B, n):
    result = []
    i = 0
    j = 0

    while(i < m and j < n):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    if i == m:    # A done
        result += B[j:]
    else:
        result += A[i:]

    return result


if __name__ == '__main__':
    A = [1, 2, 3, None, None, None]
    B = [1, 1, 3, 6]
    # solution(A, 3, B, 3)
    print(solution2(A, 3, B, 4))

