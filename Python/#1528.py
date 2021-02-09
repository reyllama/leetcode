"""
1528. Shuffle String

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [0]*len(s)
        for i, v in enumerate(s):
            l[indices[i]] = v
        return "".join(l)

"""
Runtime: 52 ms, faster than 82.58% of Python3 online submissions for Shuffle String.
Memory Usage: 14.2 MB, less than 82.65% of Python3 online submissions for Shuffle String.
"""
