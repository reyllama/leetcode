"""
807. Max Increase to Keep City Skyline

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # O(N^3)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += min(max(grid[i]), max([row[j] for row in grid])) - grid[i][j]
        return res

"""
Runtime: 164 ms, faster than 8.98% of Python3 online submissions for Max Increase to Keep City Skyline.
Memory Usage: 14.3 MB, less than 83.64% of Python3 online submissions for Max Increase to Keep City Skyline.
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        import numpy as np
        grid = np.array(grid)
        max_col = np.max(grid, axis=0)
        max_row = np.max(grid, axis=1)
        g_1 = np.tile(max_col, (len(max_row), 1))
        g_2 = np.tile(max_row, (len(max_col), 1)).T
        g = np.minimum(g_1, g_2)
        return g.sum() - grid.sum()

"""
Runtime: 124 ms, faster than 15.53% of Python3 online submissions for Max Increase to Keep City Skyline.
Memory Usage: 31.6 MB, less than 5.10% of Python3 online submissions for Max Increase to Keep City Skyline.
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # O(N^2)
        res = 0
        max_rows = [max(row) for row in grid]
        max_cols = []
        for j in range(len(grid[0])):
            t = []
            for row in grid:
                t.append(row[j])
            max_cols.append(max(t))
        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                res += min(max_rows[i], max_cols[j]) - val

        return res

"""
Runtime: 68 ms, faster than 90.49% of Python3 online submissions for Max Increase to Keep City Skyline.
Memory Usage: 14.3 MB, less than 60.05% of Python3 online submissions for Max Increase to Keep City Skyline.
"""
