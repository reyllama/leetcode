"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        ans, cur = 0, n

        for row in grid:
            ans += (n-cur)
            for i, v in enumerate(row[:cur]):
                if v < 0:
                    ans += (cur-i)
                    cur = i
                    break

        return ans

"""
Runtime: 116 ms, faster than 74.75% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 14.9 MB, less than 99.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt
