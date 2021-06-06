"""
1880. Check if Word Equals Summation of Two Words

The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.
"""

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        d = {}
        for i, s in enumerate(string.ascii_lowercase):
            d[s] = str(i)
            if s == 'j':
                break
                
        f, s, t = "", "", ""
        for x in firstWord:
            f += d[x]
        for x in secondWord:
            s += d[x]
        for x in targetWord:
            t += d[x]
        return int(f)+int(s) == int(t)

"""
Runtime: 24 ms, faster than 48.05% of Python online submissions for Check if Word Equals Summation of Two Words.
Memory Usage: 13.8 MB, less than 8.29% of Python online submissions for Check if Word Equals Summation of Two Words.
"""