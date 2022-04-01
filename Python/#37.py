"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board # Mutable
        self.solve()
        
    def solve(self):
        row, col = self.findBlank()
        if row==-1 and col==-1:
            return True
        for num in range(1, 10):
            if self.isValid(row, col, num):
                self.board[row][col] = str(num)
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
    
    def findBlank(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def isValid(self, row, col, num):
        return self.checkRow(row, num) and self.checkCol(col, num) and self.checkBox(row, col, num)
    
    def checkRow(self, row, num):
        for y in range(9):
            if self.board[row][y] == str(num):
                return False
        return True
    
    def checkCol(self, col, num):
        for x in range(9):
            if self.board[x][col] == str(num):
                return False
        return True
    
    def checkBox(self, row, col, num):
        r_off, c_off = row//3, col//3
        for x in range(3):
            for y in range(3):
                if self.board[r_off*3+x][c_off*3+y]==str(num):
                    return False
        return True

"""
Runtime: 1212 ms, faster than 6.43% of Python online submissions for Sudoku Solver.
Memory Usage: 13.7 MB, less than 42.26% of Python online submissions for Sudoku Solver.
"""
