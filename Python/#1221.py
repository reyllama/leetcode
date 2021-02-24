"""
1221. Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l, c = 0, 0, 0
        for letter in s:
            if letter == 'R':
                r += 1
            elif letter == 'L':
                l += 1
            if r==l:
                c += 1
                r, l = 0, 0
        return c

"""
Runtime: 24 ms, faster than 96.46% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 14.4 MB, less than 13.70% of Python3 online submissions for Split a String in Balanced Strings.
"""
