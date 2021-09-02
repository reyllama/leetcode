"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(candidates)
        
        def helper(target, idx=0, cur=[]):
            if target<0:
                return
            
            elif target==0:
                res.append(cur)
                return
            
            for i in range(idx, len(nums)):
                n = nums[i]
                if i!=idx and nums[i-1]==n:
                    continue
                helper(target-n, i+1, cur+[n])
                
        helper(target)
        
        return res

"""
Runtime: 84 ms, faster than 48.40% of Python online submissions for Combination Sum II.
Memory Usage: 13.5 MB, less than 62.70% of Python online submissions for Combination Sum II.
"""