"""
1370. Increasing Decreasing String

Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""

class Solution:
    def sortString(self, s: str) -> str:
        import string
        from collections import defaultdict
        cnts = defaultdict(int)
        for i in s:
            cnts[i] += 1

        res = []

        def forward(s, cnts, rev=False):
            cnts = cnts
            alphs = string.ascii_lowercase
            if rev:
                alphs = alphs[::-1]
            for alph in alphs:
                if cnts[alph]>0:
                    res.append(alph)
                    cnts[alph] -= 1
            return cnts

        while len(res) < len(s):
            cnts = forward(s, cnts)
            cnts = forward(s, cnts, rev=True)


        return "".join(res)

"""
Runtime: 60 ms, faster than 73.06% of Python3 online submissions for Increasing Decreasing String.
Memory Usage: 14.3 MB, less than 45.44% of Python3 online submissions for Increasing Decreasing String.
"""
