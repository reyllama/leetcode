"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
        for j in range(n):
            if j != n-j-1:
                ans += mat[j][n-j-1]

        return ans

"""
Runtime: 104 ms, faster than 81.73% of Python3 online submissions for Matrix Diagonal Sum.
Memory Usage: 14.6 MB, less than 15.53% of Python3 online submissions for Matrix Diagonal Sum.
"""
