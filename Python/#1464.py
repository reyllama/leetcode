"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = [0], [1001] # constraint

        for num in nums:
            if num > min(maxi):
                tmp = max(maxi)
                maxi = [tmp, num]
            if num < max(mini):
                tmp = min(mini)
                mini = [tmp, num]

        return max((maxi[0]-1)*(maxi[1]-1), (mini[0]-1)*(mini[1]-1))

"""
Runtime: 48 ms, faster than 80.10% of Python3 online submissions for Maximum Product of Two Elements in an Array.
Memory Usage: 14.3 MB, less than 72.57% of Python3 online submissions for Maximum Product of Two Elements in an Array.
"""
