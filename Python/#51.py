"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        idx = []
        res = []
        def dfs(n, cur):
            m = len(cur)
            if m == n:
                idx.append(list(cur))
                return
            for i in range(n):
                valid = True
                for j, v in enumerate(cur):
                    if m-j == v-i:
                        valid = False
                        break
                    elif m-j == i-v:
                        valid = False
                        break
                    elif v==i:
                        valid = False
                        break
                if valid:
                    cur.append(i)
                    dfs(n, cur)
                    cur.pop()
        dfs(n, [])
        def idx2board(n, idx):
            return "."*idx + "Q" + "."*(n-idx-1)
        for arr in idx:
            tmp = [idx2board(n, i) for i in arr]
            res.append(tmp)
        return res

"""
Runtime: 77 ms, faster than 56.20% of Python online submissions for N-Queens.
Memory Usage: 13.9 MB, less than 13.72% of Python online submissions for N-Queens.
"""
