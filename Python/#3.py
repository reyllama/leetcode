'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         freq = {l for l in s if s.count(l)>1}
#         if not freq:
#             return len(s)
#         ans = []
#         for f in freq:
#             t = s.split(f)
#             conseq = [t[i]+f+t[i+1] for i in range(len(t)-1)]
#             for itm in conseq:
#         return min(ans)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not {x for x in s if s.count(x)>1}:
            return len(s)
        maxima = 0
        while s:
            if len(s) < maxima:
                break
            for i in range(2, len(s)+1):
                if len(set(s[:i])) < len(s[:i]):
                    maxima = max(i-1, maxima)
                    break
                if i == len(s):
                    maxima = max(i, maxima)
                    return maxima
            s = s[1:]
        return maxima

'''
Runtime: 5472 ms, faster than 5.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.1 MB, less than 97.96% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not {x for x in s if s.count(x)>1}:
            return len(s)
        maxima = 0
        while s:
            if len(s) < maxima:
                break
            for i in range(1, len(s)):
                if s[i] in s[:i]:
                    maxima = max(i, maxima)
                    break
                if i == len(s)-1:
                    maxima = max(i+1, maxima)
                    return maxima
            s = s[1:]
        return maxima

'''
Runtime: 1244 ms, faster than 5.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, start, sofar = {}, 0, 0
        for i, v in enumerate(s):
            if v in dic:
                sofar = max(sofar, i-start)
                start = max(start, dic[v]+1)
            dic[v] = i
        return max(sofar, len(s)-start)

'''
Runtime: 56 ms, faster than 76.18% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streak = []
        maxlen = 0
        for x in s:
            if x in streak:
                streak = streak[streak.index(x)+1:]
            streak.append(x)
            maxlen = max(maxlen, len(streak))
        return maxlen

'''
Runtime: 68 ms, faster than 53.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.9 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

x = Solution()
assert x.lengthOfLongestSubstring('pwwkew') == 3
assert x.lengthOfLongestSubstring('abcdabf') == 5
assert x.lengthOfLongestSubstring('abcabcbb') == 3
assert x.lengthOfLongestSubstring('dwf') == 3
assert x.lengthOfLongestSubstring('abcdebf') == 5
