"""
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

"""
Runtime: 28 ms, faster than 92.05% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 14.2 MB, less than 87.59% of Python3 online submissions for Check If Two String Arrays are Equivalent.
"""
