"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for n in range(len(nums)+2):
            if not n in nums:
                return n

"""
Runtime: 112 ms, faster than 54.27% of Python online submissions for Missing Number.
Memory Usage: 15.3 MB, less than 8.70% of Python online submissions for Missing Number.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        grid = [0]*(len(nums)+1)
        while nums:
            n = nums.pop()
            grid[n] = 1
        for i, v in enumerate(grid):
            if v==0:
                return i