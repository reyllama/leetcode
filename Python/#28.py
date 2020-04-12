"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len(needle) = ln
        if ln==0:
            return 0
        for i in range(len(haystack)+1-ln):
            if haystack[i:i+ln]==needle:
                return i
        return -1

"""
Runtime: 24 ms, faster than 92.05% of Python3 online submissions for Implement strStr().
Memory Usage: 14 MB, less than 12.31% of Python3 online submissions for Implement strStr().
"""
