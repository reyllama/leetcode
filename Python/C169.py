"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]

"""
Runtime: 128 ms, faster than 94.60% of Python online submissions for Majority Element.
Memory Usage: 14.7 MB, less than 69.81% of Python online submissions for Majority Element.
"""