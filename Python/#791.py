"""
791. Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted.
More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :

Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        for char in S[::-1]:
            i=0
            while i < len(T):
                if T[i]==char:
                    T = T[i]+T[:i]+T[i+1:]
                i += 1
        return T

"""
Time Complexity: O(mn)
Runtime: 56 ms, faster than 5.85% of Python3 online submissions for Custom Sort String.
Memory Usage: 13.6 MB, less than 96.27% of Python3 online submissions for Custom Sort String.
"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnts = dict()
        for char in S:
            cnts[char] = T.count(char)
            T = T.replace(char, '')
        return ''.join([cnts[char]*char for char in S]) + T

"""
Time Complexity: O(mn)
Runtime: 32 ms, faster than 56.71% of Python3 online submissions for Custom Sort String.
Memory Usage: 13.9 MB, less than 32.89% of Python3 online submissions for Custom Sort String.
"""
