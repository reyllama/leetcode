"""
1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.
"""

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) <= 1:
            return 0
        
        elif len(s) == 2:
            return 1
    
        def maxpalindrome(s):
            n = len(s)
            board = [[0]*n for _ in range(n)]
            for i in range(n-1, -1, -1):
                board[i][i] = 1
                for j in range(i+1, n):
                    if s[i] == s[j]:
                        board[i][j] = board[i+1][j-1] + 2
                    else:
                        board[i][j] = max(board[i+1][j], board[i][j-1])
            return board[0][n-1]
        
        return len(s) - maxpalindrome(s)

"""
Runtime: 492 ms, faster than 97.56% of Python online submissions for Minimum Insertion Steps to Make a String Palindrome.
Memory Usage: 15.1 MB, less than 86.59% of Python online submissions for Minimum Insertion Steps to Make a String Palindrome.
"""
