"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n):
        cache = set()
        for _ in range(200):
            cache.add(n)
            nums = str(n)
            n = sum([int(num)**2 for num in nums])
            if n==1:
                return True
            if n in cache:
                return False
            
"""
Runtime: 29 ms, faster than 16.14% of Python online submissions for Happy Number.
Memory Usage: 13.6 MB, less than 12.11% of Python online submissions for Happy Number.
"""