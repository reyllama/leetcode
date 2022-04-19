"""
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

    For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = 0
        lo, hi = 0, 1
        while hi < len(nums)-1:
            itv = nums[hi]-nums[hi-1]
            if nums[hi+1] - nums[hi] == itv:
                hi += 1
            else:
                span = hi-lo+1
                cnt += (span-1)*(span-2)//2
                lo = hi
                hi = lo+1
        span = hi-lo+1
        cnt += (span-1)*(span-2)//2
        
        return cnt

"""
Runtime: 35 ms, faster than 95.36% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.2 MB, less than 12.01% of Python3 online submissions for Arithmetic Slices.
"""
