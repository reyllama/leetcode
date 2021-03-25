"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        lc, rc, cur = 0, 0, 0
        out = ""

        for i, p in enumerate(S):
            if p=="(":
                lc += 1
            elif p==")":
                rc += 1
            if lc*rc>0 and lc==rc:
                out += S[cur+1:i]
                lc, rc = 0, 0
                cur = i+1
        return out

"""
Runtime: 40 ms, faster than 53.47% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 14.2 MB, less than 94.92% of Python3 online submissions for Remove Outermost Parentheses.
"""
