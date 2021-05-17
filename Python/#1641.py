"""
1641. Count Sorted Vowel Strings

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

"""

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n == 1:
                return [1]*5
            elif n == 2:
                return [5,4,3,2,1]
            tmp = helper(n-1)
            out = []
            for i in range(len(tmp)):
                out.append(sum(tmp[i:]))
            return out
        
        return sum(helper(n))

"""
Runtime: 16 ms, faster than 80.86% of Python online submissions for Count Sorted Vowel Strings.
Memory Usage: 13.5 MB, less than 45.06% of Python online submissions for Count Sorted Vowel Strings.
"""