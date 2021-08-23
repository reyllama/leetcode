"""
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        c_board = [[0]*(n+2)] + [[0]+board[i]+[0] for i in range(m)] + [[0]*(n+2)] # Zero Padding
        def convolution(i, j, board):
            conv = sum(board[i-1][j-1:j+2])+board[i][j-1]+board[i][j+1]+sum(board[i+1][j-1:j+2])
            if board[i][j]==1:
                if conv<2 or conv>3:
                    return 0
                else:
                    return 1
            else:
                if conv==3:
                    return 1
                else:
                    return 0
        for i in range(m):
            for j in range(n):
                board[i][j] = convolution(i+1, j+1, c_board)
        return board

"""
Runtime: 20 ms, faster than 69.66% of Python online submissions for Game of Life.
Memory Usage: 13.4 MB, less than 72.86% of Python online submissions for Game of Life.
"""