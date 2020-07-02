"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element
in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits):
        num = str(int("".join([str(_) for _ in digits])) + 1)
        return [int(_) for _ in num]

"""
Runtime: 28 ms, faster than 88.93% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 36.04% of Python3 online submissions for Plus One.
"""
