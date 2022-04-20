"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        if target > nums[-1]:
            return r
        elif target < nums[0]:
            return l
        while l < r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        return l

"""
Runtime: 71 ms, faster than 47.46% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 44.22% of Python3 online submissions for Search Insert Position.
"""
