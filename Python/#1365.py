"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ref = sorted(nums)
        return [ref.index(num) for num in nums]

"""
Runtime: 84 ms, faster than 58.62% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.5 MB, less than 15.85% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
"""
