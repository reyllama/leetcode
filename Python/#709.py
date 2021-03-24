"""
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""

class Solution:
    def toLowerCase(self, str):

        res = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                res += chr(ord(char)+32)
            else:
                res += char

        return res

"""
Runtime: 24 ms, faster than 93.05% of Python3 online submissions for To Lower Case.
Memory Usage: 14.3 MB, less than 6.43% of Python3 online submissions for To Lower Case.
"""
