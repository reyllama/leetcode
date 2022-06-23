"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums = sorted(nums)
        prev, prev_set = -100, [[]]

        for n in nums:
            new_set = []
            if prev == -100:
                prev = n
            if n == prev:
                for item in prev_set:
                    new_set.append(item + [n])
            else:
                for item in res:
                    new_set.append(item + [n])
            prev_set = new_set
            res += prev_set
            prev = n
        return res

"""
Runtime: 34 ms, faster than 55.75% of Python online submissions for Subsets II.
Memory Usage: 13.6 MB, less than 73.21% of Python online submissions for Subsets II.
"""