"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        symm = set()
        while nums:
            x = nums.pop()
            if x in symm:
                symm.remove(x)
            else:
                symm.add(x)
        
        return symm.pop()

"""
Runtime: 116 ms, faster than 55.90% of Python online submissions for Single Number.
Memory Usage: 15.7 MB, less than 69.12% of Python online submissions for Single Number.
"""