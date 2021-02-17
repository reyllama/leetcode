"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(s) for s in str(n)]
        return prod(res) - sum(res)

"""
Runtime: 32 ms, faster than 57.94% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.3 MB, less than 44.41% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
