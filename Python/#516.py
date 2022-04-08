"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.max = 0
        n = len(s)
        r = s[::-1]
        
        def dp(x, y, cur):
            if not x or not y:
                self.max = max(self.max, cur)
                return
            if x[0] == y[0]:
                dp(x[1:], y[1:], cur+1)
            else:
                dp(x[1:], y, cur)
                dp(x, y[1:], cur)
                
        dp(s, r, 0)
        
        return self.max

"""
Time Limits Exceeded
"""

class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

"""
Runtime: 1993 ms, faster than 60.73% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.6 MB, less than 75.77% of Python3 online submissions for Longest Palindromic Subsequence.
"""
