"""
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        import string

        alphabet = string.ascii_lowercase
        book = dict()
        out = ""

        for i in range(1, 27):
            book[str(i)] = alphabet[i-1]

        while len(s)>0:
            if len(s)>=3 and s[2]=="#":
                out += book[s[:2]]
                s = s[3:]
            else:
                out += book[s[0]]
                s = s[1:]

        return out

"""
Runtime: 28 ms, faster than 81.62% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 14.4 MB, less than 21.58% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
"""
