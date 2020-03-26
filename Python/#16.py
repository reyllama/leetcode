"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        e = 0
        nums = sorted(nums)
        while True:
            for i in range(len(nums)-2):
                j, k = i+1, len(nums)-1
                while j<k:
                    if nums[i] + nums[j] + nums[k] < target-e:
                        j+=1
                    elif nums[i] + nums[j] + nums[k] > target+e:
                        k-=1
                    else:
                        return nums[i] + nums[j] + nums[k]
            e += 1

"""
Runtime: 136 ms, faster than 62.74% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
"""
