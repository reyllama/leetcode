"""
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""

################ Version 1. Vanilla DP ################
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.min = float("inf")

        def dp(lev, idx, cur):
            if lev==len(triangle)-1:
                self.min = min(cur, self.min)
                return
            dp(lev+1, idx, cur+triangle[lev+1][idx])
            dp(lev+1, idx+1, cur+triangle[lev+1][idx+1])

        dp(0, 0, triangle[0][0])
        return self.min

"""
Time limits exceeded
(O(1) memory usage)
"""

################ Version 2. Memoized Bottom-up ################
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        template = [[float("inf")] * (i + 1) for i in range(len(triangle))]
        template[0][0] = triangle[0][0]
        for lev in range(1, len(triangle)):
            for idx in range(lev + 1):
                if idx == 0: # leftmost
                    template[lev][idx] = template[lev - 1][idx] + triangle[lev][idx]
                elif idx == lev: # rightmost
                    template[lev][idx] = template[lev - 1][idx - 1] + triangle[lev][idx]
                else:
                    template[lev][idx] = min(template[lev - 1][idx - 1], template[lev - 1][idx]) + triangle[lev][idx]
        return min(template[-1])

"""
Runtime: 47 ms, faster than 92.82% of Python online submissions for Triangle.
Memory Usage: 14.7 MB, less than 16.79% of Python online submissions for Triangle.
"""