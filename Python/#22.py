'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''


class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            print(p, left, right, parens)
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

x = Solution()
print(x.generateParenthesis(3))
