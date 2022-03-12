"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        a,b = 0,0
        res = []

        while (a<m) and (b<n):
            res += matrix[a][b:n]
            for i in range(a+1,m-1):
                res.append(matrix[i][n-1])
            if m>a+1:
                res += matrix[m-1][n-1:b:-1]
                res.append(matrix[m-1][b])
            if n>b+1:
                for i in range(m-2,a,-1):
                    res.append(matrix[i][b])
            a += 1
            b += 1
            m -= 1
            n -= 1
        return res

sol = Solution()
lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst = [[7],[9],[6]]
print(sol.spiralOrder(lst))

"""
Runtime: 16 ms, faster than 88.38% of Python online submissions for Spiral Matrix.
Memory Usage: 13.5 MB, less than 43.39% of Python online submissions for Spiral Matrix.
"""