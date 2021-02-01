"""
1476. Subrectangle Queries

Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""

import numpy as np

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):

        self.rectangle = np.array(rectangle)


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        self.rectangle[row1:row2+1, col1:col2+1] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

"""
Runtime: 200 ms, faster than 71.23% of Python3 online submissions for Subrectangle Queries.
Memory Usage: 32.7 MB, less than 6.85% of Python3 online submissions for Subrectangle Queries.
"""
