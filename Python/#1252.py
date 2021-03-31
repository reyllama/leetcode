"""
1252. Cells with Odd Values in a Matrix

There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
"""

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        from collections import defaultdict

        rowd = defaultdict(int)
        cold = defaultdict(int)

        for (a,b) in indices:
            rowd[a] += 1
            cold[b] += 1

        codd = len([v for v in cold.values() if v % 2 == 1])
        ceve = n - codd

        cnt = 0

        for i in range(m):
            if rowd[i] % 2 == 0:
                cnt += codd
            else:
                cnt += ceve

        return cnt

"""
Runtime: 40 ms, faster than 86.59% of Python3 online submissions for Cells with Odd Values in a Matrix.
Memory Usage: 14.2 MB, less than 91.32% of Python3 online submissions for Cells with Odd Values in a Matrix.
"""
