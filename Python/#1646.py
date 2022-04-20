"""
1646. Get Maximum in Generated Array

You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i] when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums​​​.
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0, 1] + [0]*(n-1)
        
        if n < 2:
            return arr[n]
        
        curMax = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[i//2+1]
                curMax = max(curMax, arr[i])
                
        return curMax

"""
Runtime: 27 ms, faster than 96.03% of Python3 online submissions for Get Maximum in Generated Array.
Memory Usage: 13.8 MB, less than 98.51% of Python3 online submissions for Get Maximum in Generated Array.
"""
