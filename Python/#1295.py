"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([str(s) for s in nums if len(str(s))%2==0])

"""
Runtime: 52 ms, faster than 74.11% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 14.3 MB, less than 43.61% of Python3 online submissions for Find Numbers with Even Number of Digits.
"""
