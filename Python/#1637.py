"""
1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(list(set([v[0] for v in points])))
        r, s = 0, arr[0]
        for a in arr[1:]:
            if a-s > r:
                r = a-s
            s = a
        return r

"""
Runtime: 804 ms, faster than 94.84% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.
Memory Usage: 55.1 MB, less than 68.86% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.
"""
