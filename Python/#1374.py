"""
1374. Generate a String With Characters That Have Odd Counts

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.
"""

class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            ans = 'q'
        elif n % 2 == 0:
            ans = 'q' + 'c'*(n-1)
        else:
            ans = 'q' + 'c' + 'r' * (n-2)

        return ans

"""
Runtime: 32 ms, faster than 46.95% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
Memory Usage: 14.3 MB, less than 36.42% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
"""
