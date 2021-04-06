"""
1812. Determine Color of a Chessboard Square

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        d = {"a":0, "b":1, "c":0, "d":1, "e":0, "f":1, "g":0, "h":1}

        return (d[coordinates[0]]+int(coordinates[1]))%2==0

"""
Runtime: 32 ms, faster than 77.24% of Python3 online submissions for Determine Color of a Chessboard Square.
Memory Usage: 14.3 MB, less than 7.86% of Python3 online submissions for Determine Color of a Chessboard Square.
"""


class Solution:
    def squareIsWhite(self, a):
        return ord(a[0]) % 2 != int(a[1]) % 2
