"""
1329. Sort the Matrix Diagonally

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""

class Solution:

    def get_diag(self, mat, i, j):
        i_, j_ = i, j
        out = []
        while (i_ < len(mat)) and (j_ < len(mat[0])):
            out.append(mat[i_][j_])
            i_ += 1
            j_ += 1
        s = sorted(out)
        k = 0
        while (i < len(mat)) and (j < len(mat[0])):
            mat[i][j] = s[k]
            i += 1
            j += 1
            k += 1
        return mat

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) < 1:
            return None
        m, n = len(mat), len(mat[0])

        for i in range(m-1):
            mat = self.get_diag(mat, i, 0)
        for j in range(n-1):
            mat = self.get_diag(mat, 0, j)
        return mat

"""
Runtime: 88 ms, faster than 49.11% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.7 MB, less than 52.32% of Python3 online submissions for Sort the Matrix Diagonally.
"""
