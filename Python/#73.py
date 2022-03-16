"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        
        cp = deepcopy(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if cp[i][j]==0:
                    matrix[i] = [0]*len(matrix[i])
                    for c in range(len(matrix)):
                        matrix[c][j] = 0

"""
Runtime: 156 ms, faster than 67.26% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.8 MB, less than 37.64% of Python3 online submissions for Set Matrix Zeroes.
"""

s = Solution()
i = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(i)
print(i)