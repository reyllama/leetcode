"""
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        words = [set(word) for word in words]
        return sum([1 for word in words if len(word-a)==0])

"""
Runtime: 288 ms, faster than 25.37% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 20.4 MB, less than 14.91% of Python3 online submissions for Count the Number of Consistent Strings.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        return sum([1 for word in words if len(set(word)-a)==0])

"""
Runtime: 244 ms, faster than 58.21% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 16.4 MB, less than 14.91% of Python3 online submissions for Count the Number of Consistent Strings.
"""
