"""
905. Sort Array By Parity

Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.
"""

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1, arr2 = [], []

        for item in nums:
            if item % 2 == 0:
                arr1.append(item)
            else:
                arr2.append(item)
        return arr1+arr2

"""
Runtime: 52 ms, faster than 99.14% of Python online submissions for Sort Array By Parity.
Memory Usage: 14.2 MB, less than 91.08% of Python online submissions for Sort Array By Parity.
"""