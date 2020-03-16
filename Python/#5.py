'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return None
        start, leng = 0, len(s)
        while leng >=1:
            i = leng//2
            if leng % 2 == 1:
                val = s[start:start+2*i+1]
                if s[start:start+i] == s[start+i+1:start+2*i+1][::-1]:
                    return val
            else:
                val = s[start:start+2*i]
                if s[start:start+i] == s[start+i:start+2*i][::-1]:
                    return val
            if start + 2*i < len(s):
                start += 1
            else:
                start = 0
                leng -= 1

        return s[0]

'''
Runtime: 7032 ms, faster than 12.94% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''




X = Solution()
print(X.longestPalindrome("babad"))
print(X.longestPalindrome("abcdeedcf"))
print(X.longestPalindrome("babad"))
print(X.longestPalindrome("qprrpqls"))
print(X.longestPalindrome(""))
print(X.longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))
# print(len("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))
