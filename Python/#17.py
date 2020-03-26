"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from string import ascii_lowercase
        s = ascii_lowercase
        dic = dict()
        for i in range(2, 7):
            dic[str(i)] = s[3*i-6:3*i-3]
        dic['7'] = s[15:19]
        dic['8'] = s[19:22]
        dic['9'] = s[22:26]

        res = []

        for num in digits:
            if not res:
                res += dic[num]
                continue
            if num == '1':
                continue
            res = [w+v for w in res for v in dic[num]]
        return res

x = Solution()

print(x.letterCombinations('2532'))

"""
Runtime: 24 ms, faster than 88.60% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
