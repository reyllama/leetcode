"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        ref = defaultdict(int)
        for num in nums:
            ref[num] += 1
        ans = []
        for i in range(1, len(nums)+1):
            if not ref[i]:
                ans.append(i)
        return ans

"""
Runtime: 328 ms, faster than 40.74% of Python online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 24.6 MB, less than 17.60% of Python online submissions for Find All Numbers Disappeared in an Array.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set(list(range(1, len(nums)+1)))
        for num in nums:
            res.discard(num)
        return list(res)

"""
Runtime: 308 ms, faster than 65.55% of Python online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.7 MB, less than 31.26% of Python online submissions for Find All Numbers Disappeared in an Array.
"""