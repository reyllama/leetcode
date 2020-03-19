'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if strs:
            shortest = sorted(strs, key=lambda e:len(e))[0]
            for i in range(len(shortest)):
                if len({word[i] for word in strs}) == 1:
                    ans += shortest[i]
                else:
                    return ans
        return ans

'''
Runtime: 36 ms, faster than 34.10% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if strs:
            for i in range(min([len(x) for x in strs])):
                if len({word[i] for word in strs}) == 1:
                    ans += strs[0][i]
                else:
                    return ans
        return ans

'''
Runtime: 32 ms, faster than 67.07% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13 MB, less than 98.10% of Python3 online submissions for Longest Common Prefix.
'''
