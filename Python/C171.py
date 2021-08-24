"""
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        d = dict()
        ans = 0
        from string import ascii_uppercase
        for i, letter in enumerate(ascii_uppercase):
            d[letter] = i+1
        for i, letter in enumerate(columnTitle[::-1]):
            ans += (26**i)*d[letter]
        return ans

"""
Runtime: 16 ms, faster than 88.65% of Python online submissions for Excel Sheet Column Number.
Memory Usage: 13.6 MB, less than 6.81% of Python online submissions for Excel Sheet Column Number.
"""