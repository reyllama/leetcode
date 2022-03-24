"""
1402. Reducing Dishes

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        arr = sorted(satisfaction)
        res, res_sum = 0, 0
        while arr:
            val = arr.pop()
            if val + res_sum > 0:
                res = res + res_sum + val
                res_sum += val
            else:
                break
        return res

"""
Runtime: 36 ms, faster than 69.09% of Python online submissions for Reducing Dishes.
Memory Usage: 13.7 MB, less than 5.45% of Python online submissions for Reducing Dishes.
"""

