"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isvalid(arr):
            cache = set()
            arr = [int(n) for n in arr if n != "."]
            for num in arr:
                if num<1 or num>9:
                    return False
                if num in cache:
                    return False
                cache.add(num)
            return True
        
        for i in range(9):
            x, y = 3*(i//3), 3*(i%3)
            arr1, arr2, arr3 = board[i], [board[j][i] for j in range(9)], board[x][y:y+3]+board[x+1][y:y+3]+board[x+2][y:y+3]
            if not isvalid(arr1):
                return False
            if not isvalid(arr2):
                return False
            if not isvalid(arr3):
                return False
        return True

"""
Runtime: 123 ms, faster than 9.27% of Python online submissions for Valid Sudoku.
Memory Usage: 13.7 MB, less than 18.31% of Python online submissions for Valid Sudoku.
"""