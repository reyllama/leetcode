"""
1342. Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""

class Solution:
    def numberOfSteps(self, num):
        b = bin(num)[2:]
        c = 0
        while int(b)>0:
            if b[-1]=='1':
                b = b[:-1]+"0"
                c += 1
            if b == "0":
                return c
            b = b[:-1]
            c += 1
        return c

"""
Runtime: 28 ms, faster than 85.77% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.9 MB, less than 97.86% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""
