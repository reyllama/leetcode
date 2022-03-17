"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        res = False

        for i in range(m-1):
            if matrix[i][0] <= target and matrix[i + 1][0] > target:
                for j in range(n):
                    if matrix[i][j] == target:
                        res = True
                    elif matrix[i][j] > target:
                        break
        for j in range(n):
            if matrix[-1][j] == target:
                res = True
        return res

"""
Runtime: 28 ms, faster than 91.96% of Python online submissions for Search a 2D Matrix.
Memory Usage: 13.9 MB, less than 48.17% of Python online submissions for Search a 2D Matrix.
"""