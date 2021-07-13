"""
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = []
        for row in matrix:
            res+=row
        return sorted(res)[k-1]

"""
Runtime: 212 ms, faster than 44.03% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.5 MB, less than 14.44% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
"""