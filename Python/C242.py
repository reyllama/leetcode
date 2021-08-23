"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if sorted(s)==sorted(t) else False

"""
Runtime: 44 ms, faster than 60.48% of Python online submissions for Valid Anagram.
Memory Usage: 14.7 MB, less than 24.84% of Python online submissions for Valid Anagram.
"""