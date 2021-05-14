"""
921. Minimum Add to Make Parentheses Valid

Given a string s of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

"""

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        # ans: answer
        # cur: # of open parenthesis (left ones) in current step
        ans, cur = 0, 0

        for x in s:

            # No open parenthesis but got right parenthesis, so we need to add left parenthesis
            if (cur<=0) and x == ")":
                ans += 1

            if x == "(":
                # Reset cur to zero as past ones have been accounted for by ans
                if cur < 0:
                    cur = 0
                cur += 1
            elif x == ")":
                cur -= 1


        # Open Parenthesese remaining
        if cur > 0:
            ans += cur
            
        return ans
            
"""
Runtime: 12 ms, faster than 97.93% of Python online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 13.4 MB, less than 86.69% of Python online submissions for Minimum Add to Make Parentheses Valid.
"""