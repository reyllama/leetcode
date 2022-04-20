"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [None] * (len(cost)+1)
        arr[0] = arr[1] = 0
        for i in range(2, len(cost)+1):
            arr[i] = min(arr[i-1]+cost[i-1], arr[i-2]+cost[i-2])
        return arr[-1]

"""
Runtime: 60 ms, faster than 91.30% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14 MB, less than 80.64% of Python3 online submissions for Min Cost Climbing Stairs.
"""
