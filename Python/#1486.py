"""
1486. XOR Operation in an Array

Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [(start+2*i) for i in range(n)]
        for i, v in enumerate(nums):
            if i == 0:
                res = v
            else:
                res = res^v

        return res

"""
Runtime: 32 ms, faster than 61.06% of Python3 online submissions for XOR Operation in an Array.
Memory Usage: 14.4 MB, less than 20.61% of Python3 online submissions for XOR Operation in an Array.
"""
