"""
1266. Minimum Time Visiting All Points

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        if len(points)<=1:
            return time
        prev = points[0]
        for cur in points[1:]:
            time += max(abs(cur[0]-prev[0]), abs(cur[1]-prev[1]))
            prev = cur
        return time

"""
Runtime: 60 ms, faster than 60.34% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 14.5 MB, less than 6.53% of Python3 online submissions for Minimum Time Visiting All Points.
"""
