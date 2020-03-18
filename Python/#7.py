'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            r = int(str(x)[::-1])
        else:
            r = -int(str(x)[1:][::-1])
        return r if r in range(-2**31, 2**31) else 0

'''
Runtime: 20 ms, faster than 98.69% of Python3 online submissions for Reverse Integer.
Memory Usage: 13 MB, less than 99.34% of Python3 online submissions for Reverse Integer.
'''
