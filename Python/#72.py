"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        board = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            board[i][0] = i
        for j in range(n+1):
            board[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    board[i][j] = board[i-1][j-1]
                else:
                    board[i][j] = 1 + min(board[i-1][j], board[i][j-1], board[i-1][j-1])
        return board[-1][-1]

"""
Runtime: 176 ms, faster than 47.62% of Python online submissions for Edit Distance.
Memory Usage: 16.9 MB, less than 58.24% of Python online submissions for Edit Distance.
"""