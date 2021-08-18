"""
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, 2**16
        while lo<hi:
            if ((lo+hi)/2)**2 == x:
                return (lo+hi)/2
            elif ((lo+hi)/2)**2 > x:
                hi = (lo+hi)/2
            else:
                lo = (lo+hi)/2+1 # When lo and hi differ by 1 (edge case)
        return lo-1 # return lower bound

"""
Runtime: 20 ms, faster than 82.27% of Python online submissions for Sqrt(x).
Memory Usage: 13.5 MB, less than 35.65% of Python online submissions for Sqrt(x).
"""