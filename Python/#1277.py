"""
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # Bottom-up
        # board[i][j] = number for "squares of ones" that takes matrix[i][j] as the lower right vertex (mutually exclusive!)
        board = [[0]*n for _ in range(m)]
        board[0] = matrix[0]
        for i in range(m):
            board[i][0] = matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==1:
                    board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
        return sum([sum(board[i]) for i in range(m)])

"""
Runtime: 616 ms, faster than 97.09% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 16.3 MB, less than 75.67% of Python3 online submissions for Count Square Submatrices with All Ones.
"""
