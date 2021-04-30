"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n//2+1):
            ans += [i, -i]
        if n % 2 == 1:
            ans.append(0)
        return ans

"""
Runtime: 32 ms, faster than 76.08% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 14.3 MB, less than 76.53% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
"""
