"""
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        cache = dict()
        n = len(s)
        for i in range(n - 9):
            subs = s[i:i + 10]
            if cache.get(subs, False):
                res.add(subs)
            cache[subs] = True

        return list(res)

"""
Runtime: 70 ms, faster than 84.68% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 27.6 MB, less than 37.86% of Python3 online submissions for Repeated DNA Sequences.
"""