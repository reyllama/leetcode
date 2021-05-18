"""
1347. Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        from collections import defaultdict

        ref = defaultdict(int)
        reft = defaultdict(int)

        for item in s:
            ref[item] += 1

        for item in t:
            reft[item] += 1

        return sum([ref[item]-reft[item] for item in ref if (ref[item]-reft[item])>0])

"""
Runtime: 152 ms, faster than 97.18% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram.
Memory Usage: 14.5 MB, less than 28.17% of Python online submissions for Minimum Number of Steps to Make Two Strings Anagram.
"""