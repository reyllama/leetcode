"""
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # idea from @vubui
        res = []
        def _permute(num, cur, lim):
            if len(cur)==lim:
                res.append(cur[:]) # Save a copy of cur
                return
            for i in range(len(num)):
                if i>0 and num[i]==num[i-1]:
                    continue
                cur.append(num[i])
                _permute(num[:i]+num[i+1:], cur, lim)
                cur.pop()
                
        _permute(sorted(nums), [], len(nums))
                
        return res

"""
Runtime: 44 ms, faster than 88.32% of Python online submissions for Permutations II.
Memory Usage: 13.6 MB, less than 68.17% of Python online submissions for Permutations II.
"""