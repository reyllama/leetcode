"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        idx = []
        def dfs(n, cur):
            m = len(cur)
            if m==n:
                idx.append(list(cur))
                return
            for i in range(n):
                valid=True
                for j, v in enumerate(cur):
                    if i==v:
                        valid=False
                        break
                    elif m-j==i-v:
                        valid=False
                        break
                    elif m-j==v-i:
                        valid=False
                        break
                if valid:
                    cur.append(i)
                    dfs(n, cur)
                    cur.pop()
        dfs(n, [])
        return len(idx)

"""
Runtime: 71 ms, faster than 47.20% of Python online submissions for N-Queens II.
Memory Usage: 13.4 MB, less than 54.21% of Python online submissions for N-Queens II.
"""
