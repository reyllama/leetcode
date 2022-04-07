"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if sum(nums) < target:
            return 0
        
        curVal = 0
        l, r = 0, -1
        
        for i, v in enumerate(nums):
            # print(i, v, l, r, curVal)
            if curVal < target:
                curVal += nums[i]
                r = i # inclusive
                
                j = 0
                while sum(nums[l+j+1:i+1]) >= target:
                    j += 1
                l += j
                r = i
                
            else:
                if sum(nums[r+1:i+1]) > sum(nums[l:l+i-r]):
                    
                    l += (i-r)
                    r = i
                    
                    j = 0
                    while sum(nums[l+j+1:i+1]) >= target:
                        j += 1
                    l += j
                    r = i
        return r-l+1

"""
Runtime: 1984 ms, faster than 5.00% of Python online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.6 MB, less than 7.74% of Python online submissions for Minimum Size Subarray Sum.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        curVal = 0
        l = 0
        res = len(nums) + 1
        
        for i in range(len(nums)):
            
            curVal += nums[i]
            while curVal >= target:
                res = min(res, i-l+1)
                curVal -= nums[l]
                l += 1
        return res % (len(nums)+1)


"""
Runtime: 72 ms, faster than 57.23% of Python online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.3 MB, less than 94.45% of Python online submissions for Minimum Size Subarray Sum.
"""
