"""
1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
"""

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        ans = []
        for i in range(len(rowSum)):
            row = []
            for j in range(len(colSum)):
                tmp = min(rowSum[i], colSum[j])
                row.append(tmp)
                rowSum[i] -= tmp
                colSum[j] -= tmp
            ans.append(row)

        return ans

"""
Runtime: 1116 ms, faster than 48.86% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
Memory Usage: 19 MB, less than 84.64% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
"""
