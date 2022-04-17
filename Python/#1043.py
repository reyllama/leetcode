"""
1043. Partition Array for Maximum Sum

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            curMax = 0
            for j in range(1, min(i, k)+1):
                curMax = max(curMax, arr[i-j])
                dp[i] = max(dp[i], dp[i-j]+curMax*j)
        return dp[-1]

"""
Runtime: 528 ms, faster than 83.46% of Python3 online submissions for Partition Array for Maximum Sum.
Memory Usage: 14 MB, less than 36.98% of Python3 online submissions for Partition Array for Maximum Sum.
"""
