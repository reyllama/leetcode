"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([))]("
Output: false

Example 5:
Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==0:
            pairs, cache = {")":"(", "}":"{", "]":"["}, []
            for i, w in enumerate(s):
                if w in pairs.values():
                    cache.append(w)
                else:
                    if pairs[w] not in cache:
                        return False
                    elif (i-cache.index(pairs[w]))%2==1:
                        cache.append(w)
                    else:
                        return False
            return True
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        pairs, res = {"(":1, ")":2, "{":3, "}":6, "[":5, "]":10}, []
        for w in s:
            temp = pairs[w]
            if (temp%2):
                res.append(temp)
            else:
                if (len(res) and res[-1]==temp//2):
                    del res[-1]
                else:
                    return False
        return res==[]

x = Solution()
print(x.isValid("{{{[()]}}}"))
