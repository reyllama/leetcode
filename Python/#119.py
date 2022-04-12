"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex==0:
        #     return [1]
        trng = [[1] for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            trng[i] = [1] * (i+1)
            for j in range(1, i):
                trng[i][j] = trng[i-1][j-1] + trng[i-1][j]
        return trng[rowIndex]

"""
Runtime: 41 ms, faster than 59.56% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.9 MB, less than 67.04% of Python3 online submissions for Pascal's Triangle II.
"""
