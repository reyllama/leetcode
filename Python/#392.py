"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # res = False
        self.string = t
        
        def dp(i):
            if i == len(s):
                return True
            letter = s[i]
            idx = self.string.find(letter)
            if idx >= 0:
                self.string = self.string[idx+1:]
                return dp(i+1)
            
        return dp(0)

"""
Runtime: 31 ms, faster than 92.08% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.8 MB, less than 85.63% of Python3 online submissions for Is Subsequence.
"""
